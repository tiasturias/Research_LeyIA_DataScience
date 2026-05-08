import pandas as pd
from pathlib import Path

FASE5_OUTPUTS = Path("FASE5/outputs")


def test_feature_matrix_has_no_split_column():
    if not (FASE5_OUTPUTS / "feature_matrix_mvp.csv").exists():
        return
    fm = pd.read_csv(FASE5_OUTPUTS / "feature_matrix_mvp.csv")
    forbidden = {"split", "train", "test", "holdout", "partition"}
    assert not forbidden.intersection(fm.columns)


def test_phase6_feature_matrix_has_no_split_column():
    if not (FASE5_OUTPUTS / "phase6_ready" / "phase6_feature_matrix.csv").exists():
        return
    fm = pd.read_csv(FASE5_OUTPUTS / "phase6_ready" / "phase6_feature_matrix.csv")
    forbidden = {"split", "train", "test", "holdout", "partition"}
    assert not forbidden.intersection(fm.columns)
