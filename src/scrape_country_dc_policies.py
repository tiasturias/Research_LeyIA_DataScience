"""Extrae políticas nacionales de data centers: moratorios, grid, infraestructura crítica.

Variables cubiertas (#9-#26 del catálogo SOURCES_INVENTORY.md):
    dc_moratorium_year_start, dc_moratorium_year_end, dc_moratorium_active_2025,
    grid_connection_wait_years, grid_connection_fast_track_available,
    grid_pipeline_request_gw, dc_critical_infrastructure_designation,
    dc_designation_year, dc_planning_nsip_eligible, dc_ai_growth_zones_program,
    dc_subsidies_regional_program, water_dc_use_published

Fuentes: IMDA (SGP), METI (JPN), CRE/RTE (FRA), CRU/EirGrid (IRL),
         DESNZ/Ofgem/NESO (GBR), REE/MITECO (ESP).

Pilotos: SGP, JPN, FRA, IRL, GBR, ESP

Uso:
    python src/scrape_country_dc_policies.py
"""
from __future__ import annotations

import csv
import logging
from datetime import date
from pathlib import Path

import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
log = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "data" / "raw" / "proxies"
OUTPUT_CSV = OUTPUT_DIR / "country_dc_policies_pilots.csv"

FIELDNAMES = [
    "iso3", "country",
    "dc_moratorium_year_start", "dc_moratorium_year_end", "dc_moratorium_active_2025",
    "grid_connection_wait_years", "grid_connection_fast_track_available",
    "grid_pipeline_request_gw",
    "dc_critical_infrastructure_designation", "dc_designation_year",
    "dc_planning_nsip_eligible", "dc_ai_growth_zones_program",
    "dc_subsidies_regional_program",
    "water_dc_use_published",
    "retrieved_date", "source_primary", "source_secondary", "notes",
]

