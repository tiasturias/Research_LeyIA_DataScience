"""Construcción de perfiles país por Q: long y wide."""

import pandas as pd
from ._scoring import label_from_percentile, strength_weakness_label


def build_country_q_profile_long(rankings: pd.DataFrame) -> pd.DataFrame:
    out = rankings.copy()
    out["dimension_type"] = "question_outcome"
    out["observed_value"] = out["value_used_for_ranking"]
    out["score_value"] = out["value_used_for_ranking"]
    out["score_source"] = "observed_or_phase6_score"
    out["rank_global"] = out["rank_desc"]
    out["percentile_global"] = out["percentile"]
    out["z_score_global"] = pd.NA
    out["n_comparable_countries"] = out["n_ranked"]
    out["missing_observed_value"] = out["value_used_for_ranking"].isna()
    out["missing_score_value"] = out["value_used_for_ranking"].isna()
    out["strength_weakness_label"] = out["percentile"].apply(strength_weakness_label)
    out["score_scope"] = "in_sample_descriptive_positioning"
    out["independent_prediction"] = False
    out["causal_claim"] = False
    out["notes"] = "Descriptive country-level position; not external prediction or causality."
    keep = [
        "iso3", "country_name", "region", "income_group",
        "question_id", "question_label", "dimension_type", "outcome",
        "observed_value", "score_value", "score_source",
        "rank_global", "percentile_global",
        "rank_desc", "n_comparable_countries",
        "missing_observed_value", "missing_score_value",
        "interpretation_label", "strength_weakness_label",
        "score_scope", "independent_prediction", "causal_claim", "notes",
    ]
    return out[[c for c in keep if c in out.columns]]


def build_country_q_profile_wide(profile_long: pd.DataFrame, clusters: pd.DataFrame | None = None) -> pd.DataFrame:
    q_summary = (
        profile_long
        .groupby(["iso3", "country_name", "region", "income_group", "question_id"], dropna=False)
        .agg(
            question_percentile=("percentile_global", "mean"),
            n_dimensions_available=("percentile_global", "count"),
        )
        .reset_index()
    )
    q_summary["question_label_calc"] = q_summary["question_percentile"].apply(label_from_percentile)

    wide = q_summary.pivot_table(
        index=["iso3", "country_name", "region", "income_group"],
        columns="question_id",
        values="question_percentile",
        aggfunc="mean",
    ).reset_index()

    for q in ["Q1", "Q2", "Q3", "Q5", "Q6"]:
        if q in wide.columns:
            wide[f"{q}_percentile"] = wide[q]
            wide[f"{q}_label"] = wide[q].apply(label_from_percentile)
            wide = wide.drop(columns=[q])

    q_cols = [c for c in wide.columns if c.endswith("_percentile")]
    wide["overall_country_profile_score"] = wide[q_cols].mean(axis=1, skipna=True)
    wide["overall_country_profile_rank"] = wide["overall_country_profile_score"].rank(ascending=False, method="min")
    wide["overall_country_profile_label"] = wide["overall_country_profile_score"].apply(label_from_percentile)

    def strengths(row):
        out = []
        for c in q_cols:
            if pd.notna(row[c]) and row[c] >= 0.75:
                out.append(c.replace("_percentile", ""))
        return ";".join(out)

    def weaknesses(row):
        out = []
        for c in q_cols:
            if pd.notna(row[c]) and row[c] <= 0.25:
                out.append(c.replace("_percentile", ""))
        return ";".join(out)

    wide["main_strengths"] = wide.apply(strengths, axis=1)
    wide["main_weaknesses"] = wide.apply(weaknesses, axis=1)
    wide["missingness_warnings"] = wide[q_cols].isna().sum(axis=1).astype(str) + "_missing_Q_dimensions"
    wide["recommended_use_in_phase8"] = wide["overall_country_profile_label"].map({
        "top_pioneer": "benchmark_case",
        "high_performer": "positive_comparator",
        "middle_performer": "context_case",
        "low_performer": "gap_case",
        "bottom_laggard": "warning_case",
        "not_ranked_missing": "do_not_use_without_caution",
    })

    CLUSTER_LABELS = {
        0: "Cluster 0: sin ley ni proyecto IA (soft-law / sin proyecto)",
        1: "Cluster 1: proyecto de ley IA en curso (pragmático)",
        2: "Cluster 2: ley IA vigente (regulado)",
        3: "Cluster 3: ley vigente + proyecto (regulación dual)",
    }
    Q4_SIN_DATOS_LABEL = "Sin legislación IA nacional específica detectada (regulación regional/delegada o sin datos IAPP)"

    if clusters is not None and not clusters.empty and "iso3" in clusters.columns:
        cluster_cols = [c for c in clusters.columns if c in {"iso3", "cluster_id", "cluster_label", "cluster_method", "cluster_hca", "cluster_kmeans"}]
        if cluster_cols:
            wide = wide.merge(clusters[cluster_cols].drop_duplicates("iso3"), on="iso3", how="left")

    if "cluster_kmeans" in wide.columns:
        wide["Q4_regulatory_profile"] = wide["cluster_kmeans"].map(CLUSTER_LABELS)
        wide["Q4_regulatory_label"] = wide["cluster_kmeans"].map({
            0: "sin_regulacion_ia",
            1: "proyecto_en_curso",
            2: "ley_vigente",
            3: "regulacion_dual",
        })
        mask_sin_datos = wide["Q4_regulatory_profile"].isna()
        wide.loc[mask_sin_datos, "Q4_regulatory_profile"] = Q4_SIN_DATOS_LABEL
        wide.loc[mask_sin_datos, "Q4_regulatory_label"] = "sin_legislacion_nacional_detectada"

    Q4_CLUSTER_COUNTS = {
        "Cluster 0 (soft-law/sin proyecto)": ["CAN","ISR","NZL","SGP"],
        "Cluster 1 (proyecto en curso)": ["ARG","AUS","BRA","CHL","COL","GBR","IND","TWN"],
        "Cluster 2 (ley vigente)": ["ARE","JPN","KOR","PER"],
        "Cluster 3 (regulación dual)": ["CHN","USA"],
    }
    count_total = sum(len(v) for v in Q4_CLUSTER_COUNTS.values())
    Q4_CLUSTER_COUNTS[Q4_SIN_DATOS_LABEL] = []

    for i, (_, row) in enumerate(wide.iterrows()):
        iso = row["iso3"]
        found = False
        for label, iso_list in Q4_CLUSTER_COUNTS.items():
            if iso in iso_list:
                found = True
                break
        if not found and pd.isna(row.get("Q4_regulatory_profile")):
            wide.at[wide.index[i], "Q4_regulatory_profile"] = Q4_SIN_DATOS_LABEL

    wide["Q4_data_source"] = wide["cluster_kmeans"].apply(
        lambda x: "IAPP_clustering" if pd.notna(x) else "corpus_regulatory_counts"
    )

    wide["overall_country_profile_score_is_descriptive"] = True
    wide["not_a_causal_or_predictive_index"] = True
    return wide
