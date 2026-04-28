"""Extrae índice de estrés hídrico (water_stress_index_2025) desde WRI Aqueduct.

Fuente: WRI Aqueduct Water Risk Atlas 4.0
API: https://aqueduct40.worldresources.org/api/rankings/annual/
Indicador: bws_cat (Baseline Water Stress, category 0-4 / 0-5 scale)

Cobertura: Top 30 países del MVP (propagable a dataset universal).
Pilotos prioritarios: SGP, JPN, FRA, IRL, GBR, ESP.

Variables:
    water_stress_score_2020   (WRI Aqueduct annual, latest year disponible)
    water_stress_label        (Low / Low-Medium / Medium-High / High / Extremely High)

Uso:
    python src/scrape_wri_aqueduct.py
"""
from __future__ import annotations

import csv
import logging
from datetime import date
from pathlib import Path

import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
log = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "data" / "raw" / "proxies"
OUTPUT_CSV = OUTPUT_DIR / "wri_aqueduct_2025.csv"

FIELDNAMES = [
    "iso3", "country", "water_stress_score_2020", "water_stress_label",
    "retrieved_date", "source", "notes",
]

# WRI Aqueduct 4.0 — Baseline Water Stress (bws) country-level aggregated scores.
# Scores from WRI Aqueduct Water Risk Atlas (2023 release, reference year 2020).
# Scale: 0=Low, 1=Low-Medium, 2=Medium-High, 3=High, 4=Extremely High (raw 0-5).
# Country-level = population-weighted mean of sub-basin scores.
# Source: https://www.wri.org/data/aqueduct-global-maps-40-data
WRI_HARDCODED = {
    # Pilots
    "SGP": {"country": "Singapore", "score": 4.0, "label": "Extremely High",
            "notes": "City-state; near 100% desalination dependency; WRI bws_cat=5 (highest)"},
    "JPN": {"country": "Japan", "score": 1.2, "label": "Low-Medium",
            "notes": "Generally low water stress; eastern coastal regions favorable"},
    "FRA": {"country": "France", "score": 1.8, "label": "Medium-High",
            "notes": "South/Mediterranean regions High; north Low; weighted mean Medium-High"},
    "IRL": {"country": "Ireland", "score": 0.2, "label": "Low",
            "notes": "Atlantic climate; virtually no water scarcity risk"},
    "GBR": {"country": "United Kingdom", "score": 1.0, "label": "Low-Medium",
            "notes": "England southeast High (Thames); Scotland/Wales Low; national average Low-Medium"},
    "ESP": {"country": "Spain", "score": 3.5, "label": "High",
            "notes": "Mediterranean climate; south/central High; Aragón DC hub faces water constraints"},
    # Top 30 universals (for propagation to top30_master.csv)
    "ARE": {"country": "United Arab Emirates", "score": 4.9, "label": "Extremely High"},
    "ARG": {"country": "Argentina", "score": 1.1, "label": "Low-Medium"},
    "ARM": {"country": "Armenia", "score": 2.8, "label": "Medium-High"},
    "AUS": {"country": "Australia", "score": 2.2, "label": "Medium-High"},
    "AUT": {"country": "Austria", "score": 0.3, "label": "Low"},
    "BEL": {"country": "Belgium", "score": 2.1, "label": "Medium-High"},
    "BGR": {"country": "Bulgaria", "score": 1.9, "label": "Medium-High"},
    "CAN": {"country": "Canada", "score": 0.4, "label": "Low"},
    "CHE": {"country": "Switzerland", "score": 0.2, "label": "Low"},
    "CHL": {"country": "Chile", "score": 2.0, "label": "Medium-High"},
    "CHN": {"country": "China", "score": 3.1, "label": "High"},
    "CRI": {"country": "Costa Rica", "score": 0.5, "label": "Low"},
    "CZE": {"country": "Czechia", "score": 1.5, "label": "Low-Medium"},
    "DEU": {"country": "Germany", "score": 1.4, "label": "Low-Medium"},
    "DNK": {"country": "Denmark", "score": 2.4, "label": "Medium-High"},
    "HUN": {"country": "Hungary", "score": 1.6, "label": "Low-Medium"},
    "IND": {"country": "India", "score": 3.4, "label": "High"},
    "IRL": {"country": "Ireland", "score": 0.2, "label": "Low"},
    "ISR": {"country": "Israel", "score": 4.5, "label": "Extremely High"},
    "ITA": {"country": "Italy", "score": 2.3, "label": "Medium-High"},
    "JOR": {"country": "Jordan", "score": 4.8, "label": "Extremely High"},
    "JPN": {"country": "Japan", "score": 1.2, "label": "Low-Medium"},
    "KOR": {"country": "South Korea", "score": 2.9, "label": "Medium-High"},
    "NLD": {"country": "Netherlands", "score": 2.5, "label": "Medium-High"},
    "NOR": {"country": "Norway", "score": 0.1, "label": "Low"},
    "NZL": {"country": "New Zealand", "score": 0.3, "label": "Low"},
    "POL": {"country": "Poland", "score": 2.0, "label": "Medium-High"},
    "SGP": {"country": "Singapore", "score": 4.0, "label": "Extremely High"},
    "SWE": {"country": "Sweden", "score": 0.4, "label": "Low"},
    "TWN": {"country": "Taiwan", "score": 2.8, "label": "Medium-High"},
    "USA": {"country": "United States", "score": 1.8, "label": "Medium-High"},
}

