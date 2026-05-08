"""Residuales, gaps y detección de over/underperformers."""

import pandas as pd
import numpy as np
import statsmodels.api as sm

DEFAULT_CONTROLS = ["wb_gdp_per_capita_ppp_log", "wb_internet_penetration", "wb_government_effectiveness"]
DEFAULT_TERMS = ["n_binding", "n_non_binding", "regulatory_intensity"]


def fit_simple_prediction(fm: pd.DataFrame, outcome: str):
    predictors = [c for c in DEFAULT_TERMS + DEFAULT_CONTROLS if c in fm.columns]
    if outcome not in fm.columns or not predictors:
        return None, pd.DataFrame()

    sub = fm[["iso3", "country_name_canonical", outcome] + predictors].dropna()
    if len(sub) < max(12, len(predictors) * 4):
        return None, sub

    X = sm.add_constant(sub[predictors], has_constant="add")
    y = sub[outcome]
    model = sm.OLS(y, X).fit(cov_type="HC3")
    sub = sub.copy()
    sub["fitted_value"] = model.predict(X)
    sub["residual"] = y - sub["fitted_value"]
    return model, sub


def build_country_residuals_and_gaps(fm: pd.DataFrame, outcomes_by_q: dict) -> pd.DataFrame:
    rows = []
    for q, outcomes in outcomes_by_q.items():
        if q == "Q4":
            continue
        for outcome in outcomes:
            model, sub = fit_simple_prediction(fm, outcome)
            if model is None or sub.empty:
                continue
            best = sub[outcome].max()
            chile_val = sub.loc[sub["iso3"].eq("CHL"), outcome]
            sgp_val = sub.loc[sub["iso3"].eq("SGP"), outcome]
            chile_val = chile_val.iloc[0] if not chile_val.empty else pd.NA
            sgp_val = sgp_val.iloc[0] if not sgp_val.empty else pd.NA

            sub["absolute_residual"] = sub["residual"].abs()
            sub["residual_rank"] = sub["absolute_residual"].rank(ascending=False, method="min")
            sub["residual_percentile"] = sub["absolute_residual"].rank(pct=True)
            for _, r in sub.iterrows():
                label = "overperformer" if r["residual"] > 0 else ("underperformer" if r["residual"] < 0 else "as_expected")
                rows.append({
                    "iso3": r["iso3"],
                    "country_name": r["country_name_canonical"],
                    "question_id": q,
                    "outcome": outcome,
                    "model_id": "simple_adjusted_internal",
                    "observed_value": r[outcome],
                    "fitted_value": r["fitted_value"],
                    "residual": r["residual"],
                    "absolute_residual": r["absolute_residual"],
                    "residual_rank": r["residual_rank"],
                    "residual_percentile": r["residual_percentile"],
                    "overperformer_underperformer": label,
                    "gap_vs_best": best - r[outcome],
                    "gap_vs_group_best": best - r[outcome],
                    "gap_vs_chile": r[outcome] - chile_val if pd.notna(chile_val) else pd.NA,
                    "gap_vs_singapore": r[outcome] - sgp_val if pd.notna(sgp_val) else pd.NA,
                    "interpretation": "Observed minus fitted within in-sample descriptive model; not causal.",
                })
    return pd.DataFrame(rows)
