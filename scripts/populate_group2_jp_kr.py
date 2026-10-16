"""
Populates Group 2: Japanese & South Korean Brands in the Australian Car Archive.
Updates catalog/makes/<make_slug>/make.json for all 17 assigned makes.
Creates catalog/makes/<make_slug>/models/<model_slug>/model.json for the 16 deep-dive models.
"""
import json
import sys
from pathlib import Path

# Set up paths
ROOT_DIR = Path(__file__).resolve().parent.parent
CATALOG_DIR = ROOT_DIR / "catalog"
MAKES_DIR = CATALOG_DIR / "makes"

# Add scripts to sys.path
if str(ROOT_DIR / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR / "scripts"))

from group2_data.makes_catalog import ALL_GROUP2_MAKES
from group2_data.toyota_models import TOYOTA_DEEP_DIVES
from group2_data.mazda_models import MAZDA_DEEP_DIVES
from group2_data.mitsubishi_models import MITSUBISHI_DEEP_DIVES
from group2_data.nissan_models import NISSAN_DEEP_DIVES
from group2_data.subaru_models import SUBARU_DEEP_DIVES
from group2_data.korean_models import KOREAN_DEEP_DIVES

ALL_DEEP_DIVES = (
    TOYOTA_DEEP_DIVES
    + MAZDA_DEEP_DIVES
    + MITSUBISHI_DEEP_DIVES
    + NISSAN_DEEP_DIVES
    + SUBARU_DEEP_DIVES
    + KOREAN_DEEP_DIVES
)


def populate_makes() -> int:
    print(f"--- Populating Phase 1: {len(ALL_GROUP2_MAKES)} Group 2 Makes ---")
    count = 0
    for make_data in ALL_GROUP2_MAKES:
        slug = make_data["make_slug"]
        make_dir = MAKES_DIR / slug
        make_dir.mkdir(parents=True, exist_ok=True)
        make_json_path = make_dir / "make.json"

        # Load existing if available to preserve any extra custom fields
        existing_data = {}
        if make_json_path.exists():
            try:
                existing_data = json.loads(make_json_path.read_text(encoding="utf-8"))
            except Exception as e:
                print(f"  [WARN] Failed to parse existing {make_json_path}: {e}")

        merged_data = {**existing_data, **make_data}
        make_json_path.write_text(json.dumps(merged_data, indent=2, ensure_ascii=False), encoding="utf-8")
        models_count = len(make_data.get("models_catalog", []))
        print(f"  [OK] Make '{slug}': written ({models_count} catalog models)")
        count += 1
    return count


def populate_deep_dive_models() -> dict:
    print(f"\n--- Populating Phase 2: {len(ALL_DEEP_DIVES)} Deep-Dive Models ---")
    stats = {
        "models": 0,
        "generations": 0,
        "engines": 0,
        "badges": 0,
        "configurations": 0,
    }

    for model in ALL_DEEP_DIVES:
        make_slug = model["make_slug"]
        model_slug = model["model_slug"]
        model_dir = MAKES_DIR / make_slug / "models" / model_slug
        model_dir.mkdir(parents=True, exist_ok=True)
        model_json_path = model_dir / "model.json"

        # Preserve any existing downloaded pictures or manuals if re-running
        if model_json_path.exists():
            try:
                existing = json.loads(model_json_path.read_text(encoding="utf-8"))
                if existing.get("manuals") and not model.get("manuals"):
                    model["manuals"] = existing["manuals"]
                if existing.get("pictures") and not model.get("pictures"):
                    model["pictures"] = existing["pictures"]
            except Exception:
                pass

        model_json_path.write_text(json.dumps(model, indent=2, ensure_ascii=False), encoding="utf-8")
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

    return stats


def main():
    makes_count = populate_makes()
    stats = populate_deep_dive_models()
    print("\n==========================================")
    print("Group 2 Population Complete:")
    print(f"  Makes updated:         {makes_count}")
    print(f"  Deep-dive models:      {stats['models']}")
    print(f"  Generations:           {stats['generations']}")
    print(f"  Engines:               {stats['engines']}")
    print(f"  Badges/Trims:          {stats['badges']}")
    print(f"  Configurations:        {stats['configurations']}")
    print("==========================================")


if __name__ == "__main__":
    main()
