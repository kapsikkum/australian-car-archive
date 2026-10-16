"""
Populate Australian Car Archive - Wave 2 Group 1 Subagent:
Australian Domestic Manufacturers & Icons (25 Deep-Dive Models).

Models:
- Holden:
  1. 48-215 (FX)
  2. FJ
  3. FE-FC-FB-EK
  4. EJ-EH-HD-HR
  5. Astra
  6. Barina
  7. Cruze
  8. Rodeo
  9. Jackaroo
  10. Captiva
  11. Sandman
  12. Adventra-Crewman
- Ford:
  13. Cortina
  14. Escort
  15. Capri
  16. Laser
  17. Focus
  18. Mustang
  19. Everest
  20. F-Series
- Chrysler-Valiant:
  21. Centura
  22. Sigma
  23. Dodge Phoenix
- Leyland Australia:
  24. Austin 1800
  25. Morris Major / Austin Freeway & Wolseley 24/80
"""
import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

ROOT_DIR = Path(__file__).resolve().parent.parent
CATALOG_DIR = ROOT_DIR / "catalog"
MAKES_DIR = CATALOG_DIR / "makes"

# Import datasets from wave2 modules
from wave2_models_holden_1 import MODEL_48_215, MODEL_FJ, MODEL_FE_FC_FB_EK, MODEL_EJ_EH_HD_HR
from wave2_models_holden_2 import MODEL_ASTRA, MODEL_BARINA, MODEL_CRUZE, MODEL_RODEO
from wave2_models_holden_3 import MODEL_JACKAROO, MODEL_CAPTIVA, MODEL_SANDMAN, MODEL_ADVENTRA_CREWMAN
from wave2_models_ford_1 import MODEL_CORTINA, MODEL_ESCORT, MODEL_CAPRI, MODEL_LASER
from wave2_models_ford_2 import MODEL_FOCUS, MODEL_MUSTANG, MODEL_EVEREST, MODEL_F_SERIES
from wave2_models_chrysler_leyland import (
    MODEL_CENTURA,
    MODEL_SIGMA,
    MODEL_DODGE_PHOENIX,
    MODEL_AUSTIN_1800,
    MODEL_MORRIS_MAJOR_FREEWAY,
)

ALL_WAVE2_MODELS: List[Dict[str, Any]] = [
    # Holden (12)
    MODEL_48_215,
    MODEL_FJ,
    MODEL_FE_FC_FB_EK,
    MODEL_EJ_EH_HD_HR,
    MODEL_ASTRA,
    MODEL_BARINA,
    MODEL_CRUZE,
    MODEL_RODEO,
    MODEL_JACKAROO,
    MODEL_CAPTIVA,
    MODEL_SANDMAN,
    MODEL_ADVENTRA_CREWMAN,
    # Ford (8)
    MODEL_CORTINA,
    MODEL_ESCORT,
    MODEL_CAPRI,
    MODEL_LASER,
    MODEL_FOCUS,
    MODEL_MUSTANG,
    MODEL_EVEREST,
    MODEL_F_SERIES,
    # Chrysler-Valiant (3)
    MODEL_CENTURA,
    MODEL_SIGMA,
    MODEL_DODGE_PHOENIX,
    # Leyland Australia (2)
    MODEL_AUSTIN_1800,
    MODEL_MORRIS_MAJOR_FREEWAY,
]


