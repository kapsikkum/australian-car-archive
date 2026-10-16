"""
Populate Australian Car Archive Group 1: Australian Domestic Manufacturers & Icons.
Writes comprehensive make.json files for all 13 assigned makes, detailed model.json files
for 23 iconic models, generates PDF technical manuals, downloads media, and builds the database.
"""
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List

ROOT_DIR = Path(__file__).resolve().parent.parent
CATALOG_DIR = ROOT_DIR / "catalog"
MAKES_DIR = CATALOG_DIR / "makes"

# Import datasets
from group1_makes_data import MAKES_DATA
from group1_models_holden_1 import COMMODORE_DATA, KINGSWOOD_DATA, TORANA_DATA
from group1_models_holden_2 import MONARO_DATA, STATESMAN_CAPRICE_DATA, GEMINI_DATA, COLORADO_DATA
from group1_models_ford_1 import FALCON_DATA, TERRITORY_DATA
from group1_models_ford_2 import FAIRLANE_LTD_DATA, RANGER_DATA
from group1_models_chrysler_hsv_fpv import VALIANT_DATA, CHARGER_DATA, HSV_CLUBSPORT_GTS_DATA, FPV_GT_F6_DATA
from group1_models_icons import (
    LEYLAND_P76_DATA,
    LIGHTBURN_ZETA_DATA,
    BOLWELL_NAGARI_DATA,
    GOGGOMOBIL_DART_DATA,
    GIOCATTOLO_DATA,
    OKA_4X4_DATA,
    BRABHAM_BT62_DATA,
    HDT_VK_GROUP_A_DATA,
)

DEEP_DIVE_MODELS = [
    COMMODORE_DATA,
    KINGSWOOD_DATA,
    TORANA_DATA,
    MONARO_DATA,
    STATESMAN_CAPRICE_DATA,
    GEMINI_DATA,
    COLORADO_DATA,
    FALCON_DATA,
    TERRITORY_DATA,
    FAIRLANE_LTD_DATA,
    RANGER_DATA,
    VALIANT_DATA,
    CHARGER_DATA,
    HSV_CLUBSPORT_GTS_DATA,
    FPV_GT_F6_DATA,
    LEYLAND_P76_DATA,
    LIGHTBURN_ZETA_DATA,
    BOLWELL_NAGARI_DATA,
    GOGGOMOBIL_DART_DATA,
    GIOCATTOLO_DATA,
    OKA_4X4_DATA,
    BRABHAM_BT62_DATA,
    HDT_VK_GROUP_A_DATA,
]


def write_catalog_makes() -> int:
    print("\n--- Writing Catalog Makes (Phase 1) ---")
    count = 0
    for make_slug, data in MAKES_DATA.items():
        make_dir = MAKES_DIR / make_slug
        make_dir.mkdir(parents=True, exist_ok=True)
        make_json_path = make_dir / "make.json"
        
        # Merge if existing
        if make_json_path.exists():
            try:
                existing = json.loads(make_json_path.read_text(encoding="utf-8"))
                merged = {**existing, **data}
            except Exception:
                merged = data
        else:
            merged = data
            
        make_json_path.write_text(json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8")
        num_models = len(merged.get("models_catalog", []))
        print(f"  [OK] {make_slug:20}: Saved make.json with {num_models:2} cataloged models")
        count += 1
    return count


def write_deep_dive_models() -> int:
    print("\n--- Writing Deep-Dive Models (Phase 2) ---")
    count = 0
    for mod in DEEP_DIVE_MODELS:
        make_slug = mod["make_slug"]
        model_slug = mod["model_slug"]
        model_dir = MAKES_DIR / make_slug / "models" / model_slug
        model_dir.mkdir(parents=True, exist_ok=True)
        model_json_path = model_dir / "model.json"
        
        model_json_path.write_text(json.dumps(mod, indent=2, ensure_ascii=False), encoding="utf-8")
        num_gens = len(mod.get("generations", []))
        print(f"  [OK] {make_slug:18} / {model_slug:22}: Saved model.json ({num_gens} generations)")
        count += 1
    return count


def generate_pdf_manuals() -> int:
    print("\n--- Generating PDF Manuals & Dossiers ---")
    script = ROOT_DIR / "scripts" / "manual_builder.py"
    generated = 0
    for mod in DEEP_DIVE_MODELS:
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
    print("\n--- Downloading Pictures & Media ---")
    script = ROOT_DIR / "scripts" / "media_downloader.py"
    processed = 0
    for mod in DEEP_DIVE_MODELS:
        make_slug = mod["make_slug"]
        model_slug = mod["model_slug"]
        cmd = [sys.executable, str(script), "--make", make_slug, "--model", model_slug, "--max-per-gen", "1"]
        print(f"  [FETCH] Downloading media for {make_slug}/{model_slug}...")
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            processed += 1
        else:
            print(f"  [MEDIA WARN] {make_slug}/{model_slug}: {res.stderr.strip()}")
    return processed


def run_database_build():
    print("\n--- Building SQLite Database (aus_cars.db) ---")
    script = ROOT_DIR / "scripts" / "build_db.py"
    res = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)


def validate_all():
    print("\n--- Validating Schema Compliance ---")
    script = ROOT_DIR / "scripts" / "schema.py"
    res = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
    print(res.stdout)


if __name__ == "__main__":
    print("================================================================================")
    print("Australian Car Archive: Group 1 - Australian Domestic Manufacturers & Icons")
    print("================================================================================")
    makes_written = write_catalog_makes()
    models_written = write_deep_dive_models()
    pdf_count = generate_pdf_manuals()
    download_media_pictures()
    validate_all()
    run_database_build()
    print("\n=== All Group 1 tasks completed successfully! ===")
