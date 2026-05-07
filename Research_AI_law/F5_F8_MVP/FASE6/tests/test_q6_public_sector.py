"""Test Q6 Sector público outputs."""


def test_q6_results_has_tier(q6_results):
    assert "tier" in q6_results.columns
    valid_tiers = {"primary", "auxiliary_low_n"}
    assert q6_results["tier"].isin(valid_tiers).all()


def test_q6_primary_has_5_y(q6_results):
    primary = q6_results[q6_results["tier"] == "primary"]
    assert primary["y_var"].nunique() == 5


def test_q6_auxiliary_present(q6_results):
    aux = q6_results[q6_results["tier"] == "auxiliary_low_n"]
    assert len(aux) > 0


def test_q6_consistency_primary_only(q6_consistency):
    if "tier" in q6_consistency.columns:
        assert (q6_consistency["tier"] == "primary").all()


def test_q6_predictions(q6_predictions):
    assert "p_high_public_sector_use" in q6_predictions.columns
    assert q6_predictions["p_high_public_sector_use"].between(0, 1).all()
