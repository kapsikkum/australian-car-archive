"""
Media downloader and Wikimedia Commons photo fetcher for the Australian Car Archive.
Downloads images and PDF manuals directly to local disk (media/pictures and media/manuals)
and updates model.json / make.json with local_path, file_size_bytes, and sha256.
"""
import argparse
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT_DIR = Path(__file__).resolve().parent.parent
CATALOG_DIR = ROOT_DIR / "catalog"
MEDIA_DIR = ROOT_DIR / "media"

USER_AGENT = "AustralianCarArchiveBot/1.0 (https://example.org/car-manuals; archive@example.org) Python-urllib/3.13"


def sanitize_filename(name: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9._-]+", "_", name.strip())
    return cleaned[:120].strip("_") or "file"


def download_file(url: str, dest_path: Path, timeout: int = 30) -> Optional[Dict[str, Any]]:
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
            if len(data) < 512:
                return None
            dest_path.write_bytes(data)
            sha256 = hashlib.sha256(data).hexdigest()
            rel_path = dest_path.relative_to(ROOT_DIR).as_posix()
            return {
                "local_path": rel_path,
                "file_size_bytes": len(data),
                "sha256": sha256,
            }
    except Exception as e:
        print(f"  [WARN] Failed to download {url}: {e}")
        return None


def search_wikimedia_images(query: str, limit: int = 3) -> List[Dict[str, Any]]:
    """Search Wikimedia Commons for freely licensed photos matching the car query."""
    api_url = (
        "https://commons.wikimedia.org/w/api.php?"
        + urllib.parse.urlencode(
            {
                "action": "query",
                "generator": "search",
                "gsrsearch": f"filetype:bitmap {query}",
                "gsrnamespace": "6",
                "gsrlimit": str(limit * 2),
                "prop": "imageinfo",
                "iiprop": "url|size|extmetadata",
                "iiurlwidth": "1280",
                "format": "json",
            }
        )
    )
    req = urllib.request.Request(api_url, headers={"User-Agent": USER_AGENT})
    results = []
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
            pages = payload.get("query", {}).get("pages", {})
            for _, page in pages.items():
                title = page.get("title", "")
                ii_list = page.get("imageinfo", [])
                if not ii_list:
                    continue
                ii = ii_list[0]
                img_url = ii.get("thumburl") or ii.get("url")
                if not img_url:
                    continue
                low = img_url.lower()
                if not (low.endswith(".jpg") or low.endswith(".jpeg") or low.endswith(".png") or "px-" in low):
                    continue
                ext = ii.get("extmetadata", {})
                license_name = ext.get("LicenseShortName", {}).get("value", "CC / Wikimedia Commons")
                artist = re.sub(r"<[^>]+>", "", ext.get("Artist", {}).get("value", "")).strip()
                desc = re.sub(r"<[^>]+>", "", ext.get("ImageDescription", {}).get("value", title)).strip()
                results.append(
                    {
                        "title": title.replace("File:", ""),
                        "source_url": img_url,
                        "caption": desc[:240] if desc else title.replace("File:", ""),
                        "license_or_credit": f"{license_name} ({artist})" if artist else license_name,
                    }
                )
                if len(results) >= limit:
                    break
    except Exception as e:
        print(f"  [WARN] Wikimedia search failed for '{query}': {e}")
    return results


