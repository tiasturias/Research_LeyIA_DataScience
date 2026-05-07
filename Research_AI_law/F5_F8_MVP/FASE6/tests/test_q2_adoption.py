"""Test Q2 Adopción outputs."""


def test_q2_results_schema(q2_results):
    assert "question" in q2_results.columns
    assert "y_var" in q2_results.columns
    assert "model" in q2_results.columns
    assert (q2_results["question"] == "Q2").all()


def test_q2_has_logistic_and_rf(q2_results):
    models = q2_results["model"].unique()
    assert "Logistic" in models
    assert "RandomForest" in models


def test_q2_predictions_per_country(q2_predictions):
    assert "iso3" in q2_predictions.columns
    assert "p_high_adoption" in q2_predictions.columns
    assert q2_predictions["p_high_adoption"].between(0, 1).all()
