"""
download_wave2_media.py - Generates local PDF technical manuals and downloads Wikimedia photos
for all 24 Wave 2 models.
"""
import sys
import time
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from manual_builder import generate_model_pdf_manual
from media_downloader import enrich_model_pictures

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


def main():
    print(f"=== PROCESSING MANUALS & MEDIA FOR 24 WAVE 2 MODELS ===")
    
    manuals_count = 0
    for make, model in WAVE2_MODELS:
        print(f"Generating PDF Technical Manual: {make}/{model} ...")
        res = generate_model_pdf_manual(make, model)
        if res:
            manuals_count += 1
            print(f"  -> Generated: {res.get('local_path')} ({res.get('file_size_bytes')} bytes)")
        else:
            print(f"  -> [WARN] Failed to generate manual for {make}/{model}")

    print(f"\nCompleted {manuals_count}/24 PDF manuals generated.\n")
    print(f"=== DOWNLOADING WIKIMEDIA COMMONS PICTURES ===")
    
    total_pics = 0
    for make, model in WAVE2_MODELS:
        print(f"Downloading pictures for: {make}/{model} ...")
        pics = enrich_model_pictures(make, model, max_per_gen=1)
        total_pics += pics
        print(f"  -> Downloaded {pics} media files for {make}/{model}")
        time.sleep(0.5)

    print(f"\nTotal media files processed: {total_pics}")
    print(f"All 24 models enriched with PDF manuals and photos.")


if __name__ == "__main__":
    main()
