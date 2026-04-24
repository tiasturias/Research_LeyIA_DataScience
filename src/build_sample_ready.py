"""
Build the sample-ready cross-sectional dataset for the main study.

This is THE definitive dataset that feeds into 02_limpieza.ipynb. It merges
all source masters into a single iso3-keyed table with:
  - One row per country (86 study countries)
  - All principal + extended variables
  - Completeness flags per definition tier
  - Temporal metadata per variable
  - Source provenance

Hierarchy:
  PRINCIPAL MODEL (N≈72):
    Y: ai_readiness_score, ai_adoption_rate, ai_investment_usd_bn_cumulative, ai_startups_cumulative
    X1: has_ai_law, regulatory_approach, regulatory_intensity, enforcement_level, thematic_coverage
    X2: gdp_per_capita_ppp, internet_penetration, gii_score, oecd_member, region

  EXTENDED MODEL (N≈67):
    + rd_expenditure, tertiary_education

  ROBUSTNESS (separate submodels, not mixed with principal):
    ai_patents_per100k (N≈54)
    government_effectiveness (N≈63)
    ai_investment_vc_proxy (N≈33)
    OECD publications/patents

Output:
  data/interim/sample_ready_cross_section.csv
  data/interim/coverage_matrix.csv  (variable × country availability)
"""

import pandas as pd
import numpy as np
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
INTERIM = BASE / "data/interim"


# ═══════════════════════════════════════════════════════════════════════════════
# VARIABLE REGISTRY (single source of truth for hierarchy)
# ═══════════════════════════════════════════════════════════════════════════════

Y_PRINCIPAL = [
    "ai_readiness_score",
    "ai_adoption_rate",
    "ai_investment_usd_bn_cumulative",
    "ai_startups_cumulative",
]

X1_PRINCIPAL = [
    "has_ai_law",
    "regulatory_approach",
    "regulatory_intensity",
    "enforcement_level",
    "thematic_coverage",
]

X2_CORE = [
    "gdp_per_capita_ppp",
    "internet_penetration",
    "gii_score",
    "oecd_member",
    "region",
]

X2_EXTENDED = [
    "rd_expenditure",
    "tertiary_education",
]

# Digital economy proxies (agregados 2026-04 per Tarea A sub-tarea A.5).
# Proxies de "economia digital" via WDI: exportaciones de servicios ICT y
# exportaciones de alta tecnologia. No redundantes con internet_penetration
# (que mide consumo) — estos miden PRODUCCION/CAPACIDAD digital.
# Clasificadas como extended (no core confounder) porque cobertura 83/86
# es ligeramente menor que WGI/GDPR (85-86/86).
X2_DIGITAL_ECONOMY = [
    "ict_service_exports_pct",
    "high_tech_exports_pct",
]

# Confounders institucionales (agregados 2026-04 per audit Tarea A).
# Abordan el problema #6 de la auditoria: sin controlar por calidad regulatoria
# y estado de derecho, `regulatory_intensity` captura "cultura regulatoria
# general" en vez de "regulacion AI-especifica".
X2_CONFOUNDERS_GOV = [
    "regulatory_quality",
    "rule_of_law",
]

# Confounder legal-regulatorio (agregado 2026-04 per Tarea A sub-tarea A.4).
# Controla por existencia de ley comprehensiva de proteccion de datos previa
# a regulacion IA. Sin este control, `regulatory_intensity` podria capturar
# "cultura de regulacion digital pre-existente" en vez de "regulacion IA".
# Nivel ordinal (0-3): EU/EEA/adequacy > GDPR-like > basica > inexistente.
X2_CONFOUNDERS_GDPR = [
    "has_gdpr_like_law",
    "gdpr_similarity_level",
]

# Confounder politico-regimen (agregado 2026-04 per Tarea A sub-tarea A.6).
# Controla por tipo de regimen politico y libertades civiles. Democracias y
# autoritarismos regulan IA con motivaciones distintas (autoritarios: control
# de informacion/vigilancia; democracias: derechos del usuario). FH 2025
# (data ano 2024) como fuente estandar.
X2_CONFOUNDERS_FH = [
    "fh_total_score",
    "fh_democracy_level",
]

# Confounder tradicion juridica (agregado 2026-04 per Tarea A sub-tarea A.3-bis).
# Clasificacion La Porta-Lopez-de-Silanes-Shleifer (2008) "The Economic
# Consequences of Legal Origins" — cinco familias: English (common law),
# French, German, Scandinavian, Socialist. La tradicion juridica es un
# predictor robusto de estilo regulatorio (binding vs. soft) y cultura de
# enforcement. Controlarla permite separar "efecto de regulacion AI" del
# "efecto de la tradicion juridica heredada".
# Cobertura 86/86 (codificacion estable historicamente).
X2_LEGAL_ORIGIN = [
    "legal_origin",
    "is_common_law",
]

