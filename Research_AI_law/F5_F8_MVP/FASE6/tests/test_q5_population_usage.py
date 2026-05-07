"""Test Q5 Uso población outputs."""


def test_q5_results_schema(q5_results):
    assert "question" in q5_results.columns
    assert (q5_results["question"] == "Q5").all()


def test_q5_has_3_y(q5_results):
    assert q5_results["y_var"].nunique() == 3


def test_q5_consistency(q5_consistency):
    assert len(q5_consistency) >= 1
    if "direction_summary" in q5_consistency.columns:
        valid = {"robust_negative", "robust_positive", "mixed", "null"}
        non_null = q5_consistency["direction_summary"].dropna()
        assert non_null.isin(valid).all()


def test_q5_predictions(q5_predictions):
    assert "p_high_population_usage" in q5_predictions.columns
    assert q5_predictions["p_high_population_usage"].between(0, 1).all()
