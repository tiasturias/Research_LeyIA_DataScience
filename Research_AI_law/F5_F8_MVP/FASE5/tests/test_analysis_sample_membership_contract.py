import pandas as pd
from pathlib import Path

FASE5_OUTPUTS = Path("FASE5/outputs")


def test_analysis_sample_membership_contract():
    if not (FASE5_OUTPUTS / "analysis_sample_membership.csv").exists():
        return
    m = pd.read_csv(FASE5_OUTPUTS / "analysis_sample_membership.csv")
    assert len(m) == 43
    assert m["iso3"].nunique() == 43
    assert "CHL" in set(m["iso3"])
    assert m["is_primary_analysis_sample"].all()
    assert m.loc[m["iso3"].eq("CHL"), "is_chile_focal"].iloc[0] in [True, 1]

    forbidden = {"split", "train", "test", "holdout", "partition"}
    assert not forbidden.intersection(m.columns)
