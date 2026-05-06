"""Source extractors for the self-contained Fase 3 pipeline."""

from __future__ import annotations

import re

import pandas as pd
from rapidfuzz import fuzz, process

from .config import SOURCES
from .geo import build_microsoft_crosswalk, canonical_name_map
from .utils import classify_entity, is_valid_iso3, make_panel_row, slugify, to_numeric_or_text

PANEL_COLUMNS = [
    "cell_id", "iso3", "country_name_canonical", "entity_type", "source_id", "table_id",
    "original_variable", "variable_matriz", "year", "period", "value_original",
    "value_numeric", "value_text", "unit", "direction", "confidence_level",
    "extraction_rule", "source_file", "source_sheet", "row_identifier",
    "extractor_version", "created_at",
]


def extract_all() -> pd.DataFrame:
    frames = [
        extract_iapp(),
        extract_microsoft(),
        extract_oxford(),
        extract_wb(),
        extract_wipo(),
        extract_stanford(),
        extract_oecd(),
        extract_anthropic(),
    ]
    panel = pd.concat(frames, ignore_index=True)
    panel["year"] = pd.to_numeric(panel["year"], errors="coerce").astype("Int64")
    panel = panel[panel["year"].isna() | panel["year"].between(2018, 2026)].copy()
    panel = panel.drop_duplicates().reset_index(drop=True)
    duplicated = panel[panel["cell_id"].duplicated(keep=False)]
    if len(duplicated):
        cols = ["cell_id", "source_id", "variable_matriz", "year", "row_identifier"]
        raise ValueError("Duplicate panel cell_id detected:\n" + duplicated[cols].head(20).to_string(index=False))
    panel = panel[PANEL_COLUMNS]
    return panel.sort_values(["iso3", "source_id", "variable_matriz", "year"], na_position="last").reset_index(drop=True)


def extract_iapp() -> pd.DataFrame:
    path = SOURCES["iapp"]
    df = pd.read_excel(path, sheet_name="datos", engine="openpyxl")
    skip = {"iso3", "pais", "pagina_evidencia", "fuente", "fecha_fuente"}
    rows = []
    for _, r in df.iterrows():
        iso3 = str(r["iso3"]).strip().upper()
        if not is_valid_iso3(iso3):
            continue
        for col in df.columns:
            if col in skip or pd.isna(r[col]):
                continue
            variable = f"iapp_{slugify(col)}"
            num, text = to_numeric_or_text(r[col])
            unit = "binary" if col not in {"n_autoridades", "n_leyes_relacionadas", "modelo_gobernanza", "categoria_obligatoriedad"} else ("count" if col.startswith("n_") else "categorical")
            direction = "higher_better" if unit in {"binary", "count"} else "categorical"
            rows.append(make_panel_row(
                iso3=iso3, country_name=r["pais"], entity_type="country_iso3",
                source_id="iapp", table_id="datos", original_variable=col,
                variable_matriz=variable, year=pd.NA, value_original=r[col],
                value_numeric=num, value_text=text, unit=unit, direction=direction,
                extraction_rule="raw_cross_section_2026_01", source_file=path,
                source_sheet="datos", row_identifier=f"iapp:{iso3}:{col}",
            ))
    return pd.DataFrame(rows)


def extract_microsoft() -> pd.DataFrame:
    path = SOURCES["microsoft"]
    df = pd.read_excel(path, sheet_name="1_AI_Diffusion", engine="openpyxl")
    cw = build_microsoft_crosswalk()
    cw = cw[cw["action"].isin(["approved_by_human", "corrected_by_human"])].set_index("raw_entity_name")
    specs = [
        ("H1 2025 AI Diffusion (%)", "ms_h1_2025_ai_diffusion_pct"),
        ("H2 2025 AI Diffusion (%)", "ms_h2_2025_ai_diffusion_pct"),
        ("Change (pp)", "ms_change_pp"),
    ]
    rows = []
    for _, r in df.iterrows():
        economy = str(r.get("Economy", "")).strip()
        if economy not in cw.index:
            continue
        match = cw.loc[economy]
        iso3 = str(match["final_iso3"] if "final_iso3" in match else match["iso3_resuelto"]).strip().upper()
        for col, variable in specs:
            if col not in df.columns or pd.isna(r[col]):
                continue
            num, text = to_numeric_or_text(r[col])
            rows.append(make_panel_row(
                iso3=iso3, country_name=match["country_name_canonical"],
                entity_type=classify_entity(iso3, economy), source_id="microsoft",
                table_id="1_AI_Diffusion", original_variable=col,
                variable_matriz=variable, year=2025, value_original=r[col],
                value_numeric=num, value_text=text, unit="pct", direction="higher_better",
                extraction_rule="microsoft_country_name_crosswalk", source_file=path,
                source_sheet="1_AI_Diffusion", row_identifier=f"microsoft:{economy}:{col}",
            ))
    return pd.DataFrame(rows)