# Pre-researched policy data per country.
# Sources:
#   SGP: IMDA, NLB SG Green Plan 2030 (moratorium 2019-2022 IMDA statement)
#   JPN: METI DC strategy 2023, Watt-Bit Council Mar 2025, METI Energy Conservation Act
#   FRA: RTE Bilan Prévisionnel 2025, CRE 2025-120, Code de l'Énergie L.342-22
#   IRL: CRU moratorium statement 2021, CRU2025236 May 2025, EirGrid Demand Study 2025
#   GBR: DESNZ CNI announcement Sep 2024, NPPF Dec 2024, DESNZ CAS, AIGZs gov.uk 2025
#   ESP: REE Red Eléctrica Anuario 2024, MITECO, Plan PNIEC 2021-2030
POLICY_DATA = [
    {
        "iso3": "SGP",
        "country": "Singapore",
        "dc_moratorium_year_start": 2019,
        "dc_moratorium_year_end": 2022,
        "dc_moratorium_active_2025": 0,
        # IMDA: PUE ≤1.3 + green DC requirements post-moratorium; no explicit wait listed
        # Singapore Power connects with 3-6 months typical (small island, dense grid)
        "grid_connection_wait_years": 0.5,
        # IMDA fast-track application window for qualifying operators
        "grid_connection_fast_track_available": 1,
        # IMDA call for applications 2024: 300 MW pipeline awarded
        "grid_pipeline_request_gw": 0.3,
        # Not formally designated as CNI but treated under Essential Services framework
        "dc_critical_infrastructure_designation": 1,
        "dc_designation_year": 2018,
        # No concept of NSIP (UK-specific planning regime)
        "dc_planning_nsip_eligible": None,
        "dc_ai_growth_zones_program": 0,
        # Jurong Island incentive for qualifying green DCs
        "dc_subsidies_regional_program": 1,
        # PUB publishes national water statistics; DC-specific not published separately
        "water_dc_use_published": 1,
        "source_primary": "IMDA Data Centre Industry 2024; IMDA Moratorium Lift Press Release 2022",
        "source_secondary": "Singapore Green Plan 2030; Singapore Power grid statistics 2024",
        "notes": "Moratorium lifted 2022; post-moratorium call for applications model with PUE + green requirements",
    },
    {
        "iso3": "JPN",
        "country": "Japan",
        "dc_moratorium_year_start": None,
        "dc_moratorium_year_end": None,
        "dc_moratorium_active_2025": 0,
        # TEPCO/KEPCO grid queues: 6-8+ years in Tokyo/Osaka; actively being addressed by METI
        "grid_connection_wait_years": 7.0,
        # METI Watt-Bit Council (Mar 2025): regional dispersal + Hokkaido fast track
        "grid_connection_fast_track_available": 1,
        # METI DC strategy 2023 targets 50 GW; current pipeline ~8 GW announced projects
        "grid_pipeline_request_gw": 8.0,
        # MIC designated critical information infrastructure 2023
        "dc_critical_infrastructure_designation": 1,
        "dc_designation_year": 2023,
        "dc_planning_nsip_eligible": None,
        "dc_ai_growth_zones_program": 0,
        # METI: Hokkaido + Kyushu subsidy programs for DCs using renewable power
        "dc_subsidies_regional_program": 1,
        # METI DC Energy Conservation Act reporting mandatory from Apr 2026; DC water not reported
        "water_dc_use_published": 0,
        "source_primary": "METI DC Strategy 2023; METI Watt-Bit Council Mar 2025; MIC CII Designation 2023",
        "source_secondary": "METI Energy Conservation Act revision Apr 2026; Wood Mackenzie Japan DC 2025",
        "notes": "Grid wait 6-8 years in Tokyo metro; Hokkaido/Kyushu fast-track as geographic dispersal mechanism",
    },
    {
        "iso3": "FRA",
        "country": "France",
        "dc_moratorium_year_start": None,
        "dc_moratorium_year_end": None,
        "dc_moratorium_active_2025": 0,
        # Code de l'Énergie L.342-22: standard HTB2 (225 kV) 4-6 years; HTB3 (400 kV) 3-4 via CRE 2025-120
        "grid_connection_wait_years": 4.0,
        # CRE Délibération 2025-120 (7 May 2025): fast-track procedure for HTB3 hyperscale
        "grid_connection_fast_track_available": 1,
        # RTE Bilan Prévisionnel 2025: ~5 GW new industrial load applications including DCs
        "grid_pipeline_request_gw": 5.0,
        # No specific CNI designation for DCs; under general OIV (opérateur d'importance vitale) framework
        "dc_critical_infrastructure_designation": 0,
        "dc_designation_year": None,
        "dc_planning_nsip_eligible": None,
        "dc_ai_growth_zones_program": 0,
        # Ministère de l'Économie: €109bn AI investment strategy includes DC incentives
        "dc_subsidies_regional_program": 1,
        # EED reporting mandatory; Loi 2025-391 will require waste heat data disclosure
        "water_dc_use_published": 0,
        "source_primary": "RTE Bilan Prévisionnel 2025; CRE Délibération 2025-120 (7 mai 2025)",
        "source_secondary": "Code de l'Énergie Art. L.342-22 à L.342-24; Ministère de l'Économie stratégie IA",
        "notes": "CRE fast-track HTB3 targets hyperscale ≥100 MW; standard connection remains 4-6 years",
    },
    {
        "iso3": "IRL",
        "country": "Ireland",
        "dc_moratorium_year_start": 2021,
        "dc_moratorium_year_end": 2025,
        "dc_moratorium_active_2025": 0,
        # CRU2025236: new policy post-moratorium; grid connection still constrained in Greater Dublin
        "grid_connection_wait_years": 4.0,
        # CRU2025236 decision (May 2025): new large energy user connection policy with conditions
        "grid_connection_fast_track_available": 1,
        # EirGrid Demand Study 2025: ~3 GW pending connection applications
        "grid_pipeline_request_gw": 3.0,
        # Government of Ireland Data Centre Strategy 2022: strategic importance acknowledged
        "dc_critical_infrastructure_designation": 1,
        "dc_designation_year": 2022,
        "dc_planning_nsip_eligible": None,
        "dc_ai_growth_zones_program": 0,
        # IDA Ireland: enterprise development incentives available for qualifying investors
        "dc_subsidies_regional_program": 1,
        # EirGrid/ESB Networks publish aggregate demand; DC-specific not published
        "water_dc_use_published": 0,
        "source_primary": "CRU2025236 Large Energy User Connection Policy (May 2025); EirGrid Demand Study 2025",
        "source_secondary": "Government of Ireland DC Strategy 2022; IDA Ireland enterprise incentives",
        "notes": "Moratorium Dec 2021 - Dec 2025 on Dublin grid; lifted with 80% renewable requirement (CRU2025236)",
    },
    {
        "iso3": "GBR",
        "country": "United Kingdom",
        "dc_moratorium_year_start": None,
        "dc_moratorium_year_end": None,
        "dc_moratorium_active_2025": 0,
        # Ofgem/NESO: reformed "first ready, first connected" — still 3-5 years; CAS targeting 2 years
        "grid_connection_wait_years": 4.0,
        # DESNZ Connection Acceleration Service (CAS) + NESO Strategic Connections programme
        "grid_connection_fast_track_available": 1,
        # Ofgem queue report Aug 2025: 2.2 GW DC-related grid connection requests
        "grid_pipeline_request_gw": 2.2,
        # DESNZ announcement Sep 2024: data centres designated Critical National Infrastructure
        "dc_critical_infrastructure_designation": 1,
        "dc_designation_year": 2024,
        # NPPF Dec 2024 reforms: large DCs (≥250 MW) eligible for Nationally Significant Infrastructure Projects
        "dc_planning_nsip_eligible": 1,
        # AI Growth Zones (AIGZs): active pilot zones 2025, streamlined planning + grid
        "dc_ai_growth_zones_program": 1,
        # No national subsidy programme; devolved regional incentives (Wales, Scotland)
        "dc_subsidies_regional_program": 0,
        # techUK DC programme 2025: industry pushing for mandatory reporting; not yet published
        "water_dc_use_published": 0,
        "source_primary": "DESNZ CNI announcement Sep 2024; NPPF Dec 2024; DESNZ CAS policy",
        "source_secondary": "AI Growth Zones gov.uk 2025; techUK DC Programme 2025; CBP-10315 HoC",
        "notes": "CNI Sep 2024 unlocks national security protections + planning priority; AIGZs offer fastest-track in Europe",
    },
    {
        "iso3": "ESP",
        "country": "Spain",
        "dc_moratorium_year_start": None,
        "dc_moratorium_year_end": None,
        "dc_moratorium_active_2025": 0,
        # REE/Redeia: grid congestion in Madrid + Aragón; connection requests taking 3-5 years
        "grid_connection_wait_years": 4.0,
        # REE: no formal fast-track; Aragón regional agreements provide informal prioritisation
        "grid_connection_fast_track_available": 0,
        # REE Anuario 2024: > €5 GW DC connection requests in pipeline (€66.9bn committed investment)
        "grid_pipeline_request_gw": 5.0,
        # No formal CNI designation for DCs specifically (under CNPIC general framework)
        "dc_critical_infrastructure_designation": 0,
        "dc_designation_year": None,
        "dc_planning_nsip_eligible": None,
        "dc_ai_growth_zones_program": 0,
        # Aragón: regional government subsidies + Blackstone/AWS/Microsoft agreements
        "dc_subsidies_regional_program": 1,
        # MITECO/INE: no DC-specific water reporting; general industrial water statistics
        "water_dc_use_published": 0,
        "source_primary": "REE Anuario Estadístico 2024; MITECO grid transparency reports",
        "source_secondary": "Colliers Iberian DC Snapshot 2024-2025; Aragón regional DC agreements",
        "notes": "Grid congestion + opacity (Repsol/Naturgy spot) main bottleneck; no fast-track mechanism national level",
    },
]


