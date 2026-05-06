"""Bloque M: Reporte HTML + README + manifest final."""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from .config import BLOCKS, FASE4_ROOT, OUTPUTS_DIR, sha256_file


def _build_candidates_for_fe(
    variable_summary: pd.DataFrame,
    redundancy: pd.DataFrame,
) -> pd.DataFrame:
    """Clasifica variables para Feature Engineering."""
    if variable_summary.empty:
        return pd.DataFrame()

    df = variable_summary[variable_summary["status"] == "ok"].copy()

    def classify(row):
        if row["pct_complete"] < 30:
            return "exclude_low_coverage"
        if row.get("cv_robust", 1) < 0.05:
            return "exclude_constant"
        if row.get("suggest_log_transform", False):
            return "transform_log"
        if row.get("n_outliers_iqr_1_5", 0) > 10:
            return "keep_with_caution"
        if row["pct_complete"] >= 70:
            return "keep_primary"
        return "keep_with_caution"

    df["fe_recommendation"] = df.apply(classify, axis=1)

    # Mark redundant variables
    if not redundancy.empty and "var_b" in redundancy.columns:
        redundant_secondary = redundancy[
            redundancy["recommendation"].str.startswith("keep_") &
            redundancy["recommendation"].str.contains("_drop_")
        ]["var_b"].tolist()
        df.loc[df["variable_matriz"].isin(redundant_secondary), "fe_recommendation"] = "collapse_redundant"

    return df[["variable_matriz", "bloque_tematico", "source_id", "unit", "pct_complete",
               "n_outliers_iqr_1_5", "suggest_log_transform", "fe_recommendation"]].reset_index(drop=True)


def _build_data_gaps() -> pd.DataFrame:
    gaps = [
        {"gap_id": "G001", "subpregunta": "Q1_investment",
         "variable_faltante": "datacenter_construction_permits_timeline",
         "motivo": "No disponible en ninguna fuente de Fase 3",
         "fuente_potencial": "IEA, CBRE, JLL Real Estate",
         "prioridad": "alta"},
        {"gap_id": "G002", "subpregunta": "Q1_investment",
         "variable_faltante": "corporate_tax_rate_full",
         "motivo": "Cobertura parcial en WB, falta para ~40 países",
         "fuente_potencial": "OECD Tax Database, Trading Economics",
         "prioridad": "media"},
        {"gap_id": "G003", "subpregunta": "Q2_adoption",
         "variable_faltante": "ai_adoption_sme_rate",
         "motivo": "OECD cubre solo países OECD",
         "fuente_potencial": "ITU, Eurostat, encuestas nacionales",
         "prioridad": "media"},
        {"gap_id": "G004", "subpregunta": "Q3_innovation",
         "variable_faltante": "ai_patents_subtype_breakdown",
         "motivo": "Stanford da total, no desglose por campo IA",
         "fuente_potencial": "USPTO PatentsView, EPO Espacenet",
         "prioridad": "baja"},
        {"gap_id": "G005", "subpregunta": "Q4_content",
         "variable_faltante": "legal_text_nlp_embeddings",
         "motivo": "NLP de corpus legal reservado para Fase 5 via skill corpus-legal-ia",
         "fuente_potencial": "CONTEXTOS/ corpus legal + Claude corpus-legal-ia skill",
         "prioridad": "alta"},
        {"gap_id": "G006", "subpregunta": "Q1_investment",
         "variable_faltante": "usa_state_level_ai_regulation",
         "motivo": "USA es país único en wide pero tiene regulación subnacional relevante",
         "fuente_potencial": "IAPP state tracker, NCSL",
         "prioridad": "media"},
    ]
    return pd.DataFrame(gaps)


