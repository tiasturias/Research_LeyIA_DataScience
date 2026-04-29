"""Extrae compliance EU Energy Efficiency Directive (EED 2024) y políticas waste heat.

Fuente: EU EED 2024 (Directive 2023/1791), Art. 12 — Data centre reporting.
        Loi française 2025-391 (30 abr 2025) — valorización calor residual.
        Germany EnEfG 2023 — Energieeffizienzgesetz.

Variables:
    dc_eu_eed_compliance_required   0/1 — aplica EED Art.12 (≥500 kW IT)
    dc_waste_heat_mandate           0/1 — ley nacional obliga valorización calor residual
    dc_waste_heat_pct_required      float — % calor residual a valorizar (si aplica)
    dc_waste_heat_year              int — año en vigor del mandato
    dc_renewable_mandate_pct        float — % renovables exigido
    dc_renewable_mandate_year       int — año en vigor

Pilotos: SGP, JPN, FRA, IRL, GBR, ESP (+ extensibles a Top 30)

Uso:
    python src/scrape_eu_eed_registry.py
"""
from __future__ import annotations

import csv
import logging
from datetime import date
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
log = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "data" / "raw" / "proxies"
OUTPUT_CSV = OUTPUT_DIR / "eu_eed_registry_2025.csv"

FIELDNAMES = [
    "iso3", "country",
    "dc_eu_eed_compliance_required",
    "dc_waste_heat_mandate",
    "dc_waste_heat_pct_required",
    "dc_waste_heat_year",
    "dc_renewable_mandate_pct",
    "dc_renewable_mandate_year",
    "dc_pue_max_mandate",
    "dc_pue_year",
    "retrieved_date", "source", "notes",
]

