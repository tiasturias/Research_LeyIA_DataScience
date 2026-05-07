"""Q1 Inversión: OLS + Ridge + Lasso + bootstrap + PSM exploratorio."""

from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

from ._common_data import (
    load_bundle, get_train_test_split, get_x2_controls, get_x1_aggregated,
    get_x1_iapp_raw, F5_F8_MVP,
)
from ._common_regression import (
    fit_ols, fit_ols_with_bootstrap, fit_ridge_lasso_cv, fdr_benjamini_hochberg,
)

OUTPUTS = F5_F8_MVP / "FASE6" / "outputs"

Y_VARS_Q1 = [
    "oxford_ind_company_investment_emerging_tech",
    "oxford_ind_ai_unicorns_log",
    "oxford_ind_non_ai_unicorns_log",
    "oxford_ind_vc_availability",
    "wipo_c_vencapdeal_score",
    "wb_fdi_net_inflows",  # Y_Q1_or_control
]


def run_q1(seed: int = 42, n_boot: int = 2000) -> dict:
    bundle = load_bundle()
    fm = bundle["feature_matrix"]
    x1_agg = get_x1_aggregated()
    x2 = get_x2_controls()

    # Usar versiones _z donde estén disponibles, sino raw
    def col_z(c):
        return f"{c}_z" if f"{c}_z" in fm.columns else c
    x1_agg_z = [col_z(c) for c in x1_agg]
    x2_z = [col_z(c) for c in x2]

    rows_results = []
    rows_consistency = []

    for y in Y_VARS_Q1:
        if y not in fm.columns:
            continue

        # === Modelo solo controles X2 ===
        ols_x2 = fit_ols(fm, y, x2_z)
        # === Modelo X1 agregadas + X2 ===
        ols_full = fit_ols_with_bootstrap(fm, y, x1_agg_z + x2_z, n_boot=n_boot, seed=seed)
        # === Ridge + Lasso ===
        rl = fit_ridge_lasso_cv(fm, y, x1_agg_z + x2_z, seed=seed)

        # Persistir filas long
        if ols_full.get("status") == "ok":
            for x in x1_agg_z + x2_z + ["const"]:
                rows_results.append({
                    "question": "Q1", "y_var": y, "model": "OLS_full",
                    "x_var": x,
                    "coefficient": ols_full["coefficients"].get(x),
                    "std_error": ols_full["std_errors_asymptotic"].get(x),
                    "p_value": ols_full["pvalues_asymptotic"].get(x),
                    "ci95_lower": ols_full["bootstrap"].get(x, {}).get("ci95_lower"),
                    "ci95_upper": ols_full["bootstrap"].get(x, {}).get("ci95_upper"),
                    "p_value_bootstrap": ols_full["bootstrap"].get(x, {}).get("p_two_sided_bootstrap"),
                    "n_effective": ols_full["n"],
                    "r2": ols_full["r2"],
                    "ci_method": "bootstrap_2000",
                    "n_boot": n_boot,
                    "seed": seed,
                })

        if ols_x2.get("status") == "ok":
            rows_results.append({
                "question": "Q1", "y_var": y, "model": "OLS_only_X2",
                "x_var": "__model_metadata__",
                "n_effective": ols_x2["n"],
                "r2": ols_x2["r2"], "r2_adj": ols_x2["r2_adj"],
                "seed": seed,
            })

        if rl.get("status") == "ok":
            for x, coef in rl["ridge_coef"].items():
                rows_results.append({
                    "question": "Q1", "y_var": y, "model": "Ridge",
                    "x_var": x, "coefficient": coef,
                    "n_effective": rl["n"],
                    "r2": rl["ridge_cv_r2_mean"],
                    "cv_r2_mean_5fold": rl["ridge_cv_r2_mean"],
                    "cv_r2_std_5fold": rl["ridge_cv_r2_std"],
                    "loocv_r2": rl["ridge_loo_r2"],
                    "model_hyperparams_json": '{"alpha":1.0}',
                    "seed": seed,
                })
            for x, coef in rl["lasso_coef"].items():
                rows_results.append({
                    "question": "Q1", "y_var": y, "model": "Lasso",
                    "x_var": x, "coefficient": coef,
                    "n_effective": rl["n"],
                    "r2": rl["lasso_cv_r2_mean"],
                    "cv_r2_mean_5fold": rl["lasso_cv_r2_mean"],
                    "cv_r2_std_5fold": rl["lasso_cv_r2_std"],
                    "loocv_r2": rl["lasso_loo_r2"],
                    "model_hyperparams_json": '{"alpha":0.1}',
                    "seed": seed,
                })

    df = pd.DataFrame(rows_results)
    OUTPUTS.mkdir(parents=True, exist_ok=True)

    # FDR sobre p-values del X1 focal (n_binding) cruzando los 5-6 Y
    focal = "n_binding_z" if "n_binding_z" in fm.columns else "n_binding"
    focal_rows = df[(df["x_var"] == focal) & (df["model"] == "OLS_full") & df["p_value"].notna()]
    if len(focal_rows) > 0:
        pvals = focal_rows["p_value"].values
        fdr_q = fdr_benjamini_hochberg(pvals)
        df.loc[focal_rows.index, "fdr_q_value"] = fdr_q
        df.loc[focal_rows.index, "fdr_significant_05"] = (fdr_q < 0.05)

    df.to_csv(OUTPUTS / "q1_results.csv", index=False)

    # === Tabla consistency ===
    for x in x1_agg_z:
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
            "question": "Q1", "x_var": x,
            "n_y_total": n_total, "n_y_negative": int(n_neg), "n_y_positive": int(n_pos),
            "n_y_significant_05": int(n_sig_05),
            "n_y_significant_05_after_fdr": int(n_sig_fdr),
            "direction_summary": direction,
        })
    pd.DataFrame(rows_consistency).to_csv(OUTPUTS / "q1_consistency.csv", index=False)

    # === PSM EXPLORATORIO ===
    psm_result, psm_balance = propensity_score_match_exploratory(fm, treatment_col="iapp_ley_ia_vigente", caliper=0.20)
    psm_result.to_csv(OUTPUTS / "q1_psm_matched_pairs.csv", index=False)
    psm_balance.to_csv(OUTPUTS / "q1_psm_balance_diagnostics.csv", index=False)

    return {"n_rows_results": len(df), "n_rows_consistency": len(rows_consistency)}


