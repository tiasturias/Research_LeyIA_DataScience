"""Q2 Adopción: Logistic + Random Forest sobre Y binarizada."""

from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

from ._common_data import (
    load_bundle, get_x2_controls, get_x1_aggregated, F5_F8_MVP,
)
from ._common_classification import (
    binarize_by_median, fit_logistic_cv, fit_random_forest_cv,
)

OUTPUTS = F5_F8_MVP / "FASE6" / "outputs"

Y_VARS_Q2 = [
    "ms_h2_2025_ai_diffusion_pct",
    "ms_h1_2025_ai_diffusion_pct",
    "anthropic_usage_pct",
    "anthropic_collaboration_pct",
    "oecd_5_ict_business_oecd_biz_ai_pct",
    "oxford_public_sector_adoption",
    "oxford_ind_adoption_emerging_tech",
]


def run_q2(seed: int = 42) -> dict:
    bundle = load_bundle()
    fm = bundle["feature_matrix"].copy()
    x1_agg = get_x1_aggregated()
    x2 = get_x2_controls()

    def col_z(c):
        return f"{c}_z" if f"{c}_z" in fm.columns else c
    x1_z = [col_z(c) for c in x1_agg]
    x2_z = [col_z(c) for c in x2]

    rows = []
    rows_predictions = []

    for y in Y_VARS_Q2:
        if y not in fm.columns:
            continue
        sub = fm[[y, "iso3"] + x1_z + x2_z].dropna()
        if len(sub) < 20:
            continue
        y_binary, threshold = binarize_by_median(sub[y])
        sub = sub.assign(y_binary=y_binary.values)
        sub_y = sub.copy()

        log = fit_logistic_cv(sub_y, "y_binary", x1_z + x2_z, seed=seed)
        rf = fit_random_forest_cv(sub_y, "y_binary", x1_z + x2_z, seed=seed)

        if log.get("status") == "ok":
            rows.append({
                "question": "Q2", "y_var": y,
                "binarization_threshold_value": float(threshold),
                "binarization_method": "median",
                "model": "Logistic", "x_var": "__model_metadata__",
                "n_effective": log["n"],
                "n_class_0": log["n_class_0"], "n_class_1": log["n_class_1"],
                "auc_cv_5fold_mean": log["auc_cv_5fold_mean"],
                "auc_cv_5fold_std": log["auc_cv_5fold_std"],
                "auc_loocv": log["auc_loocv"],
                "confusion_tp": log["confusion_tp"], "confusion_tn": log["confusion_tn"],
                "confusion_fp": log["confusion_fp"], "confusion_fn": log["confusion_fn"],
                "model_hyperparams_json": '{"penalty":"l2","C":1.0}',
                "seed": seed,
            })
            for x, coef in log["logistic_coef"].items():
                rows.append({
                    "question": "Q2", "y_var": y, "model": "Logistic", "x_var": x,
                    "coefficient_or_importance": coef,
                    "n_effective": log["n"], "seed": seed,
                })

        if rf.get("status") == "ok":
            rows.append({
                "question": "Q2", "y_var": y, "model": "RandomForest",
                "x_var": "__model_metadata__",
                "n_effective": rf["n"],
                "auc_cv_5fold_mean": rf["auc_cv_5fold_mean"],
                "auc_cv_5fold_std": rf["auc_cv_5fold_std"],
                "auc_loocv": rf["auc_loocv"],
                "model_hyperparams_json": '{"n_estimators":300,"max_depth":4}',
                "seed": seed,
            })
            for x, imp in rf["feature_importance"].items():
                rows.append({
                    "question": "Q2", "y_var": y, "model": "RandomForest", "x_var": x,
                    "coefficient_or_importance": imp,
                    "n_effective": rf["n"], "seed": seed,
                })

        # Predicciones por país
        if log.get("status") == "ok":
            X_full = sub_y[x1_z + x2_z].values
            full_log = LogisticRegression(
                penalty="l2", C=1.0, max_iter=1000,
                class_weight="balanced", random_state=seed,
            ).fit(X_full, sub_y["y_binary"].values)
            probs = full_log.predict_proba(X_full)[:, 1]
            for iso3, prob in zip(sub_y["iso3"].values, probs):
                rows_predictions.append({
                    "y_var": y, "iso3": iso3,
                    "p_high_adoption": float(prob),
                    "model": "Logistic_in_sample", "seed": seed,
                })

    pd.DataFrame(rows).to_csv(OUTPUTS / "q2_results.csv", index=False)
    pd.DataFrame(rows_predictions).to_csv(OUTPUTS / "q2_predictions_per_country.csv", index=False)

    return {"n_rows": len(rows)}
