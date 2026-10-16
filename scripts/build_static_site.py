"""
Builds static JSON data files (data/init.json and data/makes/<make_slug>.json) from aus_cars.db
so the entire Australian Automotive Archive runs 100% client-side on GitHub Pages.
"""
import json
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = ROOT_DIR / "aus_cars.db"
DATA_DIR = ROOT_DIR / "data"


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def build_static_data() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    makes_data_dir = DATA_DIR / "makes"
    makes_data_dir.mkdir(parents=True, exist_ok=True)

    conn = get_db_connection()
    cur = conn.cursor()

    # 1. Stats
    tables = ["makes", "models", "generations", "engines", "badges", "configurations", "manuals", "pictures"]
    stats = {}
    for t in tables:
        cur.execute(f"SELECT COUNT(*) FROM {t}")
        stats[t] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(DISTINCT make_slug || '/' || model_slug) FROM engines")
    stats["deep_dive_models"] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM makes WHERE local_manufacturer = 1")
    stats["local_makes"] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM models WHERE locally_built = 1")
    stats["local_models"] = cur.fetchone()[0]

    # 2. All Makes list
    cur.execute(
        """
        SELECT m.make_slug, m.name, m.country_of_origin, m.years_active_au_start, m.years_active_au_end,
               m.currently_sold_au, m.local_manufacturer, m.overview,
               COUNT(DISTINCT mod.id) as model_count,
               COUNT(DISTINCT g.id) as generation_count,
               COUNT(DISTINCT e.id) as engine_count,
               COUNT(DISTINCT p.id) as picture_count
        FROM makes m
        LEFT JOIN models mod ON mod.make_slug = m.make_slug
        LEFT JOIN generations g ON g.make_slug = m.make_slug
        LEFT JOIN engines e ON e.make_slug = m.make_slug
        LEFT JOIN pictures p ON p.make_slug = m.make_slug AND p.local_path IS NOT NULL
        GROUP BY m.make_slug
        ORDER BY m.name ASC
        """
    )
    makes_list = [dict(r) for r in cur.fetchall()]

    # 3. Featured deep-dive models + all models index (for Random Car & instant global search)
    cur.execute(
        """
        SELECT mod.id, mod.make_slug, mk.name as make_name, mod.model_slug, mod.name, mod.vehicle_type,
               mod.years_sold_au_start, mod.years_sold_au_end, mod.locally_built, mod.overview,
               COUNT(DISTINCT g.id) as generation_count,
               COUNT(DISTINCT e.id) as engine_count,
               COUNT(DISTINCT b.id) as badge_count,
               COUNT(DISTINCT man.id) as manual_count,
               (SELECT local_path FROM pictures p WHERE p.make_slug = mod.make_slug AND p.model_slug = mod.model_slug AND p.local_path IS NOT NULL LIMIT 1) as hero_image
        FROM models mod
        JOIN makes mk ON mk.make_slug = mod.make_slug
        LEFT JOIN generations g ON g.model_id = mod.id
        LEFT JOIN engines e ON e.make_slug = mod.make_slug AND e.model_slug = mod.model_slug
        LEFT JOIN badges b ON b.make_slug = mod.make_slug AND b.model_slug = mod.model_slug
        LEFT JOIN manuals man ON man.make_slug = mod.make_slug AND man.model_slug = mod.model_slug
        GROUP BY mod.id
        ORDER BY mod.locally_built DESC, engine_count DESC, mod.make_slug ASC
        """
    )
    all_models_summary = [dict(r) for r in cur.fetchall()]
    featured_models = [m for m in all_models_summary if m["engine_count"] > 0]

    # 4. All Engines list
    cur.execute(
        """
        SELECT make_slug, model_slug, series_code, engine_code, name, displacement_litres,
               displacement_cc, cylinders, configuration, aspiration, fuel_type, power_kw, torque_nm, notes
        FROM engines
        ORDER BY power_kw DESC
        """
    )
    all_engines = [dict(r) for r in cur.fetchall()]

    # 5. All Badges list (for instant search)
    cur.execute(
        """
        SELECT make_slug, model_slug, series_code, badge_name, drivetrain, msrp_aud_min, msrp_aud_max, notes
        FROM badges
        """
    )
    all_badges = [dict(r) for r in cur.fetchall()]

    # Save data/init.json
    init_payload = {
        "stats": stats,
        "makes": makes_list,
        "featured_models": featured_models,
        "all_models": all_models_summary,
        "engines": all_engines,
        "badges": all_badges,
    }
    (DATA_DIR / "init.json").write_text(json.dumps(init_payload, ensure_ascii=False), encoding="utf-8")

    # 6. Build per-make JSON files: data/makes/<make_slug>.json
    for m_item in makes_list:
        make_slug = m_item["make_slug"]
        cur.execute(
            """
            SELECT make_slug, name, country_of_origin, years_active_au_start, years_active_au_end,
                   currently_sold_au, local_manufacturer, overview, australian_history
            FROM makes WHERE make_slug = ?
            """,
            (make_slug,),
        )
        mk_row = dict(cur.fetchone())

        make_models = [m for m in all_models_summary if m["make_slug"] == make_slug]
        mk_row["models"] = make_models
        mk_row["models_detail"] = {}

        for mod_sum in make_models:
            mslug = mod_sum["model_slug"]
            cur.execute(
                """
                SELECT id, make_slug, model_slug, name, vehicle_type, segment,
                       years_sold_au_start, years_sold_au_end, locally_built,
                       assembly_plants_au, overview, australian_market_notes
                FROM models WHERE id = ?
                """,
                (mod_sum["id"],),
            )
            mod_full = dict(cur.fetchone())

            cur.execute(
                "SELECT id, series_code, generation_name, years_start, years_end, body_styles_json, platform, ancap_rating, summary FROM generations WHERE model_id = ? ORDER BY years_start ASC, id ASC",
                (mod_full["id"],),
            )
            gens = []
            for g in cur.fetchall():
                gd = dict(g)
                try:
                    gd["body_styles"] = json.loads(gd.get("body_styles_json") or "[]")
                except Exception:
                    gd["body_styles"] = []
                cur.execute(
                    "SELECT engine_code, name, displacement_cc, displacement_litres, cylinders, configuration, aspiration, fuel_type, power_kw, power_rpm, torque_nm, torque_rpm, compression_ratio, valvetrain, notes FROM engines WHERE generation_id = ?",
                    (gd["id"],),
                )
                gd["engines"] = [dict(e) for e in cur.fetchall()]
                cur.execute(
                    "SELECT badge_name, years_start, years_end, body_styles_json, drivetrain, transmissions_json, msrp_aud_min, msrp_aud_max, fuel_consumption_l_100km, kerb_weight_kg, standard_features_json, notes FROM badges WHERE generation_id = ?",
                    (gd["id"],),
                )
                badges = []
                for b in cur.fetchall():
                    bd = dict(b)
                    try:
                        bd["transmissions"] = json.loads(bd.get("transmissions_json") or "[]")
                    except Exception:
                        bd["transmissions"] = []
                    try:
                        bd["standard_features"] = json.loads(bd.get("standard_features_json") or "[]")
                    except Exception:
                        bd["standard_features"] = []
                    badges.append(bd)
                gd["badges"] = badges
                cur.execute(
                    "SELECT badge_name, body_style, engine_code, transmission, drivetrain, years_start, years_end, msrp_aud, power_kw, torque_nm, fuel_l_100km, towing_braked_kg, notes FROM configurations WHERE generation_id = ?",
                    (gd["id"],),
                )
                gd["configurations"] = [dict(c) for c in cur.fetchall()]
                gens.append(gd)
            mod_full["generations"] = gens

            cur.execute(
                "SELECT series_code, title, manual_type, year, source_url, local_path, file_size_bytes, sha256, notes FROM manuals WHERE make_slug = ? AND model_slug = ?",
                (make_slug, mslug),
            )
            mod_full["manuals"] = [dict(m) for m in cur.fetchall()]

            cur.execute(
                "SELECT series_code, badge_name, category, caption, year, source_url, local_path, license_or_credit, file_size_bytes, sha256 FROM pictures WHERE make_slug = ? AND model_slug = ?",
                (make_slug, mslug),
            )
            mod_full["pictures"] = [dict(p) for p in cur.fetchall()]

            mk_row["models_detail"][mslug] = mod_full

        (makes_data_dir / f"{make_slug}.json").write_text(
            json.dumps(mk_row, ensure_ascii=False), encoding="utf-8"
        )

    conn.close()
    (ROOT_DIR / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Static data generated in {DATA_DIR} ({len(makes_list)} make bundles).")


if __name__ == "__main__":
    build_static_data()
