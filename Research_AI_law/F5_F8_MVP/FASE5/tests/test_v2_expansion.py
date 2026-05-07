"""Tests para expansion v2.0: 6 vars nuevas + Y_Q5/Q6 en contract."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import yaml


OUTPUTS = Path(__file__).resolve().parents[1] / "outputs"
PHASE6_READY = OUTPUTS / "phase6_ready"
NEW_VARS = [
    "oxford_e_government_delivery",
    "oxford_government_digital_policy",
    "oxford_ind_data_governance",
    "oxford_governance_ethics",
    "oecd_2_indigo_oecd_indigo_score",
    "oecd_4_digital_gov_oecd_digital_gov_overall",
]


def test_feature_matrix_46_vars(phase5_results):
    fm = pd.read_csv(OUTPUTS / "feature_matrix_mvp.csv")
    for var in NEW_VARS:
        assert var in fm.columns, f"Missing v2.0 var: {var}"
        assert f"{var}_z" in fm.columns, f"Missing v2.0 z-score: {var}_z"


def test_v1_vars_preserved_byte_for_byte(phase5_results):
    backup = OUTPUTS.parent / "outputs.v1.0.backup" / "feature_matrix_mvp.csv"
    if not backup.exists():
        return
    bk = pd.read_csv(backup)
    fm_v2 = pd.read_csv(OUTPUTS / "feature_matrix_mvp.csv")
    common_cols = [c for c in bk.columns if c in fm_v2.columns]
    pd.testing.assert_frame_equal(
        bk[common_cols].sort_values("iso3").reset_index(drop=True),
        fm_v2[common_cols].sort_values("iso3").reset_index(drop=True),
        check_exact=True,
    )


def test_modeling_contract_has_q5_q6(phase5_results):
    with open(PHASE6_READY / "phase6_modeling_contract.yaml", encoding="utf-8") as f:
        contract = yaml.safe_load(f)
    assert contract["version"] == "0.2"
    assert "Q5" in contract["questions"]
    assert "Q6" in contract["questions"]
    assert "Y_Q5_population_usage" in contract["variables_by_role"]
    assert "Y_Q6_public_sector" in contract["variables_by_role"]


def test_q6_primary_has_5_vars(phase5_results):
    with open(PHASE6_READY / "phase6_modeling_contract.yaml", encoding="utf-8") as f:
        contract = yaml.safe_load(f)
    assert len(contract["variables_by_role"]["Y_Q6_public_sector"]) == 5
    assert len(contract["variables_by_role"].get("Y_Q6_public_sector_aux", [])) == 1


def test_q5_has_3_vars(phase5_results):
    with open(PHASE6_READY / "phase6_modeling_contract.yaml", encoding="utf-8") as f:
        contract = yaml.safe_load(f)
    assert len(contract["variables_by_role"]["Y_Q5_population_usage"]) == 3


def test_no_imputation_in_feature_matrix(phase5_results):
    fm = pd.read_csv(OUTPUTS / "feature_matrix_mvp.csv")
    aux_var = "oecd_4_digital_gov_oecd_digital_gov_overall"
    n_null = fm[aux_var].isna().sum()
    assert n_null > 0, f"{aux_var} deberia conservar NaN; no debe estar imputada"


def test_overlap_y_variables_documented(phase5_results):
    with open(PHASE6_READY / "phase6_modeling_contract.yaml", encoding="utf-8") as f:
        contract = yaml.safe_load(f)
    overlap = contract.get("overlap_y_variables", {})
    assert "anthropic_usage_pct" in overlap
    assert set(overlap["anthropic_usage_pct"]) == {"Q2", "Q5"}
    assert "oxford_public_sector_adoption" in overlap
    assert set(overlap["oxford_public_sector_adoption"]) == {"Q2", "Q6"}


def test_no_pca_outputs_in_bundle(phase5_results):
    forbidden = list(PHASE6_READY.glob("*pca*"))
    assert len(forbidden) == 0, f"Archivos PCA inesperados: {forbidden}"
