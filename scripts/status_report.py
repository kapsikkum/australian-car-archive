"""
Generates a live coverage and statistics report for the Australian Car Archive.
"""
import json
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = ROOT_DIR / "aus_cars.db"
MEDIA_DIR = ROOT_DIR / "media"


def get_media_disk_stats() -> dict:
    pics = list((MEDIA_DIR / "pictures").rglob("*")) if (MEDIA_DIR / "pictures").exists() else []
    pic_files = [p for p in pics if p.is_file()]
    mans = list((MEDIA_DIR / "manuals").rglob("*")) if (MEDIA_DIR / "manuals").exists() else []
    man_files = [m for m in mans if m.is_file()]
    return {
        "picture_files_on_disk": len(pic_files),
        "picture_bytes_on_disk": sum(p.stat().st_size for p in pic_files),
        "manual_files_on_disk": len(man_files),
        "manual_bytes_on_disk": sum(m.stat().st_size for m in man_files),
    }


def main():
    if not DB_PATH.exists():
        print("Database aus_cars.db not found. Run scripts/build_db.py first.")
        return

    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    tables = ["makes", "models", "generations", "engines", "badges", "configurations", "manuals", "pictures"]
    counts = {}
    for t in tables:
        cur.execute(f"SELECT COUNT(*) FROM {t}")
        counts[t] = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM makes WHERE local_manufacturer = 1")
    local_makes = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM models WHERE locally_built = 1")
    local_models = cur.fetchone()[0]

    cur.execute(
        """
        SELECT m.name, COUNT(DISTINCT mod.id) as model_cnt, COUNT(DISTINCT g.id) as gen_cnt
        FROM makes m
        LEFT JOIN models mod ON mod.make_slug = m.make_slug
        LEFT JOIN generations g ON g.make_slug = m.make_slug
        GROUP BY m.make_slug
        ORDER BY model_cnt DESC, gen_cnt DESC
        LIMIT 15
        """
    )
    top_makes = [{"make": r[0], "models": r[1], "generations": r[2]} for r in cur.fetchall()]

    conn.close()

    disk_stats = get_media_disk_stats()
    report = {
        "database_counts": counts,
        "australian_manufacturing": {
            "local_manufacturers": local_makes,
            "locally_built_models": local_models,
        },
        "media_on_disk": disk_stats,
        "top_15_makes_by_model_count": top_makes,
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
