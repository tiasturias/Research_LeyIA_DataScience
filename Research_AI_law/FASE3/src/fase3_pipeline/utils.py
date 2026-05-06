"""Utility helpers for Fase 3."""

from __future__ import annotations

import hashlib
import re
import unicodedata
from pathlib import Path

import pandas as pd

from .config import ROOT


COUNTRY_ISO3 = {
    "AFG", "ALB", "DZA", "AND", "AGO", "ATG", "ARG", "ARM", "AUS", "AUT", "AZE",
    "BHS", "BHR", "BGD", "BRB", "BLR", "BEL", "BLZ", "BEN", "BTN", "BOL", "BIH",
    "BWA", "BRA", "BRN", "BGR", "BFA", "BDI", "CPV", "KHM", "CMR", "CAN", "CAF",
    "TCD", "CHL", "CHN", "COL", "COM", "COG", "COD", "CRI", "CIV", "HRV", "CUB",
    "CYP", "CZE", "DNK", "DJI", "DMA", "DOM", "ECU", "EGY", "SLV", "GNQ", "ERI",
    "EST", "SWZ", "ETH", "FJI", "FIN", "FRA", "GAB", "GMB", "GEO", "DEU", "GHA",
    "GRC", "GRD", "GTM", "GIN", "GNB", "GUY", "HTI", "VAT", "HND", "HUN", "ISL",
    "IND", "IDN", "IRN", "IRQ", "IRL", "ISR", "ITA", "JAM", "JPN", "JOR", "KAZ",
    "KEN", "KIR", "PRK", "KOR", "KWT", "KGZ", "LAO", "LVA", "LBN", "LSO", "LBR",
    "LBY", "LIE", "LTU", "LUX", "MDG", "MWI", "MYS", "MDV", "MLI", "MLT", "MHL",
    "MRT", "MUS", "MEX", "FSM", "MDA", "MCO", "MNG", "MNE", "MAR", "MOZ", "MMR",
    "NAM", "NRU", "NPL", "NLD", "NZL", "NIC", "NER", "NGA", "MKD", "NOR", "OMN",
    "PAK", "PLW", "PSE", "PAN", "PNG", "PRY", "PER", "PHL", "POL", "PRT", "QAT",
    "ROU", "RUS", "RWA", "KNA", "LCA", "VCT", "WSM", "SMR", "STP", "SAU", "SEN",
    "SRB", "SYC", "SLE", "SGP", "SVK", "SVN", "SLB", "SOM", "ZAF", "SSD", "ESP",
    "LKA", "SDN", "SUR", "SWE", "CHE", "SYR", "TJK", "TZA", "THA", "TLS", "TGO",
    "TON", "TTO", "TUN", "TUR", "TKM", "TUV", "UGA", "UKR", "ARE", "GBR", "USA",
    "URY", "UZB", "VUT", "VEN", "VNM", "YEM", "ZMB", "ZWE",
}

HUMAN_APPROVED_COMPARABLE = {"HKG", "PRI", "TWN", "XKX"}

TERRITORY_ISO3 = {
    "ABW", "AIA", "ALA", "ASM", "BES", "BMU", "BLM", "BVT", "CCK", "COK", "CUW",
    "CYM", "CXR", "FLK", "FRO", "GGY", "GIB", "GLP", "GRL", "GUF", "GUM", "HMD",
    "IMN", "IOT", "JEY", "MAC", "MAF", "MNP", "MSR", "MTQ", "MYT", "NCL", "NFK",
    "NIU", "PCN", "PYF", "REU", "SGS", "SHN", "SJM", "SPM", "SXM", "TCA", "TKL",
    "UMI", "VGB", "VIR", "WLF",
}