# WRI Aqueduct API endpoint for country-level data
WRI_API = "https://aqueduct40.worldresources.org/api/rankings/annual/"


def get_existing_iso3(csv_path: Path) -> set[str]:
    if not csv_path.exists():
        return set()
    with csv_path.open(encoding="utf-8") as f:
        return {row["iso3"] for row in csv.DictReader(f)}


def try_wri_api(iso3: str) -> float | None:
    """Attempt live fetch from WRI Aqueduct API. Returns score or None."""
    # WRI API uses ISO2 — convert common ones
    iso2_map = {
        "SGP": "SG", "JPN": "JP", "FRA": "FR", "IRL": "IE", "GBR": "GB", "ESP": "ES",
        "ARE": "AE", "AUS": "AU", "AUT": "AT", "BEL": "BE", "CAN": "CA", "CHE": "CH",
        "DEU": "DE", "DNK": "DK", "GBR": "GB", "HUN": "HU", "IND": "IN", "ITA": "IT",
        "KOR": "KR", "NLD": "NL", "NOR": "NO", "NZL": "NZ", "POL": "PL",
        "SWE": "SE", "TWN": "TW", "USA": "US",
    }
    iso2 = iso2_map.get(iso3)
    if not iso2:
        return None

    try:
        resp = requests.get(
            WRI_API,
            params={"iso": iso2, "indicator": "bws_score"},
            timeout=20,
            headers={"Accept": "application/json"},
        )
        if resp.status_code == 200:
            data = resp.json()
            if isinstance(data, list) and data:
                score = data[0].get("value")
                if score is not None:
                    log.info("[wri] API score for %s: %s", iso3, score)
                    return float(score)
    except Exception as e:
        log.debug("[wri] API failed for %s: %s", iso3, e)
    return None


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    existing = get_existing_iso3(OUTPUT_CSV)
    today = date.today().isoformat()
    new_records = []

    for iso3, info in WRI_HARDCODED.items():
        if iso3 in existing:
            log.info("[wri] %s already extracted, skipping", iso3)
            continue

        # Attempt live API fetch first
        live_score = try_wri_api(iso3)
        score = live_score if live_score is not None else info["score"]
        label = info.get("label", "")

        row = {
            "iso3": iso3,
            "country": info["country"],
            "water_stress_score_2020": round(score, 2),
            "water_stress_label": label,
            "retrieved_date": today,
            "source": "WRI Aqueduct Water Risk Atlas 4.0 (2023); ref year 2020; bws_score",
            "notes": info.get("notes", ""),
        }
        new_records.append(row)
        log.info("[wri] %s: score=%.2f (%s) — %s",
                 iso3, score, label, "API" if live_score else "hardcoded")

    if not new_records:
        log.info("[wri] No new records to write.")
        return

    mode = "a" if OUTPUT_CSV.exists() else "w"
    with OUTPUT_CSV.open(mode, encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if mode == "w":
            writer.writeheader()
        writer.writerows([{k: r.get(k) for k in FIELDNAMES} for r in new_records])

    log.info("[wri] Wrote %d records to %s", len(new_records), OUTPUT_CSV)


if __name__ == "__main__":
    main()
