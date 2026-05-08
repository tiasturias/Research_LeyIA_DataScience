import statsmodels.api as sm
import pandas as pd


def rescale_percent_to_fraction(y):
    y = y.astype(float)
    if y.max(skipna=True) > 1.0:
        return y / 100.0
    return y


def fit_fractional_logit_or_ols(sub, outcome: str, predictors: list[str]) -> dict:
    """Ajusta GLM binomial fraccional si el outcome está en [0,1]; fallback OLS HC3."""
    y_frac = rescale_percent_to_fraction(sub[outcome])
    X = sm.add_constant(sub[predictors].astype(float), has_constant="add")

    if y_frac.notna().all() and y_frac.between(0, 1).all() and y_frac.nunique() > 2:
        try:
            glm = sm.GLM(y_frac, X, family=sm.families.Binomial()).fit(cov_type="HC3")
            rows = []
            for term in glm.params.index:
                rows.append({
                    "term": term,
                    "estimate": float(glm.params[term]),
                    "std_error_hc3": float(glm.bse[term]),
                    "p_value": float(glm.pvalues[term]),
                    "model_family": "fractional_logit_quasi_binomial",
                    "outcome_scale_used": "fraction_0_1",
                })
            return {"model": glm, "rows": rows, "fit_status": "ok_fractional_logit"}
        except Exception as e:
            fallback_reason = str(e)[:250]
    else:
        fallback_reason = "outcome_not_fractional_or_not_variable_enough"

    ols = sm.OLS(y_frac, X).fit(cov_type="HC3")
    rows = []
    for term in ols.params.index:
        rows.append({
            "term": term,
            "estimate": float(ols.params[term]),
            "std_error_hc3": float(ols.bse[term]),
            "p_value": float(ols.pvalues[term]),
            "model_family": "ols_on_fraction_or_score_fallback",
            "outcome_scale_used": "fraction_or_original",
            "fallback_reason": fallback_reason,
        })
    return {"model": ols, "rows": rows, "fit_status": "ok_ols_fallback"}
