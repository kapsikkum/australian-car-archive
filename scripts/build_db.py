"""
Builds the normalized SQLite database (aus_cars.db) from the file-based JSON catalog.
"""
import json
import sqlite3
from pathlib import Path
from typing import Any, Dict

ROOT_DIR = Path(__file__).resolve().parent.parent
CATALOG_DIR = ROOT_DIR / "catalog"
DB_PATH = ROOT_DIR / "aus_cars.db"

SCHEMA_SQL = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS makes (
    make_slug TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    country_of_origin TEXT,
    years_active_au_start INTEGER,
    years_active_au_end TEXT,
    currently_sold_au INTEGER DEFAULT 0,
    local_manufacturer INTEGER DEFAULT 0,
    logo_local_path TEXT,
    logo_source_url TEXT,
    overview TEXT,
    australian_history TEXT,
    raw_json TEXT
);

CREATE TABLE IF NOT EXISTS models (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    make_slug TEXT NOT NULL REFERENCES makes(make_slug) ON DELETE CASCADE,
    model_slug TEXT NOT NULL,
    name TEXT NOT NULL,
    vehicle_type TEXT,
    segment TEXT,
    years_sold_au_start INTEGER,
    years_sold_au_end TEXT,
    locally_built INTEGER DEFAULT 0,
    assembly_plants_au TEXT,
    overview TEXT,
    australian_market_notes TEXT,
    raw_json TEXT,
    UNIQUE(make_slug, model_slug)
);

CREATE TABLE IF NOT EXISTS generations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id INTEGER NOT NULL REFERENCES models(id) ON DELETE CASCADE,
    make_slug TEXT NOT NULL,
    model_slug TEXT NOT NULL,
    series_code TEXT NOT NULL,
    generation_name TEXT,
    years_start INTEGER,
    years_end TEXT,
    body_styles_json TEXT,
    platform TEXT,
    ancap_rating TEXT,
    summary TEXT,
    raw_json TEXT,
    UNIQUE(model_id, series_code)
);

CREATE TABLE IF NOT EXISTS engines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    generation_id INTEGER NOT NULL REFERENCES generations(id) ON DELETE CASCADE,
    make_slug TEXT NOT NULL,
    model_slug TEXT NOT NULL,
    series_code TEXT NOT NULL,
    engine_code TEXT,
    name TEXT,
    displacement_cc INTEGER,
    displacement_litres REAL,
    cylinders INTEGER,
    configuration TEXT,
    aspiration TEXT,
    fuel_type TEXT,
    power_kw REAL,
    power_rpm TEXT,
    torque_nm REAL,
    torque_rpm TEXT,
    compression_ratio TEXT,
    valvetrain TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS badges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    generation_id INTEGER NOT NULL REFERENCES generations(id) ON DELETE CASCADE,
    make_slug TEXT NOT NULL,
    model_slug TEXT NOT NULL,
    series_code TEXT NOT NULL,
    badge_name TEXT NOT NULL,
    years_start INTEGER,
    years_end TEXT,
    body_styles_json TEXT,
    drivetrain TEXT,
    transmissions_json TEXT,
    msrp_aud_min INTEGER,
    msrp_aud_max INTEGER,
    fuel_consumption_l_100km REAL,
    kerb_weight_kg INTEGER,
    standard_features_json TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS configurations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    generation_id INTEGER NOT NULL REFERENCES generations(id) ON DELETE CASCADE,
    make_slug TEXT NOT NULL,
    model_slug TEXT NOT NULL,
    series_code TEXT NOT NULL,
    badge_name TEXT,
    body_style TEXT,
    engine_code TEXT,
    transmission TEXT,
    drivetrain TEXT,
    years_start INTEGER,
    years_end TEXT,
    msrp_aud INTEGER,
    power_kw REAL,
    torque_nm REAL,
    fuel_l_100km REAL,
    towing_braked_kg INTEGER,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS manuals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    make_slug TEXT NOT NULL,
    model_slug TEXT,
    series_code TEXT,
    title TEXT NOT NULL,
    manual_type TEXT,
    year INTEGER,
    language TEXT DEFAULT 'en',
    source_url TEXT,
    local_path TEXT,
    file_size_bytes INTEGER,
    sha256 TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS pictures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    make_slug TEXT NOT NULL,
    model_slug TEXT,
    series_code TEXT,
    badge_name TEXT,
    category TEXT,
    caption TEXT,
    year INTEGER,
    source_url TEXT,
    local_path TEXT,
    license_or_credit TEXT,
    file_size_bytes INTEGER,
    sha256 TEXT
);