def _build_decisions_for_fase5(
    candidates: pd.DataFrame,
    submuestras: pd.DataFrame,
) -> dict:
    decisions = {
        "version": "1.0",
        "fecha": datetime.now(timezone.utc).isoformat(),
        "nota": "Decisiones revisadas metodologicamente para Fase 5. No constituyen seleccion causal final ni muestra final unica.",
        "candidatos_outcome_Y": {
            "Q1_investment": [
                "oxford_ind_company_investment_emerging_tech",
                "oxford_ind_ai_unicorns_log",
                "oxford_ind_non_ai_unicorns_log",
                "oxford_ind_vc_availability",
                "wipo_c_vencapdeal_score",
                "wb_fdi_net_inflows",
            ],
            "Q2_adoption": [
                "ms_h2_2025_ai_diffusion_pct",
                "ms_h1_2025_ai_diffusion_pct",
                "ms_change_pp",
                "anthropic_usage_pct",
                "anthropic_collaboration_pct",
                "oecd_5_ict_business_oecd_biz_ai_pct",
                "oecd_5_ict_business_oecd_biz_bigdata_pct",
                "oxford_public_sector_adoption",
                "oxford_ind_adoption_emerging_tech",
            ],
            "Q3_innovation": [
                "wipo_out_score",
                "oxford_total_score",
                "wipo_gii_score",
                "oxford_innovation_capacity",
                "oxford_ind_ai_research_papers_log",
                "stanford_fig_6_3_5_fig_6_3_5_volume_of_publications",
                "wb_patent_applications_residents",
            ],
            "Q4_content": ["iapp_*", "stanford_fig_3_5_2_*", "stanford_fig_3_6_1_*", "stanford_fig_3_7_*"],
        },
        "candidatos_tratamiento_X1": {
            "all": [
                "iapp_categoria_obligatoriedad",
                "iapp_ley_ia_vigente",
                "iapp_proyecto_ley_ia",
                "iapp_modelo_gobernanza",
                "iapp_n_leyes_relacionadas",
                "iapp_n_autoridades",
            ],
        },
        "controles_X2": {
            "economicos": ["wb_gdp_per_capita_ppp", "wb_internet_penetration", "wb_fdi_net_inflows"],
            "institucionales": ["wb_government_effectiveness", "wb_rule_of_law", "wb_regulatory_quality"],
            "capital_humano": ["wb_tertiary_education_enrollment", "wb_rd_expenditure_pct_gdp", "wb_researchers_rd_per_million"],
        },
        "submuestras_recomendadas": {
            "nota": "Fase 4 no selecciona muestra final. Fase 5 debe preparar features para multiples submuestras.",
            "candidatas_prioritarias": ["regulada", "oecd_plus_latam", "densa_60"],
            "sensibilidad": ["densa_80", "comparable_chile", "full"],
        },
        "variables_a_colapsar": [],
        "variables_a_transformar_log": [],
        "gaps_para_fase3B": ["G001", "G002", "G005"],
        "estado_firma_humana": "REVISADO_CODEx_USUARIO_2026-05-06",
        "restricciones_para_fase5": [
            "No imputar como dato observado.",
            "No seleccionar una muestra final unica en Fase 5.",
            "Preparar transformaciones por submuestra para multiverse analysis.",
            "Mantener gap G001: no hay variable observada de permisos/capacidad de datacenters.",
        ],
    }

    if not candidates.empty and "fe_recommendation" in candidates.columns:
        decisions["variables_a_colapsar"] = candidates[
            candidates["fe_recommendation"] == "collapse_redundant"
        ]["variable_matriz"].tolist()
        decisions["variables_a_transformar_log"] = candidates[
            candidates["fe_recommendation"] == "transform_log"
        ]["variable_matriz"].tolist()

    return decisions


