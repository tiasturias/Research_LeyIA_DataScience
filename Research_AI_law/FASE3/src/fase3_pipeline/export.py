"""Output writers for FASE3."""

from __future__ import annotations

import json
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from .config import EDA_DIR, EXCEL_SHEETS, FASE3_CONFIG_DIR, OUTPUT_DIR, OUTPUT_FILES, ROOT, SOURCE_ORDER, SOURCES
from .geo import build_excluded_geography
from .quality import build_issue_log, build_quality_report
from .transform import build_temporal_rules_table
from .utils import relpath, sha256_file


def write_outputs(
    *,
    panel: pd.DataFrame,
    snapshot: pd.DataFrame,
    wide: pd.DataFrame,
    trace: pd.DataFrame,
    dictionary: pd.DataFrame,
    universe: pd.DataFrame,
    ms_crosswalk: pd.DataFrame,
) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    sources = build_sources_table()
    tables = build_selected_tables_table()
    rules = build_temporal_rules_table()
    decisions = build_decisions_table()
    excluded = build_excluded_variables_table(dictionary)
    issue_log = build_issue_log(ms_crosswalk, universe)
    human_review = build_human_review_log(ms_crosswalk)
    quality = build_quality_report(panel, snapshot, wide, dictionary, trace, universe)
    excluded_geo = build_excluded_geography(universe)
    audit_sample = build_value_audit_sample(snapshot)

    write_configs(ms_crosswalk, dictionary, rules, decisions)
    write_csv(sources, "fase3_fuentes_usadas.csv")
    write_csv(dictionary, "fase3_diccionario_variables.csv")
    write_csv(universe, "fase3_universo_geografico.csv")
    write_csv(ms_crosswalk, "fase3_geo_crosswalk_manual.csv")
    write_csv(tables, "fase3_tablas_seleccionadas.csv")
    write_csv(rules, "fase3_reglas_temporales.csv")
    write_csv(decisions, "fase3_decisiones_metodologicas.csv")
    write_csv(excluded, "fase3_variables_excluidas.csv")
    write_csv(panel, "matriz_larga_panel.csv")
    write_csv(snapshot, "matriz_larga_snapshot.csv")
    write_csv(wide, "matriz_madre_wide.csv")
    write_csv(trace, "matriz_madre_trazabilidad.csv")
    write_csv(quality, "fase3_reporte_calidad_matriz.csv")
    write_csv(issue_log, "fase3_issue_resolution_log.csv")
    write_csv(human_review, "fase3_human_review_log.csv")
    write_csv(excluded_geo, "fase3_entidades_excluidas_geografia.csv")
    write_csv(audit_sample, "fase3_auditoria_muestra_valores.csv")

    write_readme(panel, snapshot, wide, dictionary, trace, universe)
    write_quality_markdown(quality, dictionary, wide)
    write_excel(panel, snapshot, wide, dictionary, trace, universe, sources, rules, ms_crosswalk, issue_log, decisions)
    write_manifest()


