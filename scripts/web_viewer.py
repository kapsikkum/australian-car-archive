"""
Local Web UI Server for the Australian Automotive Archive.
Serves the interactive frontend (web/index.html), JSON REST API backed by aus_cars.db,
and static media files (media/pictures/ and media/manuals/).

Usage:
  python scripts/web_viewer.py --port 8080
"""
import argparse
import json
import mimetypes
import sqlite3
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = ROOT_DIR / "aus_cars.db"
WEB_DIR = ROOT_DIR / "web"
MEDIA_DIR = ROOT_DIR / "media"


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


class ArchiveRequestHandler(BaseHTTPRequestHandler):
    def log_message(self, format: str, *args) -> None:
        # Keep console output clean
        pass

    def send_json(self, data: object, status: int = 200) -> None:
        payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(payload)

    def send_file(self, file_path: Path) -> None:
        if not file_path.exists() or not file_path.is_file():
            self.send_error(404, "File not found")
            return
        ctype, _ = mimetypes.guess_type(str(file_path))
        if not ctype:
            ctype = "application/octet-stream"
        data = file_path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        qs = urllib.parse.parse_qs(parsed.query)

        if path == "/" or path == "/index.html":
            self.send_file(WEB_DIR / "index.html")
            return

        if path.startswith("/media/"):
            rel = path.lstrip("/")
            target = (ROOT_DIR / rel).resolve()
            if MEDIA_DIR.resolve() in target.parents:
                self.send_file(target)
                return
            self.send_error(403, "Forbidden")
            return

        if path == "/api/stats":
            conn = get_db_connection()
            cur = conn.cursor()
            tables = ["makes", "models", "generations", "engines", "badges", "configurations", "manuals", "pictures"]
            counts = {}
            for t in tables:
                cur.execute(f"SELECT COUNT(*) FROM {t}")
                counts[t] = cur.fetchone()[0]
            cur.execute("SELECT COUNT(DISTINCT make_slug || '/' || model_slug) FROM engines")
            counts["deep_dive_models"] = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM makes WHERE local_manufacturer = 1")
            counts["local_makes"] = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM models WHERE locally_built = 1")
            counts["local_models"] = cur.fetchone()[0]
            conn.close()
            self.send_json(counts)
            return

        if path == "/api/makes":
            conn = get_db_connection()
            cur = conn.cursor()
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
            rows = [dict(r) for r in cur.fetchall()]
            conn.close()
            self.send_json(rows)
            return

        if path.startswith("/api/makes/") and "/models/" not in path:
            make_slug = path.split("/api/makes/", 1)[1].strip("/")
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                """
                SELECT make_slug, name, country_of_origin, years_active_au_start, years_active_au_end,
                       currently_sold_au, local_manufacturer, overview, australian_history
                FROM makes WHERE make_slug = ?
                """,
                (make_slug,),
            )
            mk = cur.fetchone()
            if not mk:
                conn.close()
                self.send_json({"error": "Make not found"}, 404)
                return
            res = dict(mk)
            cur.execute(
                """
                SELECT mod.id, mod.make_slug, mod.model_slug, mod.name, mod.vehicle_type, mod.segment,
                       mod.years_sold_au_start, mod.years_sold_au_end, mod.locally_built, mod.assembly_plants_au,
                       mod.overview,
                       COUNT(DISTINCT g.id) as generation_count,
                       COUNT(DISTINCT e.id) as engine_count,
                       COUNT(DISTINCT b.id) as badge_count,
                       COUNT(DISTINCT man.id) as manual_count,
                       (SELECT local_path FROM pictures p WHERE p.make_slug = mod.make_slug AND p.model_slug = mod.model_slug AND p.local_path IS NOT NULL LIMIT 1) as hero_image
                FROM models mod
                LEFT JOIN generations g ON g.model_id = mod.id
                LEFT JOIN engines e ON e.make_slug = mod.make_slug AND e.model_slug = mod.model_slug
                LEFT JOIN badges b ON b.make_slug = mod.make_slug AND b.model_slug = mod.model_slug
                LEFT JOIN manuals man ON man.make_slug = mod.make_slug AND man.model_slug = mod.model_slug
                WHERE mod.make_slug = ?
                GROUP BY mod.id
                ORDER BY engine_count DESC, mod.years_sold_au_start ASC, mod.name ASC
                """,
                (make_slug,),
            )
            res["models"] = [dict(r) for r in cur.fetchall()]
            conn.close()
            self.send_json(res)
            return

        if path.startswith("/api/makes/") and "/models/" in path:
            parts = path.split("/api/makes/", 1)[1].split("/models/", 1)
            make_slug = parts[0].strip("/")
            model_slug = parts[1].strip("/")
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                """
                SELECT id, make_slug, model_slug, name, vehicle_type, segment,
                       years_sold_au_start, years_sold_au_end, locally_built,
                       assembly_plants_au, overview, australian_market_notes
                FROM models WHERE make_slug = ? AND model_slug = ?
                """,
                (make_slug, model_slug),
            )
            mod = cur.fetchone()
            if not mod:
                conn.close()
                self.send_json({"error": "Model not found"}, 404)
                return
            res = dict(mod)
            cur.execute(
                "SELECT id, series_code, generation_name, years_start, years_end, body_styles_json, platform, ancap_rating, summary FROM generations WHERE model_id = ? ORDER BY years_start ASC, id ASC",
                (res["id"],),
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
            res["generations"] = gens

            cur.execute(
                "SELECT series_code, title, manual_type, year, source_url, local_path, file_size_bytes, sha256, notes FROM manuals WHERE make_slug = ? AND model_slug = ?",
                (make_slug, model_slug),
            )
            res["manuals"] = [dict(m) for m in cur.fetchall()]

            cur.execute(
                "SELECT series_code, badge_name, category, caption, year, source_url, local_path, license_or_credit, file_size_bytes, sha256 FROM pictures WHERE make_slug = ? AND model_slug = ?",
                (make_slug, model_slug),
            )
            res["pictures"] = [dict(p) for p in cur.fetchall()]
            conn.close()
            self.send_json(res)
            return

        if path == "/api/models/featured":
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                """
                SELECT mod.make_slug, mk.name as make_name, mod.model_slug, mod.name, mod.vehicle_type,
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
                HAVING engine_count > 0
                ORDER BY mod.locally_built DESC, engine_count DESC, mod.make_slug ASC
                LIMIT 200
                """
            )
            rows = [dict(r) for r in cur.fetchall()]
            conn.close()
            self.send_json(rows)
            return

        if path == "/api/models/random":
            scope = (qs.get("scope", ["deep"])[0]).strip().lower()
            conn = get_db_connection()
            cur = conn.cursor()
            if scope == "all":
                cur.execute(
                    """
                    SELECT mod.make_slug, mk.name as make_name, mod.model_slug, mod.name
                    FROM models mod
                    JOIN makes mk ON mk.make_slug = mod.make_slug
                    ORDER BY RANDOM()
                    LIMIT 1
                    """
                )
            else:
                cur.execute(
                    """
                    SELECT mod.make_slug, mk.name as make_name, mod.model_slug, mod.name
                    FROM models mod
                    JOIN makes mk ON mk.make_slug = mod.make_slug
                    WHERE EXISTS (SELECT 1 FROM engines e WHERE e.make_slug = mod.make_slug AND e.model_slug = mod.model_slug)
                    ORDER BY RANDOM()
                    LIMIT 1
                    """
                )
            row = cur.fetchone()
            conn.close()
            if row:
                self.send_json(dict(row))
            else:
                self.send_json({"error": "No models found"}, 404)
            return

        if path == "/api/engines":
            q = (qs.get("q", [""])[0]).strip()
            conn = get_db_connection()
            cur = conn.cursor()
            if q:
                cur.execute(
                    """
                    SELECT make_slug, model_slug, series_code, engine_code, name, displacement_litres,
                           displacement_cc, cylinders, configuration, aspiration, fuel_type, power_kw, torque_nm, notes
                    FROM engines
                    WHERE engine_code LIKE ? OR name LIKE ? OR make_slug LIKE ? OR model_slug LIKE ? OR notes LIKE ?
                    ORDER BY power_kw DESC
                    LIMIT 150
                    """,
                    (f"%{q}%", f"%{q}%", f"%{q}%", f"%{q}%", f"%{q}%"),
                )
            else:
                cur.execute(
                    """
                    SELECT make_slug, model_slug, series_code, engine_code, name, displacement_litres,
                           displacement_cc, cylinders, configuration, aspiration, fuel_type, power_kw, torque_nm, notes
                    FROM engines
                    ORDER BY power_kw DESC
                    LIMIT 150
                    """
                )
            rows = [dict(r) for r in cur.fetchall()]
            conn.close()
            self.send_json(rows)
            return

        if path == "/api/search":
            q = (qs.get("q", [""])[0]).strip()
            if not q:
                self.send_json([])
                return
            conn = get_db_connection()
            cur = conn.cursor()
            like_q = f"%{q}%"
            results = []
            # Search models
            cur.execute(
                """
                SELECT 'model' as type, mod.make_slug, mod.model_slug, mk.name || ' ' || mod.name as title,
                       mod.vehicle_type || ' (' || COALESCE(mod.years_sold_au_start, '?') || '-' || COALESCE(mod.years_sold_au_end, '?') || ')' as subtitle,
                       SUBSTR(mod.overview, 1, 180) as snippet
                FROM models mod
                JOIN makes mk ON mk.make_slug = mod.make_slug
                WHERE mod.name LIKE ? OR mk.name LIKE ? OR mod.overview LIKE ? OR mod.australian_market_notes LIKE ?
                LIMIT 25
                """,
                (like_q, like_q, like_q, like_q),
            )
            results.extend([dict(r) for r in cur.fetchall()])
            # Search generations / series codes
            cur.execute(
                """
                SELECT 'series' as type, g.make_slug, g.model_slug,
                       UPPER(g.make_slug) || ' ' || UPPER(g.model_slug) || ' — Series ' || g.series_code as title,
                       COALESCE(g.generation_name, '') || ' (' || COALESCE(g.years_start, '?') || '-' || COALESCE(g.years_end, '?') || ')' as subtitle,
                       SUBSTR(g.summary, 1, 180) as snippet
                FROM generations g
                WHERE g.series_code LIKE ? OR g.generation_name LIKE ? OR g.summary LIKE ?
                LIMIT 25
                """,
                (like_q, like_q, like_q),
            )
            results.extend([dict(r) for r in cur.fetchall()])
            # Search badges
            cur.execute(
                """
                SELECT 'badge' as type, b.make_slug, b.model_slug,
                       UPPER(b.make_slug) || ' ' || UPPER(b.model_slug) || ' ' || b.badge_name || ' (' || b.series_code || ')' as title,
                       COALESCE(b.drivetrain, '') || ' | AUD $' || COALESCE(b.msrp_aud_min, '?') as subtitle,
                       COALESCE(b.notes, '') as snippet
                FROM badges b
                WHERE b.badge_name LIKE ? OR b.notes LIKE ?
                LIMIT 25
                """,
                (like_q, like_q),
            )
            results.extend([dict(r) for r in cur.fetchall()])
            # Search engines
            cur.execute(
                """
                SELECT 'engine' as type, e.make_slug, e.model_slug,
                       e.engine_code || ' — ' || COALESCE(e.name, '') || ' (' || UPPER(e.make_slug) || ' ' || UPPER(e.model_slug) || ' ' || e.series_code || ')' as title,
                       COALESCE(e.power_kw, '?') || ' kW / ' || COALESCE(e.torque_nm, '?') || ' Nm | ' || COALESCE(e.fuel_type, '') as subtitle,
                       COALESCE(e.notes, '') as snippet
                FROM engines e
                WHERE e.engine_code LIKE ? OR e.name LIKE ? OR e.notes LIKE ?
                LIMIT 25
                """,
                (like_q, like_q, like_q),
            )
            results.extend([dict(r) for r in cur.fetchall()])
            conn.close()
            self.send_json(results)
            return

        self.send_error(404, "Endpoint not found")


def main():
    parser = argparse.ArgumentParser(description="Start the Australian Automotive Archive Web UI")
    parser.add_argument("--port", type=int, default=8080, help="Port to listen on (default: 8080)")
    args = parser.parse_args()

    server = ThreadingHTTPServer(("127.0.0.1", args.port), ArchiveRequestHandler)
    print(f"Australian Automotive Archive Web UI running at http://127.0.0.1:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