# EU EED 2024 (Directive 2023/1791): mandatory annual reporting for DC ≥500 kW IT
# effective March 2024. Applies to all EU Member States.
# Germany EnEfG (Energieeffizienzgesetz, Nov 2023):
#   - 50% renewable by 2024, 100% by 2027
#   - waste heat valorisation 20% by 2028
#   - applies to DC ≥300 kW IT
# France Loi 2025-391 (30 Apr 2025): valorisation calor residual obligatoria
# Ireland CRU2025236: 80% renewables on-site requirement for new DC connections
# Singapore: NEA Green DC standard — PUE ≤1.3 (2014), no mandatory waste heat
# Japan: METI Energy Conservation Act revision (Apr 2026) — PUE ≤1.3 post-2029
EED_DATA = [
    {
        "iso3": "SGP",
        "country": "Singapore",
        "dc_eu_eed_compliance_required": 0,
        "dc_waste_heat_mandate": 0,
        "dc_waste_heat_pct_required": None,
        "dc_waste_heat_year": None,
        "dc_renewable_mandate_pct": None,
        "dc_renewable_mandate_year": None,
        "dc_pue_max_mandate": 1.3,
        "dc_pue_year": 2014,
        "source": "IMDA/NEA Singapore Green DC Standard 2014; BCA Green Mark",
        "notes": "PUE ≤1.3 mandatory since 2014 for new DC; no waste heat mandate; no renewable mandate",
    },
    {
        "iso3": "JPN",
        "country": "Japan",
        "dc_eu_eed_compliance_required": 0,
        "dc_waste_heat_mandate": 0,
        "dc_waste_heat_pct_required": None,
        "dc_waste_heat_year": None,
        "dc_renewable_mandate_pct": None,
        "dc_renewable_mandate_year": None,
        "dc_pue_max_mandate": 1.3,
        "dc_pue_year": 2029,
        "source": "METI Energy Conservation Act revision (Act enforcement Apr 2026); METI DC standard",
        "notes": "PUE ≤1.3 target from 2029 with penalty fees; Hokkaido/Kyushu renewable incentives (not mandate)",
    },
    {
        "iso3": "FRA",
        "country": "France",
        "dc_eu_eed_compliance_required": 1,
        "dc_waste_heat_mandate": 1,
        "dc_waste_heat_pct_required": None,   # specific % TBD in implementing decrees
        "dc_waste_heat_year": 2025,
        "dc_renewable_mandate_pct": None,
        "dc_renewable_mandate_year": None,
        "dc_pue_max_mandate": None,           # EED sets target, not hard cap
        "dc_pue_year": None,
        "source": "EU EED 2023/1791 Art.12; Loi 2025-391 du 30 avril 2025 (caleur résiduelle)",
        "notes": "EED annual reporting mandatory ≥500 kW IT from Mar 2024; Loi 2025-391 obliges valorisation waste heat",
    },
    {
        "iso3": "IRL",
        "country": "Ireland",
        "dc_eu_eed_compliance_required": 1,
        "dc_waste_heat_mandate": 0,
        "dc_waste_heat_pct_required": None,
        "dc_waste_heat_year": None,
        "dc_renewable_mandate_pct": 80.0,
        "dc_renewable_mandate_year": 2025,
        "dc_pue_max_mandate": None,
        "dc_pue_year": None,
        "source": "EU EED 2023/1791; CRU2025236 Large Energy User Connection Policy (May 2025)",
        "notes": "CRU2025236: 80% on-site renewables required for new grid connections post-moratorium",
    },
    {
        "iso3": "GBR",
        "country": "United Kingdom",
        "dc_eu_eed_compliance_required": 0,
        "dc_waste_heat_mandate": 0,
        "dc_waste_heat_pct_required": None,
        "dc_waste_heat_year": None,
        "dc_renewable_mandate_pct": None,
        "dc_renewable_mandate_year": None,
        "dc_pue_max_mandate": None,
        "dc_pue_year": None,
        "source": "DESNZ UK DC policy 2025; NPPF Dec 2024",
        "notes": "Post-Brexit: not subject to EU EED; voluntary reporting under PPN 006/21; no hard PUE or waste heat mandate",
    },
    {
        "iso3": "ESP",
        "country": "Spain",
        "dc_eu_eed_compliance_required": 1,
        "dc_waste_heat_mandate": 0,
        "dc_waste_heat_pct_required": None,
        "dc_waste_heat_year": None,
        "dc_renewable_mandate_pct": None,
        "dc_renewable_mandate_year": None,
        "dc_pue_max_mandate": None,
        "dc_pue_year": None,
        "source": "EU EED 2023/1791 transpuesta RD; MITECO Plan PNIEC 2021-2030",
        "notes": "EED reporting required; no additional DC-specific mandates beyond EED; PNIEC 2030 general renewables target",
    },
]


def get_existing_iso3(csv_path: Path) -> set[str]:
    if not csv_path.exists():
        return set()
    with csv_path.open(encoding="utf-8") as f:
        return {row["iso3"] for row in csv.DictReader(f)}


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    existing = get_existing_iso3(OUTPUT_CSV)
    today = date.today().isoformat()
    new_records = []

    for entry in EED_DATA:
        iso3 = entry["iso3"]
        if iso3 in existing:
            log.info("[eed] %s already extracted, skipping", iso3)
            continue
        row = {k: entry.get(k) for k in FIELDNAMES}
        row["retrieved_date"] = today
        new_records.append(row)
        log.info("[eed] %s: EED=%s, waste_heat=%s, renewable=%s%%",
                 iso3,
                 entry["dc_eu_eed_compliance_required"],
                 entry["dc_waste_heat_mandate"],
                 entry.get("dc_renewable_mandate_pct"))

    if not new_records:
        log.info("[eed] No new records to write.")
        return

    mode = "a" if OUTPUT_CSV.exists() else "w"
    with OUTPUT_CSV.open(mode, encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if mode == "w":
            writer.writeheader()
        writer.writerows(new_records)

    log.info("[eed] Wrote %d records to %s", len(new_records), OUTPUT_CSV)


if __name__ == "__main__":
    main()
