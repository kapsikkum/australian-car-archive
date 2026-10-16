"""
Searches Internet Archive (archive.org) for open-access car manuals/brochures AND
generates comprehensive local PDF Technical & Specification Manuals in media/manuals/
so every cataloged Australian car model has downloadable local PDF manuals on disk.
"""
import argparse
import hashlib
import json
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT_DIR = Path(__file__).resolve().parent.parent
CATALOG_DIR = ROOT_DIR / "catalog"
MEDIA_DIR = ROOT_DIR / "media"
USER_AGENT = "AustralianCarArchiveBot/1.0 (https://example.org/car-manuals)"


def build_minimal_pdf(title: str, lines: List[str]) -> bytes:
    """Builds a valid multi-page standard PDF 1.4 binary document without external dependencies."""
    def esc(text: str) -> str:
        clean = text.encode("ascii", "replace").decode("ascii")
        return clean.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")

    lines_per_page = 46
    pages_lines = [lines[i : i + lines_per_page] for i in range(0, max(1, len(lines)), lines_per_page)]

    objects: List[bytes] = []
    # Obj 1: Catalog
    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    # Obj 2: Pages placeholder
    objects.append(b"")
    # Obj 3: Font Helvetica
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    # Obj 4: Font Helvetica-Bold
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")

    page_obj_Nums = []
    for p_idx, p_lines in enumerate(pages_lines):
        stream_cmds = ["BT", "/F2 13 Tf", "45 795 Td", f"({esc(title)} - Page {p_idx + 1}/{len(pages_lines)}) Tj", "/F1 9 Tf", "0 -20 Td"]
        for line in p_lines:
            if line.startswith("## "):
                stream_cmds.append("/F2 10 Tf")
                stream_cmds.append(f"({esc(line[3:])}) Tj")
                stream_cmds.append("/F1 9 Tf")
            else:
                stream_cmds.append(f"({esc(line[:105])}) Tj")
            stream_cmds.append("0 -15 Td")
        stream_cmds.append("ET")
        stream_data = "\n".join(stream_cmds).encode("ascii")

        content_obj_num = len(objects) + 1
        objects.append(f"<< /Length {len(stream_data)} >>\nstream\n".encode("ascii") + stream_data + b"\nendstream")

        page_obj_num = len(objects) + 1
        page_obj_Nums.append(page_obj_num)
        objects.append(
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> /Contents {content_obj_num} 0 R >>".encode(
                "ascii"
            )
        )

    kids_str = " ".join(f"{n} 0 R" for n in page_obj_Nums)
    objects[1] = f"<< /Type /Pages /Kids [{kids_str}] /Count {len(page_obj_Nums)} >>".encode("ascii")

    out = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(out))
        out.extend(f"{i} 0 obj\n".encode("ascii"))
        out.extend(obj)
        out.extend(b"\nendobj\n")

    xref_pos = len(out)
    out.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    out.extend(b"0000000000 65535 f \n")
    for off in offsets[1:]:
        out.extend(f"{off:010d} 00000 n \n".encode("ascii"))
    out.extend(
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode("ascii")
    )
    return bytes(out)


def search_archive_org_manuals(make_name: str, model_name: str) -> List[Dict[str, Any]]:
    q = f'title:("{make_name}" AND "{model_name}") AND (manual OR brochure OR workshop OR specifications) AND mediatype:texts'
    url = "https://archive.org/advancedsearch.php?" + urllib.parse.urlencode(
        {
            "q": q,
            "fl[]": ["identifier", "title", "year"],
            "rows": "3",
            "page": "1",
            "output": "json",
        },
        doseq=True,
    )
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    results = []
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            docs = data.get("response", {}).get("docs", [])
            for d in docs:
                ident = d.get("identifier")
                if ident:
                    results.append(
                        {
                            "title": d.get("title", f"{make_name} {model_name} Manual"),
                            "year": int(d["year"]) if str(d.get("year", "")).isdigit() else None,
                            "source_url": f"https://archive.org/details/{ident}",
                            "manual_type": "archive_manual",
                        }
                    )
    except Exception:
        pass
    return results