CREATE VIRTUAL TABLE IF NOT EXISTS search_index USING fts5(
    entity_type,
    make_slug,
    model_slug,
    series_code,
    title,
    body
);
"""


def parse_years(val: Any) -> tuple[Any, Any]:
    if isinstance(val, dict):
        return val.get("start"), str(val.get("end")) if val.get("end") is not None else None
    if isinstance(val, str) and "-" in val:
        parts = val.split("-", 1)
        try:
            start = int(parts[0].strip())
        except ValueError:
            start = None
        return start, parts[1].strip()
    if isinstance(val, int):
        return val, str(val)
    return None, None


def build_database() -> Dict[str, int]:
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()
    cur.executescript(SCHEMA_SQL)

    counts = {
        "makes": 0,
        "models": 0,
        "generations": 0,
        "engines": 0,
        "badges": 0,
        "configurations": 0,
        "manuals": 0,
        "pictures": 0,
    }

    # 1. Load makes_index.json if present as baseline
    makes_index_file = CATALOG_DIR / "makes_index.json"
    indexed_makes: Dict[str, Dict[str, Any]] = {}
    if makes_index_file.exists():
        try:
            idx_data = json.loads(makes_index_file.read_text(encoding="utf-8"))
            items = idx_data.get("makes", idx_data) if isinstance(idx_data, dict) else idx_data
            for item in items:
                if isinstance(item, dict) and "make_slug" in item:
                    indexed_makes[item["make_slug"]] = item
        except Exception as e:
            print(f"Warning: could not parse makes_index.json: {e}")

    # 2. Scan catalog/makes/<make_slug>/make.json
    makes_dir = CATALOG_DIR / "makes"
    if makes_dir.exists():
        for make_folder in sorted(makes_dir.iterdir()):
            if not make_folder.is_dir():
                continue
            make_json_path = make_folder / "make.json"
            if make_json_path.exists():
                try:
                    mdata = json.loads(make_json_path.read_text(encoding="utf-8"))
                    slug = mdata.get("make_slug", make_folder.name)
                    merged = {**indexed_makes.get(slug, {}), **mdata}
                    indexed_makes[slug] = merged
                except Exception as e:
                    print(f"Warning reading {make_json_path}: {e}")

    # Insert all makes
    for slug, mdata in sorted(indexed_makes.items()):
        y_start, y_end = parse_years(mdata.get("years_active_au"))
        cur.execute(
            """
            INSERT OR REPLACE INTO makes (
                make_slug, name, country_of_origin, years_active_au_start, years_active_au_end,
                currently_sold_au, local_manufacturer, logo_local_path, logo_source_url,
                overview, australian_history, raw_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                slug,
                mdata.get("name", slug.replace("-", " ").title()),
                mdata.get("country_of_origin"),
                y_start,
                y_end,
                1 if mdata.get("currently_sold_au") else 0,
                1 if mdata.get("local_manufacturer") else 0,
                mdata.get("logo_local_path"),
                mdata.get("logo_source_url"),
                mdata.get("overview"),
                mdata.get("australian_history"),
                json.dumps(mdata, ensure_ascii=False),
            ),
        )
        counts["makes"] += 1
        cur.execute(
            "INSERT INTO search_index VALUES (?, ?, ?, ?, ?, ?)",
            (
                "make",
                slug,
                "",
                "",
                mdata.get("name", slug),
                f"{mdata.get('country_of_origin', '')} {mdata.get('overview', '')} {mdata.get('australian_history', '')}",
            ),
        )

        # Also check if make.json has embedded models_summary or models list
        embedded_models = mdata.get("models_catalog", [])
        if isinstance(embedded_models, list):
            for em in embedded_models:
                if not isinstance(em, dict) or "model_slug" not in em:
                    continue
                mslug = em["model_slug"]
                # Only insert stub if full model.json doesn't exist
                full_model_path = makes_dir / slug / "models" / mslug / "model.json"
                if not full_model_path.exists():
                    my_start, my_end = parse_years(em.get("years_sold_au"))
                    cur.execute(
                        """
                        INSERT OR IGNORE INTO models (
                            make_slug, model_slug, name, vehicle_type, segment,
                            years_sold_au_start, years_sold_au_end, locally_built,
                            assembly_plants_au, overview, australian_market_notes, raw_json
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            slug,
                            mslug,
                            em.get("name", mslug.replace("-", " ").title()),
                            em.get("vehicle_type"),
                            em.get("segment"),
                            my_start,
                            my_end,
                            1 if em.get("locally_built") else 0,
                            json.dumps(em.get("assembly_plants_au")) if isinstance(em.get("assembly_plants_au"), list) else em.get("assembly_plants_au"),
                            em.get("overview"),
                            em.get("australian_market_notes"),
                            json.dumps(em, ensure_ascii=False),
                        ),
                    )
                    if cur.rowcount > 0:
                        counts["models"] += 1
                        model_id = cur.lastrowid
                        for gen in em.get("generations", []):
                            if isinstance(gen, dict):
                                scode = str(gen.get("series_code") or gen.get("generation_name") or "GEN1")
                                gy_start, gy_end = parse_years(gen.get("years"))
                                cur.execute(
                                    """
                                    INSERT OR IGNORE INTO generations (
                                        model_id, make_slug, model_slug, series_code, generation_name,
                                        years_start, years_end, body_styles_json, platform, ancap_rating,
                                        summary, raw_json
                                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                    """,
                                    (
                                        model_id,
                                        slug,
                                        mslug,
                                        scode,
                                        gen.get("generation_name"),
                                        gy_start,
                                        gy_end,
                                        json.dumps(gen.get("body_styles", [])),
                                        gen.get("platform"),
                                        gen.get("ancap_rating"),
                                        gen.get("summary"),
                                        json.dumps(gen, ensure_ascii=False),
                                    ),
                                )
                                if cur.rowcount > 0:
                                    counts["generations"] += 1

    # 3. Scan full model.json files
    if makes_dir.exists():
        for make_folder in sorted(makes_dir.iterdir()):
            if not make_folder.is_dir():
                continue
            slug = make_folder.name
            # Ensure make exists in DB
            cur.execute("SELECT 1 FROM makes WHERE make_slug = ?", (slug,))
            if not cur.fetchone():
                cur.execute(
                    "INSERT INTO makes (make_slug, name) VALUES (?, ?)",
                    (slug, slug.replace("-", " ").title()),
                )
                counts["makes"] += 1

            models_dir = make_folder / "models"
            if not models_dir.exists():
                continue

            for model_folder in sorted(models_dir.iterdir()):
                if not model_folder.is_dir():
                    continue
                model_json_path = model_folder / "model.json"
                if not model_json_path.exists():
                    continue
                try:
                    mod = json.loads(model_json_path.read_text(encoding="utf-8"))
                except Exception as e:
                    print(f"Error parsing {model_json_path}: {e}")
                    continue

                mslug = mod.get("model_slug", model_folder.name)
                my_start, my_end = parse_years(mod.get("years_sold_au"))

                cur.execute(
                    """
                    INSERT OR REPLACE INTO models (
                        make_slug, model_slug, name, vehicle_type, segment,
                        years_sold_au_start, years_sold_au_end, locally_built,
                        assembly_plants_au, overview, australian_market_notes, raw_json
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        slug,
                        mslug,
                        mod.get("name", mslug.replace("-", " ").title()),
                        mod.get("vehicle_type"),
                        mod.get("segment"),
                        my_start,
                        my_end,
                        1 if mod.get("locally_built") else 0,
                        json.dumps(mod.get("assembly_plants_au")) if isinstance(mod.get("assembly_plants_au"), list) else mod.get("assembly_plants_au"),
                        mod.get("overview"),
                        mod.get("australian_market_notes"),
                        json.dumps(mod, ensure_ascii=False),
                    ),
                )
                model_id = cur.lastrowid
                counts["models"] += 1

                cur.execute(
                    "INSERT INTO search_index VALUES (?, ?, ?, ?, ?, ?)",
                    (
                        "model",
                        slug,
                        mslug,
                        "",
                        f"{slug.title()} {mod.get('name', mslug)}",
                        f"{mod.get('overview', '')} {mod.get('australian_market_notes', '')}",
                    ),
                )

                # Model-level manuals & pictures
                for man in mod.get("manuals", []):
                    if isinstance(man, dict):
                        cur.execute(
                            """
                            INSERT INTO manuals (
                                make_slug, model_slug, series_code, title, manual_type,
                                year, language, source_url, local_path, file_size_bytes, sha256, notes
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                            (
                                slug,
                                mslug,
                                man.get("series_code"),
                                man.get("title", "Manual"),
                                man.get("manual_type") or man.get("type"),
                                man.get("year"),
                                man.get("language", "en"),
                                man.get("source_url"),
                                man.get("local_path"),
                                man.get("file_size_bytes"),
                                man.get("sha256"),
                                man.get("notes"),
                            ),
                        )
                        counts["manuals"] += 1

                for pic in mod.get("pictures", []):
                    if isinstance(pic, dict):
                        cur.execute(
                            """
                            INSERT INTO pictures (
                                make_slug, model_slug, series_code, badge_name, category,
                                caption, year, source_url, local_path, license_or_credit,
                                file_size_bytes, sha256
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                            (
                                slug,
                                mslug,
                                pic.get("series_code"),
                                pic.get("badge_name") or pic.get("badge"),
                                pic.get("category", "exterior"),
                                pic.get("caption"),
                                pic.get("year"),
                                pic.get("source_url"),
                                pic.get("local_path"),
                                pic.get("license_or_credit"),
                                pic.get("file_size_bytes"),
                                pic.get("sha256"),
                            ),
                        )
                        counts["pictures"] += 1

                # Generations
                for idx, gen in enumerate(mod.get("generations", [])):
                    if not isinstance(gen, dict):
                        continue
                    scode = str(gen.get("series_code") or gen.get("generation_name") or f"GEN_{idx+1}")
                    gy_start, gy_end = parse_years(gen.get("years"))
                    cur.execute(
                        """
                        INSERT OR REPLACE INTO generations (
                            model_id, make_slug, model_slug, series_code, generation_name,
                            years_start, years_end, body_styles_json, platform, ancap_rating,
                            summary, raw_json
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            model_id,
                            slug,
                            mslug,
                            scode,
                            gen.get("generation_name"),
                            gy_start,
                            gy_end,
                            json.dumps(gen.get("body_styles", [])),
                            gen.get("platform"),
                            str(gen.get("ancap_rating")) if gen.get("ancap_rating") is not None else None,
                            gen.get("summary") or gen.get("overview"),
                            json.dumps(gen, ensure_ascii=False),
                        ),
                    )
                    gen_id = cur.lastrowid
                    counts["generations"] += 1

                    # Engines
                    for eng in gen.get("engines", []):
                        if not isinstance(eng, dict):
                            continue
                        cur.execute(
                            """
                            INSERT INTO engines (
                                generation_id, make_slug, model_slug, series_code,
                                engine_code, name, displacement_cc, displacement_litres,
                                cylinders, configuration, aspiration, fuel_type,
                                power_kw, power_rpm, torque_nm, torque_rpm,
                                compression_ratio, valvetrain, notes
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                            (
                                gen_id,
                                slug,
                                mslug,
                                scode,
                                eng.get("engine_code"),
                                eng.get("name"),
                                eng.get("displacement_cc"),
                                eng.get("displacement_litres"),
                                eng.get("cylinders"),
                                eng.get("configuration"),
                                eng.get("aspiration"),
                                eng.get("fuel_type"),
                                eng.get("power_kw"),
                                str(eng.get("power_rpm")) if eng.get("power_rpm") is not None else None,
                                eng.get("torque_nm"),
                                str(eng.get("torque_rpm")) if eng.get("torque_rpm") is not None else None,
                                eng.get("compression_ratio"),
                                eng.get("valvetrain"),
                                eng.get("notes"),
                            ),
                        )
                        counts["engines"] += 1

                    # Badges / trims
                    for bdg in gen.get("badges", []):
                        if not isinstance(bdg, dict):
                            continue
                        by_start, by_end = parse_years(bdg.get("years") or gen.get("years"))
                        cur.execute(
                            """
                            INSERT INTO badges (
                                generation_id, make_slug, model_slug, series_code,
                                badge_name, years_start, years_end, body_styles_json,
                                drivetrain, transmissions_json, msrp_aud_min, msrp_aud_max,
                                fuel_consumption_l_100km, kerb_weight_kg, standard_features_json, notes
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                            (
                                gen_id,
                                slug,
                                mslug,
                                scode,
                                bdg.get("badge_name") or bdg.get("name", "Base"),
                                by_start,
                                by_end,
                                json.dumps(bdg.get("body_styles", [])),
                                bdg.get("drivetrain"),
                                json.dumps(bdg.get("transmissions", [])),
                                bdg.get("msrp_aud_min") or bdg.get("msrp_aud"),
                                bdg.get("msrp_aud_max") or bdg.get("msrp_aud"),
                                bdg.get("fuel_consumption_l_100km"),
                                bdg.get("kerb_weight_kg"),
                                json.dumps(bdg.get("standard_features", [])),
                                bdg.get("notes"),
                            ),
                        )
                        counts["badges"] += 1

                    # Configurations
                    for cfg in gen.get("configurations", []):
                        if not isinstance(cfg, dict):
                            continue
                        cy_start, cy_end = parse_years(cfg.get("years") or gen.get("years"))
                        cur.execute(
                            """
                            INSERT INTO configurations (
                                generation_id, make_slug, model_slug, series_code,
                                badge_name, body_style, engine_code, transmission,
                                drivetrain, years_start, years_end, msrp_aud,
                                power_kw, torque_nm, fuel_l_100km, towing_braked_kg, notes
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                            (
                                gen_id,
                                slug,
                                mslug,
                                scode,
                                cfg.get("badge_name") or cfg.get("badge"),
                                cfg.get("body_style"),
                                cfg.get("engine_code"),
                                cfg.get("transmission"),
                                cfg.get("drivetrain"),
                                cy_start,
                                cy_end,
                                cfg.get("msrp_aud"),
                                cfg.get("power_kw"),
                                cfg.get("torque_nm"),
                                cfg.get("fuel_l_100km"),
                                cfg.get("towing_braked_kg"),
                                cfg.get("notes"),
                            ),
                        )
                        counts["configurations"] += 1

                    # Generation-level manuals & pictures
                    for man in gen.get("manuals", []):
                        if isinstance(man, dict):
                            cur.execute(
                                """
                                INSERT INTO manuals (
                                    make_slug, model_slug, series_code, title, manual_type,
                                    year, language, source_url, local_path, file_size_bytes, sha256, notes
                                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                """,
                                (
                                    slug,
                                    mslug,
                                    scode,
                                    man.get("title", "Manual"),
                                    man.get("manual_type") or man.get("type"),
                                    man.get("year"),
                                    man.get("language", "en"),
                                    man.get("source_url"),
                                    man.get("local_path"),
                                    man.get("file_size_bytes"),
                                    man.get("sha256"),
                                    man.get("notes"),
                                ),
                            )
                            counts["manuals"] += 1

                    for pic in gen.get("pictures", []):
                        if isinstance(pic, dict):
                            cur.execute(
                                """
                                INSERT INTO pictures (
                                    make_slug, model_slug, series_code, badge_name, category,
                                    caption, year, source_url, local_path, license_or_credit,
                                    file_size_bytes, sha256
                                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                """,
                                (
                                    slug,
                                    mslug,
                                    scode,
                                    pic.get("badge_name") or pic.get("badge"),
                                    pic.get("category", "exterior"),
                                    pic.get("caption"),
                                    pic.get("year"),
                                    pic.get("source_url"),
                                    pic.get("local_path"),
                                    pic.get("license_or_credit"),
                                    pic.get("file_size_bytes"),
                                    pic.get("sha256"),
                                ),
                            )
                            counts["pictures"] += 1

    # Re-calculate exact row counts from tables
    for tbl in counts.keys():
        cur.execute(f"SELECT COUNT(*) FROM {tbl}")
        counts[tbl] = cur.fetchone()[0]

    conn.commit()
    conn.close()
    return counts


if __name__ == "__main__":
    stats = build_database()
    print(f"Database built at: {DB_PATH}")
    print(json.dumps(stats, indent=2))
