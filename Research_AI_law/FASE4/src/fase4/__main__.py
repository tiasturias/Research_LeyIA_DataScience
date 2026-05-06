"""CLI: python -m src.fase4 [build-all | validate | report]"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def _add_fase3_to_path():
    fase3 = Path(__file__).resolve().parents[3] / "FASE3"
    for path in (fase3, fase3 / "src"):
        if str(path) not in sys.path:
            sys.path.insert(0, str(path))


def cmd_build_all():
    _add_fase3_to_path()
    from .contracts import run_contracts
    from .coverage import run_coverage_analysis
    from .univariate import run_univariate_analysis
    from .bivariate import run_bivariate_analysis
    from .blocks import run_block_analysis
    from .binding import run_taxonomy_analysis
    from .countries import run_country_analysis
    from .temporal import run_temporal_analysis
    from .question_mapping import run_question_mapping
    from .submuestras import run_submuestras_analysis
    from .reporting import run_reporting

    print("[Fase 4] build-all iniciado")
    print("[A] Contrato de datos y hashes Fase 3...")
    run_contracts()
    print("[B] Cobertura y missingness...")
    run_coverage_analysis()
    print("[C] Estadística univariada...")
    run_univariate_analysis()
    print("[D/K] Bloques, PCA y clustering exploratorio...")
    run_block_analysis()
    print("[E/F] Correlaciones y redundancia...")
    run_bivariate_analysis()
    print("[G] Mapeo a sub-preguntas...")
    run_question_mapping()
    print("[H] Taxonomías binding/enabling...")
    run_taxonomy_analysis()
    print("[I] Perfiles de país...")
    run_country_analysis()
    print("[J] Sensibilidad temporal...")
    run_temporal_analysis()
    print("[L] Submuestras candidatas...")
    run_submuestras_analysis()
    print("[M] Recomendaciones y reporte...")
    run_reporting()
    print("[Fase 4] build-all completado ✓")


def cmd_validate():
    _add_fase3_to_path()
    from .config import OUTPUTS_DIR
    from .load import load_wide, load_dictionary, current_version

    errors = []
    wide = load_wide()
    d = load_dictionary()

    if wide.shape[0] != 199:
        errors.append(f"wide rows: expected 199, got {wide.shape[0]}")
    if "CHL" not in wide["iso3"].values:
        errors.append("Chile (CHL) not in wide")
    if "bloque_tematico" not in d.columns:
        errors.append("dictionary missing bloque_tematico column")

    required_outputs = [
        "contract_check",
        "fase3_input_hashes",
        "eda_quality_overview",
        "eda_missingness_by_country",
        "eda_missingness_by_variable",
        "eda_missingness_by_block",
        "eda_missingness_by_region",
        "eda_variable_summary",
        "eda_numeric_distributions",
        "eda_categorical_distributions",
        "eda_outliers",
        "eda_correlations_spearman",
        "eda_correlations_pearson",
        "eda_correlations_kendall",
        "eda_mutual_information",
        "eda_redundancy_report",
        "eda_vif_diagnostics",
        "eda_inter_block_correlations",
        "eda_inter_block_fdr",
        "eda_partial_correlations",
        "eda_country_profiles",
        "eda_chile_profile",
        "eda_chile_vs_peers",
        "eda_singapore_uae_ireland_profiles",
        "eda_binding_classification",
        "eda_enabling_classification",
        "eda_binding_vs_outcome",
        "eda_temporal_stability",
        "eda_snapshot_vs_panel",
        "eda_year_used_distribution",
        "eda_pca_global",
        "eda_clustering_countries",
        "eda_umap_coords",
        "eda_question_q1_investment",
        "eda_question_q2_adoption",
        "eda_question_q3_innovation",
        "eda_question_q4_content",
        "eda_question_viability",
        "eda_submuestras_candidatas",
        "eda_submuestra_membership",
        "eda_data_gaps",
        "eda_candidates_for_feature_engineering",
    ]
    for block in [
        "regulatory_treatment",
        "ecosystem_outcome",
        "adoption_diffusion",
        "socioeconomic_control",
        "institutional_control",
        "tech_infrastructure_control",
    ]:
        required_outputs.append(f"eda_block_{block}_summary")
    for out in required_outputs:
        p = OUTPUTS_DIR / f"{out}.csv"
        if not p.exists():
            errors.append(f"missing output: {out}.csv")
        elif p.stat().st_size == 0:
            errors.append(f"empty output: {out}.csv")

    for out in ["EDA_Principal_Fase4.html", "README_EDA_PRINCIPAL.md", "manifest_eda_principal.json", "eda_decisions_for_fase5.yaml"]:
        p = OUTPUTS_DIR / out
        if not p.exists():
            errors.append(f"missing output: {out}")
        elif p.stat().st_size == 0:
            errors.append(f"empty output: {out}")

    if errors:
        print("[FAIL] Fase 4 validation failed:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("Fase 4 validation passed ✓")


def cmd_report():
    _add_fase3_to_path()
    from .reporting import run_reporting
    run_reporting()
    print("Reporte generado ✓")


def main():
    parser = argparse.ArgumentParser(prog="src.fase4")
    parser.add_argument("command", choices=["build-all", "validate", "report"])
    args = parser.parse_args()

    if args.command == "build-all":
        cmd_build_all()
    elif args.command == "validate":
        cmd_validate()
    elif args.command == "report":
        cmd_report()


if __name__ == "__main__":
    main()