def extract_oxford() -> pd.DataFrame:
    path = SOURCES["oxford"]
    df = pd.read_excel(path, sheet_name="Consolidado", engine="openpyxl")
    skip = {"iso3", "entity_type", "pais_original", "year", "scale", "framework", "region_pertenece"}
    rows = []
    for _, r in df.iterrows():
        year = int(r["year"]) if pd.notna(r.get("year")) else pd.NA
        if year == 2019:
            continue
        iso3 = str(r.get("iso3", "")).strip().upper()
        if not is_valid_iso3(iso3):
            continue
        entity_type = classify_entity(iso3, str(r.get("pais_original", "")))
        for col in df.columns:
            cl = str(col).lower()
            if col in skip or pd.isna(r[col]):
                continue
            if "rank_" in cl or cl.startswith("score_") or cl.startswith("rank"):
                continue
            if cl in {"data_availability.1", "ranking_detail"}:
                continue
            num, text = to_numeric_or_text(r[col])
            if num is None and text is None:
                continue
            unit = "score_0_100" if num is not None else "categorical"
            direction = "higher_better" if num is not None else "categorical"
            rows.append(make_panel_row(
                iso3=iso3, country_name=r.get("pais_original", iso3), entity_type=entity_type,
                source_id="oxford", table_id="Consolidado", original_variable=col,
                variable_matriz=f"oxford_{slugify(col)}", year=year,
                value_original=r[col], value_numeric=num, value_text=text, unit=unit,
                direction=direction, extraction_rule="exclude_2019_scale_incompatible",
                source_file=path, source_sheet="Consolidado",
                row_identifier=f"oxford:{iso3}:{col}:{year}",
            ))
    return pd.DataFrame(rows)


def extract_wb() -> pd.DataFrame:
    path = SOURCES["wb"]
    df = pd.read_excel(path, sheet_name="MATRIZ_COMPLETA", engine="openpyxl")
    year_pattern = re.compile(r"^(.+)_(\d{4})$")
    skip = {"iso3", "country_name", "wb_region", "wb_income_group"}
    rows = []
    for _, r in df.iterrows():
        iso3 = str(r["iso3"]).strip().upper()
        if not is_valid_iso3(iso3):
            continue
        for col in df.columns:
            if col in skip or pd.isna(r[col]):
                continue
            match = year_pattern.match(str(col))
            if not match:
                continue
            indicator, year = match.group(1), int(match.group(2))
            num, text = to_numeric_or_text(r[col])
            rows.append(make_panel_row(
                iso3=iso3, country_name=r.get("country_name", iso3),
                entity_type=classify_entity(iso3, r.get("country_name", "")),
                source_id="wb", table_id="MATRIZ_COMPLETA", original_variable=col,
                variable_matriz=f"wb_{slugify(indicator)}", year=year,
                value_original=r[col], value_numeric=num, value_text=text,
                unit=_unit_from_name(indicator), direction=_direction_from_name(indicator),
                extraction_rule="wide_indicator_year_parse", source_file=path,
                source_sheet="MATRIZ_COMPLETA", row_identifier=f"wb:{iso3}:{col}",
            ))
    return pd.DataFrame(rows)


def extract_wipo() -> pd.DataFrame:
    path = SOURCES["wipo"]
    df = pd.read_excel(path, sheet_name="MATRIZ_GII", engine="openpyxl")
    score_cols = [c for c in df.columns if "SCORE" in str(c).upper()]
    year_pattern = re.compile(r"_(\d{4})$")
    rows = []
    for _, r in df.iterrows():
        iso3 = str(r["ISO3"]).strip().upper()
        if not is_valid_iso3(iso3):
            continue
        for col in score_cols:
            if pd.isna(r[col]):
                continue
            year_match = year_pattern.search(str(col))
            year = int(year_match.group(1)) if year_match else pd.NA
            base = re.sub(r"_SCORE_\d{4}$", "_SCORE", str(col), flags=re.IGNORECASE)
            num, text = to_numeric_or_text(r[col])
            rows.append(make_panel_row(
                iso3=iso3, country_name=r.get("ECONOMY_NAME", iso3),
                entity_type=classify_entity(iso3, r.get("ECONOMY_NAME", "")),
                source_id="wipo", table_id="MATRIZ_GII", original_variable=col,
                variable_matriz=f"wipo_{slugify(base)}", year=year,
                value_original=r[col], value_numeric=num, value_text=text,
                unit="score_0_100", direction="higher_better",
                extraction_rule="score_only_rank_excluded", source_file=path,
                source_sheet="MATRIZ_GII", row_identifier=f"wipo:{iso3}:{col}",
            ))
    return pd.DataFrame(rows)


