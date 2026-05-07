"""Utilidades de regresión: OLS, Ridge, Lasso, bootstrap, FDR."""

from __future__ import annotations
import warnings

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import (
    cross_val_score, RepeatedKFold, LeaveOneOut, KFold
)


def fdr_benjamini_hochberg(pvalues: np.ndarray, alpha: float = 0.05) -> np.ndarray:
    """BH FDR correction. Returns adjusted p-values."""
    n = len(pvalues)
    if n == 0:
        return pvalues
    pvalues = np.nan_to_num(pvalues.astype(float), nan=1.0, posinf=1.0, neginf=1.0)
    order = np.argsort(pvalues)
    ranked = np.empty(n)
    ranked[order] = np.arange(1, n + 1)
    adjusted = np.minimum(1.0, pvalues * n / ranked)
    for i in range(n - 2, -1, -1):
        adjusted[order[i]] = min(adjusted[order[i]], adjusted[order[i + 1]])
    return adjusted


def fit_ols(df: pd.DataFrame, y: str, x_cols: list[str]) -> dict:
    """OLS con statsmodels. Retorna coeficientes, IC asintóticos, p-values."""
    sub = df[[y] + x_cols].dropna()
    if len(sub) < 10:
        return {"status": "insufficient_n", "n": len(sub)}
    X = sm.add_constant(sub[x_cols])
    model = sm.OLS(sub[y], X).fit()
    ci = model.conf_int(0.05)
    return {
        "status": "ok",
        "n": len(sub),
        "r2": float(model.rsquared),
        "r2_adj": float(model.rsquared_adj),
        "coefficients": model.params.to_dict(),
        "std_errors": model.bse.to_dict(),
        "pvalues": model.pvalues.to_dict(),
        "ci95_lower": ci[0].to_dict(),
        "ci95_upper": ci[1].to_dict(),
    }


def fit_ols_with_bootstrap(
    df: pd.DataFrame, y: str, x_cols: list[str],
    n_boot: int = 2000, seed: int = 42,
) -> dict:
    """OLS + bootstrap (B=2000) para IC95 BCa de cada coeficiente."""
    sub = df[[y] + x_cols].dropna()
    if len(sub) < 15:
        return {"status": "insufficient_n", "n": len(sub)}

    rng = np.random.default_rng(seed)
    point = sm.OLS(sub[y], sm.add_constant(sub[x_cols])).fit()
    point_coefs = point.params

    boot_coefs = {col: [] for col in point_coefs.index}
    for _ in range(n_boot):
        idx = rng.integers(0, len(sub), len(sub))
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                b = sm.OLS(
                    sub[y].iloc[idx],
                    sm.add_constant(sub[x_cols].iloc[idx]),
                ).fit()
            for col in point_coefs.index:
                boot_coefs[col].append(b.params.get(col, np.nan))
        except Exception:
            continue

    results = {}
    for col, vals in boot_coefs.items():
        arr = np.array(vals)
        arr = arr[np.isfinite(arr)]
        if len(arr) < 100:
            results[col] = {
                "ci95_lower": np.nan, "ci95_upper": np.nan,
                "p_two_sided_bootstrap": np.nan,
                "n_boot_valid": int(len(arr)),
            }
            continue
        results[col] = {
            "ci95_lower": float(np.nanpercentile(arr, 2.5)),
            "ci95_upper": float(np.nanpercentile(arr, 97.5)),
            "p_two_sided_bootstrap": float(2 * min(
                (arr <= 0).mean(), (arr >= 0).mean(),
            )),
            "n_boot_valid": int(len(arr)),
        }

    return {
        "status": "ok",
        "n": len(sub),
        "r2": float(point.rsquared),
        "r2_adj": float(point.rsquared_adj),
        "coefficients": point_coefs.to_dict(),
        "std_errors_asymptotic": point.bse.to_dict(),
        "pvalues_asymptotic": point.pvalues.to_dict(),
        "bootstrap": results,
    }


def fit_ridge_lasso_cv(
    df: pd.DataFrame, y: str, x_cols: list[str],
    alpha_ridge: float = 1.0, alpha_lasso: float = 0.1,
    cv_repeats: int = 10, cv_splits: int = 5, seed: int = 42,
) -> dict:
    """Ridge y Lasso con Repeated K-fold CV."""
    sub = df[[y] + x_cols].dropna()
    if len(sub) < 15:
        return {"status": "insufficient_n", "n": len(sub)}
    X = sub[x_cols].values
    ytrue = sub[y].values
    cv = RepeatedKFold(n_splits=cv_splits, n_repeats=cv_repeats, random_state=seed)

    ridge = Ridge(alpha=alpha_ridge, random_state=seed)
    lasso = Lasso(alpha=alpha_lasso, max_iter=10000, random_state=seed)

    ridge_cv = cross_val_score(ridge, X, ytrue, cv=cv, scoring="r2")
    lasso_cv = cross_val_score(lasso, X, ytrue, cv=cv, scoring="r2")

    ridge_full = Ridge(alpha=alpha_ridge, random_state=seed).fit(X, ytrue)
    lasso_full = Lasso(alpha=alpha_lasso, max_iter=10000, random_state=seed).fit(X, ytrue)

    # LOOCV sanity check
    loo = LeaveOneOut()
    ridge_loo = cross_val_score(ridge, X, ytrue, cv=loo, scoring="r2").mean()
    lasso_loo = cross_val_score(lasso, X, ytrue, cv=loo, scoring="r2").mean()

    return {
        "status": "ok",
        "n": len(sub),
        "ridge_cv_r2_mean": float(ridge_cv.mean()),
        "ridge_cv_r2_std": float(ridge_cv.std()),
        "ridge_loo_r2": float(ridge_loo),
        "ridge_coef": dict(zip(x_cols, ridge_full.coef_.tolist())),
        "ridge_intercept": float(ridge_full.intercept_),
        "lasso_cv_r2_mean": float(lasso_cv.mean()),
        "lasso_cv_r2_std": float(lasso_cv.std()),
        "lasso_loo_r2": float(lasso_loo),
        "lasso_coef": dict(zip(x_cols, lasso_full.coef_.tolist())),
        "lasso_intercept": float(lasso_full.intercept_),
    }