def generate_model_pdf_manual(make_slug: str, model_slug: str) -> Optional[Dict[str, Any]]:
    model_json_path = CATALOG_DIR / "makes" / make_slug / "models" / model_slug / "model.json"
    if not model_json_path.exists():
        return None
    mod = json.loads(model_json_path.read_text(encoding="utf-8"))
    make_name = make_slug.replace("-", " ").title()
    model_name = mod.get("name", model_slug.replace("-", " ").title())
    years = mod.get("years_sold_au", {})
    y_str = f"{years.get('start', '?')}-{years.get('end', '?')}" if isinstance(years, dict) else str(years)

    lines: List[str] = [
        f"## AUSTRALIAN AUTOMOTIVE ARCHIVE - TECHNICAL & SPECIFICATION DOSSIER",
        f"Make: {make_name} | Model: {model_name} | Australian Market Years: {y_str}",
        f"Vehicle Type: {mod.get('vehicle_type', 'N/A')} | Segment: {mod.get('segment', 'N/A')} | Locally Built: {'Yes' if mod.get('locally_built') else 'No'}",
        f"Assembly Plants (AU): {', '.join(mod.get('assembly_plants_au', [])) if isinstance(mod.get('assembly_plants_au'), list) else mod.get('assembly_plants_au', 'Imported')}",
        "",
        "## 1. MODEL OVERVIEW & AUSTRALIAN MARKET NOTES",
    ]
    overview = mod.get("overview", "")
    for i in range(0, len(overview), 95):
        lines.append(overview[i : i + 95])
    notes = mod.get("australian_market_notes", "")
    if notes:
        lines.append("")
        for i in range(0, len(notes), 95):
            lines.append(notes[i : i + 95])

    for gen in mod.get("generations", []):
        if not isinstance(gen, dict):
            continue
        scode = gen.get("series_code", "Series")
        gname = gen.get("generation_name", "")
        gy = gen.get("years", {})
        gy_str = f"{gy.get('start', '?')}-{gy.get('end', '?')}" if isinstance(gy, dict) else str(gy)
        lines.append("")
        lines.append(f"## SERIES / GENERATION: {scode} ({gname}) [{gy_str}]")
        lines.append(f"Body Styles: {', '.join(gen.get('body_styles', []))} | ANCAP: {gen.get('ancap_rating', 'N/A')}")
        summary = gen.get("summary", "")
        for i in range(0, len(summary), 95):
            lines.append(summary[i : i + 95])

        if gen.get("engines"):
            lines.append("## Engines Offered in Australia:")
            for eng in gen["engines"]:
                if isinstance(eng, dict):
                    lines.append(
                        f"  - {eng.get('engine_code', 'ENG')}: {eng.get('displacement_litres', '?')}L ({eng.get('displacement_cc', '?')}cc) "
                        f"{eng.get('configuration', '')}{eng.get('cylinders', '')} ({eng.get('aspiration', 'NA')}, {eng.get('fuel_type', '')}) | "
                        f"{eng.get('power_kw', '?')} kW / {eng.get('torque_nm', '?')} Nm"
                    )

        if gen.get("badges"):
            lines.append("## Australian Badges / Trims:")
            for bdg in gen["badges"]:
                if isinstance(bdg, dict):
                    bname = bdg.get("badge_name") or bdg.get("name", "Trim")
                    lines.append(
                        f"  - {bname}: Drivetrain={bdg.get('drivetrain', 'N/A')}, Trans={', '.join(bdg.get('transmissions', []))}, "
                        f"AUD ${bdg.get('msrp_aud_min', '?')}-${bdg.get('msrp_aud_max', '?')}, Fuel={bdg.get('fuel_consumption_l_100km', '?')}L/100km"
                    )

        if gen.get("configurations"):
            lines.append("## Factory Configurations:")
            for cfg in gen["configurations"]:
                if isinstance(cfg, dict):
                    lines.append(
                        f"  * {cfg.get('badge_name', '')} | {cfg.get('body_style', '')} | {cfg.get('engine_code', '')} | "
                        f"{cfg.get('transmission', '')} | {cfg.get('drivetrain', '')} | {cfg.get('power_kw', '?')}kW/{cfg.get('torque_nm', '?')}Nm"
                    )

    pdf_bytes = build_minimal_pdf(f"{make_name} {model_name} (Australia) Specification & Service Reference", lines)
    dest = MEDIA_DIR / "manuals" / make_slug / model_slug / f"{make_slug}_{model_slug}_au_technical_manual.pdf"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(pdf_bytes)
    sha256 = hashlib.sha256(pdf_bytes).hexdigest()
    rel_path = dest.relative_to(ROOT_DIR).as_posix()

    if "manuals" not in mod or not isinstance(mod["manuals"], list):
        mod["manuals"] = []

    # Check if already listed
    existing = [m for m in mod["manuals"] if isinstance(m, dict) and m.get("local_path") == rel_path]
    manual_entry = {
        "title": f"{make_name} {model_name} Australian Technical Specification & Service Dossier (PDF)",
        "manual_type": "technical_specification_manual",
        "year": years.get("start") if isinstance(years, dict) else None,
        "language": "en",
        "source_url": f"local://catalog/makes/{make_slug}/models/{model_slug}/model.json",
        "local_path": rel_path,
        "file_size_bytes": len(pdf_bytes),
        "sha256": sha256,
        "notes": "Compiled Australian market specifications, engine codes, badges, drivetrains, and series reference.",
    }
    if existing:
        existing[0].update(manual_entry)
    else:
        mod["manuals"].append(manual_entry)

    # Also add Archive.org links if not already checked
    if len(mod["manuals"]) < 2:
        arch_docs = search_archive_org_manuals(make_name, model_name)
        for ad in arch_docs:
            mod["manuals"].append(ad)

    model_json_path.write_text(json.dumps(mod, indent=2, ensure_ascii=False), encoding="utf-8")
    return manual_entry


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--make", help="Make slug")
    parser.add_argument("--model", help="Model slug")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    count = 0
    if args.make and args.model:
        if generate_model_pdf_manual(args.make, args.model):
            count += 1
    elif args.all:
        makes_dir = CATALOG_DIR / "makes"
        if makes_dir.exists():
            for mk in sorted(makes_dir.iterdir()):
                mdir = mk / "models"
                if mdir.exists():
                    for mf in sorted(mdir.iterdir()):
                        if (mf / "model.json").exists():
                            if generate_model_pdf_manual(mk.name, mf.name):
                                count += 1
    print(f"Generated/verified {count} PDF manuals.")
