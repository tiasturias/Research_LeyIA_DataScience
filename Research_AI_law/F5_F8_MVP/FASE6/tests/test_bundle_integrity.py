import pandas as pd
from pathlib import Path
FASE5_BUNDLE = Path(__file__).resolve().parents[2] / "FASE5" / "outputs" / "phase6_ready"

def test_feature_matrix_shape():
    fm = pd.read_csv(FASE5_BUNDLE / "phase6_feature_matrix.csv")
    assert fm.shape[0] == 43