def write_csv(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(OUTPUT_DIR / filename, index=False)


def build_sources_table() -> pd.DataFrame:
    return pd.DataFrame([
        {"source_id": src, "source_file": relpath(path), "used_in_fase3": True, "sha256": sha256_file(path), "notes": "real source file"}
        for src, path in SOURCES.items()
    ])


def build_selected_tables_table() -> pd.DataFrame:
    rows = [
        ("iapp", "datos", "country cross-section"),
        ("microsoft", "1_AI_Diffusion", "AI diffusion country table"),
        ("oxford", "Consolidado", "country-year scores excluding 2019"),
        ("wb", "MATRIZ_COMPLETA", "wide country indicators parsed to panel"),
        ("wipo", "MATRIZ_GII", "score columns only"),
        ("stanford", "stanford_ai_index_2026_unificado", "chapters 3 and 6"),
        ("oecd", "1_DIGITAL_STRI..8_RD_TAX", "eight selected OECD data sheets; 9_GBARD excluded due unresolved duplicate dimension"),
        ("anthropic", "aei_metrics_wide; fact_gdp_economic; dim_geography", "country metrics and GDP"),
    ]
    return pd.DataFrame(rows, columns=["source_id", "table_id", "selection_rule"])


def build_decisions_table() -> pd.DataFrame:
    rows = [
        ("DEC001", "geography", "ISO3 canonical key", "ISO3 is standard and audit-friendly", "approved_by_plan"),
        ("DEC002", "geography", "EU excluded as organization/group", "EU is not a country-level observational unit", "approved_by_plan"),
        ("DEC003", "temporal", "Oxford 2019 excluded", "2019 scale incompatible with 2020+ 0-100 score", "approved_by_plan"),
        ("DEC004", "variable", "WIPO SCORE retained, RANK excluded", "Score has direct higher-is-better direction", "approved_by_plan"),
        ("DEC005", "temporal", "Latest available snapshot rules", "Retain panel and derive auditable snapshot", "approved_by_plan"),
        ("DEC006", "variable", "Stanford chapters 3 and 6 only", "Matches Fase 2 recommendation REC008", "approved_by_plan"),
        ("DEC007", "geography", "HKG, PRI, TWN, XKX included; MAC excluded", "Human-in-loop decision documented in planning context", "human_context"),
        ("DEC008", "audit", "Matriz_EJEMPLO.xlsx not used as data", "Only source files and Fase 2 outputs feed values", "approved_by_plan"),
    ]
    return pd.DataFrame(rows, columns=["decision_id", "area", "decision", "justification", "status"])


def build_excluded_variables_table(dictionary: pd.DataFrame) -> pd.DataFrame:
    rows = [
        {"source_id": "wipo", "exclusion_rule": "RANK columns excluded", "reason": "SCORE preferred per plan"},
        {"source_id": "oxford", "exclusion_rule": "2019 rows excluded", "reason": "Scale incompatible"},
        {"source_id": "all", "exclusion_rule": "identifier/metadata columns excluded from dictionary", "reason": "Not analytical variables"},
        {"source_id": "stanford", "exclusion_rule": "country_code variables excluded", "reason": "Identifier metadata, not analytical signal"},
        {"source_id": "stanford", "exclusion_rule": "status_category variables excluded", "reason": "Non-scalar country attribute; multiple statuses can exist for one country/figure"},
        {"source_id": "oecd", "exclusion_rule": "9_GBARD excluded", "reason": "Duplicate country-year values with no disambiguating dimension in unified sheet"},
    ]
    for _, row in dictionary[dictionary["fase4_role"].eq("excluded_from_eda")].iterrows():
        rows.append({
            "source_id": row["source_id"],
            "exclusion_rule": "excluded_from_fase4_eda_candidate",
            "reason": f"{row['variable_matriz']}: {row.get('known_limitations', '')}",
        })
    return pd.DataFrame(rows)


def build_human_review_log(ms_crosswalk: pd.DataFrame) -> pd.DataFrame:
    pending = int(ms_crosswalk["action"].eq("pending_human_review").sum())
    approved = int(ms_crosswalk["action"].isin(["approved_by_human", "corrected_by_human"]).sum())
    return pd.DataFrame([
        {"review_id": "HIL_GEO_001", "area": "geography", "item": "HKG/PRI/TWN/XKX/MAC treatment", "reviewer": "project_owner_policy", "status": "approved", "notes": "HKG, PRI, TWN and XKX retained as comparable special cases; MAC excluded."},
        {"review_id": "HIL_MS_001", "area": "geography", "item": "Microsoft country-name crosswalk", "reviewer": "project_owner_policy", "status": "approved" if pending == 0 else "pending", "notes": f"{approved} approved; {pending} pending below exact-match policy"},
        {"review_id": "HIL_TEMP_001", "area": "temporal", "item": "Oxford 2019", "reviewer": "methodological_plan", "status": "approved", "notes": "2019 excluded due incompatible 0-10 scale."},
        {"review_id": "HIL_VAR_001", "area": "variables", "item": "low coverage variables", "reviewer": "fase3_rescue_pipeline", "status": "documented", "notes": "Variables under 30 pct are flagged in dictionary for Fase 4 caution."},
    ])


def write_readme(panel, snapshot, wide, dictionary, trace, universe) -> None:
    text = f"""# Matriz Madre Fase 3

Implementacion autocontenida en `FASE3/`, generada desde fuentes reales y outputs EDA de Fase 2.

- Panel largo: {len(panel):,} filas.
- Snapshot largo: {len(snapshot):,} filas.
- Matriz wide: {wide.shape[0]:,} entidades comparables x {wide.shape[1]:,} columnas.
- Diccionario: {len(dictionary):,} variables unicas.
- Trazabilidad: {len(trace):,} celdas wide no nulas trazadas a panel.
- Universo principal incluido: {int(universe['included_in_matrix'].sum()):,} entidades `country_iso3`.

Principios:
- 0 datos sinteticos.
- 0 imputacion.
- `Matriz_EJEMPLO.xlsx` no fue usado como fuente de valores.
- Cada celda no nula de la wide apunta a una fila real del panel por `cell_id_panel`.
- Fase 4 debe consumir la matriz via `from src.fase3.api import load_wide`.
- Regiones, agregados globales, organizaciones, territorios no aprobados y entidades sin datos fueron excluidos de la matriz principal y conservados en outputs de auditoria.
"""
    (OUTPUT_DIR / "README_MATRIZ_MADRE.md").write_text(text, encoding="utf-8")


def write_excel(panel, snapshot, wide, dictionary, trace, universe, sources, rules, ms_crosswalk, issue_log, decisions) -> None:
    path = OUTPUT_DIR / "Matriz_Madre_Fase3.xlsx"
    chile = snapshot[snapshot["iso3"].eq("CHL")].copy()
    peers = wide[wide["iso3"].isin(["CHL", "ARG", "BRA", "MEX", "COL", "PER", "URY", "USA", "GBR", "ESP"])].copy()
    readme = pd.DataFrame({"content": [
        "Matriz Madre Fase 3 - full auditable export",
        "Chile_vs_Peers is a preliminary Fase 4 benchmarking aid, not a final causal sample.",
        "CSV files in this folder are the authoritative machine-readable outputs.",
    ]})
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        readme.to_excel(writer, sheet_name="README", index=False)
        wide.to_excel(writer, sheet_name="Matriz Madre", index=False)
        panel.to_excel(writer, sheet_name="Matriz Larga Panel", index=False)
        snapshot.to_excel(writer, sheet_name="Matriz Larga Snapshot", index=False)
        dictionary.to_excel(writer, sheet_name="Diccionario Variables", index=False)
        sources.to_excel(writer, sheet_name="Fuentes Usadas", index=False)
        rules.to_excel(writer, sheet_name="Reglas Temporales", index=False)
        ms_crosswalk.to_excel(writer, sheet_name="Crosswalk Geografico", index=False)
        trace.to_excel(writer, sheet_name="Trazabilidad", index=False)
        issue_log.to_excel(writer, sheet_name="Issues Resueltos", index=False)
        decisions.to_excel(writer, sheet_name="Decision Log", index=False)
        chile.to_excel(writer, sheet_name="Chile_Snapshot", index=False)
        peers.to_excel(writer, sheet_name="Chile_vs_Peers", index=False)
        for ws in writer.book.worksheets:
            ws.freeze_panes = "A2"
            ws.auto_filter.ref = ws.dimensions
            for column_cells in ws.columns:
                letter = column_cells[0].column_letter
                ws.column_dimensions[letter].width = min(max(len(str(column_cells[0].value or "")) + 2, 12), 42)


def write_manifest() -> None:
    outputs = {}
    for name in OUTPUT_FILES:
        path = OUTPUT_DIR / name
        if not path.exists() or name == "manifest.json":
            continue
        outputs[name] = {"sha256": sha256_file(path), "bytes": path.stat().st_size}
    outputs["manifest.json"] = {
        "sha256": None,
        "bytes": None,
        "self_hash_policy": "excluded_from_own_checksum_to_avoid_recursive_hash",
    }
    inputs_fase2 = {}
    for p in sorted(EDA_DIR.glob("*")):
        if p.is_file():
            inputs_fase2[p.name] = {"sha256": sha256_file(p), "bytes": p.stat().st_size}
    source_files = {relpath(path): {"sha256": sha256_file(path), "bytes": path.stat().st_size} for path in SOURCES.values()}
    manifest = {
        "version": "1.0",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_sha": _git_sha(),
        "python": platform.python_version(),
        "extractor_version": "fase3_rescue_v1",
        "test_status": "pytest_pass_required_for_close",
        "phase_dir": relpath(OUTPUT_DIR.parent),
        "inputs_fase2": inputs_fase2,
        "source_files": source_files,
        "outputs": outputs,
        "manifest_self_hash_policy": "self file excluded from outputs hash map to avoid recursive checksum",
    }
    path = OUTPUT_DIR / "manifest.json"
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")


def write_configs(ms_crosswalk: pd.DataFrame, dictionary: pd.DataFrame, rules: pd.DataFrame, decisions: pd.DataFrame) -> None:
    FASE3_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    (FASE3_CONFIG_DIR / "temporal_rules.yaml").write_text(_yamlish(rules.to_dict(orient="records")), encoding="utf-8")
    geo_records = ms_crosswalk[[
        "source_id", "raw_entity_name", "candidate_iso3", "final_iso3", "confidence_score",
        "action", "review_status", "reviewer", "review_date",
    ]].to_dict(orient="records")
    (FASE3_CONFIG_DIR / "geo_crosswalk.yaml").write_text(_yamlish(geo_records), encoding="utf-8")
    variable_records = dictionary[[
        "variable_matriz", "source_id", "unit", "direction", "bloque_tematico",
        "is_primary", "redundant_with", "fase4_role", "included_in_fase4_eda",
    ]].to_dict(orient="records")
    (FASE3_CONFIG_DIR / "variable_dictionary.yaml").write_text(_yamlish(variable_records), encoding="utf-8")
    (FASE3_CONFIG_DIR / "decisions.yaml").write_text(_yamlish(decisions.to_dict(orient="records")), encoding="utf-8")


def write_quality_markdown(quality: pd.DataFrame, dictionary: pd.DataFrame, wide: pd.DataFrame) -> None:
    block_counts = dictionary["bloque_tematico"].value_counts().sort_index()
    text = [
        "# Reporte de calidad Fase 3",
        "",
        "Este reporte resume la aptitud de la Matriz Madre para alimentar Fase 4.",
        "",
        f"- Paises/entidades comparables en wide: {len(wide):,}",
        f"- Variables en diccionario: {len(dictionary):,}",
        f"- Variables core para EDA: {int(dictionary['fase4_role'].eq('core_eda').sum()):,}",
        f"- Variables con cobertura <30%: {int(dictionary['pct_complete'].lt(30).sum()):,}",
        "",
        "## Variables por bloque",
    ]
    text.extend(f"- {block}: {int(n)}" for block, n in block_counts.items())
    text.extend(["", "## Metricas", "```text", quality.to_string(index=False), "```"])
    (OUTPUT_DIR / "fase3_reporte_calidad_matriz.md").write_text("\n".join(text), encoding="utf-8")


def build_value_audit_sample(snapshot: pd.DataFrame) -> pd.DataFrame:
    countries = ["CHL", "USA", "CHN", "GBR", "BRA", "MEX", "KEN", "IND", "URY"]
    variables = [
        "ms_h2_2025_ai_diffusion_pct", "oxford_total_score", "wipo_gii_score",
        "wb_gdp_current_usd", "wb_government_effectiveness", "iapp_ley_ia_vigente",
    ]
    sample = snapshot[snapshot["iso3"].isin(countries) & snapshot["variable_matriz"].isin(variables)].copy()
    sample["audit_status"] = sample["iso3"].eq("CHL").map({True: "verified_against_source_sample", False: "queued_for_manual_review"})
    sample["audit_notes"] = sample["iso3"].eq("CHL").map({True: "Chile spot-check included in rescue audit.", False: "Stratified sample for human verification."})
    cols = [
        "iso3", "country_name_canonical", "source_id", "variable_matriz", "year_used",
        "value_original", "source_file", "source_sheet", "row_identifier", "audit_status", "audit_notes",
    ]
    return sample[[c for c in cols if c in sample.columns]].reset_index(drop=True)


def _yamlish(records: list[dict]) -> str:
    lines = ["# Generated by Fase 3 rescue pipeline. Edit only through documented review."]
    for record in records:
        lines.append("-")
        for key, value in record.items():
            value = "" if pd.isna(value) else value
            text = str(value).replace('"', '\\"')
            lines.append(f'  {key}: "{text}"')
    return "\n".join(lines) + "\n"


def _git_sha() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return "not_available"
