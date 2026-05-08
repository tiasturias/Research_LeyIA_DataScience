import pandas as pd
from pathlib import Path

TRANSFORMS = Path("FASE5/outputs/mvp_transform_params.csv")


def test_non_estimable_transforms_flagged():
    if not TRANSFORMS.exists():
        return
    t = pd.read_csv(TRANSFORMS)
    required_cols = {"status", "used_in_primary_modeling", "exclusion_reason"}
    assert required_cols.issubset(t.columns)

    mask = t["status"].isin([
        "zero_mad_or_not_estimable",
        "constant_or_quasi_constant",
        "insufficient_non_missing_values",
        "source_missing",
    ])
    if mask.any():
        assert (t.loc[mask, "used_in_primary_modeling"] == False).all()
        assert t.loc[mask, "exclusion_reason"].notna().all()