def build_html_report() -> str:
    """Genera HTML simple autocontenido con resumen del EDA."""
    sections = []

    def _load_safe(name: str) -> pd.DataFrame:
        p = OUTPUTS_DIR / f"{name}.csv"
        return pd.read_csv(p) if p.exists() else pd.DataFrame()

    quality = _load_safe("eda_quality_overview")
    miss_block = _load_safe("eda_missingness_by_block")
    submuestras = _load_safe("eda_submuestras_candidatas")
    chile = _load_safe("eda_chile_profile")
    country_profiles = _load_safe("eda_country_profiles")

    html = ["""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>EDA Principal - Fase 4 - Research AI Law</title>
<style>
  body { font-family: Arial, sans-serif; margin: 40px; color: #222; }
  h1 { color: #1a3a5c; border-bottom: 3px solid #1a3a5c; }
  h2 { color: #2c5282; border-bottom: 1px solid #ccc; margin-top: 40px; }
  h3 { color: #2d3748; }
  table { border-collapse: collapse; width: 100%; margin: 20px 0; font-size: 13px; }
  th { background: #2c5282; color: white; padding: 8px 12px; text-align: left; }
  td { padding: 6px 12px; border-bottom: 1px solid #e2e8f0; }
  tr:hover { background: #edf2f7; }
  .highlight { background: #ebf8ff; font-weight: bold; }
  .metric-box { display: inline-block; background: #f7fafc; border: 1px solid #bee3f8;
                border-radius: 8px; padding: 16px 24px; margin: 8px; text-align: center; }
  .metric-value { font-size: 28px; font-weight: bold; color: #2c5282; }
  .metric-label { font-size: 12px; color: #718096; margin-top: 4px; }
  .alert { background: #fff5f5; border-left: 4px solid #fc8181; padding: 12px; margin: 12px 0; }
  .note { background: #fffff0; border-left: 4px solid #f6e05e; padding: 12px; margin: 12px 0; }
  .ok { background: #f0fff4; border-left: 4px solid #68d391; padding: 12px; margin: 12px 0; }
  .toc a { display: block; color: #2c5282; text-decoration: none; padding: 4px 0; }
  .toc a:hover { text-decoration: underline; }
</style>
</head>
<body>
<h1>EDA Principal - Fase 4</h1>
<p><strong>Proyecto:</strong> Research AI Law — Boletín 16821-19 (Ley Marco de IA Chile)</p>
<p><strong>Fecha:</strong> """ + datetime.now(timezone.utc).strftime("%Y-%m-%d") + """</p>
<p><strong>Fuente de datos:</strong> Matriz Madre Fase 3 v1.1 (199 países × 1,203 columnas)</p>

<div class="note">
<strong>Principio rector:</strong> Este EDA explora patrones y prepara el terreno para modelado (Fase 6).
No responde causalmente la pregunta principal. No imputa datos. No decide muestra final.
</div>

<div class="toc">
<h2>Tabla de Contenidos</h2>
<a href="#quality">1. Calidad y Cobertura</a>
<a href="#blocks">2. Cobertura por Bloque Temático</a>
<a href="#submuestras">3. Submuestras Candidatas (Multiverse Analysis)</a>
<a href="#chile">4. Perfil de Chile</a>
<a href="#countries">5. Rankings de Países</a>
<a href="#methodology">6. Nota Metodológica</a>
</div>
"""]

    # Section 1: Quality
    html.append('<h2 id="quality">1. Calidad y Cobertura Global</h2>')
    if not quality.empty:
        key_metrics = quality[quality["metric"].isin([
            "n_countries", "n_variables", "pct_overall_coverage",
            "n_vars_above_70pct", "n_vars_below_30pct", "chile_pct_coverage"
        ])]
        html.append('<div>')
        for _, row in key_metrics.iterrows():
            label = str(row["metric"]).replace("_", " ").title()
            val = row["value"]
            if isinstance(val, float):
                val_str = f"{val:.1f}" + ("%" if "pct" in str(row["metric"]) else "")
            else:
                val_str = str(int(val))
            html.append(f'<div class="metric-box"><div class="metric-value">{val_str}</div><div class="metric-label">{label}</div></div>')
        html.append('</div>')

    # Section 2: Blocks
    html.append('<h2 id="blocks">2. Cobertura por Bloque Temático</h2>')
    if not miss_block.empty:
        html.append(miss_block.to_html(index=False, classes="", border=0))
        html.append("""<div class="alert">
<strong>Cuello de botella estructural:</strong> El bloque <code>regulatory_treatment</code>
(IAPP) tiene cobertura ~14% (~28 países). Esto limita directamente la capacidad de responder
las preguntas causales Q1-Q3. Ver submuestras 'regulada' para el análisis focalizado.
</div>""")

    # Section 3: Submuestras
    html.append('<h2 id="submuestras">3. Submuestras Candidatas (Multiverse Analysis)</h2>')
    html.append("""<div class="note">
<strong>Filosofía:</strong> Fase 4 propone múltiples submuestras candidatas con criterios explícitos
preregistrados. Fase 6 modela con una. Fase 7 remodela con todas para evaluar robustez.
Esta práctica sigue los estándares de <em>multiverse analysis</em> (Simonsohn et al. 2020).
</div>""")
    if not submuestras.empty:
        html.append(submuestras.to_html(index=False, classes="", border=0))

    # Section 4: Chile
    html.append('<h2 id="chile">4. Perfil de Chile</h2>')
    if not chile.empty:
        html.append('<div>')
        for col in chile.columns:
            val = chile[col].iloc[0]
            if pd.notna(val):
                label = str(col).replace("_", " ").title()
                html.append(f'<div class="metric-box"><div class="metric-value">{val}</div><div class="metric-label">{label}</div></div>')
        html.append('</div>')
    html.append("""<div class="note">
<strong>Nota metodológica:</strong> Las afirmaciones sobre Chile (n=1) son descriptivas, no causales.
Chile es el caso focal del estudio (Boletín 16821-19), no un dato estadístico.
</div>""")

    # Section 5: Country rankings
    html.append('<h2 id="countries">5. Rankings de Países — Ecosystem Outcome</h2>')
    if not country_profiles.empty and "zscore_ecosystem_outcome_mean" in country_profiles.columns:
        top20 = country_profiles[["iso3", "country_name_canonical", "region",
                                  "zscore_ecosystem_outcome_mean",
                                  "zscore_regulatory_treatment_mean"]].head(20)
        html.append(top20.to_html(index=False, classes="", border=0))

    # Section 6: Methodology
    html.append("""<h2 id="methodology">6. Nota Metodológica</h2>
<div class="ok">
<strong>Principios de esta fase (no negociables):</strong><br>
• Estadística robusta primero: mediana &gt; media, Spearman &gt; Pearson, IQR/MAD &gt; std<br>
• Corrección FDR (Benjamini-Hochberg) para correlaciones masivas<br>
• Outliers preservados (USA, SGP, ARE, IRL, EST) — son información, no ruido<br>
• Sin imputación, sin modelos, sin decisión Y/X<br>
• Toda correlación reportada ≠ causalidad<br>
• El plan de exploración fue preregistrado en <code>config/fase4/decisions.yaml</code>
</div>
<p><strong>Referencias:</strong><br>
Simonsohn, Simmons &amp; Nelson (2020). Specification Curve Analysis. <em>Nature Human Behaviour</em>.<br>
Steegen, Tuerlinckx, Gelman &amp; Vanpaemel (2016). Increasing Transparency Through a Multiverse Analysis. <em>Perspectives on Psychological Science</em>.
</p>
""")

    html.append("</body></html>")
    return "\n".join(html)