def propensity_score_match_exploratory(
    fm: pd.DataFrame, treatment_col: str = "iapp_ley_ia_vigente",
    caliper: float = 0.20, seed: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """PSM 1:1 con caliper amplio. Marcado como exploratorio.
    Retorna (matched_pairs, balance_diagnostics)."""
    from ._common_data import get_x2_controls
    x2 = get_x2_controls()
    sub = fm[[treatment_col, "iso3"] + x2].dropna()
    if sub[treatment_col].sum() < 3 or (1 - sub[treatment_col]).sum() < 3:
        return (
            pd.DataFrame([{"status": "insufficient_n"}]),
            pd.DataFrame([{"status": "insufficient_n"}]),
        )

    X = sub[x2].values
    T = sub[treatment_col].astype(int).values

    ps_model = LogisticRegression(max_iter=1000).fit(X, T)
    ps = ps_model.predict_proba(X)[:, 1]
    sub = sub.assign(propensity=ps)

    treated = sub[sub[treatment_col] == 1].sort_values("propensity")
    control = sub[sub[treatment_col] == 0].sort_values("propensity")

    # Balance diagnostics pre-matching
    balance_rows = []
    for var in x2:
        t_mean = treated[var].mean()
        c_mean = control[var].mean()
        pooled_std = np.sqrt((treated[var].std()**2 + control[var].std()**2) / 2)
        smd = (t_mean - c_mean) / pooled_std if pooled_std > 0 else 0.0
        balance_rows.append({
            "variable": var,
            "treated_mean": float(t_mean),
            "control_mean": float(c_mean),
            "smd_pre": float(smd),
            "smd_post": np.nan,
        })

    matches = []
    used_idx = set()
    for tidx, trow in treated.iterrows():
        candidates = control[~control.index.isin(used_idx)]
        if candidates.empty:
            break
        diffs = (candidates["propensity"] - trow["propensity"]).abs()
        best = diffs.idxmin()
        if diffs[best] <= caliper:
            matches.append({
                "treated_iso3": trow["iso3"],
                "control_iso3": candidates.loc[best, "iso3"],
                "propensity_treated": float(trow["propensity"]),
                "propensity_control": float(candidates.loc[best, "propensity"]),
                "ps_diff": float(diffs[best]),
                "caliper": caliper,
                "treatment_col": treatment_col,
                "status": "ok",
            })
            used_idx.add(best)

    if len(matches) < 5:
        for m in matches:
            m["status"] = "exploratory_low_n"
    if len(matches) == 0:
        pairs_df = pd.DataFrame([{"status": "insufficient_n", "caliper": caliper, "treatment_col": treatment_col}])
    else:
        pairs_df = pd.DataFrame(matches)

    # Post-matching SMD if we have matches
    if len(matches) > 0:
        matched_treated_iso3 = [m["treated_iso3"] for m in matches]
        matched_control_iso3 = [m["control_iso3"] for m in matches]
        t_matched = sub[sub["iso3"].isin(matched_treated_iso3)]
        c_matched = sub[sub["iso3"].isin(matched_control_iso3)]
        for i, row in enumerate(balance_rows):
            var = row["variable"]
            t_mean = t_matched[var].mean()
            c_mean = c_matched[var].mean()
            pooled_std = np.sqrt((t_matched[var].std()**2 + c_matched[var].std()**2) / 2)
            balance_rows[i]["smd_post"] = float((t_mean - c_mean) / pooled_std) if pooled_std > 0 else 0.0

    balance_df = pd.DataFrame(balance_rows)
    return pairs_df, balance_df
