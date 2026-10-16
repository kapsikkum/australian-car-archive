"""
Enrich remaining media for Group 3 models where combined model slug needed targeted search.
"""
import json
from pathlib import Path
import sys

SCRIPTS_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPTS_DIR.parent
CATALOG_DIR = ROOT_DIR / "catalog"
sys.path.insert(0, str(SCRIPTS_DIR))

from media_downloader import search_wikimedia_images, download_file, sanitize_filename, MEDIA_DIR

enrich_targets = [
    ("byd", "shark-6-atto-3", [("Atto-3", "BYD Atto 3"), ("Shark-6", "BYD Shark ute")]),
    ("mg", "zs-mg4", [("ZS-ZST", "MG ZS car"), ("MG4", "MG4 EV car")]),
    ("gwm-haval", "cannon-h6", [("Cannon-Ute", "GWM Cannon ute"), ("Haval-H6-Gen3", "Haval H6")])
]

def main():
    for make_slug, model_slug, gen_queries in enrich_targets:
        mpath = CATALOG_DIR / "makes" / make_slug / "models" / model_slug / "model.json"
        if not mpath.exists():
            continue
        mod = json.loads(mpath.read_text(encoding="utf-8"))
        if "pictures" not in mod or not isinstance(mod["pictures"], list):
            mod["pictures"] = []
        
        main_query = gen_queries[0][1]
        hero_imgs = search_wikimedia_images(main_query, limit=1)
        if hero_imgs and not any(p.get("category") == "hero" for p in mod["pictures"]):
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
                print(f"Downloaded hero for {make_slug}/{model_slug}")

        for gen in mod.get("generations", []):
            scode = gen.get("series_code")
            match_q = next((q for s, q in gen_queries if s == scode), None)
            if match_q:
                imgs = search_wikimedia_images(match_q, limit=1)
                if imgs:
                    img = imgs[0]
                    fname = sanitize_filename(f"{make_slug}_{model_slug}_{scode}_{img['title']}") + ".jpg"
                    dest = MEDIA_DIR / "pictures" / make_slug / model_slug / fname
                    meta = download_file(img["source_url"], dest)
                    if meta:
                        if "pictures" not in gen:
                            gen["pictures"] = []
                        gen["pictures"].append({
                            "series_code": scode,
                            "category": "exterior",
                            "caption": img["caption"],
                            "source_url": img["source_url"],
                            "license_or_credit": img["license_or_credit"],
                            **meta
                        })
                        print(f"Downloaded gen pic for {make_slug}/{model_slug} [{scode}]")

        mpath.write_text(json.dumps(mod, indent=2, ensure_ascii=False), encoding="utf-8")

if __name__ == "__main__":
    main()
