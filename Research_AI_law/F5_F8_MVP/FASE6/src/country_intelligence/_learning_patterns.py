"""Patrones de aprendizaje, headline flags y análisis estratégico."""

import pandas as pd


def build_headline_flags(profile_wide: pd.DataFrame) -> pd.DataFrame:
    out = profile_wide[["iso3", "country_name"]].copy()
    q_cols = [c for c in profile_wide.columns if c.endswith("_percentile")]

    for q in ["Q1", "Q2", "Q3", "Q5", "Q6"]:
        col = f"{q}_percentile"
        if col in profile_wide.columns:
            out[f"is_top_5_{q.lower()}"] = profile_wide[col].rank(ascending=False, method="min") <= 5
            out[f"is_bottom_5_{q.lower()}"] = profile_wide[col].rank(ascending=True, method="min") <= 5

    out["is_consistent_pioneer"] = profile_wide[q_cols].ge(0.75).sum(axis=1) >= 3
    out["is_consistent_laggard"] = profile_wide[q_cols].le(0.25).sum(axis=1) >= 3
    out["is_chile_benchmark"] = profile_wide["iso3"].isin(["SGP", "EST", "IRL", "ARE", "KOR", "URY", "BRA"])
    out["is_latam_leader"] = False
    if "region" in profile_wide.columns:
        latam = profile_wide["region"].astype(str).str.contains("Latin", case=False, na=False)
        if latam.any():
            max_score = profile_wide.loc[latam, "overall_country_profile_score"].max()
            out["is_latam_leader"] = latam & profile_wide["overall_country_profile_score"].eq(max_score)

    out["headline_candidate"] = out[["is_consistent_pioneer", "is_consistent_laggard", "is_chile_benchmark", "is_latam_leader"]].any(axis=1)
    out["suggested_headline"] = out.apply(
        lambda r: "caso pionero consistente" if r["is_consistent_pioneer"] else (
            "caso rezagado para aprendizaje de errores" if r["is_consistent_laggard"] else (
                "benchmark relevante para Chile" if r["is_chile_benchmark"] else ""
            )
        ),
        axis=1
    )
    out["caution_note"] = "Descriptive flag; verify robustness in Fase 7."
    return out


def build_learning_patterns(profile_wide: pd.DataFrame, best_worst: pd.DataFrame) -> pd.DataFrame:
    rows = []

    pioneers = profile_wide[profile_wide["overall_country_profile_label"].isin(["top_pioneer", "high_performer"])]
    laggards = profile_wide[profile_wide["overall_country_profile_label"].isin(["bottom_laggard", "low_performer"])]

    rows.append({
        "pattern_id": "global_pioneer_pattern",
        "question_id": "Q_ALL",
        "group_name": "global_43",
        "pattern_type": "pioneer_pattern",
        "countries_in_pattern": ";".join(pioneers["iso3"].head(10).tolist()),
        "shared_strengths": "high percentiles across multiple Q dimensions",
        "shared_weaknesses": "must be assessed country-by-country",
        "regulatory_profile_summary": "see Q4 cluster profile",
        "ecosystem_profile_summary": "multi-dimensional high performance",
        "lesson_for_chile": "study institutional, adoption and public-sector capabilities of high performers before copying legal form",
        "risk_of_overinterpretation": "Do not infer causality from descriptive ranking.",
        "evidence_strength": "pre_robustness_descriptive",
        "recommended_phase8_use": "benchmark cases after Fase 7 validation",
    })

    rows.append({
        "pattern_id": "global_laggard_pattern",
        "question_id": "Q_ALL",
        "group_name": "global_43",
        "pattern_type": "laggard_pattern",
        "countries_in_pattern": ";".join(laggards["iso3"].head(10).tolist()),
        "shared_strengths": "",
        "shared_weaknesses": "low percentiles across multiple Q dimensions",
        "regulatory_profile_summary": "see Q4 cluster profile",
        "ecosystem_profile_summary": "multi-dimensional lower performance",
        "lesson_for_chile": "identify recurring capability gaps and avoid assuming law alone solves ecosystem weaknesses",
        "risk_of_overinterpretation": "Poor ranking may reflect missingness or structural factors outside regulation.",
        "evidence_strength": "pre_robustness_descriptive",
        "recommended_phase8_use": "warning cases after Fase 7 validation",
    })

    # Adoption without hard law pattern
    if "Q2_percentile" in profile_wide.columns and "Q4_regulatory_cluster" in profile_wide.columns:
        soft_law_high_adoption = profile_wide[
            (profile_wide["Q2_percentile"] >= 0.75) &
            (profile_wide["Q4_regulatory_cluster"].isin([0, 1]) if profile_wide["Q4_regulatory_cluster"].dtype != 'O' else False)
        ]
        if not soft_law_high_adoption.empty:
            rows.append({
                "pattern_id": "adoption_without_hard_law_pattern",
                "question_id": "Q2",
                "group_name": "global_43",
                "pattern_type": "adoption_without_hard_law_pattern",
                "countries_in_pattern": ";".join(soft_law_high_adoption["iso3"].head(5).tolist()),
                "shared_strengths": "high adoption with low binding regulatory intensity",
                "shared_weaknesses": "may lack formal AI-specific law",
                "regulatory_profile_summary": "soft law or project-stage",
                "ecosystem_profile_summary": "high adoption driven by digital infrastructure and private sector",
                "lesson_for_chile": "adoption high can be associated with digital capabilities and institutional quality, not only hard AI law",
                "risk_of_overinterpretation": "Do not infer causality; validate in Fase 7.",
                "evidence_strength": "pre_robustness_descriptive",
                "recommended_phase8_use": "benchmark for institutional-capability focus",
            })

    return pd.DataFrame(rows)
