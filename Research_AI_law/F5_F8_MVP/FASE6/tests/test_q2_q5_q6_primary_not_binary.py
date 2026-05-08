from pathlib import Path
import pandas as pd

FASE6_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = FASE6_ROOT / "outputs"


def _check_primary_not_binary(fname):
    path = OUTPUTS / fname
    if not path.exists():
        return
    df = pd.read_csv(path)
    assert "analysis_role" in df.columns
    primary = df[df["analysis_role"].astype(str).str.contains("primary", na=False)]
    assert not primary.empty, f"{fname} no tiene análisis primario"
    assert not primary["analysis_role"].astype(str).str.contains("binary_median", na=False).any(), fname
    if "primary_analysis" in df.columns:
        bad = df[(df["primary_analysis"] == True) & (df["analysis_role"].astype(str).str.contains("binary_median", na=False))]
        assert bad.empty, f"{fname} usa binario mediana como primario"


def test_q2_primary_is_continuous_or_fractional():
    _check_primary_not_binary("q2_results.csv")


def test_q5_primary_is_continuous_or_fractional():
    _check_primary_not_binary("q5_results.csv")


def test_q6_primary_is_continuous_or_score():
    _check_primary_not_binary("q6_results.csv")
