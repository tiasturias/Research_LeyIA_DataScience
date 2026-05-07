"""Q6 Uso de IA en sector público:
- Y primarias (5, 100% cobertura): oxford_public_sector_adoption,
  oxford_e_government_delivery, oxford_government_digital_policy,
  oxford_ind_data_governance, oecd_2_indigo_oecd_indigo_score
- Y auxiliar (1, 31/43): oecd_4_digital_gov_oecd_digital_gov_overall (tier_low_n)
- Modelos: OLS con bootstrap + Logistic con clasificación binarizada."""

from __future__ import annotations
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

Y_VARS_Q6_PRIMARY = [
    "oxford_public_sector_adoption",
    "oxford_e_government_delivery",
    "oxford_government_digital_policy",
    "oxford_ind_data_governance",
    "oecd_2_indigo_oecd_indigo_score",
]
Y_VARS_Q6_AUXILIARY = [
    "oecd_4_digital_gov_oecd_digital_gov_overall",
]


def run_q6(seed: int = 42, n_boot: int = 2000) -> dict:
    bundle = load_bundle()
    fm = bundle["feature_matrix"]
    x1_agg = get_x1_aggregated()
    x2 = get_x2_controls()

    def col_z(c):
        return f"{c}_z" if f"{c}_z" in fm.columns else c
    x1_z = [col_z(c) for c in x1_agg]
    x2_z = [col_z(c) for c in x2]

    rows = []
    rows_predictions = []

    def fit_and_record(y, tier):
        # OLS bootstrap
        ols = fit_ols_with_bootstrap(fm, y, x1_z + x2_z, n_boot=n_boot, seed=seed)
        if ols.get("status") == "ok":
            for x in x1_z + x2_z + ["const"]:
                rows.append({
                    "question": "Q6", "tier": tier,
                    "y_var": y, "model": "OLS_full", "x_var": x,
                    "coefficient": ols["coefficients"].get(x),
                    "std_error": ols["std_errors_asymptotic"].get(x),
                    "p_value": ols["pvalues_asymptotic"].get(x),
                    "ci95_lower": ols["bootstrap"].get(x, {}).get("ci95_lower"),
                    "ci95_upper": ols["bootstrap"].get(x, {}).get("ci95_upper"),
                    "p_value_bootstrap": ols["bootstrap"].get(x, {}).get("p_two_sided_bootstrap"),
                    "n_effective": ols["n"], "r2": ols["r2"], "ci_method": "bootstrap_2000",
                    "n_boot": n_boot, "seed": seed,
                })

        # Logistic clasificación
        sub = fm[[y, "iso3"] + x1_z + x2_z].dropna()
        if len(sub) >= 20:
            y_bin, threshold = binarize_by_median(sub[y])
            sub = sub.assign(y_binary=y_bin.values)
            log = fit_logistic_cv(sub, "y_binary", x1_z + x2_z, seed=seed)
            if log.get("status") == "ok":
                rows.append({
                    "question": "Q6", "tier": tier, "y_var": y,
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
                        "question": "Q6", "tier": tier, "y_var": y,
                        "model": "Logistic", "x_var": x,
                        "coefficient": coef, "n_effective": log["n"], "seed": seed,
                    })
                X_full = sub[x1_z + x2_z].values
                full_log = LogisticRegression(
                    penalty="l2", C=1.0, max_iter=1000,
                    class_weight="balanced", random_state=seed,
                ).fit(X_full, sub["y_binary"].values)
                probs = full_log.predict_proba(X_full)[:, 1]
                for iso3, prob in zip(sub["iso3"].values, probs):
                    rows_predictions.append({
                        "y_var": y, "tier": tier, "iso3": iso3,
                        "p_high_public_sector_use": float(prob),
                        "model": "Logistic_in_sample", "seed": seed,
                    })

    for y in Y_VARS_Q6_PRIMARY:
        if y in fm.columns:
            fit_and_record(y, tier="primary")
    for y in Y_VARS_Q6_AUXILIARY:
        if y in fm.columns:
            fit_and_record(y, tier="auxiliary_low_n")

    df = pd.DataFrame(rows)

    # FDR solo sobre tier=primary
    focal = "n_binding_z" if "n_binding_z" in fm.columns else "n_binding"
    primary_focal = df[
        (df["x_var"] == focal) & (df["model"] == "OLS_full") &
        (df["tier"] == "primary") & df["p_value"].notna()
    ]
    if len(primary_focal) > 0:
        pvals = primary_focal["p_value"].values
        fdr_q = fdr_benjamini_hochberg(pvals)
        df.loc[primary_focal.index, "fdr_q_value"] = fdr_q
        df.loc[primary_focal.index, "fdr_significant_05"] = (fdr_q < 0.05)

    df.to_csv(OUTPUTS / "q6_results.csv", index=False)
    pd.DataFrame(rows_predictions).to_csv(
        OUTPUTS / "q6_predictions_per_country.csv", index=False)

    # consistency tier=primary
    cons = []
    for x in x1_z:
        sub = df[(df["x_var"] == x) & (df["model"] == "OLS_full") & (df["tier"] == "primary")]
        if len(sub) == 0:
            continue
        n_neg = (sub["coefficient"] < 0).sum()
        n_pos = (sub["coefficient"] > 0).sum()
        n_sig = (sub["p_value"] < 0.05).sum()
        cons.append({
            "question": "Q6", "tier": "primary", "x_var": x,
            "n_y_total": len(sub),
            "n_y_negative": int(n_neg),
            "n_y_positive": int(n_pos),
            "n_y_significant_05": int(n_sig),
        })
    pd.DataFrame(cons).to_csv(OUTPUTS / "q6_consistency.csv", index=False)

    return {"n_rows": len(df)}
