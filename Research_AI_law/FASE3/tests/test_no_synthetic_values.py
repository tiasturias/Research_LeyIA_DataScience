from pathlib import Path


def test_source_files_exist_for_panel(panel):
    root = Path(__file__).resolve().parents[2]
    missing = sorted({p for p in panel["source_file"].unique() if not (root / p).exists()})
    assert not missing


def test_values_are_observed_not_empty(panel):
    assert panel["value_original"].astype(str).str.len().gt(0).all()
    assert ~(panel["value_numeric"].isna() & panel["value_text"].isna()).any()
    assert set(panel["confidence_level"]).issubset({"verified", "extracted", "inferred", "missing_explicit", "missing_no_data"})
