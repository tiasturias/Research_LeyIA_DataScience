import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import RepeatedKFold, cross_val_score
from sklearn.linear_model import RidgeCV


def fit_ols_adjusted(sub, outcome: str, predictors: list[str]) -> dict:
    X = sm.add_constant(sub[predictors].astype(float), has_constant="add")
    y = sub[outcome].astype(float)
    model = sm.OLS(y, X).fit(cov_type="HC3")
    rows = []
    for term in model.params.index:
        rows.append({
            "term": term,
            "estimate": float(model.params[term]),
            "std_error_hc3": float(model.bse[term]),
            "p_value": float(model.pvalues[term]),
            "r2_in_sample": float(model.rsquared),
            "adj_r2_in_sample": float(model.rsquared_adj),
        })
    return {"model": model, "rows": rows}


def repeated_kfold_regression_diagnostic(X, y, estimator=None, n_splits=5, n_repeats=20):
    n = len(y)
    if n < 12:
        return {"cv_r2_mean": np.nan, "cv_rmse_mean": np.nan, "cv_note": "not_computed_low_n"}
    k = min(n_splits, max(3, n // 5))
    cv = RepeatedKFold(n_splits=k, n_repeats=n_repeats, random_state=20260508)
    if estimator is None:
        estimator = RidgeCV(alphas=np.logspace(-3, 3, 25))
    r2_scores = cross_val_score(estimator, X, y, cv=cv, scoring="r2")
    neg_mse = cross_val_score(estimator, X, y, cv=cv, scoring="neg_mean_squared_error")
    return {
        "cv_r2_mean": float(np.nanmean(r2_scores)),
        "cv_r2_sd": float(np.nanstd(r2_scores)),
        "cv_rmse_mean": float(np.sqrt(-np.nanmean(neg_mse))),
        "cv_note": "repeated_kfold_internal_not_external_test",
    }


def loocv_r2_policy():
    return {
        "loo_r2": np.nan,
        "loocv_note": "not_computed_r2_undefined_for_single_observation_test_folds",
    }
