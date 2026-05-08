import pandas as pd
from pathlib import Path
OUTPUTS = Path(__file__).resolve().parents[1] / "outputs"

def test_q6_results():
    if not (OUTPUTS / "q6_results.csv").exists():
        return
    df = pd.read_csv(OUTPUTS / "q6_results.csv")
    assert "outcome" in df.columns
    assert "analysis_role" in df.columns
