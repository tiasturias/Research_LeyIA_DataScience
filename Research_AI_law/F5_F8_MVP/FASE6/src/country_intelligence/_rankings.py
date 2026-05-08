"""Rankings globales, por grupo, y mejores/peores por Q."""

import pandas as pd
from ._scoring import percentile_rank, descending_rank, label_from_percentile


def rank_outcome(
    df: pd.DataFrame,
    outcome: str,
    question_id: str,
    question_label: str,
    higher_is_better: bool = True,
) -> pd.DataFrame:
    if outcome not in df.columns:
        return pd.DataFrame()

    out = df[["iso3", "country_name_canonical", "region", "income_group", outcome]].copy()
    out = out.rename(columns={
        "country_name_canonical": "country_name",
        outcome: "value_used_for_ranking",
    })
    out["question_id"] = question_id
    out["question_label"] = question_label
    out["outcome"] = outcome
    out["outcome_label"] = outcome
    out["value_type"] = "observed_or_score"
    out["rank_desc"] = descending_rank(out["value_used_for_ranking"], higher_is_better)
    out["rank_asc"] = descending_rank(out["value_used_for_ranking"], not higher_is_better)
    out["percentile"] = percentile_rank(out["value_used_for_ranking"], higher_is_better)
    out["n_ranked"] = out["value_used_for_ranking"].notna().sum()
    out["is_top_5_global"] = out["rank_desc"] <= 5
    out["is_bottom_5_global"] = out["rank_asc"] <= 5
    out["interpretation_label"] = out["percentile"].apply(label_from_percentile)
    out["missingness_flag"] = out["value_used_for_ranking"].isna()
    out["why_high_or_low_short"] = out["interpretation_label"].map({
        "top_pioneer": "ubicado en el tramo superior de la muestra",
        "high_performer": "desempeño alto relativo",
        "middle_performer": "desempeño intermedio relativo",
        "low_performer": "desempeño bajo relativo",
        "bottom_laggard": "ubicado en el tramo inferior de la muestra",
        "not_ranked_missing": "sin dato suficiente para ranking",
    })
    return out


def build_rankings_by_group(rankings: pd.DataFrame, group_membership: pd.DataFrame) -> pd.DataFrame:
    merged = rankings.merge(group_membership, on="iso3", how="left")
    rows = []
    for (group_name, question_id, outcome), g in merged.groupby(["group_name", "question_id", "outcome"], dropna=False):
        g = g.copy()
        valid = g["value_used_for_ranking"].notna()
        g["rank_within_group"] = g.loc[valid, "value_used_for_ranking"].rank(ascending=False, method="min")
        g["percentile_within_group"] = g.loc[valid, "value_used_for_ranking"].rank(pct=True, method="average")
        g["n_group_ranked"] = valid.sum()
        g["is_best_in_group"] = g["rank_within_group"] == 1
        g["is_worst_in_group"] = g["rank_within_group"] == g["n_group_ranked"]
        best_val = g.loc[valid, "value_used_for_ranking"].max() if valid.any() else pd.NA
        med_val = g.loc[valid, "value_used_for_ranking"].median() if valid.any() else pd.NA
        chile_val = g.loc[g["iso3"].eq("CHL"), "value_used_for_ranking"]
        chile_val = chile_val.iloc[0] if not chile_val.empty else pd.NA
        g["distance_to_group_best"] = best_val - g["value_used_for_ranking"]
        g["distance_to_group_median"] = med_val - g["value_used_for_ranking"]
        g["distance_to_chile"] = g["value_used_for_ranking"] - chile_val if pd.notna(chile_val) else pd.NA
        g["why_best_or_worst"] = g.apply(
            lambda r: "mejor de su grupo" if r.get("is_best_in_group") else ("peor de su grupo" if r.get("is_worst_in_group") else ""),
            axis=1
        )
        rows.append(g)
    return pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()


def build_best_worst_by_q(rankings: pd.DataFrame, rankings_group: pd.DataFrame, top_n=5, bottom_n=5) -> pd.DataFrame:
    rows = []
    for (q, outcome), g in rankings.groupby(["question_id", "outcome"], dropna=False):
        valid = g[g["value_used_for_ranking"].notna()].copy()
        top = valid.nsmallest(top_n, "rank_desc")
        bottom = valid.nsmallest(bottom_n, "rank_asc")
        for rank_type, sub in [("best_global", top), ("worst_global", bottom)]:
            for _, r in sub.iterrows():
                rows.append({
                    "question_id": q,
                    "question_label": r.get("question_label"),
                    "group_name": "global_43",
                    "rank_type": rank_type,
                    "iso3": r["iso3"],
                    "country_name": r["country_name"],
                    "rank": r["rank_desc"] if rank_type == "best_global" else r["rank_asc"],
                    "percentile": r["percentile"],
                    "value_summary": r["value_used_for_ranking"],
                    "main_driver_1": r["outcome"],
                    "main_driver_2": "",
                    "main_driver_3": "",
                    "why_this_country_is_best_or_worst": r["why_high_or_low_short"],
                    "lesson_for_chile": "comparar perfil país y drivers antes de extraer lección política",
                    "caution_note": "ranking descriptivo in-sample; no causalidad",
                })

    # Agregar best/worst por grupo relevantes
    if not rankings_group.empty:
        for (group_name, q, outcome), g in rankings_group.groupby(["group_name", "question_id", "outcome"], dropna=False):
            valid = g[g["value_used_for_ranking"].notna()].copy()
            if len(valid) == 0:
                continue
            top = valid.nsmallest(3, "rank_within_group")
            bottom = valid.nlargest(3, "rank_within_group")
            for rank_type, sub in [("best_group", top), ("worst_group", bottom)]:
                for _, r in sub.iterrows():
                    rows.append({
                        "question_id": q,
                        "question_label": r.get("question_label"),
                        "group_name": group_name,
                        "rank_type": rank_type,
                        "iso3": r["iso3"],
                        "country_name": r["country_name"],
                        "rank": r["rank_within_group"],
                        "percentile": r["percentile_within_group"],
                        "value_summary": r["value_used_for_ranking"],
                        "main_driver_1": r["outcome"],
                        "main_driver_2": "",
                        "main_driver_3": "",
                        "why_this_country_is_best_or_worst": r["why_best_or_worst"],
                        "lesson_for_chile": "comparar perfil país y drivers antes de extraer lección política",
                        "caution_note": "ranking descriptivo in-sample; no causalidad",
                    })
    return pd.DataFrame(rows)
