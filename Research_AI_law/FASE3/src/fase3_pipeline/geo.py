"""Geographic universe and crosswalk construction."""

from __future__ import annotations

import pandas as pd
from rapidfuzz import fuzz, process

from .config import EDA_DIR, SOURCES, SOURCE_ORDER
from .utils import classify_entity, is_valid_iso3


# Manual canonical names for entities where best_effort lacks a usable human
# name or where we want a specific official label. Used by _resolve_name() to
# guarantee that country_name_canonical is never the raw ISO3 code for a
# real country.
_CANONICAL_NAME_OVERRIDES: dict[str, str] = {
    "USA": "United States",
    "GBR": "United Kingdom",
    "RUS": "Russia",
    "KOR": "South Korea",
    "PRK": "North Korea",
    "IRN": "Iran",
    "VEN": "Venezuela",
    "BOL": "Bolivia",
    "CIV": "Cote d'Ivoire",
    "CPV": "Cabo Verde",
    "COD": "Democratic Republic of the Congo",
    "COG": "Republic of the Congo",
    "CZE": "Czech Republic",
    "EGY": "Egypt",
    "FRA": "France",
    "DEU": "Germany",
    "GRC": "Greece",
    "HKG": "Hong Kong",
    "MAC": "Macao",
    "MDA": "Moldova",
    "MKD": "North Macedonia",
    "PRI": "Puerto Rico",
    "SVK": "Slovakia",
    "SVN": "Slovenia",
    "SYR": "Syria",
    "TWN": "Taiwan",
    "TZA": "Tanzania",
    "VNM": "Vietnam",
    "LAO": "Laos",
    "BRN": "Brunei",
    "PSE": "Palestine",
    "XKX": "Kosovo",
    "XKV": "Kosovo",
    "ARE": "United Arab Emirates",
    "GMB": "The Gambia",
    "BHS": "The Bahamas",
}


def _resolve_name(iso3: str, raw_best_effort: str) -> str:
    """Extract human-readable country name from a `country_name_best_effort`
    field that may have format `"ISO3 | Name"` or `"Name | ISO3"` or just
    `"Name"`. Falls back to manual override or ISO3 if nothing else works.

    This is the canonical resolver used everywhere in geo.py to avoid the
    historical bug where split(' | ')[0] would return the ISO3 code instead
    of the human name (fix v1.1, 2026-05-06).
    """
    iso3_norm = str(iso3).strip().upper()
    if iso3_norm in _CANONICAL_NAME_OVERRIDES:
        return _CANONICAL_NAME_OVERRIDES[iso3_norm]
    if pd.isna(raw_best_effort) or not str(raw_best_effort).strip():
        return iso3_norm
    parts = [p.strip() for p in str(raw_best_effort).split("|")]
    candidates = [p for p in parts if p and p.upper() != iso3_norm]
    if not candidates:
        return iso3_norm
    candidates.sort(key=lambda x: (-len(x), x))
    return candidates[0]


ALIASES = {
    "Türkiye": "TUR",
    "Turkey": "TUR",
    "South Korea": "KOR",
    "Republic of Korea": "KOR",
    "Korea, Rep.": "KOR",
    "Czechia": "CZE",
    "Czech Republic": "CZE",
    "Ivory Coast": "CIV",
    "Cote D'Ivoire": "CIV",
    "Côte d'Ivoire": "CIV",
    "Netherlands": "NLD",
    "The Netherlands": "NLD",
    "Bosnia And Herzegovina": "BIH",
    "Bosnia and Herzegovina": "BIH",
    "Congo (DRC)": "COD",
    "Democratic Republic of the Congo": "COD",
    "Russia": "RUS",
    "Russian Federation": "RUS",
    "Iran": "IRN",
    "Iran, Islamic Rep.": "IRN",
    "Venezuela": "VEN",
    "Venezuela, RB": "VEN",
    "Vietnam": "VNM",
    "Viet Nam": "VNM",
    "Laos": "LAO",
    "Lao PDR": "LAO",
    "Bolivia": "BOL",
    "Tanzania": "TZA",
    "United States": "USA",
    "United States of America": "USA",
    "United Kingdom": "GBR",
    "UK": "GBR",
    "Egypt": "EGY",
    "Gambia": "GMB",
    "Yemen": "YEM",
    "Slovakia": "SVK",
    "Hong Kong": "HKG",
    "Hong Kong, China": "HKG",
    "China, Hong Kong Special Administrative Region": "HKG",
    "Puerto Rico": "PRI",
    "Macao": "MAC",
    "Macau": "MAC",
    "Taiwan": "TWN",
    "Kosovo": "XKX",
    "United Arab Emirates": "ARE",
}


