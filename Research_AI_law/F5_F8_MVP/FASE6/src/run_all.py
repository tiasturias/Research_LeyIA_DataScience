"""Orquestador de Fase 6 v2.1+: estimación inferencial."""

from __future__ import annotations
from pathlib import Path
import json
import pandas as pd
import yaml
from datetime import datetime, timezone

from ._common_data import load_feature_matrix, load_modeling_contract, validate_inferential_contract
from .q1_investment import run_q1
from .q2_adoption import run_q2
from .q3_innovation import run_q3
from .q4_clustering import run_q4
from .q5_population_usage import run_q5
from .q6_public_sector import run_q6


FASE6_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = FASE6_ROOT / "outputs"


def generate_manifest(results_meta: dict) -> dict:
    try:
        import subprocess
        git_sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(FASE6_ROOT), stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        git_sha = "unknown"

    manifest = {
        "fase6_version": "2.1+",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "methodology_version": "mvp-v0.2-methodology-correction-plus",
        "methodology": "inferential_comparative_observational",
        "primary_estimand": "adjusted_association",
        "analysis_scope": "full_preregistered_sample_available_by_outcome",
        "validation_scope": "internal_resampling_not_external_test",
        "analysis_sample_n": 43,
        "holdout_used": False,
        "train_test_split_used": False,
        "external_validation_used": False,
        "split_column_present": False,
        "phase6_train_test_split_present": False,
        "q2_q5_q6_primary_model_policy": "continuous_or_fractional_primary_binary_median_sensitivity_only",
        "bootstrap_policy": {
            "n_resamples_default": 2000,
            "ci_method_preferred": "BCa",
            "fallback": "percentile_logged"
        },
        "loocv_policy": {
            "auc_loocv_used": False,
            "r2_loocv_used": False,
            "reason": "undefined_for_single_observation_test_folds"
        },
        "language_policy": {
            "causal_claim": False,
            "independent_prediction_claim": False,
            "external_validation_claim": False
        },
        "outputs": {
            "q1_results.csv": "adjusted_associations",
            "q2_results.csv": "continuous_or_fractional_adjusted_associations",
            "q2_scores_per_country.csv": "in_sample_descriptive_positioning",
            "q3_results.csv": "adjusted_associations",
            "q4_clusters.csv": "descriptive_typology",
            "q5_results.csv": "continuous_or_fractional_adjusted_associations",
            "q5_scores_per_country.csv": "in_sample_descriptive_positioning",
            "q6_results.csv": "continuous_score_adjusted_associations",
            "q6_scores_per_country.csv": "in_sample_descriptive_positioning"
        },
        "run_metadata": results_meta
    }
    return manifest


def main():
    print("Iniciando Fase 6 (Modelado Inferencial)...")
    contract_status = validate_inferential_contract()
    print(f"Contrato inferencial validado: {contract_status}")

    fm = load_feature_matrix()
    
    # We load the design plan if available, else fallback to modeling_contract
    try:
        config = yaml.safe_load((FASE6_ROOT / "config" / "phase6_analysis_plan.yaml").read_text())
    except FileNotFoundError:
        config = load_modeling_contract()
        
    OUTPUTS.mkdir(exist_ok=True)
    
    print("Ejecutando Q1...")
    q1 = run_q1(fm, config)
    q1.to_csv(OUTPUTS / "q1_results.csv", index=False)
    
    print("Ejecutando Q2...")
    q2, q2_scores = run_q2(fm, config)
    q2.to_csv(OUTPUTS / "q2_results.csv", index=False)
    q2_scores.to_csv(OUTPUTS / "q2_scores_per_country.csv", index=False)
    
    print("Ejecutando Q3...")
    q3 = run_q3(fm, config)
    q3.to_csv(OUTPUTS / "q3_results.csv", index=False)
    
    print("Ejecutando Q4...")
    q4, q4_dist = run_q4(fm, config)
    if not q4.empty:
        q4.to_csv(OUTPUTS / "q4_clusters.csv", index=False)
        q4_dist.to_csv(OUTPUTS / "q4_distance_matrix.csv")
    
    print("Ejecutando Q5...")
    q5, q5_scores = run_q5(fm, config)
    q5.to_csv(OUTPUTS / "q5_results.csv", index=False)
    q5_scores.to_csv(OUTPUTS / "q5_scores_per_country.csv", index=False)
    
    print("Ejecutando Q6...")
    q6, q6_scores = run_q6(fm, config)
    q6.to_csv(OUTPUTS / "q6_results.csv", index=False)
    q6_scores.to_csv(OUTPUTS / "q6_scores_per_country.csv", index=False)
    
    results_meta = {
        "q1_rows": len(q1),
        "q2_rows": len(q2),
        "q3_rows": len(q3),
        "q4_countries": len(q4),
        "q5_rows": len(q5),
        "q6_rows": len(q6),
    }
    
    manifest = generate_manifest(results_meta)
    (OUTPUTS / "fase6_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    
    # Consolidate primary results and effective_n
    primary_results = pd.concat([
        df for df in [q1, q2, q3, q5, q6] if not df.empty
    ], ignore_eval=True) if any(not df.empty for df in [q1, q2, q3, q5, q6]) else pd.DataFrame()
    
    if not primary_results.empty:
        primary_results.to_csv(OUTPUTS / "primary_results_long.csv", index=False)
        eff_n = primary_results[["question", "outcome", "model_family", "analysis_role", "n_effective"]].drop_duplicates()
        eff_n.to_csv(OUTPUTS / "phase6_effective_n_by_outcome.csv", index=False)
    
    print("Fase 6 completada exitosamente.")


if __name__ == "__main__":
    main()
