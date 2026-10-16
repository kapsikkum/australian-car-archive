"""
CLI tool to query the Australian Car Archive SQLite database (aus_cars.db).
Usage examples:
  python scripts/query_cli.py --search "Barra"
  python scripts/query_cli.py --make holden --model commodore
  python scripts/query_cli.py --engine "RB30"
  python scripts/query_cli.py --badge "XR6 Turbo"
"""
import argparse
import json
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = ROOT_DIR / "aus_cars.db"


def main():
    parser = argparse.ArgumentParser(description="Query the Australian Car Archive DB")
    parser.add_argument("--search", help="Full-text search across makes, models, and notes")
    parser.add_argument("--make", help="Filter by make slug (e.g. holden, ford, toyota)")
    parser.add_argument("--model", help="Filter by model slug (e.g. commodore, falcon, hilux)")
    parser.add_argument("--series", help="Filter by series code (e.g. VF, BA, N80)")
    parser.add_argument("--engine", help="Search engines by code or name (e.g. LS3, Barra, 1VD)")
    parser.add_argument("--badge", help="Search badges/trims (e.g. SS, XR6, GXL, STI)")
    parser.add_argument("--random", action="store_true", help="Show a random car listing from the archive")
    args = parser.parse_args()

    if not DB_PATH.exists():
        print("Database not found at aus_cars.db. Run python scripts/build_db.py first.")
        return

    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    if args.random:
        cur.execute(
            """
            SELECT make_slug, model_slug
            FROM models mod
            WHERE EXISTS (SELECT 1 FROM engines e WHERE e.make_slug = mod.make_slug AND e.model_slug = mod.model_slug)
            ORDER BY RANDOM()
            LIMIT 1
            """
        )
        picked = cur.fetchone()
        if picked:
            args.make = picked["make_slug"]
            args.model = picked["model_slug"]

    if args.search:
        cur.execute(
            "SELECT entity_type, make_slug, model_slug, title, snippet(search_index, 5, '[', ']', '...', 24) as match FROM search_index WHERE search_index MATCH ? LIMIT 25",
            (args.search,),
        )
        print(json.dumps([dict(r) for r in cur.fetchall()], indent=2))
        return

    if args.engine:
        cur.execute(
            """
            SELECT make_slug, model_slug, series_code, engine_code, name, displacement_litres,
                   cylinders, configuration, aspiration, fuel_type, power_kw, torque_nm
            FROM engines
            WHERE engine_code LIKE ? OR name LIKE ? OR notes LIKE ?
            ORDER BY power_kw DESC
            LIMIT 40
            """,
            (f"%{args.engine}%", f"%{args.engine}%", f"%{args.engine}%"),
        )
        print(json.dumps([dict(r) for r in cur.fetchall()], indent=2))
        return

    if args.badge:
        cur.execute(
            """
            SELECT make_slug, model_slug, series_code, badge_name, drivetrain,
                   msrp_aud_min, msrp_aud_max, fuel_consumption_l_100km, kerb_weight_kg
            FROM badges
            WHERE badge_name LIKE ?
            LIMIT 40
            """,
            (f"%{args.badge}%",),
        )
        print(json.dumps([dict(r) for r in cur.fetchall()], indent=2))
        return

    if args.make and args.model:
        cur.execute(
            "SELECT make_slug, model_slug, name, vehicle_type, segment, years_sold_au_start, years_sold_au_end, locally_built, assembly_plants_au, overview, australian_market_notes FROM models WHERE make_slug = ? AND model_slug = ?",
            (args.make, args.model),
        )
        mod = cur.fetchone()
        if not mod:
            print(f"No model found for {args.make}/{args.model}")
            return
        result = dict(mod)
        q_gen = "SELECT id, series_code, generation_name, years_start, years_end, body_styles_json, ancap_rating, summary FROM generations WHERE make_slug = ? AND model_slug = ?"
        params = [args.make, args.model]
        if args.series:
            q_gen += " AND series_code LIKE ?"
            params.append(f"%{args.series}%")
        cur.execute(q_gen, params)
        gens = []
        for g in cur.fetchall():
            gd = dict(g)
            cur.execute("SELECT engine_code, name, displacement_litres, cylinders, aspiration, fuel_type, power_kw, torque_nm FROM engines WHERE generation_id = ?", (gd["id"],))
            gd["engines"] = [dict(e) for e in cur.fetchall()]
            cur.execute("SELECT badge_name, drivetrain, msrp_aud_min, msrp_aud_max, fuel_consumption_l_100km FROM badges WHERE generation_id = ?", (gd["id"],))
            gd["badges"] = [dict(b) for b in cur.fetchall()]
            cur.execute("SELECT badge_name, body_style, engine_code, transmission, drivetrain, power_kw, torque_nm FROM configurations WHERE generation_id = ?", (gd["id"],))
            gd["configurations"] = [dict(c) for c in cur.fetchall()]
            gens.append(gd)
        result["generations"] = gens
        cur.execute("SELECT title, manual_type, year, local_path, source_url, file_size_bytes FROM manuals WHERE make_slug = ? AND model_slug = ?", (args.make, args.model))
        result["manuals"] = [dict(m) for m in cur.fetchall()]
        cur.execute("SELECT series_code, category, caption, local_path, source_url, file_size_bytes FROM pictures WHERE make_slug = ? AND model_slug = ?", (args.make, args.model))
        result["pictures"] = [dict(p) for p in cur.fetchall()]
        print(json.dumps(result, indent=2))
        return

    if args.make:
        cur.execute("SELECT make_slug, name, country_of_origin, years_active_au_start, years_active_au_end, currently_sold_au, local_manufacturer, overview, australian_history FROM makes WHERE make_slug = ?", (args.make,))
        mk = cur.fetchone()
        if not mk:
            print(f"Make not found: {args.make}")
            return
        res = dict(mk)
        cur.execute("SELECT model_slug, name, vehicle_type, years_sold_au_start, years_sold_au_end, locally_built FROM models WHERE make_slug = ? ORDER BY years_sold_au_start", (args.make,))
        res["models"] = [dict(m) for m in cur.fetchall()]
        print(json.dumps(res, indent=2))
        return

    parser.print_help()


if __name__ == "__main__":
    main()
