"""
Enriches remaining Wave 2 models where multi-word model names prevented Wikimedia image discovery.
"""
import json
import sys
import time
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT_DIR / "scripts"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from media_downloader import search_wikimedia_images, download_file, sanitize_filename, MEDIA_DIR, CATALOG_DIR

TARGET_MODELS = [
    {
        "make": "toyota",
        "model": "yaris",
        "hero_query": "Toyota Yaris",
        "gen_queries": {
            "NCP10": "Toyota Echo",
            "NCP90": "Toyota Yaris NCP90",
            "NCP130": "Toyota Yaris XP130",
            "XP210": "Toyota GR Yaris",
        }
    },
    {
        "make": "mitsubishi",
        "model": "starion-cordia",
        "hero_query": "Mitsubishi Starion",
        "gen_queries": {
            "AA/AB/AC": "Mitsubishi Cordia",
            "JA/JB/JD": "Mitsubishi Starion",
        }
    },
    {
        "make": "suzuki",
        "model": "jimny-sierra",
        "hero_query": "Suzuki Jimny",
        "gen_queries": {
            "LJ50/LJ80": "Suzuki LJ80",
            "SJ410/SJ413": "Suzuki Sierra",
            "JB33/JB43": "Suzuki Jimny JB43",
            "JB64/JB74": "Suzuki Jimny JB74",
        }
    }
]

def main():
    print("=== Enriching Media for Models with Custom Search Queries ===")
    total = 0

    for item in TARGET_MODELS:
        make_slug = item["make"]
        model_slug = item["model"]
        json_path = CATALOG_DIR / "makes" / make_slug / "models" / model_slug / "model.json"

        if not json_path.exists():
            continue

        mod = json.loads(json_path.read_text(encoding="utf-8"))
        if "pictures" not in mod or not isinstance(mod["pictures"], list):
            mod["pictures"] = []

        # 1. Fetch hero pictures if missing
        if not mod["pictures"]:
            heroes = search_wikimedia_images(item["hero_query"], limit=2)
            for idx, h in enumerate(heroes):
                fname = sanitize_filename(f"{make_slug}_{model_slug}_hero_{idx+1}_{h['title']}") + ".jpg"
                dest = MEDIA_DIR / "pictures" / make_slug / model_slug / fname
                meta = download_file(h["source_url"], dest)
                if meta:
                    mod["pictures"].append({
                        "category": "hero" if idx == 0 else "exterior",
                        "caption": h["caption"],
                        "source_url": h["source_url"],
                        "license_or_credit": h["license_or_credit"],
                        **meta
                    })
                    total += 1
                time.sleep(0.3)

        # 2. Fetch generation pictures
        for gen in mod.get("generations", []):
            scode = gen.get("series_code")
            if "pictures" not in gen or not isinstance(gen["pictures"], list):
                gen["pictures"] = []

            has_pic = any(isinstance(p, dict) and p.get("local_path") for p in gen["pictures"])
            if not has_pic and scode in item["gen_queries"]:
                q = item["gen_queries"][scode]
                found = search_wikimedia_images(q, limit=1)
                for idx, pic in enumerate(found):
                    fname = sanitize_filename(f"{make_slug}_{model_slug}_{scode}_{idx+1}_{pic['title']}") + ".jpg"
                    dest = MEDIA_DIR / "pictures" / make_slug / model_slug / fname
                    meta = download_file(pic["source_url"], dest)
                    if meta:
                        gen["pictures"].append({
                            "series_code": scode,
                            "category": "exterior",
                            "caption": pic["caption"],
                            "source_url": pic["source_url"],
                            "license_or_credit": pic["license_or_credit"],
                            **meta
                        })
                        total += 1
                    time.sleep(0.3)

        json_path.write_text(json.dumps(mod, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  [OK] {make_slug}/{model_slug} enriched.")

    print(f"Total additional media files downloaded: {total}")

if __name__ == "__main__":
    main()
