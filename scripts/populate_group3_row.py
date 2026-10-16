"""
populate_group3_row.py - Populates Australian Car Archive catalog files for Group 3:
European, British, American, Chinese & Other Brands in Australia.
"""
import json
from pathlib import Path
import sys

# Add scripts directory to path to import modules
SCRIPTS_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPTS_DIR.parent
CATALOG_DIR = ROOT_DIR / "catalog"

sys.path.insert(0, str(SCRIPTS_DIR))

from group3_euro_makes import EURO_MAKES
from group3_british_makes import BRITISH_MAKES
from group3_american_makes import AMERICAN_MAKES
from group3_chinese_other_makes import CHINESE_OTHER_MAKES
from group3_models_data_1 import DEEP_DIVE_MODELS_PART1
from group3_models_data_2 import DEEP_DIVE_MODELS_PART2


def main():
    all_makes = {}
    all_makes.update(EURO_MAKES)
    all_makes.update(BRITISH_MAKES)
    all_makes.update(AMERICAN_MAKES)
    all_makes.update(CHINESE_OTHER_MAKES)

    all_models = {}
    all_models.update(DEEP_DIVE_MODELS_PART1)
    all_models.update(DEEP_DIVE_MODELS_PART2)

    print(f"=== POPULATING GROUP 3 CATALOG ===")
    print(f"Total Group 3 Makes to process: {len(all_makes)}")
    print(f"Total Group 3 Deep-Dive Models to process: {len(all_models)}")

    # 1. Write make.json files
    makes_written = 0
    total_catalog_models = 0
    for make_slug, make_data in sorted(all_makes.items()):
        make_dir = CATALOG_DIR / "makes" / make_slug
        make_dir.mkdir(parents=True, exist_ok=True)
        (make_dir / "models").mkdir(parents=True, exist_ok=True)

        make_json_path = make_dir / "make.json"
        existing = {}
        if make_json_path.exists():
            try:
                existing = json.loads(make_json_path.read_text(encoding="utf-8"))
            except Exception:
                pass

        # Merge preserving logo paths if already present
        merged_make = {**existing, **make_data}
        make_json_path.write_text(json.dumps(merged_make, indent=2, ensure_ascii=False), encoding="utf-8")
        makes_written += 1
        total_catalog_models += len(make_data.get("models_catalog", []))

    print(f"Successfully wrote {makes_written} make.json files with {total_catalog_models} catalogued models.")

    # 2. Write deep-dive model.json files
    models_written = 0
    total_generations = 0
    total_engines = 0
    total_badges = 0
    total_configs = 0

    for model_key, model_data in sorted(all_models.items()):
        make_slug, model_slug = model_key.split("/", 1)
        model_dir = CATALOG_DIR / "makes" / make_slug / "models" / model_slug
        model_dir.mkdir(parents=True, exist_ok=True)

        model_json_path = model_dir / "model.json"
        existing_model = {}
        if model_json_path.exists():
            try:
                existing_model = json.loads(model_json_path.read_text(encoding="utf-8"))
            except Exception:
                pass

        # If existing has manuals or pictures downloaded, preserve them
        if existing_model.get("manuals"):
            model_data["manuals"] = existing_model["manuals"]
        if existing_model.get("pictures"):
            model_data["pictures"] = existing_model["pictures"]

        model_json_path.write_text(json.dumps(model_data, indent=2, ensure_ascii=False), encoding="utf-8")
        models_written += 1

        for gen in model_data.get("generations", []):
            total_generations += 1
            total_engines += len(gen.get("engines", []))
            total_badges += len(gen.get("badges", []))
            total_configs += len(gen.get("configurations", []))

    print(f"Successfully wrote {models_written} deep-dive model.json files.")
    print(f"Deep-dive statistics:")
    print(f"  - Generations: {total_generations}")
    print(f"  - Engines: {total_engines}")
    print(f"  - Badges / Trims: {total_badges}")
    print(f"  - Configurations: {total_configs}")


if __name__ == "__main__":
    main()
