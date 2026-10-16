"""
enrich_wave2_photos.py - Enriches any generation in the 24 Wave 2 models that lacks photos
using clean, targeted Wikimedia search queries.
"""
import json
import re
import time
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
CATALOG_DIR = ROOT_DIR / "catalog"
MEDIA_DIR = ROOT_DIR / "media"

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from media_downloader import search_wikimedia_images, download_file, sanitize_filename

WAVE2_MODELS = [
    ("volkswagen", "beetle-kombi"),
    ("volkswagen", "tiguan"),
    ("volkswagen", "polo"),
    ("bmw", "5-series-m5"),
    ("bmw", "x5"),
    ("mercedes-benz", "e-class"),
    ("mercedes-benz", "g-class"),
    ("audi", "a3-s3-rs3"),
    ("audi", "q5-sq5"),
    ("porsche", "911"),
    ("porsche", "cayenne-macan"),
    ("volvo", "240-850"),
    ("saab", "900-9-3"),
    ("skoda", "octavia"),
    ("peugeot", "205-308-gti"),
    ("renault", "clio-megane-rs"),
    ("alfa-romeo", "giulia-gtv"),
    ("fiat", "500-abarth"),
    ("land-rover", "range-rover-discovery"),
    ("jaguar", "xj-xjs"),
    ("chevrolet-gmsv", "corvette-silverado"),
    ("jeep", "grand-cherokee"),
    ("ldv", "t60"),
    ("proton", "jumbuck-satria"),
]

CLEAN_QUERIES = {
    ("volkswagen", "beetle-kombi", "Type 1"): "Volkswagen Beetle Type 1",
    ("volkswagen", "beetle-kombi", "Type 197"): "Volkswagen Country Buggy",
    ("volkswagen", "beetle-kombi", "Type 2"): "Volkswagen Kombi T2",
    ("audi", "a3-s3-rs3", "8L"): "Audi S3 8L",
    ("audi", "a3-s3-rs3", "8P"): "Audi RS3 8P",
    ("audi", "a3-s3-rs3", "8V"): "Audi RS3 8V",
    ("audi", "a3-s3-rs3", "8Y"): "Audi RS3 8Y",
    ("audi", "q5-sq5", "8R"): "Audi SQ5 8R",
    ("audi", "q5-sq5", "FY"): "Audi Q5 FY",
    ("volvo", "240-850", "240 Series"): "Volvo 240 GL",
    ("volvo", "240-850", "850 Series"): "Volvo 850 R",
    ("peugeot", "205-308-gti", "205 GTi"): "Peugeot 205 GTI",
    ("peugeot", "205-308-gti", "306 GTi-6"): "Peugeot 306 GTI",
    ("peugeot", "205-308-gti", "308 GTi"): "Peugeot 308 GTI",
    ("alfa-romeo", "giulia-gtv", "105/115 Series"): "Alfa Romeo 2000 GTV Bertone",
    ("alfa-romeo", "giulia-gtv", "Alfetta GTV"): "Alfa Romeo Alfetta GTV6",
    ("alfa-romeo", "giulia-gtv", "952 Series"): "Alfa Romeo Giulia Quadrifoglio",
    ("chevrolet-gmsv", "corvette-silverado", "C8 Corvette"): "Chevrolet Corvette C8 Stingray",
    ("chevrolet-gmsv", "corvette-silverado", "Silverado 1500"): "Chevrolet Silverado 1500 ZR2",
    ("chevrolet-gmsv", "corvette-silverado", "Silverado 2500HD"): "Chevrolet Silverado 2500HD",
    ("proton", "jumbuck-satria", "Satria C99"): "Proton Satria GTi",
    ("proton", "jumbuck-satria", "Jumbuck C90"): "Proton Jumbuck ute",
    ("proton", "jumbuck-satria", "Satria Neo"): "Proton Satria Neo",
}


def main():
    print("=== ENRICHING MISSING PHOTOS FOR WAVE 2 GENERATIONS ===")
    total_added = 0
    
    for make_slug, model_slug in WAVE2_MODELS:
        mpath = CATALOG_DIR / "makes" / make_slug / "models" / model_slug / "model.json"
        if not mpath.exists():
            continue
        try:
            mdata = json.loads(mpath.read_text(encoding="utf-8"))
        except Exception:
            continue

        changed = False
        make_display = make_slug.replace("-", " ").title()
        if make_slug == "mercedes-benz":
            make_display = "Mercedes-Benz"
        elif make_slug == "chevrolet-gmsv":
            make_display = "Chevrolet"

        for gen in mdata.get("generations", []):
            scode = gen.get("series_code", "")
            pics = gen.setdefault("pictures", [])
            has_local = any(p.get("local_path") for p in pics if isinstance(p, dict))
            if not has_local:
                query = CLEAN_QUERIES.get((make_slug, model_slug, scode))
                if not query:
                    gname = gen.get("generation_name", scode)
                    query = f"{make_display} {gname}"
                
                print(f"Searching: '{query}' for {make_slug}/{model_slug} [{scode}] ...")
                results = search_wikimedia_images(query, limit=1)
                if not results:
                    # fallback to simpler query
                    results = search_wikimedia_images(f"{make_display} {scode}", limit=1)
                
                if results:
                    item = results[0]
                    fname = sanitize_filename(f"{make_slug}_{model_slug}_{scode}_1_{item['title']}")
                    if not (fname.lower().endswith(".jpg") or fname.lower().endswith(".png")):
                        fname += ".jpg"
                    dest = MEDIA_DIR / "pictures" / make_slug / model_slug / fname
                    meta = download_file(item["source_url"], dest)
                    if meta:
                        pics.append({
                            "series_code": scode,
                            "category": "exterior",
                            "caption": item["caption"],
                            "source_url": item["source_url"],
                            "license_or_credit": item["license_or_credit"],
                            **meta
                        })
                        total_added += 1
                        changed = True
                        print(f"  -> Added {fname} ({meta['file_size_bytes']} bytes)")
                time.sleep(0.3)

        if changed:
            mpath.write_text(json.dumps(mdata, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nTotal additional photos enriched: {total_added}")


if __name__ == "__main__":
    main()
