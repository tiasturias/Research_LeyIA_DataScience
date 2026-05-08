from pathlib import Path
import yaml

CONTRACT = Path("FASE5/outputs/phase6_ready/phase6_modeling_contract.yaml")


def test_phase6_contract_no_holdout():
    if not CONTRACT.exists():
        return
    contract = yaml.safe_load(CONTRACT.read_text())
    assert contract["methodology"] == "inferential_comparative_observational"
    assert contract["primary_estimand"] == "adjusted_association"
    assert contract["sample_policy"]["n_primary_sample"] == 43
    assert contract["sample_policy"]["use_holdout_test_set"] is False
    assert contract["sample_policy"]["train_test_split_created"] is False
    assert contract["sample_policy"]["split_column_present"] is False
    assert contract["validation_policy"]["leave_group_out_is_external_test"] is False
    assert contract["contract"]["n_observed_core_variables"] == 46