def enrich_model_pictures(make_slug: str, model_slug: str, max_per_gen: int = 2) -> int:
    model_json_path = CATALOG_DIR / "makes" / make_slug / "models" / model_slug / "model.json"
    if not model_json_path.exists():
        print(f"Model file not found: {model_json_path}")
        return 0

    mod = json.loads(model_json_path.read_text(encoding="utf-8"))
    make_name = make_slug.replace("-", " ").title()
    model_name = mod.get("name", model_slug.replace("-", " ").title())
    downloaded = 0

    # Ensure model-level pictures list
    if "pictures" not in mod or not isinstance(mod["pictures"], list):
        mod["pictures"] = []

    # 1. Download any existing picture URLs missing local_path
    for pic in mod["pictures"]:
        if isinstance(pic, dict) and pic.get("source_url") and not pic.get("local_path"):
            ext = ".jpg"
            if ".png" in pic["source_url"].lower():
                ext = ".png"
            fname = sanitize_filename(f"{make_slug}_{model_slug}_{pic.get('series_code', 'hero')}_{downloaded}") + ext
            dest = MEDIA_DIR / "pictures" / make_slug / model_slug / fname
            meta = download_file(pic["source_url"], dest)
            if meta:
                pic.update(meta)
                downloaded += 1

    # 2. If model has no downloaded hero picture yet, fetch from Wikimedia Commons
    has_local_model_pic = any(isinstance(p, dict) and p.get("local_path") for p in mod["pictures"])
    if not has_local_model_pic:
        query = f"{make_name} {model_name} Australia car"
        found = search_wikimedia_images(query, limit=2)
        if not found:
            found = search_wikimedia_images(f"{make_name} {model_name}", limit=2)
        for idx, item in enumerate(found):
            fname = sanitize_filename(f"{make_slug}_{model_slug}_hero_{idx+1}_{item['title']}")
            if not (fname.lower().endswith(".jpg") or fname.lower().endswith(".png")):
                fname += ".jpg"
            dest = MEDIA_DIR / "pictures" / make_slug / model_slug / fname
            meta = download_file(item["source_url"], dest)
            if meta:
                mod["pictures"].append(
                    {
                        "category": "hero" if idx == 0 else "exterior",
                        "caption": item["caption"],
                        "source_url": item["source_url"],
                        "license_or_credit": item["license_or_credit"],
                        **meta,
                    }
                )
                downloaded += 1
            time.sleep(0.3)

    # 3. For each generation, fetch or download pictures if needed
    for gen in mod.get("generations", []):
        if not isinstance(gen, dict):
            continue
        scode = str(gen.get("series_code") or gen.get("generation_name") or "gen")
        if "pictures" not in gen or not isinstance(gen["pictures"], list):
            gen["pictures"] = []

        # Download existing URLs if missing local_path
        for pic in gen["pictures"]:
            if isinstance(pic, dict) and pic.get("source_url") and not pic.get("local_path"):
                fname = sanitize_filename(f"{make_slug}_{model_slug}_{scode}_{downloaded}.jpg")
                dest = MEDIA_DIR / "pictures" / make_slug / model_slug / fname
                meta = download_file(pic["source_url"], dest)
                if meta:
                    pic.update(meta)
                    downloaded += 1

        has_gen_pic = any(isinstance(p, dict) and p.get("local_path") for p in gen["pictures"])
        if not has_gen_pic and max_per_gen > 0:
            q = f"{make_name} {model_name} {scode}"
            found = search_wikimedia_images(q, limit=max_per_gen)
            for idx, item in enumerate(found):
                fname = sanitize_filename(f"{make_slug}_{model_slug}_{scode}_{idx+1}_{item['title']}")
                if not (fname.lower().endswith(".jpg") or fname.lower().endswith(".png")):
                    fname += ".jpg"
                dest = MEDIA_DIR / "pictures" / make_slug / model_slug / fname
                meta = download_file(item["source_url"], dest)
                if meta:
                    gen["pictures"].append(
                        {
                            "series_code": scode,
                            "category": "exterior",
                            "caption": item["caption"],
                            "source_url": item["source_url"],
                            "license_or_credit": item["license_or_credit"],
                            **meta,
                        }
                    )
                    downloaded += 1
                time.sleep(0.3)

    # 4. Download any manual URLs that don't yet have local_path
    for man in mod.get("manuals", []):
        if isinstance(man, dict) and man.get("source_url") and not man.get("local_path"):
            url = man["source_url"]
            ext = ".pdf" if ".pdf" in url.lower() else ".html"
            fname = sanitize_filename(f"{make_slug}_{model_slug}_{man.get('series_code', 'manual')}_{man.get('title', 'doc')}") + ext
            dest = MEDIA_DIR / "manuals" / make_slug / model_slug / fname
            meta = download_file(url, dest)
            if meta:
                man.update(meta)
                downloaded += 1

    for gen in mod.get("generations", []):
        if not isinstance(gen, dict):
            continue
        scode = str(gen.get("series_code") or "gen")
        for man in gen.get("manuals", []):
            if isinstance(man, dict) and man.get("source_url") and not man.get("local_path"):
                url = man["source_url"]
                ext = ".pdf" if ".pdf" in url.lower() else ".html"
                fname = sanitize_filename(f"{make_slug}_{model_slug}_{scode}_{man.get('title', 'doc')}") + ext
                dest = MEDIA_DIR / "manuals" / make_slug / model_slug / fname
                meta = download_file(url, dest)
                if meta:
                    man.update(meta)
                    downloaded += 1

    model_json_path.write_text(json.dumps(mod, indent=2, ensure_ascii=False), encoding="utf-8")
    return downloaded


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download media for Australian Car Archive")
    parser.add_argument("--make", help="Make slug (e.g. holden)")
    parser.add_argument("--model", help="Model slug (e.g. commodore)")
    parser.add_argument("--max-per-gen", type=int, default=1, help="Max Wikimedia photos per generation")
    parser.add_argument("--all", action="store_true", help="Run across all models in catalog")
    args = parser.parse_args()

    total = 0
    if args.make and args.model:
        total += enrich_model_pictures(args.make, args.model, args.max_per_gen)
    elif args.make:
        mdir = CATALOG_DIR / "makes" / args.make / "models"
        if mdir.exists():
            for mf in sorted(mdir.iterdir()):
                if mf.is_dir():
                    total += enrich_model_pictures(args.make, mf.name, args.max_per_gen)
    elif args.all:
        makes_dir = CATALOG_DIR / "makes"
        if makes_dir.exists():
            for mk in sorted(makes_dir.iterdir()):
                mdir = mk / "models"
                if mdir.exists():
                    for mf in sorted(mdir.iterdir()):
                        if mf.is_dir():
                            total += enrich_model_pictures(mk.name, mf.name, args.max_per_gen)
    print(f"Total media files downloaded: {total}")