def canonical_name_map() -> dict[str, str]:
    coverage = pd.read_csv(EDA_DIR / "cobertura_pais_fuente.csv")
    out = {}
    for _, row in coverage.iterrows():
        iso3 = str(row["iso3"]).strip().upper()
        if not is_valid_iso3(iso3) or classify_entity(iso3, str(row["country_name_best_effort"])) not in {"country_iso3", "territory_iso3"}:
            continue
        for name in str(row["country_name_best_effort"]).split(" | "):
            name = name.strip()
            if name:
                out[name] = iso3
    out.update(ALIASES)
    return out


def build_microsoft_crosswalk(threshold: int = 90) -> pd.DataFrame:
    ms = pd.read_excel(SOURCES["microsoft"], sheet_name="1_AI_Diffusion", engine="openpyxl")
    names = ms["Economy"].dropna().astype(str).str.strip().drop_duplicates().tolist()
    metadata_markers = ["Fuente:", "Global AI", "Columna Region", "Widening Digital Divide"]
    names = [n for n in names if n and not any(marker in n for marker in metadata_markers)]
    name_map = canonical_name_map()
    choices = list(name_map.keys())
    rows = []
    for raw in names:
        match = process.extractOne(raw, choices, scorer=fuzz.token_sort_ratio)
        if match is None:
            matched_name, score, iso3 = "", 0, ""
        else:
            matched_name, score, _ = match
            iso3 = name_map[matched_name]
        if score == 100:
            action = "approved_by_human"
            review_status = "approved_by_bulk_exact_match_policy"
            reviewer = "project_owner_policy"
            review_date = "2026-05-06"
        elif score >= threshold:
            action = "pending_human_review"
            review_status = "requires_human_review_score_below_100"
            reviewer = "pending"
            review_date = ""
        else:
            action = "pending_human_review"
            review_status = "requires_human_review_below_threshold"
            reviewer = "pending"
            review_date = ""
        rows.append({
            "source_id": "microsoft",
            "raw_entity_name": raw,
            "raw_geo_code": "",
            "candidate_iso3": iso3,
            "final_iso3": iso3 if action == "approved_by_human" else "",
            "iso3_resuelto": iso3 if action == "approved_by_human" else "",
            "country_name_canonical": matched_name,
            "entity_type_final": classify_entity(iso3, raw),
            "match_method": "fuzzy_token_sort_ratio",
            "confidence_score": float(score),
            "action": action,
            "review_status": review_status,
            "reviewer": reviewer,
            "review_date": review_date,
            "evidence": f"candidate={matched_name}; score={score}",
            "notes": "Exact matches bulk-approved under documented rescue policy; lower scores remain excluded until reviewed.",
        })
    return pd.DataFrame(rows)


