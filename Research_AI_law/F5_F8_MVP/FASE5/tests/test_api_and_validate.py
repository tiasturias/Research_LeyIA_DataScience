from __future__ import annotations

from FASE5.src.api import (
    load_coverage_report,
    load_feature_matrix,
    load_manifest,
    load_mvp_countries,
    load_mvp_variables_catalog,
    load_phase6_column_groups,
    load_phase6_feature_matrix,
    load_phase6_llm_context,
    load_phase6_modeling_contract,
    load_phase6_ready_manifest,
    load_phase6_schema,
    load_analysis_sample_membership,
    load_transform_params,
)
from FASE5.src.validate import validate_phase5


def test_phase5_public_api_loads_outputs(phase5_results):
    assert load_feature_matrix().shape[0] == 43
    assert load_coverage_report().shape[0] == 46
    assert load_mvp_countries().shape[0] == 43
    assert load_mvp_variables_catalog().shape[0] == 46
    assert not load_transform_params().empty
    assert load_analysis_sample_membership().shape[0] == 43
    assert load_manifest()["rules"]["no_imputation"] is True
    assert load_phase6_feature_matrix().shape == load_feature_matrix().shape
    assert load_phase6_schema().shape[0] == load_feature_matrix().shape[1]
    assert len(load_phase6_column_groups()["observed_core_40"]) == 40
    assert len(load_phase6_column_groups()["observed_core_46"]) == 46
    assert load_phase6_llm_context()["primary_dataset"] == "phase6_feature_matrix.csv"
    assert load_phase6_modeling_contract()["contract"]["no_imputation"] is True
    assert load_phase6_ready_manifest()["bundle_type"] == "phase6_ready_technical"


def test_phase5_validator_passes(phase5_results):
    assert validate_phase5() == [
        "outputs_exist",
        "data_contracts",
        "phase6_ready_contract",
        "excel_contract",
        "manifest_hashes",
    ]
