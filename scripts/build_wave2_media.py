"""
Builds PDF manuals and downloads Wikimedia pictures for all Wave 2 Japanese and Korean models.
"""
import sys
from pathlib import Path
import time

ROOT_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT_DIR / "scripts"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from group2_wave2_data import ALL_WAVE2_MODELS
from manual_builder import generate_model_pdf_manual
from media_downloader import enrich_model_pictures


def main():
    print(f"=== Generating PDF Manuals & Downloading Media for {len(ALL_WAVE2_MODELS)} Models ===")
    total_manuals = 0
    total_pictures = 0

    for idx, model in enumerate(ALL_WAVE2_MODELS, 1):
        make_slug = model["make_slug"]
        model_slug = model["model_slug"]
        print(f"\n[{idx}/{len(ALL_WAVE2_MODELS)}] Processing {make_slug}/{model_slug}...")

        # 1. Generate PDF Manual
        try:
            manual_meta = generate_model_pdf_manual(make_slug, model_slug)
            if manual_meta:
                total_manuals += 1
                print(f"  [PDF] Generated manual: {manual_meta.get('local_path')}")
        except Exception as e:
            print(f"  [WARN] Failed manual generation for {make_slug}/{model_slug}: {e}")

        # 2. Enrich Wikimedia Media
        try:
            pic_count = enrich_model_pictures(make_slug, model_slug, max_per_gen=1)
            total_pictures += pic_count
            print(f"  [MEDIA] Downloaded {pic_count} media files.")
        except Exception as e:
            print(f"  [WARN] Failed media download for {make_slug}/{model_slug}: {e}")

        time.sleep(0.5)

    print("\n==========================================")
    print("Wave 2 Media Processing Complete:")
    print(f"  PDF Manuals generated: {total_manuals}")
    print(f"  Media files fetched:   {total_pictures}")
    print("==========================================")


if __name__ == "__main__":
    main()
