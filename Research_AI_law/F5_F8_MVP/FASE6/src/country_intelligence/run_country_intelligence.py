"""Orquestador principal de Fase 6.2 Country Intelligence Layer."""

from pathlib import Path
import json
import pandas as pd
import yaml
from datetime import datetime, timezone

from ._load import ROOT, FASE5_BUNDLE, FASE6_OUTPUTS, CI_OUTPUTS, validate_preflight
from ._groups import build_group_membership
from ._rankings import rank_outcome, build_rankings_by_group, build_best_worst_by_q
from ._profiles import build_country_q_profile_long, build_country_q_profile_wide
from ._contributions import build_country_model_contributions
from ._residuals import build_country_residuals_and_gaps
from ._learning_patterns import build_headline_flags, build_learning_patterns
from ._graphics import build_graphics
from ._country_cards import write_country_card_data


OUTCOMES_BY_Q = {
    "Q1": [
        "oxford_ind_company_investment_emerging_tech",
        "oxford_ind_ai_unicorns_log",
        "oxford_ind_vc_availability",
        "wipo_c_vencapdeal_score",
    ],
    "Q2": [
        "ms_h2_2025_ai_diffusion_pct",
        "oecd_5_ict_business_oecd_biz_ai_pct",
        "anthropic_usage_pct",
        "oxford_public_sector_adoption",
        "oxford_ind_adoption_emerging_tech",
    ],
    "Q3": [
        "oxford_total_score",
        "wipo_out_score",
        "stanford_fig_6_3_5_volume_of_publications",
        "stanford_fig_6_3_4_ai_patent_count",
    ],
    "Q5": [
        "anthropic_usage_pct",
        "anthropic_collaboration_pct",
        "oxford_ind_adoption_emerging_tech",
    ],
    "Q6": [
        "oxford_public_sector_adoption",
        "oxford_e_government_delivery",
        "oxford_government_digital_policy",
        "oxford_ind_data_governance",
        "oxford_governance_ethics",
        "oecd_2_indigo_oecd_indigo_score",
        "oecd_4_digital_gov_oecd_digital_gov_overall",
    ],
}

QUESTION_LABELS = {
    "Q1": "Inversión",
    "Q2": "Adopción",
    "Q3": "Innovación",
    "Q4": "Perfil regulatorio",
    "Q5": "Uso poblacional",
    "Q6": "Sector público",
}


def load_config():
    path = ROOT / "FASE6" / "config" / "phase6_2_country_intelligence.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_phase6_results():
    files = {
        "Q1": "q1_results.csv",
        "Q2": "q2_results.csv",
        "Q3": "q3_results.csv",
        "Q5": "q5_results.csv",
        "Q6": "q6_results.csv",
    }
    out = {}
    for q, fname in files.items():
        path = FASE6_OUTPUTS / fname
        if path.exists():
            out[q] = pd.read_csv(path)
    return out