def run_reporting(save: bool = True) -> dict:
    """Genera todos los outputs del Bloque M."""
    candidates = pd.DataFrame()
    redundancy = pd.DataFrame()

    var_summary_path = OUTPUTS_DIR / "eda_variable_summary.csv"
    redundancy_path = OUTPUTS_DIR / "eda_redundancy_report.csv"

    if var_summary_path.exists():
        candidates = _build_candidates_for_fe(pd.read_csv(var_summary_path), redundancy)
    if redundancy_path.exists():
        redundancy = pd.read_csv(redundancy_path)
        if not candidates.empty:
            candidates = _build_candidates_for_fe(pd.read_csv(var_summary_path), redundancy)

    submuestras_path = OUTPUTS_DIR / "eda_submuestras_candidatas.csv"
    submuestras = pd.read_csv(submuestras_path) if submuestras_path.exists() else pd.DataFrame()

    data_gaps = _build_data_gaps()
    decisions = _build_decisions_for_fase5(candidates, submuestras)
    html_content = build_html_report()
    readme_content = _build_readme(candidates, data_gaps, submuestras)

    if save:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        if not candidates.empty:
            candidates.to_csv(OUTPUTS_DIR / "eda_candidates_for_feature_engineering.csv", index=False)
        data_gaps.to_csv(OUTPUTS_DIR / "eda_data_gaps.csv", index=False)

        import yaml
        with open(OUTPUTS_DIR / "eda_decisions_for_fase5.yaml", "w", encoding="utf-8") as f:
            yaml.dump(decisions, f, allow_unicode=True, sort_keys=False)

        with open(OUTPUTS_DIR / "EDA_Principal_Fase4.html", "w", encoding="utf-8") as f:
            f.write(html_content)

        with open(OUTPUTS_DIR / "README_EDA_PRINCIPAL.md", "w", encoding="utf-8") as f:
            f.write(readme_content)

        # Manifest
        _write_manifest()

    return {
        "candidates": candidates,
        "data_gaps": data_gaps,
        "decisions": decisions,
    }


