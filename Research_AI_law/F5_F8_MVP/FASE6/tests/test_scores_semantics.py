from pathlib import Path
import pandas as pd

FASE6_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = FASE6_ROOT / "outputs"


def test_country_scores_are_descriptive_not_independent_predictions():
    candidates = [
        "q2_scores_per_country.csv",
        "q5_scores_per_country.csv",
        "q6_scores_per_country.csv",
        "q2_predictions_per_country.csv",
        "q5_predictions_per_country.csv",
        "q6_predictions_per_country.csv",
    ]
    if not OUTPUTS.exists():
        return
    existing = [OUTPUTS / f for f in candidates if (OUTPUTS / f).exists()]
    assert existing, "Debe existir al menos un archivo de scores por país"
    for path in existing:
        df = pd.read_csv(path)
        assert "score_scope" in df.columns, path.name
        assert df["score_scope"].eq("in_sample_descriptive_positioning").all(), path.name
        assert "independent_prediction" in df.columns, path.name
        assert df["independent_prediction"].fillna(False).eq(False).all(), path.name
        assert "holdout_used" in df.columns, path.name
        assert df["holdout_used"].fillna(False).eq(False).all(), path.name
