# Australian Automotive Archive (`car-manuals`)

A file-based JSON catalog and compiled SQLite database (`aus_cars.db`) covering car makes, models, series/generations, Australian badges/trims, engine specifications, drivetrain configurations, downloaded photos, and PDF manuals/technical dossiers for vehicles sold or manufactured in Australia.

---

## Repository Structure

```text
e:\code\archive\car-manuals\
├── aus_cars.db                          # Compiled SQLite database (with FTS5 full-text search)
├── catalog/
│   ├── makes_index.json                 # Master index of 100+ makes sold in Australia
│   └── makes/
│       └── <make_slug>/
│           ├── make.json                # Brand metadata, Australian history & full models_catalog
│           └── models/
│               └── <model_slug>/
│                   └── model.json       # Deep-dive generations, engines, badges, configurations, manuals, pictures
├── media/
│   ├── pictures/<make_slug>/<model_slug>/  # Downloaded local car photos (with SHA-256 & license attribution)
│   └── manuals/<make_slug>/<model_slug>/   # Downloaded/compiled PDF manuals & Australian technical dossiers
└── scripts/
    ├── schema.py                        # Validates JSON files across catalog/
    ├── build_db.py                      # Compiles catalog/ JSON tree into aus_cars.db
    ├── media_downloader.py              # Fetches Wikimedia Commons photos & external manual PDFs to media/
    ├── manual_builder.py                # Queries Archive.org & builds local PDF Technical Dossiers
    ├── status_report.py                 # Outputs database & disk media coverage metrics
    └── query_cli.py                     # CLI query tool for makes, models, engines, badges & full-text search
```

---

## Quick Start & Commands

### 1. Build / Rebuild the SQLite Database
```powershell
python scripts/build_db.py
```

### 2. Check Coverage & Media Statistics
```powershell
python scripts/status_report.py
```

### 3. Validate Catalog Schema
```powershell
python scripts/schema.py
```

### 4. Query the Database via CLI
```powershell
# Inspect a specific make and its Australian model lineup
python scripts/query_cli.py --make holden

# Deep-dive into a specific model (generations, engines, badges, manuals, pictures)
python scripts/query_cli.py --make holden --model commodore
python scripts/query_cli.py --make ford --model falcon --series BA

# Search across all Australian engines (e.g., Barra, LS3, RB30, 1VD-FTV)
python scripts/query_cli.py --engine "Barra"

# Search by badge/trim (e.g., XR6 Turbo, SS-V, GXL, STI)
python scripts/query_cli.py --badge "XR6"

# Full-text search across the entire archive
python scripts/query_cli.py --search "Tonsley Park"
```

### 5. Launch the Local Interactive Web UI
```powershell
python scripts/web_viewer.py --port 8080
```
Then open `http://127.0.0.1:8080` in your browser to explore all 100 makes, deep-dive model dossiers, Australian series/generations, engine explorer, badge specifications, local photo galleries, and PDF technical manuals.

### 6. Download Additional Photos & Build PDF Manuals
```powershell
# Download photos & manuals for a specific make/model
python scripts/media_downloader.py --make holden --model commodore --max-per-gen 2
python scripts/manual_builder.py --make holden --model commodore

# Or run across all deep-dive models in the catalog
python scripts/media_downloader.py --all --max-per-gen 1
python scripts/manual_builder.py --all
```