def _build_readme(candidates: pd.DataFrame, data_gaps: pd.DataFrame, submuestras: pd.DataFrame) -> str:
    """README ejecutivo reproducible para stakeholders no técnicos."""
    n_candidates = len(candidates) if candidates is not None else 0
    n_gaps = len(data_gaps) if data_gaps is not None else 0
    n_sub = len(submuestras) if submuestras is not None else 0
    return f"""# README EDA Principal - Fase 4

Proyecto: Research_AI_law
Fase: 4 - EDA Principal
Version: 1.0
Fecha de generación: {datetime.now(timezone.utc).isoformat()}

## Propósito

Esta fase transforma la Matriz Madre de Fase 3 en una cartografía estadística
para preparar Feature Engineering y modelado. No responde causalmente la
pregunta del estudio, no imputa datos, no decide Y/X y no selecciona una
muestra final única.

## Entregables principales

- `EDA_Principal_Fase4.html`: reporte autocontenido con narrativa ejecutiva.
- `manifest_eda_principal.json`: hashes de inputs Fase 3 y outputs Fase 4.
- `eda_candidates_for_feature_engineering.csv`: {n_candidates} variables clasificadas para Fase 5.
- `eda_submuestras_candidatas.csv`: {n_sub} submuestras para multiverse analysis.
- `eda_data_gaps.csv`: {n_gaps} gaps formales para Fase 3B/Fase 5.
- `eda_question_q*.csv`: mapeo de las cuatro sub-preguntas a variables reales observadas.

## Reglas metodológicas preservadas

- Fase 4 consume Fase 3 mediante API pública (`fase3.api` / `src.fase3.api`).
- Fase 4 no modifica archivos de Fase 3.
- Estadística robusta primero: mediana, IQR, MAD, Spearman.
- FDR/Holm se reportan como diagnóstico de multiplicidad.
- Outliers como USA, SGP, ARE, IRL y EST se preservan y documentan.
- El cuello de botella IAPP/regulatorio se reporta explícitamente.

## Uso desde Fase 5

```python
from fase4.api import load_candidates, load_submuestras, load_chile_profile

candidates = load_candidates()
submuestras = load_submuestras()
chile = load_chile_profile()
```

## Comandos de reproducción

```bash
python3 -m src.fase4 build-all
python3 -m src.fase4 validate
pytest tests/fase4 -v
```
"""


def _write_manifest():
    """Escribe manifest_eda_principal.json con hashes y metadata."""
    try:
        git_sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(OUTPUTS_DIR.parents[2]), stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        git_sha = "unknown"

    manifest = {
        "version": "1.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "git_sha": git_sha,
        "fase3_outputs_hashed": {},
        "fase4_outputs": {},
    }

    # Hash de outputs Fase 3
    fase3_outputs = OUTPUTS_DIR.parents[2] / "FASE3" / "outputs"
    for p in sorted(fase3_outputs.glob("*.csv")):
        try:
            manifest["fase3_outputs_hashed"][p.name] = sha256_file(p)
        except Exception:
            pass

    # Hash de outputs Fase 4
    for p in sorted(OUTPUTS_DIR.glob("*")):
        if p.suffix in (".csv", ".html", ".yaml", ".md") and p.name != "manifest_eda_principal.json":
            try:
                manifest["fase4_outputs"][p.name] = {
                    "sha256": sha256_file(p),
                    "bytes": p.stat().st_size,
                }
            except Exception:
                pass

    for target in [OUTPUTS_DIR / "manifest_eda_principal.json", FASE4_ROOT / "manifest_eda_principal.json"]:
        with open(target, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
