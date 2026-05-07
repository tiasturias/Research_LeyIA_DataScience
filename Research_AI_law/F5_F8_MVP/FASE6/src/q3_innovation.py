"""Q3 Innovación: Ridge + Gradient Boosting, primary vs auxiliary tier."""

from __future__ import annotations
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score, RepeatedKFold, LeaveOneOut

from ._common_data import (
    load_bundle, get_x2_controls, get_x1_aggregated, F5_F8_MVP,
)
from ._common_regression import (
    fit_ols_with_bootstrap, fit_ridge_lasso_cv, fdr_benjamini_hochberg,
)

OUTPUTS = F5_F8_MVP / "FASE6" / "outputs"

Y_VARS_Q3_PRIMARY = [
    "wipo_out_score",
    "oxford_total_score",
    "wipo_gii_score",
    "oxford_innovation_capacity",
    "oxford_ind_ai_research_papers_log",
    "wb_patent_applications_residents",
]
Y_VARS_Q3_AUXILIARY = [
    "stanford_fig_6_3_5_fig_6_3_5_volume_of_publications",
]


def run_q3(seed: int = 42, n_boot: int = 2000) -> dict:
    bundle = load_bundle()
    fm = bundle["feature_matrix"]
    x1_agg = get_x1_aggregated()
    x2 = get_x2_controls()

    def col_z(c):
        return f"{c}_z" if f"{c}_z" in fm.columns else c
    x1_z = [col_z(c) for c in x1_agg]
    x2_z = [col_z(c) for c in x2]

    rows = []

    def fit_and_record(y, tier):
        ols = fit_ols_with_bootstrap(fm, y, x1_z + x2_z, n_boot=n_boot, seed=seed)
        rl = fit_ridge_lasso_cv(fm, y, x1_z + x2_z, seed=seed)

        # GBR
        sub = fm[[y] + x1_z + x2_z].dropna()
        if len(sub) >= 15:
            X, ytrue = sub[x1_z + x2_z].values, sub[y].values
            cv = RepeatedKFold(n_splits=5, n_repeats=10, random_state=seed)
            gbr = GradientBoostingRegressor(
                n_estimators=200, max_depth=3, learning_rate=0.05, random_state=seed,
            )
            gbr_cv = cross_val_score(gbr, X, ytrue, cv=cv, scoring="r2")
            gbr_loo = cross_val_score(gbr, X, ytrue, cv=LeaveOneOut(), scoring="r2").mean()
            gbr_full = GradientBoostingRegressor(
                n_estimators=200, max_depth=3, learning_rate=0.05, random_state=seed,
            ).fit(X, ytrue)
            for x, imp in zip(x1_z + x2_z, gbr_full.feature_importances_):
                rows.append({
                    "question": "Q3", "tier": tier,
                    "y_var": y, "model": "GBR", "x_var": x,
                    "coefficient_or_importance": float(imp),
                    "n_effective": len(sub),
                    "cv_r2_mean_5fold": float(gbr_cv.mean()),
                    "cv_r2_std_5fold": float(gbr_cv.std()),
                    "loocv_r2": float(gbr_loo),
                    "model_hyperparams_json": '{"n_estimators":200,"max_depth":3,"lr":0.05}',
                    "seed": seed,
                })

        if ols.get("status") == "ok":
            for x in x1_z + x2_z + ["const"]:
                rows.append({
                    "question": "Q3", "tier": tier,
                    "y_var": y, "model": "OLS_full", "x_var": x,
                    "coefficient_or_importance": ols["coefficients"].get(x),
                    "std_error": ols["std_errors_asymptotic"].get(x),
                    "p_value": ols["pvalues_asymptotic"].get(x),
                    "ci95_lower": ols["bootstrap"].get(x, {}).get("ci95_lower"),
                    "ci95_upper": ols["bootstrap"].get(x, {}).get("ci95_upper"),
                    "p_value_bootstrap": ols["bootstrap"].get(x, {}).get("p_two_sided_bootstrap"),
                    "n_effective": ols["n"], "r2": ols["r2"],
                    "ci_method": "bootstrap_2000", "n_boot": n_boot, "seed": seed,
                })

        if rl.get("status") == "ok":
            for x, coef in rl["ridge_coef"].items():
                rows.append({
                    "question": "Q3", "tier": tier,
                    "y_var": y, "model": "Ridge", "x_var": x,
                    "coefficient_or_importance": coef,
                    "n_effective": rl["n"],
                    "cv_r2_mean_5fold": rl["ridge_cv_r2_mean"],
                    "cv_r2_std_5fold": rl["ridge_cv_r2_std"],
                    "loocv_r2": rl["ridge_loo_r2"],
                    "model_hyperparams_json": '{"alpha":1.0}', "seed": seed,
                })

    for y in Y_VARS_Q3_PRIMARY:
        if y in fm.columns:
            fit_and_record(y, tier="primary")
    for y in Y_VARS_Q3_AUXILIARY:
        if y in fm.columns:
            fit_and_record(y, tier="auxiliary_low_n")

    df = pd.DataFrame(rows)

    # FDR sobre n_binding cruzando solo Y primary
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

    df.to_csv(OUTPUTS / "q3_results.csv", index=False)

    # consistency tabla
    cons = []
    for x in x1_z:
        for tier in ["primary", "auxiliary_low_n"]:
            sub = df[(df["x_var"] == x) & (df["model"] == "OLS_full") & (df["tier"] == tier)]
            if len(sub) == 0:
                continue
            n_neg = (sub["coefficient_or_importance"] < 0).sum()
            n_pos = (sub["coefficient_or_importance"] > 0).sum()
            n_sig = (sub["p_value"] < 0.05).sum()
            cons.append({
                "question": "Q3", "tier": tier, "x_var": x,
                "n_y_total": len(sub),
                "n_y_negative": int(n_neg),
                "n_y_positive": int(n_pos),
                "n_y_significant_05": int(n_sig),
            })
    pd.DataFrame(cons).to_csv(OUTPUTS / "q3_consistency.csv", index=False)

    return {"n_rows": len(df)}
