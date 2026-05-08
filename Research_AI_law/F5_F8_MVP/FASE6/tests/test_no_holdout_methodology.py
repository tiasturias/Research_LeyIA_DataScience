from pathlib import Path
import pandas as pd
import yaml

FASE6_ROOT = Path(__file__).resolve().parents[1]
MVP_ROOT = FASE6_ROOT.parents[0]
FASE5_BUNDLE = MVP_ROOT / "FASE5" / "outputs" / "phase6_ready"
OUTPUTS = FASE6_ROOT / "outputs"


def test_no_split_artifacts_in_bundle():
    assert not (FASE5_BUNDLE / "phase6_train_test_split.csv").exists()
    fm = pd.read_csv(FASE5_BUNDLE / "phase6_feature_matrix.csv")
    assert "split" not in fm.columns


def test_contract_declares_no_holdout():
    contract = yaml.safe_load((FASE5_BUNDLE / "phase6_modeling_contract.yaml").read_text())
    assert contract["methodology"] == "inferential_comparative_observational"
    assert contract["sample_policy"]["use_holdout_test_set"] is False
    assert contract["sample_policy"]["train_test_split_created"] is False
    assert contract["sample_policy"]["split_column_present"] is False


def test_outputs_do_not_use_holdout():
    for fname in ["q1_results.csv", "q2_results.csv", "q3_results.csv", "q5_results.csv", "q6_results.csv"]:
        path = OUTPUTS / fname
        if not path.exists():
            continue
        df = pd.read_csv(path)
        assert "holdout_used" in df.columns, fname
        assert df["holdout_used"].fillna(False).eq(False).all(), fname
        assert "split" not in df.columns, fname
