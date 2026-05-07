"""Test Q1 Inversión outputs."""

import numpy as np


def test_q1_results_schema(q1_results):
    expected_cols = {"question", "y_var", "model", "x_var", "coefficient", "n_effective", "seed"}
    assert expected_cols.issubset(q1_results.columns)


def test_q1_n_effective_per_y(q1_results):
    for y in q1_results["y_var"].unique():
        sub = q1_results[(q1_results["y_var"] == y) & (q1_results["model"] == "OLS_full")]
        if len(sub) > 0:
            n = sub["n_effective"].iloc[0]
            assert n >= 15 or sub["status"].iloc[0] == "insufficient_n"


def test_q1_bootstrap_ci_finite(q1_results):
    sub = q1_results[(q1_results["model"] == "OLS_full") & q1_results["ci95_lower"].notna()]
    assert sub["ci95_lower"].apply(np.isfinite).all()
    assert sub["ci95_upper"].apply(np.isfinite).all()


def test_q1_psm_status_valid(q1_psm_pairs):
    valid = {"ok", "exploratory_low_n", "insufficient_n"}
    assert q1_psm_pairs["status"].isin(valid).all()


def test_q1_consistency_direction_valid(q1_consistency):
    valid = {"robust_negative", "robust_positive", "mixed", "null"}
    assert q1_consistency["direction_summary"].isin(valid).all()


def test_q1_psm_balance_has_smd(q1_psm_balance):
    assert "smd_pre" in q1_psm_balance.columns
    assert "variable" in q1_psm_balance.columns