def extract_stanford() -> pd.DataFrame:
    path = SOURCES["stanford"]
    df = pd.read_csv(path)
    df = df[df["chapter"].isin([3, 6])].copy()
    name_map = canonical_name_map()
    name_choices = list(name_map.keys())
    rows = []
    for _, r in df.iterrows():
        raw_name = str(r.get("entity_name_raw", "")).strip()
        iso3 = _resolve_entity_name_to_iso3(raw_name, r.get("iso3", ""), name_map, name_choices)
        if not is_valid_iso3(iso3) or pd.isna(r.get("value")):
            continue
        if str(r.get("entity_type", "")).lower() not in {"country", "country_iso3", "territory_iso3"}:
            continue
        variable_raw = str(r.get("variable", ""))
        if (
            "country_code" in variable_raw.lower()
            or "country code" in variable_raw.lower()
            or "status_category" in variable_raw.lower()
            or "status category" in variable_raw.lower()
        ):
            continue
        year = int(r["year"]) if pd.notna(r.get("year")) else pd.NA
        fig_id = slugify(r.get("fig_id", "fig"))
        variable = f"stanford_{fig_id}_{slugify(variable_raw)}"
        num, text = to_numeric_or_text(r["value"])
        rows.append(make_panel_row(
            iso3=iso3, country_name=r.get("entity_name_std", iso3),
            entity_type=classify_entity(iso3, r.get("entity_name_std", "")),
            source_id="stanford", table_id="stanford_ai_index_2026_unificado",
            original_variable=f"{r.get('fig_id')}/{variable_raw}",
            variable_matriz=variable, year=year, value_original=r["value"],
            value_numeric=num, value_text=text, unit="count" if num is not None else "categorical",
            direction="unknown" if num is not None else "categorical",
            extraction_rule="chapters_3_and_6_only", source_file=path, source_sheet="CSV",
            row_identifier=f"stanford:{iso3}:{r.get('fig_id')}:{variable_raw}:{year}",
        ))
    return pd.DataFrame(rows)


def _resolve_entity_name_to_iso3(raw_name: str, source_iso3: object, name_map: dict[str, str], choices: list[str]) -> str:
    if raw_name in name_map:
        return name_map[raw_name]
    match = process.extractOne(raw_name, choices, scorer=fuzz.token_sort_ratio)
    if match and match[1] >= 96:
        return name_map[match[0]]
    return str(source_iso3).strip().upper()


def extract_oecd() -> pd.DataFrame:
    path = SOURCES["oecd"]
    tables = [
        "1_DIGITAL_STRI", "2_INDIGO", "3_REGULATORY_GOV", "4_DIGITAL_GOV",
        "5_ICT_BUSINESS", "6_FDI_RESTRICTIVENESS", "7_PMR", "8_RD_TAX",
    ]
    rows = []
    for sheet in tables:
        df = pd.read_excel(path, sheet_name=sheet, engine="openpyxl")
        for _, r in df.iterrows():
            iso3 = str(r.get("iso3", "")).strip().upper()
            if not is_valid_iso3(iso3):
                continue
            year = int(r["year"]) if pd.notna(r.get("year")) else pd.NA
            for col in df.columns:
                if col in {"iso3", "year"} or pd.isna(r[col]):
                    continue
                num, text = to_numeric_or_text(r[col])
                rows.append(make_panel_row(
                    iso3=iso3, country_name=iso3, entity_type=classify_entity(iso3),
                    source_id="oecd", table_id=sheet, original_variable=col,
                    variable_matriz=f"oecd_{slugify(sheet)}_{slugify(col)}", year=year,
                    value_original=r[col], value_numeric=num, value_text=text,
                    unit=_unit_from_name(col), direction=_direction_from_name(col),
                    extraction_rule="raw_panel_table", source_file=path, source_sheet=sheet,
                    row_identifier=f"oecd:{iso3}:{sheet}:{col}:{year}",
                ))
    return pd.DataFrame(rows)


