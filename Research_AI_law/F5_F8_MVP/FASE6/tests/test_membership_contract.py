from pathlib import Path
import pandas as pd

FASE6_ROOT = Path(__file__).resolve().parents[1]
MVP_ROOT = FASE6_ROOT.parents[0]
FASE5_BUNDLE = MVP_ROOT / "FASE5" / "outputs" / "phase6_ready"


def test_membership_exists_and_has_43_primary_countries():
    path = FASE5_BUNDLE / "phase6_analysis_sample_membership.csv"
    assert path.exists()
    m = pd.read_csv(path)
    assert len(m) == 43
    assert m["iso3"].nunique() == 43
    assert m["is_primary_analysis_sample"].fillna(False).all()
    forbidden = {"split", "train", "test", "holdout"}
    assert not forbidden.intersection(set(c.lower() for c in m.columns))
