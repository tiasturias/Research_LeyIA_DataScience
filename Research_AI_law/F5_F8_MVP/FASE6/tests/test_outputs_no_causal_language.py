"""Test outputs no causal language: prohibir palabras causales en columnas."""

import pandas as pd
from pathlib import Path

OUTPUTS = Path(__file__).resolve().parents[1] / "outputs"


def test_no_causal_words_in_csv_columns():
    forbidden = ["causes", "produces", "impact", "causa", "produce"]
    for csv_path in sorted(OUTPUTS.glob("*.csv")):
        df = pd.read_csv(csv_path, nrows=5)
        for col in df.columns:
            for word in forbidden:
                assert word.lower() not in col.lower(), \
                    f"{csv_path.name}.{col} contains forbidden word '{word}'"
