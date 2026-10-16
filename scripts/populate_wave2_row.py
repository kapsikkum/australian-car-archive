"""
populate_wave2_row.py - Creates 24 deep-dive model.json files for Wave 2 Group 3 (Euro, British, US, Asian).
"""
import json
from pathlib import Path
import sys

SCRIPTS_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPTS_DIR.parent
CATALOG_DIR = ROOT_DIR / "catalog"

sys.path.insert(0, str(SCRIPTS_DIR))

from wave2_row_data_1 import WAVE2_MODELS_PART1
from wave2_row_data_2 import WAVE2_MODELS_PART2
from wave2_row_data_3 import WAVE2_MODELS_PART3


def update_make_catalog(make_slug: str, model_data: dict):
    make_json_path = CATALOG_DIR / "makes" / make_slug / "make.json"
    if not make_json_path.exists():
        return
    try:
        make_data = json.loads(make_json_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error reading {make_json_path}: {e}")
        return

    models_catalog = make_data.setdefault("models_catalog", [])
    model_slug = model_data["model_slug"]

    # Build catalog entry
    cat_gens = []
    for g in model_data.get("generations", []):
        cat_gens.append({
            "series_code": g.get("series_code", ""),
            "generation_name": g.get("generation_name", ""),
            "years": g.get("years", {}),
            "body_styles": g.get("body_styles", []),
            "summary": g.get("summary", "")
        })

    cat_entry = {
        "model_slug": model_slug,
        "name": model_data.get("name", model_slug.title()),
        "vehicle_type": model_data.get("vehicle_type", "Passenger Car"),
        "segment": model_data.get("segment", "Medium Car"),
        "years_sold_au": model_data.get("years_sold_au", {}),
        "locally_built": model_data.get("locally_built", False),
        "overview": model_data.get("overview", ""),
        "generations": cat_gens
    }

    # Find existing or append
    found_idx = None
    for idx, m in enumerate(models_catalog):
        if m.get("model_slug") == model_slug:
            found_idx = idx
            break

    if found_idx is not None:
        models_catalog[found_idx] = cat_entry
    else:
        models_catalog.append(cat_entry)

    make_json_path.write_text(json.dumps(make_data, indent=2, ensure_ascii=False), encoding="utf-8")


def main():
    all_models = {}
    all_models.update(WAVE2_MODELS_PART1)
    all_models.update(WAVE2_MODELS_PART2)
    all_models.update(WAVE2_MODELS_PART3)

    print(f"=== POPULATING WAVE 2 GROUP 3 MODELS ===")
    print(f"Total Wave 2 Models to process: {len(all_models)}")

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

        # If existing has manuals or pictures already populated, preserve them
        if existing_model.get("manuals"):
            model_data["manuals"] = existing_model["manuals"]
        if existing_model.get("pictures"):
            model_data["pictures"] = existing_model["pictures"]

        model_json_path.write_text(json.dumps(model_data, indent=2, ensure_ascii=False), encoding="utf-8")
        models_written += 1

        # Also update make.json
        update_make_catalog(make_slug, model_data)

        for gen in model_data.get("generations", []):
            total_generations += 1
            total_engines += len(gen.get("engines", []))
            total_badges += len(gen.get("badges", []))
            total_configs += len(gen.get("configurations", []))

    print(f"Successfully wrote {models_written} deep-dive model.json files and updated make catalogs.")
    print(f"Wave 2 Deep-Dive Statistics:")
    print(f"  - Generations: {total_generations}")
    print(f"  - Engines: {total_engines}")
    print(f"  - Badges / Trims: {total_badges}")
    print(f"  - Configurations: {total_configs}")


if __name__ == "__main__":
    main()
