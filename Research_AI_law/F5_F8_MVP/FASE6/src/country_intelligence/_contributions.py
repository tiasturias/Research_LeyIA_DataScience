"""Contribuciones descriptivas de términos de modelo por país."""

import pandas as pd


def extract_coefficients(results: dict[str, pd.DataFrame]) -> pd.DataFrame:
    frames = []
    for q, df in results.items():
        if q == "Q4":
            continue
        temp = df.copy()
        temp["question_id"] = temp.get("question_id", q)
        if "term" not in temp.columns and "predictor" in temp.columns:
            temp = temp.rename(columns={"predictor": "term"})
        if "estimate" not in temp.columns and "coefficient" in temp.columns:
            temp = temp.rename(columns={"coefficient": "estimate"})
        if "term" in temp.columns and "estimate" in temp.columns:
            frames.append(temp[["question_id", "outcome", "term", "estimate"]].dropna())
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def build_country_model_contributions(fm: pd.DataFrame, results: dict[str, pd.DataFrame]) -> pd.DataFrame:
    coefs = extract_coefficients(results)
    rows = []
    if coefs.empty:
        return pd.DataFrame()

    for _, coef in coefs.iterrows():
        term = coef["term"]
        if term not in fm.columns or str(term).lower() in {"const", "intercept"}:
            continue

        s = pd.to_numeric(fm[term], errors="coerce")
        if s.std(skipna=True) and s.std(skipna=True) > 0:
            term_z = (s - s.mean(skipna=True)) / s.std(skipna=True)
        else:
            term_z = pd.Series([pd.NA] * len(fm), index=fm.index)

        for idx, r in fm.iterrows():
            contribution = term_z.loc[idx] * coef["estimate"] if pd.notna(term_z.loc[idx]) else pd.NA
            rows.append({
                "iso3": r["iso3"],
                "country_name": r.get("country_name_canonical", r.get("country_name", "")),
                "question_id": coef["question_id"],
                "outcome": coef["outcome"],
                "model_id": "phase6_primary_or_available",
                "term": term,
                "term_value": r.get(term),
                "term_percentile": s.rank(pct=True).loc[idx] if pd.notna(r.get(term)) else pd.NA,
                "coefficient_or_weight": coef["estimate"],
                "standardized_contribution": contribution,
                "contribution_direction": "positive" if pd.notna(contribution) and contribution > 0 else ("negative" if pd.notna(contribution) and contribution < 0 else "neutral_or_missing"),
                "contribution_rank_within_country": pd.NA,
                "contribution_label": "descriptive_driver_not_causal",
                "driver_type": "model_term",
                "interpretation": "Descriptive contribution based on in-sample model coefficient and country value; not causal.",
                "causal_claim": False,
            })

    out = pd.DataFrame(rows)
    if not out.empty:
        out["abs_contribution"] = pd.to_numeric(out["standardized_contribution"], errors="coerce").abs()
        out["contribution_rank_within_country"] = out.groupby(["iso3", "question_id", "outcome"])["abs_contribution"].rank(ascending=False, method="min")
    return out
