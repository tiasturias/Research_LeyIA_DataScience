"""Test split integrity: 43 países, 34/9, CHL en train."""

import pandas as pd
from pathlib import Path

FASE5_BUNDLE = Path(__file__).resolve().parents[2] / "FASE5" / "outputs" / "phase6_ready"


def test_split_disjoint_and_complete():
    s = pd.read_csv(FASE5_BUNDLE / "phase6_train_test_split.csv")
    assert len(s) == 43
    assert s["iso3"].nunique() == 43
    assert set(s["split"].unique()) == {"train", "test"}
    counts = s["split"].value_counts().to_dict()
    assert counts["train"] == 34 and counts["test"] == 9
    assert "CHL" in s["iso3"].values
    chile_split = s[s["iso3"] == "CHL"]["split"].iloc[0]
    assert chile_split == "train"
