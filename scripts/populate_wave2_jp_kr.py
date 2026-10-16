"""
Populate Wave 2: 26 Iconic Japanese & South Korean Models in the Australian Car Archive.
Creates catalog/makes/<make_slug>/models/<model_slug>/model.json files
and ensures make.json models_catalog reflects all newly cataloged models.
"""
import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
CATALOG_DIR = ROOT_DIR / "catalog"
MAKES_DIR = CATALOG_DIR / "makes"

if str(ROOT_DIR / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR / "scripts"))

from group2_wave2_data import ALL_WAVE2_MODELS


def update_make_catalog(model_data: dict):
    """Ensures the make.json models_catalog contains the model_slug."""
    make_slug = model_data["make_slug"]
    model_slug = model_data["model_slug"]
    make_json_path = MAKES_DIR / make_slug / "make.json"

    if not make_json_path.exists():
        return

    try:
        make_data = json.loads(make_json_path.read_text(encoding="utf-8"))
        catalog = make_data.get("models_catalog", [])
        existing_slugs = [m.get("model_slug") for m in catalog if isinstance(m, dict)]

        if model_slug not in existing_slugs:
            # Build catalog entry from model_data
            gens_summary = []
            for g in model_data.get("generations", []):
                gens_summary.append({
                    "series_code": g.get("series_code"),
                    "generation_name": g.get("generation_name"),
                    "years": g.get("years"),
                    "body_styles": g.get("body_styles", []),
                    "summary": g.get("summary", "")[:120]
                })

            entry = {
                "model_slug": model_slug,
                "name": model_data.get("name"),
                "vehicle_type": model_data.get("vehicle_type"),
                "segment": model_data.get("segment"),
                "years_sold_au": model_data.get("years_sold_au"),
                "locally_built": model_data.get("locally_built", False),
                "overview": model_data.get("overview", "")[:180],
                "generations": gens_summary
            }
            catalog.append(entry)
            make_data["models_catalog"] = catalog
            make_json_path.write_text(json.dumps(make_data, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"  [UPDATED] Added '{model_slug}' to {make_slug}/make.json models_catalog")
    except Exception as e:
        print(f"  [WARN] Failed to update make catalog for {make_slug}: {e}")


def populate_models():
    print(f"=== Populating Wave 2: {len(ALL_WAVE2_MODELS)} Japanese & Korean Models ===")
    stats = {
        "models": 0,
        "generations": 0,
        "engines": 0,
        "badges": 0,
        "configurations": 0,
    }

    for model in ALL_WAVE2_MODELS:
        make_slug = model["make_slug"]
        model_slug = model["model_slug"]
        model_dir = MAKES_DIR / make_slug / "models" / model_slug
        model_dir.mkdir(parents=True, exist_ok=True)
        model_json_path = model_dir / "model.json"

        # Preserve existing manuals/pictures if already generated
        if model_json_path.exists():
            try:
                existing = json.loads(model_json_path.read_text(encoding="utf-8"))
                if existing.get("manuals") and not model.get("manuals"):
                    model["manuals"] = existing["manuals"]
                if existing.get("pictures") and not model.get("pictures"):
                    model["pictures"] = existing["pictures"]
                # Also preserve generation-level pictures/manuals if any
                for i, gen in enumerate(model.get("generations", [])):
                    if i < len(existing.get("generations", [])):
                        ex_gen = existing["generations"][i]
                        if ex_gen.get("pictures") and not gen.get("pictures"):
                            gen["pictures"] = ex_gen["pictures"]
                        if ex_gen.get("manuals") and not gen.get("manuals"):
                            gen["manuals"] = ex_gen["manuals"]
            except Exception:
                pass

        model_json_path.write_text(json.dumps(model, indent=2, ensure_ascii=False), encoding="utf-8")
        update_make_catalog(model)
        stats["models"] += 1

        gen_count = len(model.get("generations", []))
        eng_count = sum(len(g.get("engines", [])) for g in model.get("generations", []))
        badge_count = sum(len(g.get("badges", [])) for g in model.get("generations", []))
        cfg_count = sum(len(g.get("configurations", [])) for g in model.get("generations", []))

        stats["generations"] += gen_count
        stats["engines"] += eng_count
        stats["badges"] += badge_count
        stats["configurations"] += cfg_count

        print(
            f"  [OK] Model '{make_slug}/{model_slug}': {gen_count} gens, "
            f"{eng_count} engines, {badge_count} badges, {cfg_count} configs"
        )

    print("\n==========================================")
    print("Wave 2 Models Population Complete:")
    print(f"  Models created:        {stats['models']}")
    print(f"  Generations:           {stats['generations']}")
    print(f"  Engines:               {stats['engines']}")
    print(f"  Badges/Trims:          {stats['badges']}")
    print(f"  Configurations:        {stats['configurations']}")
    print("==========================================")
    return stats


if __name__ == "__main__":
    populate_models()