def update_make_json_catalog(models: List[Dict[str, Any]]):
    """Ensure every model slug is represented in its make.json models_catalog list."""
    print("\n--- Updating make.json models_catalog (if needed) ---")
    models_by_make: Dict[str, List[Dict[str, Any]]] = {}
    for m in models:
        models_by_make.setdefault(m["make_slug"], []).append(m)

    for make_slug, model_list in models_by_make.items():
        make_file = MAKES_DIR / make_slug / "make.json"
        if not make_file.exists():
            continue
        try:
            make_data = json.loads(make_file.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  [WARN] Failed to read {make_file}: {e}")
            continue

        if "models_catalog" not in make_data or not isinstance(make_data["models_catalog"], list):
            make_data["models_catalog"] = []

        existing_slugs = {item.get("model_slug") for item in make_data["models_catalog"] if isinstance(item, dict)}
        added_count = 0
        for m in model_list:
            mslug = m["model_slug"]
            if mslug not in existing_slugs:
                entry = {
                    "model_slug": mslug,
                    "name": m.get("name", mslug.replace("-", " ").title()),
                    "vehicle_type": m.get("vehicle_type", "Passenger Car"),
                    "segment": m.get("segment", "Large"),
                    "years_sold_au": m.get("years_sold_au", {}),
                    "locally_built": m.get("locally_built", False),
                    "overview": m.get("overview", "")[:300] + "...",
                    "generations": [
                        {
                            "series_code": g.get("series_code", "GEN"),
                            "generation_name": g.get("generation_name", ""),
                            "years": g.get("years", {}),
                            "body_styles": g.get("body_styles", []),
                            "summary": g.get("summary", "")[:200]
                        }
                        for g in m.get("generations", [])
                    ]
                }
                make_data["models_catalog"].append(entry)
                existing_slugs.add(mslug)
                added_count += 1

        if added_count > 0:
            make_file.write_text(json.dumps(make_data, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"  [OK] {make_slug}: Added {added_count} missing models to models_catalog")
        else:
            print(f"  [OK] {make_slug}: All model slugs already present in make.json")


def write_deep_dive_models() -> int:
    """Write model.json for all 25 models."""
    print("\n--- Writing Wave 2 Deep-Dive Models (Phase 1) ---")
    count = 0
    for mod in ALL_WAVE2_MODELS:
        make_slug = mod["make_slug"]
        model_slug = mod["model_slug"]
        model_dir = MAKES_DIR / make_slug / "models" / model_slug
        model_dir.mkdir(parents=True, exist_ok=True)
        model_json_path = model_dir / "model.json"

        # If existing model.json has manuals/pictures from prior run, preserve them
        if model_json_path.exists():
            try:
                existing = json.loads(model_json_path.read_text(encoding="utf-8"))
                if existing.get("manuals"):
                    mod["manuals"] = existing["manuals"]
                if existing.get("pictures"):
                    mod["pictures"] = existing["pictures"]
            except Exception:
                pass

        model_json_path.write_text(json.dumps(mod, indent=2, ensure_ascii=False), encoding="utf-8")
        num_gens = len(mod.get("generations", []))
        total_eng = sum(len(g.get("engines", [])) for g in mod.get("generations", []))
        total_bdg = sum(len(g.get("badges", [])) for g in mod.get("generations", []))
        total_cfg = sum(len(g.get("configurations", [])) for g in mod.get("generations", []))
        print(f"  [OK] {make_slug:18} / {model_slug:24}: Saved model.json ({num_gens} gen, {total_eng} eng, {total_bdg} bdg, {total_cfg} cfg)")
        count += 1
    return count


def generate_pdf_manuals() -> int:
    """Run manual_builder.py for each of the 25 models."""
    print("\n--- Generating PDF Technical Specification Manuals (Phase 2) ---")
    script = ROOT_DIR / "scripts" / "manual_builder.py"
    generated = 0
    for mod in ALL_WAVE2_MODELS:
        make_slug = mod["make_slug"]
        model_slug = mod["model_slug"]
        cmd = [sys.executable, str(script), "--make", make_slug, "--model", model_slug]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            generated += 1
            print(f"  [PDF OK] {make_slug}/{model_slug} manual generated.")
        else:
            print(f"  [PDF ERR] {make_slug}/{model_slug}: {res.stderr}")
    return generated


def download_media_pictures() -> int:
    """Run media_downloader.py for each of the 25 models."""
    print("\n--- Downloading Pictures & Media from Wikimedia Commons (Phase 3) ---")
    script = ROOT_DIR / "scripts" / "media_downloader.py"
    processed = 0
    for idx, mod in enumerate(ALL_WAVE2_MODELS, start=1):
        make_slug = mod["make_slug"]
        model_slug = mod["model_slug"]
        print(f"  [{idx:2}/25] Fetching media for {make_slug}/{model_slug}...")
        cmd = [sys.executable, str(script), "--make", make_slug, "--model", model_slug, "--max-per-gen", "1"]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            processed += 1
            # print output line
            for line in res.stdout.strip().split("\n"):
                if "Downloaded" in line or "Total media" in line:
                    print(f"        {line.strip()}")
        else:
            print(f"  [MEDIA WARN] {make_slug}/{model_slug}: {res.stderr.strip()[:100]}")
    return processed


def validate_all():
    """Run schema.py to validate the whole catalog."""
    print("\n--- Validating Schema Compliance (Phase 4) ---")
    script = ROOT_DIR / "scripts" / "schema.py"
    res = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
    print(res.stdout)


def summarize_stats():
    """Prints total stats of created models."""
    total_models = len(ALL_WAVE2_MODELS)
    total_gens = sum(len(m.get("generations", [])) for m in ALL_WAVE2_MODELS)
    total_engines = sum(sum(len(g.get("engines", [])) for g in m.get("generations", [])) for m in ALL_WAVE2_MODELS)
    total_badges = sum(sum(len(g.get("badges", [])) for g in m.get("generations", [])) for m in ALL_WAVE2_MODELS)
    total_configs = sum(sum(len(g.get("configurations", [])) for g in m.get("generations", [])) for m in ALL_WAVE2_MODELS)

    print("\n================================================================================")
    print("WAVE 2 GROUP 1 SUMMARY:")
    print(f"  Target Models Created:      {total_models}")
    print(f"  Generations Cataloged:      {total_gens}")
    print(f"  Engine Variants Defined:    {total_engines}")
    print(f"  Trim Badges Configured:     {total_badges}")
    print(f"  Factory Configurations:     {total_configs}")
    print("================================================================================")


if __name__ == "__main__":
    print("================================================================================")
    print("Australian Car Archive: Wave 2 Group 1 - Australian & Classic Icons")
    print("================================================================================")
    update_make_json_catalog(ALL_WAVE2_MODELS)
    models_written = write_deep_dive_models()
    pdf_count = generate_pdf_manuals()
    download_media_pictures()
    validate_all()
    summarize_stats()
    print("\n=== Wave 2 Group 1 catalog population completed! ===")
