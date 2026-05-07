"""Test Q3 Innovación outputs."""


def test_q3_results_has_tier(q3_results):
    assert "tier" in q3_results.columns
    valid_tiers = {"primary", "auxiliary_low_n"}
    assert q3_results["tier"].isin(valid_tiers).all()


def test_q3_primary_has_multiple_y(q3_results):
    primary = q3_results[q3_results["tier"] == "primary"]
    assert primary["y_var"].nunique() >= 5


def test_q3_consistency(q3_consistency):
    assert "tier" in q3_consistency.columns
    assert "direction_summary" not in q3_consistency.columns or \
           q3_consistency.get("direction_summary", pd.Series()).isin(
               {"robust_negative", "robust_positive", "mixed", "null", float("nan")}
           ).all()
