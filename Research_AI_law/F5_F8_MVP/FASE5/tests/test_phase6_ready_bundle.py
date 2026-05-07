from __future__ import annotations

import json

import pandas as pd
import yaml

from _common.paths import FASE5_OUTPUTS, FASE5_PHASE6_READY
from FASE5.src.api import (
    load_phase6_column_groups,
    load_phase6_feature_matrix,
    load_phase6_llm_context,
    load_phase6_modeling_contract,
    load_phase6_ready_manifest,
    load_phase6_schema,
)
from FASE5.src.validate import EXPECTED_PHASE6_READY_OUTPUTS


def test_phase6_ready_outputs_exist(phase5_results):
    for filename in EXPECTED_PHASE6_READY_OUTPUTS:
        path = FASE5_PHASE6_READY / filename
        assert path.exists(), filename
        assert path.stat().st_size > 0, filename


def test_phase6_feature_matrix_mirrors_canonical_feature_matrix(phase5_results):
    canonical = pd.read_csv(FASE5_OUTPUTS / "feature_matrix_mvp.csv")
    phase6 = pd.read_csv(FASE5_PHASE6_READY / "phase6_feature_matrix.csv")

    assert phase6.shape == canonical.shape
    assert list(phase6.columns) == list(canonical.columns)
    assert phase6["iso3"].tolist() == canonical["iso3"].tolist()


def test_phase6_schema_and_column_groups_contract(phase5_results):
    schema = load_phase6_schema()
    groups = load_phase6_column_groups()
    feature_matrix = load_phase6_feature_matrix()

    assert schema.shape[0] == feature_matrix.shape[1]
    assert len(groups["observed_core_40"]) == 40
    assert len(groups["observed_core_46"]) == 46
    assert len(groups["observed_core_v2_added"]) == 6
    assert set(groups["observed_categorical"]) == {
        "iapp_categoria_obligatoriedad",
        "iapp_modelo_gobernanza",
    }
    assert len(groups["candidate_numeric_model_features"]) > 0
    assert "split" in groups["split_cols"]


def test_phase6_modeling_contract_is_machine_readable(phase5_results):
    contract = load_phase6_modeling_contract()
    llm_context = load_phase6_llm_context()

    assert contract["contract"]["grain"] == "country_iso3"
    assert contract["contract"]["primary_key"] == "iso3"
    assert contract["contract"]["n_rows"] == 43
    assert contract["contract"]["n_columns"] >= 138
    assert contract["contract"]["n_observed_core_variables"] == 46
    assert contract["contract"]["no_imputation"] is True
    assert "Q1" in contract["questions"]
    assert "Q5" in contract["questions"]
    assert "Q6" in contract["questions"]
    assert "X1_regulatory" in contract["variables_by_role"]
    assert "Y_Q5_population_usage" in contract["variables_by_role"]
    assert "Y_Q6_public_sector" in contract["variables_by_role"]
    assert llm_context["hard_rules"]["human_audit_excel_is_not_model_input"] is True


def test_phase6_manifest_hashes_bundle_files(phase5_results):
    manifest = load_phase6_ready_manifest()

    assert manifest["bundle_type"] == "phase6_ready_technical"
    assert set(manifest["files"]) == set(EXPECTED_PHASE6_READY_OUTPUTS) - {"phase6_ready_manifest.json"}
    raw_manifest = json.loads((FASE5_PHASE6_READY / "phase6_ready_manifest.json").read_text(encoding="utf-8"))
    yaml.safe_load((FASE5_PHASE6_READY / "phase6_column_groups.yaml").read_text(encoding="utf-8"))
    assert raw_manifest["rules"]["human_audit_excel_excluded"] is True