def main():
    CI_OUTPUTS.mkdir(parents=True, exist_ok=True)
    (CI_OUTPUTS / "figures").mkdir(parents=True, exist_ok=True)

    preflight = validate_preflight()
    preflight.to_csv(CI_OUTPUTS / "phase6_2_quality_checks.csv", index=False)
    if ((preflight["status"] == "FAIL") & (preflight["severity"] == "P0")).any():
        raise RuntimeError("Fase 6.2 abortada por fallas P0 en pre-flight.")

    config = load_config()
    fm = pd.read_csv(FASE5_BUNDLE / "phase6_feature_matrix.csv")
    membership = pd.read_csv(FASE5_BUNDLE / "phase6_analysis_sample_membership.csv")
    clusters = pd.read_csv(FASE6_OUTPUTS / "q4_clusters.csv") if (FASE6_OUTPUTS / "q4_clusters.csv").exists() else pd.DataFrame()
    phase6_results = load_phase6_results()

    # Enriquecer fm con region e income_group desde membership
    if "region" not in fm.columns and "region" in membership.columns:
        fm = fm.merge(membership[["iso3", "region"]], on="iso3", how="left")
    if "income_group" not in fm.columns and "income_group" in membership.columns:
        fm = fm.merge(membership[["iso3", "income_group"]], on="iso3", how="left")

    # Construir rankings por outcomes observados en feature matrix.
    ranking_frames = []
    for q, outcomes in OUTCOMES_BY_Q.items():
        for outcome in outcomes:
            if outcome in fm.columns:
                ranking_frames.append(rank_outcome(
                    df=fm,
                    outcome=outcome,
                    question_id=q,
                    question_label=QUESTION_LABELS.get(q, q),
                    higher_is_better=True,
                ))
    rankings = pd.concat(ranking_frames, ignore_index=True) if ranking_frames else pd.DataFrame()
    rankings.to_csv(CI_OUTPUTS / "country_rankings_by_outcome.csv", index=False)

    group_membership = build_group_membership(membership, config)
    rankings_group = build_rankings_by_group(rankings, group_membership) if not rankings.empty else pd.DataFrame()
    rankings_group.to_csv(CI_OUTPUTS / "country_rankings_by_group.csv", index=False)

    best_worst = build_best_worst_by_q(rankings, rankings_group) if not rankings.empty else pd.DataFrame()
    best_worst.to_csv(CI_OUTPUTS / "country_best_worst_by_q.csv", index=False)

    profile_long = build_country_q_profile_long(rankings) if not rankings.empty else pd.DataFrame()
    profile_long.to_csv(CI_OUTPUTS / "country_q_profile_long.csv", index=False)

    profile_wide = build_country_q_profile_wide(profile_long, clusters=clusters) if not profile_long.empty else pd.DataFrame()
    profile_wide.to_csv(CI_OUTPUTS / "country_q_profile_wide.csv", index=False)

    contributions = build_country_model_contributions(fm, phase6_results)
    contributions.to_csv(CI_OUTPUTS / "country_model_contributions.csv", index=False)

    residuals = build_country_residuals_and_gaps(fm, OUTCOMES_BY_Q)
    residuals.to_csv(CI_OUTPUTS / "country_residuals_and_gaps.csv", index=False)

    cluster_profile = clusters.copy()
    if not cluster_profile.empty:
        cluster_profile["score_scope"] = "descriptive_regulatory_typology"
        cluster_profile["independent_prediction"] = False
        cluster_profile["causal_claim"] = False
    cluster_profile.to_csv(CI_OUTPUTS / "country_cluster_profile.csv", index=False)

    headline_flags = build_headline_flags(profile_wide) if not profile_wide.empty else pd.DataFrame()
    headline_flags.to_csv(CI_OUTPUTS / "country_headline_flags.csv", index=False)

    learning = build_learning_patterns(profile_wide, best_worst) if not profile_wide.empty else pd.DataFrame()
    learning.to_csv(CI_OUTPUTS / "country_learning_patterns.csv", index=False)

    # Comparaciones de pares: Chile vs benchmarks.
    pairs = []
    if not profile_wide.empty:
        chile = profile_wide[profile_wide["iso3"] == "CHL"]
        for iso in config.get("country_groups", {}).get("chile_priority_benchmarks", []):
            other = profile_wide[profile_wide["iso3"] == iso]
            if not chile.empty and not other.empty:
                for c in [col for col in profile_wide.columns if col.endswith("_percentile")]:
                    pairs.append({
                        "country_a": "CHL",
                        "country_b": iso,
                        "dimension": c.replace("_percentile", ""),
                        "country_a_percentile": chile[c].iloc[0],
                        "country_b_percentile": other[c].iloc[0],
                        "gap_b_minus_a": other[c].iloc[0] - chile[c].iloc[0],
                        "interpretation": "positive gap means benchmark above Chile",
                    })
    pd.DataFrame(pairs).to_csv(CI_OUTPUTS / "country_comparison_pairs.csv", index=False)

    figures = build_graphics(rankings, profile_wide, residuals, CI_OUTPUTS / "figures") if not profile_wide.empty else pd.DataFrame()
    figures.to_csv(CI_OUTPUTS / "country_graphics_catalog.csv", index=False)

    written_cards = write_country_card_data(
        profile_wide=profile_wide,
        profile_long=profile_long,
        rankings_group=rankings_group,
        contributions=contributions,
        residuals=residuals,
        outdir=CI_OUTPUTS,
    )

    manifest = {
        "fase6_2_version": "2.2",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "module": "country_intelligence_layer",
        "methodology": "inferential_comparative_observational",
        "scope": "descriptive_country_level_positioning",
        "holdout_used": False,
        "train_test_split_used": False,
        "external_validation_used": False,
        "independent_prediction": False,
        "causal_claim": False,
        "preserved_existing_fase6_outputs": True,
        "outputs": {
            "country_q_profile_long.csv": "country_question_outcome_long_profile",
            "country_q_profile_wide.csv": "one_row_per_country_summary",
            "country_rankings_by_outcome.csv": "global_rankings_by_outcome",
            "country_rankings_by_group.csv": "subsample_group_rankings",
            "country_best_worst_by_q.csv": "top_bottom_by_question",
            "country_model_contributions.csv": "descriptive_model_term_contributions",
            "country_residuals_and_gaps.csv": "observed_vs_fitted_and_gaps",
            "country_cluster_profile.csv": "q4_regulatory_profile",
            "country_headline_flags.csv": "narrative_candidate_flags",
            "country_learning_patterns.csv": "lessons_from_pioneers_and_laggards",
            "country_graphics_catalog.csv": "generated_figures_catalog",
        },
        "key_country_cards_written": written_cards,
        "n_countries_profiled": int(profile_wide["iso3"].nunique()) if not profile_wide.empty else 0,
        "n_figures": int(len(figures)) if not figures.empty else 0,
    }
    (CI_OUTPUTS / "phase6_2_country_intelligence_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    return manifest


if __name__ == "__main__":
    main()