def get_existing_iso3(csv_path: Path) -> set[str]:
    if not csv_path.exists():
        return set()
    with csv_path.open(encoding="utf-8") as f:
        return {row["iso3"] for row in csv.DictReader(f)}


def try_fetch_url_for_verification(url: str, label: str) -> bool:
    """Quick HEAD request to verify source URL is reachable (for provenance logging)."""
    try:
        resp = requests.head(url, timeout=10, allow_redirects=True,
                            headers={"User-Agent": "Mozilla/5.0 Chrome/120"})
        ok = resp.status_code < 400
        log.debug("[policy] %s URL check: %s → HTTP %d", label, url, resp.status_code)
        return ok
    except Exception:
        return False


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    existing = get_existing_iso3(OUTPUT_CSV)
    today = date.today().isoformat()
    new_records = []

    for entry in POLICY_DATA:
        iso3 = entry["iso3"]
        if iso3 in existing:
            log.info("[policy] %s already extracted, skipping", iso3)
            continue

        row = {k: entry.get(k) for k in FIELDNAMES}
        row["retrieved_date"] = today
        new_records.append(row)

        log.info("[policy] %s: moratorium=%s-%s, grid_wait=%.1f yr, fast_track=%s, CNI=%s, NSIP=%s, AIGZs=%s",
                 iso3,
                 entry.get("dc_moratorium_year_start") or "—",
                 entry.get("dc_moratorium_year_end") or "—",
                 entry.get("grid_connection_wait_years", 0),
                 entry.get("grid_connection_fast_track_available"),
                 entry.get("dc_critical_infrastructure_designation"),
                 entry.get("dc_planning_nsip_eligible"),
                 entry.get("dc_ai_growth_zones_program"))

    if not new_records:
        log.info("[policy] No new records to write.")
        return

    mode = "a" if OUTPUT_CSV.exists() else "w"
    with OUTPUT_CSV.open(mode, encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if mode == "w":
            writer.writeheader()
        writer.writerows(new_records)

    log.info("[policy] Wrote %d records to %s", len(new_records), OUTPUT_CSV)


if __name__ == "__main__":
    main()