def extract_anthropic() -> pd.DataFrame:
    path = SOURCES["anthropic"]
    geo = pd.read_excel(path, sheet_name="dim_geography", engine="openpyxl")
    geo_map = {
        str(r["iso_alpha_2"]).upper(): (str(r["iso_alpha_3"]).upper(), str(r["country_name"]))
        for _, r in geo.iterrows()
        if r.get("geography_type") == "country" and pd.notna(r.get("iso_alpha_2")) and pd.notna(r.get("iso_alpha_3"))
    }
    metrics = pd.read_excel(path, sheet_name="aei_metrics_wide", engine="openpyxl")
    metrics["_date_start_dt"] = pd.to_datetime(metrics["date_start"], errors="coerce")
    metrics = metrics.sort_values("_date_start_dt").drop_duplicates(
        subset=["geo_id", "platform_and_product"], keep="last"
    )
    key_metrics = ["collaboration_pct", "usage_pct", "ai_autonomy_mean", "ai_autonomy_median", "ai_education_years_mean"]
    rows = []
    for _, r in metrics.iterrows():
        geo_id = str(r.get("geo_id", "")).strip().upper()
        if geo_id not in geo_map:
            continue
        iso3, country = geo_map[geo_id]
        year = pd.to_datetime(r.get("date_start")).year if pd.notna(r.get("date_start")) else pd.NA
        for col in key_metrics:
            if col not in metrics.columns or pd.isna(r[col]):
                continue
            num, text = to_numeric_or_text(r[col])
            rows.append(make_panel_row(
                iso3=iso3, country_name=country, entity_type=classify_entity(iso3, country),
                source_id="anthropic", table_id="aei_metrics_wide", original_variable=col,
                variable_matriz=f"anthropic_{slugify(col)}", year=year,
                value_original=r[col], value_numeric=num, value_text=text,
                unit="pct" if "pct" in col else "count", direction="higher_better" if "pct" in col else "unknown",
                extraction_rule="country_iso2_to_iso3", source_file=path, source_sheet="aei_metrics_wide",
                row_identifier=f"anthropic:{iso3}:{col}:{r.get('date_start')}",
            ))
    gdp = pd.read_excel(path, sheet_name="fact_gdp_economic", engine="openpyxl")
    for _, r in gdp.iterrows():
        iso3 = str(r.get("iso_alpha_3", "")).strip().upper()
        if not is_valid_iso3(iso3) or pd.isna(r.get("gdp_total")):
            continue
        year = int(r["year_gdp"]) if pd.notna(r.get("year_gdp")) else pd.NA
        num, text = to_numeric_or_text(r["gdp_total"])
        rows.append(make_panel_row(
            iso3=iso3, country_name=iso3, entity_type=classify_entity(iso3),
            source_id="anthropic", table_id="fact_gdp_economic", original_variable="gdp_total",
            variable_matriz="anthropic_gdp_total", year=year, value_original=r["gdp_total"],
            value_numeric=num, value_text=text, unit="usd", direction="higher_better",
            extraction_rule="raw_fact_gdp_economic", source_file=path, source_sheet="fact_gdp_economic",
            row_identifier=f"anthropic:{iso3}:gdp_total:{year}",
        ))
    return pd.DataFrame(rows)


def _unit_from_name(name: object) -> str:
    text = str(name).lower()
    if any(k in text for k in ["corruption", "effectiveness", "political_stability", "regulatory_quality", "rule_of_law", "voice_accountability"]):
        return "wgi_-2.5_2.5"
    if any(k in text for k in ["enrollment", "enrolment", "tertiary"]):
        return "pct"
    if "pct" in text or "percent" in text or "per100" in text or "per_100" in text:
        return "pct"
    if "usd" in text or "gdp" in text or "gbard" in text:
        return "usd"
    if "score" in text or "index" in text:
        return "score_0_100"
    return "count"


def _direction_from_name(name: object) -> str:
    text = str(name).lower()
    if any(k in text for k in ["stri", "restrict", "unemployment", "inflation"]):
        return "lower_better"
    if any(k in text for k in ["score", "index", "gdp", "internet", "broadband", "education", "research", "corruption", "effectiveness", "political_stability", "regulatory_quality", "rule_of_law", "voice_accountability", "quality"]):
        return "higher_better"
    return "unknown"
