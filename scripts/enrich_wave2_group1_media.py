"""
Enrich media for Wave 2 Group 1 models where compound model names needed targeted search queries.
"""
import json
from pathlib import Path
import sys
import time

SCRIPTS_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPTS_DIR.parent
CATALOG_DIR = ROOT_DIR / "catalog"
sys.path.insert(0, str(SCRIPTS_DIR))

from media_downloader import search_wikimedia_images, download_file, sanitize_filename, MEDIA_DIR

ENRICH_TARGETS = [
    (
        "holden",
        "fe-fc-fb-ek",
        "Holden FC sedan car",
        [
            ("FE", "Holden FE sedan"),
            ("FC", "Holden FC Special"),
            ("FB", "Holden FB sedan"),
            ("EK", "Holden EK sedan"),
        ]
    ),
    (
        "holden",
        "ej-eh-hd-hr",
        "Holden EH sedan car",
        [
            ("EJ", "Holden EJ Premier"),
            ("EH", "Holden EH sedan"),
            ("HD", "Holden HD sedan"),
            ("HR", "Holden HR sedan"),
        ]
    ),
    (
        "leyland-australia",
        "austin-1800",
        "Austin 1800 car",
        [
            ("Mk-I", "Austin 1800 car"),
            ("Mk-II", "Austin 1800 utility car"),
        ]
    ),
    (
        "leyland-australia",
        "morris-major-freeway",
        "Morris Major car",
        [
            ("Major-Series-I-II-Elite", "Morris Major car"),
            ("Freeway-Wolseley-24-80", "Austin Freeway car"),
        ]
    )
]

def main():
    total_dl = 0
    for make_slug, model_slug, hero_query, gen_queries in ENRICH_TARGETS:
        mpath = CATALOG_DIR / "makes" / make_slug / "models" / model_slug / "model.json"
        if not mpath.exists():
            continue
        mod = json.loads(mpath.read_text(encoding="utf-8"))
        if "pictures" not in mod or not isinstance(mod["pictures"], list):
            mod["pictures"] = []

        # Download hero if none exists
        has_hero = any(p.get("category") == "hero" and p.get("local_path") for p in mod["pictures"])
        if not has_hero:
            hero_imgs = search_wikimedia_images(hero_query, limit=1)
            if not hero_imgs:
                hero_imgs = search_wikimedia_images(f"{make_slug} {model_slug[:6]}", limit=1)
            if hero_imgs:
                h = hero_imgs[0]
                fname = sanitize_filename(f"{make_slug}_{model_slug}_hero_{h['title']}") + ".jpg"
                dest = MEDIA_DIR / "pictures" / make_slug / model_slug / fname
                meta = download_file(h["source_url"], dest)
                if meta:
                    mod["pictures"].append({
                        "category": "hero",
                        "caption": h["caption"],
                        "source_url": h["source_url"],
                        "license_or_credit": h["license_or_credit"],
                        **meta
                    })
                    total_dl += 1
                    print(f"  [HERO OK] {make_slug}/{model_slug}")
            time.sleep(0.3)

        for gen in mod.get("generations", []):
            scode = gen.get("series_code")
            if "pictures" not in gen or not isinstance(gen["pictures"], list):
                gen["pictures"] = []
            has_gen_pic = any(p.get("local_path") for p in gen["pictures"])
            if not has_gen_pic:
                match_q = next((q for s, q in gen_queries if s == scode), None)
                if match_q:
                    imgs = search_wikimedia_images(match_q, limit=1)
                    if imgs:
                        img = imgs[0]
                        fname = sanitize_filename(f"{make_slug}_{model_slug}_{scode}_{img['title']}") + ".jpg"
                        dest = MEDIA_DIR / "pictures" / make_slug / model_slug / fname
                        meta = download_file(img["source_url"], dest)
                        if meta:
                            gen["pictures"].append({
                                "series_code": scode,
                                "category": "exterior",
                                "caption": img["caption"],
                                "source_url": img["source_url"],
                                "license_or_credit": img["license_or_credit"],
                                **meta
                            })
                            total_dl += 1
                            print(f"  [GEN PIC OK] {make_slug}/{model_slug} [{scode}]")
                    time.sleep(0.3)

        mpath.write_text(json.dumps(mod, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Enrichment completed: {total_dl} photos added.")

if __name__ == "__main__":
    main()
