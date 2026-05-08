import pandas as pd
from pathlib import Path
OUTPUTS = Path(__file__).resolve().parents[1] / "outputs"

def test_no_causal_words_in_csv_columns():
    if not OUTPUTS.exists():
        return
    for p in OUTPUTS.glob("*.csv"):
        df = pd.read_csv(p)
        for col in df.columns:
            if col == 'causal_claim':
                assert df[col].dropna().astype(str).str.lower().isin(['false', '0']).all()
            else:
                assert 'causal' not in str(col).lower()