REGION_OR_AGGREGATE = {
    "AFE", "AFW", "ARB", "CEB", "CSS", "EAP", "EAR", "EAS", "ECA", "ECS", "EMU",
    "EUU", "FCS", "HIC", "HPC", "IBD", "IBT", "IDA", "IDB", "IDX", "INX", "LAC",
    "LCN", "LDC", "LIC", "LMC", "LMY", "LTE", "MEA", "MIC", "MNA", "NAC", "OED",
    "OSS", "PRE", "PSS", "PST", "SAS", "SSA", "SSF", "SST", "TEA", "TEC", "TLA",
    "TMN", "TSA", "TSS", "UMC",
}

ORGANIZATION_CODES = {"EU", "EU27", "EU28", "OECD", "OPEC", "ASEAN"}
GLOBAL_CODES = {"WLD", "WOR", "GLO", "GLOBAL", "WORLD"}
OBSOLETE_OR_NON_COMPARABLE = {"ANT", "SCG", "ESH"}


def slugify(value: object) -> str:
    text = "" if value is None else str(value)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.replace("&", " and ")
    text = re.sub(r"[^0-9A-Za-z]+", "_", text).strip("_").lower()
    text = re.sub(r"_+", "_", text)
    return text or "unknown"


def relpath(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def year_or_na(year: object) -> str:
    if pd.isna(year):
        return "na"
    return str(int(float(year)))


def make_cell_id(iso3: str, source_id: str, variable_matriz: str, year: object) -> str:
    return f"{iso3}_{source_id}_{slugify(variable_matriz)}_{year_or_na(year)}"


def classify_entity(iso3: str, name: str = "") -> str:
    code = str(iso3).strip().upper()
    if code in HUMAN_APPROVED_COMPARABLE:
        return "country_iso3"
    if code in COUNTRY_ISO3:
        return "country_iso3"
    if code in TERRITORY_ISO3:
        return "territory_iso3"
    if code in ORGANIZATION_CODES:
        return "organization_or_group"
    if code in GLOBAL_CODES:
        return "global"
    if code in REGION_OR_AGGREGATE:
        return "region"
    if code in OBSOLETE_OR_NON_COMPARABLE:
        return "obsolete_or_non_comparable"
    return "unknown_requires_review" if len(code) == 3 and code.isalpha() else "unknown"


def is_valid_iso3(value: object) -> bool:
    code = str(value).strip().upper()
    return len(code) == 3 and code.isalpha() and code not in {"NAN", "NON", "NUL", "NA"}


def is_matrix_country(value: object) -> bool:
    return classify_entity(str(value)) == "country_iso3"


def to_numeric_or_text(value: object) -> tuple[float | None, str | None]:
    if pd.isna(value):
        return None, None
    try:
        return float(value), None
    except (TypeError, ValueError):
        return None, str(value)


def make_panel_row(
    *,
    iso3: str,
    country_name: str,
    entity_type: str,
    source_id: str,
    table_id: str,
    original_variable: str,
    variable_matriz: str,
    year: object,
    value_original: object,
    value_numeric: float | None,
    value_text: str | None,
    unit: str,
    direction: str,
    extraction_rule: str,
    source_file: Path,
    source_sheet: str,
    row_identifier: str,
    confidence_level: str = "extracted",
) -> dict:
    return {
        "cell_id": make_cell_id(iso3, source_id, variable_matriz, year),
        "iso3": str(iso3).strip().upper(),
        "country_name_canonical": str(country_name),
        "entity_type": entity_type,
        "source_id": source_id,
        "table_id": table_id,
        "original_variable": str(original_variable),
        "variable_matriz": slugify(variable_matriz),
        "year": int(year) if pd.notna(year) else pd.NA,
        "value_original": "" if value_original is None else str(value_original),
        "value_numeric": value_numeric,
        "value_text": value_text,
        "unit": unit,
        "direction": direction,
        "confidence_level": confidence_level,
        "extraction_rule": extraction_rule,
        "source_file": relpath(source_file),
        "source_sheet": source_sheet,
        "row_identifier": row_identifier,
        "period": "" if pd.isna(year) else str(int(year)),
        "extractor_version": "fase3_rescue_v1",
        "created_at": "2026-05-06T00:00:00+00:00",
    }
