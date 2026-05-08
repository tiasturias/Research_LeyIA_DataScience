"""Carga y validación de insumos para Fase 6.2 Country Intelligence Layer."""

from pathlib import Path
import json
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[3]
FASE5_BUNDLE = ROOT / "FASE5" / "outputs" / "phase6_ready"
FASE6_OUTPUTS = ROOT / "FASE6" / "outputs"
CI_OUTPUTS = FASE6_OUTPUTS / "country_intelligence"

REQUIRED_FASE6 = [
    "fase6_manifest.json",
    "q1_results.csv",
    "q2_results.csv",
    "q2_scores_per_country.csv",
    "q3_results.csv",
    "q4_clusters.csv",
    "q4_distance_matrix.csv",
    "q5_results.csv",
    "q5_scores_per_country.csv",
    "q6_results.csv",
    "q6_scores_per_country.csv",
]


def validate_preflight():
    checks = []
    for fname in REQUIRED_FASE6:
        path = FASE6_OUTPUTS / fname
        checks.append({
            "check": f"exists_{fname}",
            "status": "PASS" if path.exists() else "FAIL",
            "severity": "P0" if not path.exists() else "INFO",
            "path": str(path),
        })

    manifest = json.loads((FASE6_OUTPUTS / "fase6_manifest.json").read_text())
    checks.append({
        "check": "manifest_no_holdout",
        "status": "PASS" if manifest.get("holdout_used") is False else "FAIL",
        "severity": "P0",
    })
    checks.append({
        "check": "manifest_no_external_validation",
        "status": "PASS" if manifest.get("external_validation_used") is False else "FAIL",
        "severity": "P0",
    })
    checks.append({
        "check": "manifest_no_train_test_split",
        "status": "PASS" if manifest.get("train_test_split_used") is False else "FAIL",
        "severity": "P0",
    })

    fm = pd.read_csv(FASE5_BUNDLE / "phase6_feature_matrix.csv")
    checks.append({
        "check": "feature_matrix_43_rows",
        "status": "PASS" if len(fm) == 43 else "FAIL",
        "severity": "P0",
        "observed": len(fm),
    })
    checks.append({
        "check": "feature_matrix_no_split",
        "status": "PASS" if "split" not in fm.columns else "FAIL",
        "severity": "P0",
    })

    return pd.DataFrame(checks)
