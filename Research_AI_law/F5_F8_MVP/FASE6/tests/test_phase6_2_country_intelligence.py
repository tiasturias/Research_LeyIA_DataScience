"""Tests obligatorios para Fase 6.2 Country Intelligence Layer."""

from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
CI = ROOT / "FASE6" / "outputs" / "country_intelligence"


def test_country_intelligence_outputs_exist():
    required = [
        "country_q_profile_long.csv",
        "country_q_profile_wide.csv",
        "country_rankings_by_outcome.csv",
        "country_rankings_by_group.csv",
        "country_best_worst_by_q.csv",
        "country_model_contributions.csv",
        "country_residuals_and_gaps.csv",
        "country_cluster_profile.csv",
        "country_headline_flags.csv",
        "country_learning_patterns.csv",
        "country_graphics_catalog.csv",
        "phase6_2_country_intelligence_manifest.json",
    ]
    for fname in required:
        assert (CI / fname).exists(), fname


def test_country_profiles_include_chile_and_singapore():
    wide = pd.read_csv(CI / "country_q_profile_wide.csv")
    assert "CHL" in set(wide["iso3"])
    assert "SGP" in set(wide["iso3"])


def test_country_profile_semantics():
    long = pd.read_csv(CI / "country_q_profile_long.csv")
    assert "score_scope" in long.columns
    assert long["score_scope"].eq("in_sample_descriptive_positioning").all()
    assert "independent_prediction" in long.columns
    assert long["independent_prediction"].fillna(False).eq(False).all()
    assert "causal_claim" in long.columns
    assert long["causal_claim"].fillna(False).eq(False).all()


def test_rankings_have_questions():
    rankings = pd.read_csv(CI / "country_rankings_by_outcome.csv")
    assert set(["Q1", "Q2", "Q3", "Q5", "Q6"]).intersection(set(rankings["question_id"]))


def test_group_rankings_exist():
    group = pd.read_csv(CI / "country_rankings_by_group.csv")
    assert "group_name" in group.columns
    assert "rank_within_group" in group.columns


def test_manifest_no_causal_or_prediction_claims():
    manifest = json.loads((CI / "phase6_2_country_intelligence_manifest.json").read_text())
    assert manifest["holdout_used"] is False
    assert manifest["train_test_split_used"] is False
    assert manifest["external_validation_used"] is False
    assert manifest["independent_prediction"] is False
    assert manifest["causal_claim"] is False


def test_graphics_catalog_not_empty():
    catalog = pd.read_csv(CI / "country_graphics_catalog.csv")
    assert len(catalog) > 0


def test_preservation_of_original_fase6_outputs():
    fase6_outputs = ROOT / "FASE6" / "outputs"
    originals = [
        "fase6_manifest.json",
        "q1_results.csv",
        "q2_results.csv",
        "q2_scores_per_country.csv",
        "q3_results.csv",
        "q4_clusters.csv",
        "q4_distance_matrix.csv",
        "q5_results.csv",
        "q5_scores_per_country.csv",
        "q6_results.csv",
        "q6_scores_per_country.csv",
    ]
    for fname in originals:
        assert (fase6_outputs / fname).exists(), f"Fase 6 original output missing: {fname}"
