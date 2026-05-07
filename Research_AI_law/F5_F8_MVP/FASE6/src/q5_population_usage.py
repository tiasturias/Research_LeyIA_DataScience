"""Q5 Uso de IA por la población:
- Y candidatas: anthropic_usage_pct, anthropic_collaboration_pct, oxford_ind_adoption_emerging_tech
- Modelos: OLS con bootstrap (regresión continua) + Logistic (clasificación binarizada)
- Reusa Y de Q2_adoption (decisión M)."""

from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

from ._common_data import (
    load_bundle, get_x2_controls, get_x1_aggregated, F5_F8_MVP,
)
from ._common_regression import (
    fit_ols_with_bootstrap, fit_ridge_lasso_cv, fdr_benjamini_hochberg,
)
from ._common_classification import (
    binarize_by_median, fit_logistic_cv,
)

OUTPUTS = F5_F8_MVP / "FASE6" / "outputs"

Y_VARS_Q5 = [
    "anthropic_usage_pct",
    "anthropic_collaboration_pct",
    "oxford_ind_adoption_emerging_tech",
]


def run_q5(seed: int = 42, n_boot: int = 2000) -> dict:
    bundle = load_bundle()
    fm = bundle["feature_matrix"]
    x1_agg = get_x1_aggregated()
    x2 = get_x2_controls()

    def col_z(c):
        return f"{c}_z" if f"{c}_z" in fm.columns else c
    x1_z = [col_z(c) for c in x1_agg]
    x2_z = [col_z(c) for c in x2]

    rows = []
    rows_consistency = []
    rows_predictions = []

    for y in Y_VARS_Q5:
        if y not in fm.columns:
            continue

        # === OLS regresión continua ===
        ols = fit_ols_with_bootstrap(fm, y, x1_z + x2_z, n_boot=n_boot, seed=seed)
        if ols.get("status") == "ok":
            for x in x1_z + x2_z + ["const"]:
                rows.append({
                    "question": "Q5", "y_var": y, "model": "OLS_full", "x_var": x,
                    "coefficient": ols["coefficients"].get(x),
                    "std_error": ols["std_errors_asymptotic"].get(x),
                    "p_value": ols["pvalues_asymptotic"].get(x),
                    "ci95_lower": ols["bootstrap"].get(x, {}).get("ci95_lower"),
                    "ci95_upper": ols["bootstrap"].get(x, {}).get("ci95_upper"),
                    "p_value_bootstrap": ols["bootstrap"].get(x, {}).get("p_two_sided_bootstrap"),
                    "n_effective": ols["n"], "r2": ols["r2"], "ci_method": "bootstrap_2000",
                    "n_boot": n_boot, "seed": seed,
                })

        # === Logistic clasificación (Y binarizada) ===
        sub = fm[[y, "iso3"] + x1_z + x2_z].dropna()
        if len(sub) >= 20:
            y_bin, threshold = binarize_by_median(sub[y])
            sub = sub.assign(y_binary=y_bin.values)
            log = fit_logistic_cv(sub, "y_binary", x1_z + x2_z, seed=seed)
            if log.get("status") == "ok":
                rows.append({
                    "question": "Q5", "y_var": y,
                    "binarization_threshold_value": float(threshold),
                    "binarization_method": "median",
                    "model": "Logistic", "x_var": "__model_metadata__",
                    "n_effective": log["n"],
                    "n_class_0": log["n_class_0"], "n_class_1": log["n_class_1"],
                    "auc_cv_5fold_mean": log["auc_cv_5fold_mean"],
                    "auc_cv_5fold_std": log["auc_cv_5fold_std"],
                    "auc_loocv": log["auc_loocv"],
                    "model_hyperparams_json": '{"penalty":"l2","C":1.0}', "seed": seed,
                })
                for x, coef in log["logistic_coef"].items():
                    rows.append({
                        "question": "Q5", "y_var": y, "model": "Logistic", "x_var": x,
                        "coefficient": coef, "n_effective": log["n"], "seed": seed,
                    })
                # predictions per country
                X_full = sub[x1_z + x2_z].values
                full_log = LogisticRegression(
                    penalty="l2", C=1.0, max_iter=1000,
                    class_weight="balanced", random_state=seed,
                ).fit(X_full, sub["y_binary"].values)
                probs = full_log.predict_proba(X_full)[:, 1]
                for iso3, prob in zip(sub["iso3"].values, probs):
                    rows_predictions.append({
                        "y_var": y, "iso3": iso3,
                        "p_high_population_usage": float(prob),
                        "model": "Logistic_in_sample", "seed": seed,
                    })

    df = pd.DataFrame(rows)
    OUTPUTS.mkdir(parents=True, exist_ok=True)

    # FDR sobre n_binding cruzando los 3 Y
    focal = "n_binding_z" if "n_binding_z" in fm.columns else "n_binding"
    focal_rows = df[(df["x_var"] == focal) & (df["model"] == "OLS_full") & df["p_value"].notna()]
    if len(focal_rows) > 0:
        pvals = focal_rows["p_value"].values
        fdr_q = fdr_benjamini_hochberg(pvals)
        df.loc[focal_rows.index, "fdr_q_value"] = fdr_q
        df.loc[focal_rows.index, "fdr_significant_05"] = (fdr_q < 0.05)

    df.to_csv(OUTPUTS / "q5_results.csv", index=False)
    pd.DataFrame(rows_predictions).to_csv(
        OUTPUTS / "q5_predictions_per_country.csv", index=False)

    # consistency table
    for x in x1_z:
        x_rows = df[(df["x_var"] == x) & (df["model"] == "OLS_full")]
        n_total = len(x_rows)
        if n_total == 0:
            continue
        n_neg = (x_rows["coefficient"] < 0).sum()
        n_pos = (x_rows["coefficient"] > 0).sum()
        n_sig_05 = (x_rows["p_value"] < 0.05).sum()
        n_sig_fdr = (x_rows.get("fdr_significant_05", pd.Series(False)) == True).sum()
        if n_neg >= max(2, 0.66 * n_total) and n_sig_05 >= 1:
            direction = "robust_negative"
        elif n_pos >= max(2, 0.66 * n_total) and n_sig_05 >= 1:
            direction = "robust_positive"
        elif n_sig_05 == 0:
            direction = "null"
        else:
            direction = "mixed"
        rows_consistency.append({
            "question": "Q5", "x_var": x,
            "n_y_total": n_total, "n_y_negative": int(n_neg), "n_y_positive": int(n_pos),
            "n_y_significant_05": int(n_sig_05),
            "n_y_significant_05_after_fdr": int(n_sig_fdr),
            "direction_summary": direction,
        })
    pd.DataFrame(rows_consistency).to_csv(OUTPUTS / "q5_consistency.csv", index=False)

    return {"n_rows_results": len(df), "n_rows_consistency": len(rows_consistency)}