Y_ROBUSTNESS = [
    "ai_patents_per100k",
    "ai_investment_usd_bn_2024",
    "ai_startups_2024",
]

X2_ROBUSTNESS = [
    "government_effectiveness",
    "control_of_corruption",
    "ai_investment_vc_proxy",
]


def build_sample_ready():
    """Assemble the sample-ready cross-section from source masters."""

    # ── Load source masters ──────────────────────────────────────────────────
    x1 = pd.read_csv(INTERIM / "x1_master.csv")
    stanford = pd.read_csv(INTERIM / "y_stanford_master.csv")
    microsoft = pd.read_csv(INTERIM / "y_microsoft_master.csv")
    oxford = pd.read_csv(INTERIM / "y_oxford_master.csv")
    wipo = pd.read_csv(INTERIM / "x2_wipo_master.csv")
    wb = pd.read_csv(INTERIM / "x2_wb_master.csv")
    derived = pd.read_csv(INTERIM / "derived_controls.csv")
    oecd_rob = pd.read_csv(INTERIM / "oecd_robustness_master.csv")
    gdpr = pd.read_csv(INTERIM / "x2_gdpr_master.csv")
    fh = pd.read_csv(INTERIM / "x2_fh_master.csv")
    legal = pd.read_csv(INTERIM / "x2_legal_origin_master.csv")

    # ── Start with X1 backbone (86 countries) ────────────────────────────────
    master = x1[["iso3", "has_ai_law", "regulatory_approach", "regulatory_intensity",
                  "year_enacted", "enforcement_level", "thematic_coverage",
                  "regulatory_status_group", "x1_source"]].copy()

    # ── Merge Y: Stanford ────────────────────────────────────────────────────
    s_cols = ["iso3", "ai_patents_per100k", "ai_investment_usd_bn_cumulative",
              "ai_investment_usd_bn_2024", "ai_startups_cumulative", "ai_startups_2024",
              "patents_year", "investment_year", "startups_year"]
    master = pd.merge(master, stanford[s_cols], on="iso3", how="left")

    # ── Merge Y: Microsoft ───────────────────────────────────────────────────
    m_cols = ["iso3", "ai_adoption_rate", "adoption_period"]
    master = pd.merge(master, microsoft[m_cols], on="iso3", how="left")

    # ── Merge Y: Oxford ──────────────────────────────────────────────────────
    o_cols = ["iso3", "ai_readiness_score", "readiness_year"]
    master = pd.merge(master, oxford[o_cols], on="iso3", how="left")

    # ── Merge X2: WIPO ───────────────────────────────────────────────────────
    w_cols = ["iso3", "gii_score", "gii_year"]
    master = pd.merge(master, wipo[w_cols], on="iso3", how="left")

    # ── Merge X2: World Bank ─────────────────────────────────────────────────
    wb_cols = ["iso3", "gdp_per_capita_ppp", "gdp_per_capita_ppp_year",
               "rd_expenditure", "rd_expenditure_year",
               "internet_penetration", "internet_penetration_year",
               "tertiary_education", "tertiary_education_year",
               "regulatory_quality", "regulatory_quality_year",
               "rule_of_law", "rule_of_law_year",
               "government_effectiveness", "government_effectiveness_year",
               "control_of_corruption", "control_of_corruption_year",
               "ict_service_exports_pct", "ict_service_exports_pct_year",
               "high_tech_exports_pct", "high_tech_exports_pct_year",
               "population", "gdp_current_usd"]
    master = pd.merge(master, wb[wb_cols], on="iso3", how="left")

    # ── Merge X2: Derived controls ───────────────────────────────────────────
    master = pd.merge(master, derived[["iso3", "oecd_member", "region"]],
                       on="iso3", how="left")

    # ── Merge robustness: OECD ───────────────────────────────────────────────
    rob_cols = ["iso3", "ai_investment_vc_proxy", "vc_proxy_year",
                "ai_publications_frac", "ai_publications_frac_year"]
    available_rob_cols = [c for c in rob_cols if c in oecd_rob.columns]
    master = pd.merge(master, oecd_rob[available_rob_cols], on="iso3", how="left")

    # ── Merge X2: GDPR-like confounder (Tarea A sub-tarea A.4) ───────────────
    gdpr_cols = ["iso3", "has_gdpr_like_law", "gdpr_similarity_level",
                 "dp_law_year", "has_dpa", "eu_status", "enforcement_active"]
    master = pd.merge(master, gdpr[gdpr_cols], on="iso3", how="left")

    # ── Merge X2: Freedom House regime confounder (Tarea A sub-tarea A.6) ────
    fh_cols = ["iso3", "fh_total_score", "fh_status", "fh_pr_score",
               "fh_cl_score", "fh_democracy_level", "fh_year"]
    master = pd.merge(master, fh[fh_cols], on="iso3", how="left")

    # ── Merge X2: Legal origin confounder (Tarea A sub-tarea A.3-bis) ────────
    legal_cols = ["iso3", "legal_origin", "is_common_law"]
    master = pd.merge(master, legal[legal_cols], on="iso3", how="left")

    # ═══════════════════════════════════════════════════════════════════════════
    # COMPLETENESS FLAGS
    # ═══════════════════════════════════════════════════════════════════════════

    # year_enacted: conditional on has_ai_law
    master["year_enacted_ok"] = master.apply(
        lambda r: True if r.get("has_ai_law") == 0
                  else pd.notna(r.get("year_enacted")),
        axis=1,
    )

    def _all_present(row, var_list):
        return all(pd.notna(row.get(v)) for v in var_list)

    # Tier 1: PRINCIPAL (4Y + 5X1 + 5X2)
    principal_vars = Y_PRINCIPAL + X1_PRINCIPAL + X2_CORE
    master["complete_principal"] = master.apply(
        lambda r: int(_all_present(r, principal_vars) and r["year_enacted_ok"]),
        axis=1,
    )

    # Tier 2: EXTENDED (principal + rd_expenditure + tertiary_education)
    extended_vars = principal_vars + X2_EXTENDED
    master["complete_extended"] = master.apply(
        lambda r: int(_all_present(r, extended_vars) and r["year_enacted_ok"]),
        axis=1,
    )

    # Tier 2b: CONFOUNDED (principal + institutional confounders - recomendado post-Audit 2026-04)
    # Este es el modelo recomendado tras la auditoria Tarea A: incluye controles
    # de calidad regulatoria general, estado de derecho, y proteccion de datos
    # pre-existente (GDPR-like). Estos tres controles separan el efecto de la
    # regulacion AI-especifica del "efecto institucional general" y del
    # "efecto de tradicion regulatoria digital".
    confounded_vars = principal_vars + X2_CONFOUNDERS_GOV + X2_CONFOUNDERS_GDPR
    master["complete_confounded"] = master.apply(
        lambda r: int(_all_present(r, confounded_vars) and r["year_enacted_ok"]),
        axis=1,
    )

    # Tier 2c: DIGITAL (confounded + digital economy proxies - added 2026-04 A.5)
    # Tier separada para analisis de robustez con controles de economia digital.
    # No se fuerza al modelo principal porque cobertura ICT/high-tech es 83/86
    # (vs 85-86/86 de WGI/GDPR), lo que reduciria ligeramente la muestra.
    digital_vars = confounded_vars + X2_DIGITAL_ECONOMY
    master["complete_digital"] = master.apply(
        lambda r: int(_all_present(r, digital_vars) and r["year_enacted_ok"]),
        axis=1,
    )

    # Tier 2d: REGIME (confounded + FH regime controls - added 2026-04 A.6)
    # Tier separada para analisis de robustez con control de regimen politico.
    # Permite testear si el efecto de regulacion IA se mantiene al controlar
    # por democracia/autoritarismo (heterogeneidad explicita de motivaciones
    # regulatorias). Cobertura FH 86/86 -> no reduce muestra vs confounded.
    regime_vars = confounded_vars + X2_CONFOUNDERS_FH
    master["complete_regime"] = master.apply(
        lambda r: int(_all_present(r, regime_vars) and r["year_enacted_ok"]),
        axis=1,
    )

    # Tier 2e: LEGAL_TRADITION (confounded + legal_origin - added 2026-04 A.3-bis)
    # Tier separada para robustness con control de tradicion juridica La Porta.
    # Permite testear si el efecto de regulacion IA persiste al controlar por
    # la familia legal heredada (common-law vs civil-law: French/German/
    # Scandinavian/Socialist). Cobertura 86/86 -> no reduce muestra vs
    # confounded.
    legal_tradition_vars = confounded_vars + X2_LEGAL_ORIGIN
    master["complete_legal_tradition"] = master.apply(
        lambda r: int(_all_present(r, legal_tradition_vars) and r["year_enacted_ok"]),
        axis=1,
    )

    # Tier 3: STRICT (extended + patents + gov_effectiveness)
    strict_vars = extended_vars + ["ai_patents_per100k", "government_effectiveness"]
    master["complete_strict"] = master.apply(
        lambda r: int(_all_present(r, strict_vars) and r["year_enacted_ok"]),
        axis=1,
    )

    # Per-variable availability flags
    all_analytic_vars = (Y_PRINCIPAL + X1_PRINCIPAL + X2_CORE + X2_EXTENDED +
                         X2_CONFOUNDERS_GOV + X2_CONFOUNDERS_GDPR +
                         X2_DIGITAL_ECONOMY + X2_CONFOUNDERS_FH +
                         X2_LEGAL_ORIGIN +
                         Y_ROBUSTNESS + X2_ROBUSTNESS)
    for v in all_analytic_vars:
        if v in master.columns:
            master[f"has_{v}"] = master[v].notna().astype(int)

    # ═══════════════════════════════════════════════════════════════════════════
    # REGULATORY GROUP REPRESENTATION CHECK
    # ═══════════════════════════════════════════════════════════════════════════

    n_principal = master["complete_principal"].sum()
    n_confounded = master["complete_confounded"].sum()
    n_digital = master["complete_digital"].sum()
    n_regime = master["complete_regime"].sum()
    n_legal = master["complete_legal_tradition"].sum()
    n_extended = master["complete_extended"].sum()
    n_strict = master["complete_strict"].sum()

    print("=" * 70)
    print("SAMPLE-READY CROSS-SECTION SUMMARY")
    print("=" * 70)
    print(f"\n  Total countries: {len(master)}")
    print(f"  Principal complete  (4Y+5X1+5X2):                        {n_principal}/86")
    print(f"  Confounded complete (+WGI_RQ+WGI_RL+GDPR-like):          {n_confounded}/86  [recommended]")
    print(f"  Digital complete    (+ICT_services+high_tech_exports):   {n_digital}/86")
    print(f"  Regime complete     (+FH_score+FH_democracy):            {n_regime}/86")
    print(f"  Legal-tradition complete (+legal_origin La Porta):       {n_legal}/86")
    print(f"  Extended complete   (+R&D+educ):                         {n_extended}/86")
    print(f"  Strict complete     (+patents+GE):                       {n_strict}/86")

    print(f"\n  Regulatory representation (Principal):")
    complete = master[master["complete_principal"] == 1]
    for g, cnt in complete["regulatory_status_group"].value_counts().items():
        print(f"    {g:<25s}: {cnt}")

    print(f"\n  Regulatory representation (Confounded - recommended model):")
    complete_conf = master[master["complete_confounded"] == 1]
    for g, cnt in complete_conf["regulatory_status_group"].value_counts().items():
        print(f"    {g:<25s}: {cnt}")

    # Per-variable coverage
    print(f"\n  Variable coverage:")
    for v in (Y_PRINCIPAL + X1_PRINCIPAL + X2_CORE
              + X2_CONFOUNDERS_GOV + X2_CONFOUNDERS_GDPR
              + X2_DIGITAL_ECONOMY + X2_CONFOUNDERS_FH
              + X2_LEGAL_ORIGIN + X2_EXTENDED):
        n = master[v].notna().sum() if v in master.columns else 0
        print(f"    {v:<40s}: {n}/86")

    # Missing from principal
    missing = master[master["complete_principal"] == 0]
    if len(missing) > 0:
        print(f"\n  Countries missing from principal ({len(missing)}):")
        for _, r in missing.iterrows():
            gaps = [v for v in principal_vars if pd.isna(r.get(v))]
            print(f"    {r['iso3']} ({r.get('regulatory_status_group','?')}): {', '.join(gaps)}")

    # ═══════════════════════════════════════════════════════════════════════════
    # SAVE
    # ═══════════════════════════════════════════════════════════════════════════

    master.sort_values("iso3", inplace=True)
    out = INTERIM / "sample_ready_cross_section.csv"
    master.to_csv(out, index=False)
    print(f"\n  Saved to {out}")

    # ── Coverage matrix (long format for auditing) ───────────────────────────
    coverage_rows = []
    for _, r in master.iterrows():
        for v in all_analytic_vars:
            coverage_rows.append({
                "iso3": r["iso3"],
                "variable": v,
                "has_value": int(pd.notna(r.get(v))),
                "tier": (
                    "Y_principal" if v in Y_PRINCIPAL
                    else "X1_principal" if v in X1_PRINCIPAL
                    else "X2_core" if v in X2_CORE
                    else "X2_confounder_gov" if v in X2_CONFOUNDERS_GOV
                    else "X2_confounder_gdpr" if v in X2_CONFOUNDERS_GDPR
                    else "X2_digital_economy" if v in X2_DIGITAL_ECONOMY
                    else "X2_confounder_fh" if v in X2_CONFOUNDERS_FH
                    else "X2_legal_origin" if v in X2_LEGAL_ORIGIN
                    else "X2_extended" if v in X2_EXTENDED
                    else "Y_robustness" if v in Y_ROBUSTNESS
                    else "X2_robustness"
                ),
            })
    coverage = pd.DataFrame(coverage_rows)
    cov_out = INTERIM / "coverage_matrix.csv"
    coverage.to_csv(cov_out, index=False)
    print(f"  Coverage matrix saved to {cov_out}")

    return master


if __name__ == "__main__":
    build_sample_ready()
