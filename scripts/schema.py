"""
Schema definition and validation utilities for the Australian Car Archive.
"""
from typing import Any, Dict, List, Optional
import json
from pathlib import Path

REQUIRED_MAKE_FIELDS = ["make_slug", "name", "country_of_origin", "years_active_au"]
REQUIRED_MODEL_FIELDS = ["make_slug", "model_slug", "name", "vehicle_type", "years_sold_au", "generations"]

def validate_make_dict(data: Dict[str, Any]) -> List[str]:
    errors = []
    for f in REQUIRED_MAKE_FIELDS:
        if f not in data:
            errors.append(f"Missing required make field: {f}")
    return errors

def validate_model_dict(data: Dict[str, Any]) -> List[str]:
    errors = []
    for f in REQUIRED_MODEL_FIELDS:
        if f not in data:
            errors.append(f"Missing required model field: {f}")
    if "generations" in data and not isinstance(data["generations"], list):
        errors.append("'generations' must be a list")
    return errors

def validate_catalog(catalog_dir: Path) -> Dict[str, Any]:
    makes_dir = catalog_dir / "makes"
    report = {
        "valid_makes": 0,
        "valid_models": 0,
        "errors": []
    }
    if not makes_dir.exists():
        return report

    for make_path in sorted(makes_dir.iterdir()):
        if not make_path.is_dir():
            continue
        make_json = make_path / "make.json"
        if make_json.exists():
            try:
                data = json.loads(make_json.read_text(encoding="utf-8"))
                errs = validate_make_dict(data)
                if errs:
                    report["errors"].append({"file": str(make_json), "errors": errs})
                else:
                    report["valid_makes"] += 1
            except Exception as e:
                report["errors"].append({"file": str(make_json), "errors": [str(e)]})
        
        models_dir = make_path / "models"
        if models_dir.exists():
            for model_path in sorted(models_dir.iterdir()):
                if not model_path.is_dir():
                    continue
                model_json = model_path / "model.json"
                if model_json.exists():
                    try:
                        mdata = json.loads(model_json.read_text(encoding="utf-8"))
                        merrs = validate_model_dict(mdata)
                        if merrs:
                            report["errors"].append({"file": str(model_json), "errors": merrs})
                        else:
                            report["valid_models"] += 1
                    except Exception as e:
                        report["errors"].append({"file": str(model_json), "errors": [str(e)]})
    return report

if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    res = validate_catalog(root / "catalog")
    print(json.dumps(res, indent=2))