def build_universe(ms_crosswalk: pd.DataFrame) -> pd.DataFrame:
    coverage = pd.read_csv(EDA_DIR / "cobertura_pais_fuente.csv")
    geo_meta = _world_bank_geo_metadata()
    entities: dict[str, dict] = {}

    for _, row in coverage.iterrows():
        iso3 = str(row["iso3"]).strip().upper()
        if not is_valid_iso3(iso3):
            continue
        entity_type = classify_entity(iso3, str(row["country_name_best_effort"]))
        meta = geo_meta.get(iso3, {})
        entities[iso3] = {
            "iso3": iso3,
            "country_name_canonical": _resolve_name(iso3, row["country_name_best_effort"]),
            "entity_type": entity_type,
            "region": meta.get("region", ""),
            "income_group": meta.get("income_group", ""),
            **{f"present_{src}": int(row.get(f"present_{src}", 0)) for src in SOURCE_ORDER if src != "microsoft"},
            "present_microsoft": 0,
        }

    approved_ms = ms_crosswalk[ms_crosswalk["action"].isin(["approved_by_human", "corrected_by_human"])]
    for _, row in approved_ms.iterrows():
        iso3 = str(row["iso3_resuelto"]).strip().upper()
        if not is_valid_iso3(iso3):
            continue
        meta = geo_meta.get(iso3, {})
        if iso3 not in entities:
            ms_name = str(row["country_name_canonical"] or row["raw_entity_name"])
            entities[iso3] = {
                "iso3": iso3,
                "country_name_canonical": _resolve_name(iso3, ms_name),
                "entity_type": classify_entity(iso3, str(row["raw_entity_name"])),
                "region": meta.get("region", ""),
                "income_group": meta.get("income_group", ""),
                **{f"present_{src}": 0 for src in SOURCE_ORDER},
            }
        entities[iso3]["present_microsoft"] = 1

    rows = []
    for iso3, data in sorted(entities.items()):
        entity_type = classify_entity(iso3, data.get("country_name_canonical", ""))
        sources = [src for src in SOURCE_ORDER if int(data.get(f"present_{src}", 0)) == 1]
        included = entity_type == "country_iso3"
        if iso3 in {"HKG", "PRI", "TWN", "XKX"}:
            notes = "included by documented human-in-loop decision; comparable special case"
        elif entity_type == "territory_iso3":
            notes = "territory excluded from principal country matrix"
        elif entity_type == "organization_or_group":
            notes = "organization/group excluded from country matrix"
        elif entity_type == "region":
            notes = "regional aggregate excluded from country matrix"
        elif entity_type == "global":
            notes = "global aggregate excluded from country matrix"
        elif entity_type in {"obsolete_or_non_comparable", "unknown_requires_review", "unknown"}:
            notes = f"{entity_type} excluded until explicit human approval"
        else:
            notes = ""
        rows.append({
            "iso3": iso3,
            "country_name_canonical": data.get("country_name_canonical", iso3),
            "entity_type": entity_type,
            "region": data.get("region", ""),
            "income_group": data.get("income_group", ""),
            **{f"present_{src}": int(data.get(f"present_{src}", 0)) for src in SOURCE_ORDER},
            "n_sources_present": len(sources),
            "source_list": ", ".join(sources),
            "included_in_matrix": bool(included),
            "included_in_dense_candidate": bool(included and len(sources) >= 5),
            "inclusion_notes": notes,
        })
    return pd.DataFrame(rows).sort_values(["included_in_matrix", "n_sources_present", "iso3"], ascending=[False, False, True]).reset_index(drop=True)


def build_excluded_geography(universe: pd.DataFrame) -> pd.DataFrame:
    excluded = universe[~universe["included_in_matrix"].astype(bool)].copy()
    if excluded.empty:
        return pd.DataFrame(columns=[
            "iso3", "country_name_canonical", "entity_type", "n_sources_present",
            "source_list", "exclusion_reason", "human_decision_required",
        ])
    excluded["exclusion_reason"] = excluded["inclusion_notes"].fillna("")
    excluded["human_decision_required"] = excluded["entity_type"].isin(["territory_iso3", "unknown_requires_review"]).map({True: "yes", False: "no"})
    return excluded[[
        "iso3", "country_name_canonical", "entity_type", "n_sources_present",
        "source_list", "exclusion_reason", "human_decision_required",
    ]].reset_index(drop=True)


def _world_bank_geo_metadata() -> dict[str, dict[str, str]]:
    path = SOURCES["wb"]
    try:
        df = pd.read_excel(path, sheet_name="MATRIZ_COMPLETA", engine="openpyxl", usecols=["iso3", "wb_region", "wb_income_group"])
    except Exception:
        return {}
    out = {}
    for _, row in df.dropna(subset=["iso3"]).iterrows():
        iso3 = str(row["iso3"]).strip().upper()
        out[iso3] = {
            "region": "" if pd.isna(row.get("wb_region")) else str(row.get("wb_region")),
            "income_group": "" if pd.isna(row.get("wb_income_group")) else str(row.get("wb_income_group")),
        }
    return out
