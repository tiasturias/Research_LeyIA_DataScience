"""Validacion reproducible de contratos de Fase 5 MVP."""

from __future__ import annotations

import hashlib
import json

import pandas as pd
import yaml
from openpyxl import load_workbook

from _common.paths import FASE5_OUTPUTS, FASE5_PHASE6_READY, MVP_ROOT
from .api import (
    load_coverage_report,
    load_feature_matrix,
    load_manifest,
    load_mvp_countries,
    load_mvp_variables_catalog,
    load_train_test_split,
    load_transform_params,
)


EXPECTED_OUTPUTS = [
    "feature_matrix_mvp.csv",
    "coverage_report_mvp.csv",
    "mvp_countries.csv",
    "mvp_variables_catalog.csv",
    "mvp_transform_params.csv",
    "mvp_train_test_split.csv",
    "MVP_AUDITABLE.xlsx",
    "fase5_manifest.json",
]

EXPECTED_PHASE6_READY_OUTPUTS = [
    "phase6_feature_matrix.csv",
    "phase6_schema.csv",
    "phase6_schema.json",
    "phase6_column_groups.yaml",
    "phase6_modeling_contract.yaml",
    "phase6_missingness_by_column.csv",
    "phase6_missingness_by_country.csv",
    "phase6_variables_catalog.csv",
    "phase6_transform_params.csv",
    "phase6_train_test_split.csv",
    "phase6_llm_context.json",
    "phase6_ready_manifest.json",
]

EXPECTED_EXCEL_SHEETS = [
    "0_Leer_Primero",
    "1_Hipotesis",
    "2_Como_Auditar",
    "3_Paises_43",
    "4_Ingreso_Region",
    "5_Variables_40",
    "5b_Variables_46_Detalle",
    "6_Matriz_40_Humana",
    "7_Leyenda_Colores",
    "8_Casos_Atencion",
    "9_Normalizacion",
    "10_Cobertura",
    "11_Features_Fase6",
    "11b_Features_Fase6_v2",
    "12_Diccionario_Cols",
    "13_Trazabilidad",
    "14_Transformaciones",
]


def _sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_phase5() -> list[str]:
    checks: list[str] = []
    for filename in EXPECTED_OUTPUTS:
        path = FASE5_OUTPUTS / filename
        if not path.exists() or path.stat().st_size == 0:
            raise AssertionError(f"Output faltante o vacio: {path}")
    for filename in EXPECTED_PHASE6_READY_OUTPUTS:
        path = FASE5_PHASE6_READY / filename
        if not path.exists() or path.stat().st_size == 0:
            raise AssertionError(f"Output tecnico Fase 6 faltante o vacio: {path}")
    checks.append("outputs_exist")

    feature_matrix = load_feature_matrix()
    coverage = load_coverage_report()
    countries = load_mvp_countries()
    variables_catalog = load_mvp_variables_catalog()
    transform_params = load_transform_params()
    split = load_train_test_split()
    manifest = load_manifest()

    assert feature_matrix.shape[0] == 43
    assert feature_matrix["iso3"].is_unique
    assert countries.shape[0] == 43
    assert variables_catalog.shape[0] == 46
    assert coverage.shape[0] == 46
    assert not coverage["below_threshold"].any()
    assert coverage["pct_complete"].ge(30.0).all()
    assert set(split["split"]) == {"train", "test"}
    assert split.shape[0] == 43
    assert "log_transform" in set(transform_params["transform"])
    assert "robust_zscore" in set(transform_params["transform"])
    assert not any(col.endswith("_transform_method") for col in feature_matrix.columns)
    checks.append("data_contracts")

    # The technical bundle intentionally mirrors the canonical Fase 5 feature matrix.
    phase6_feature_matrix = pd.read_csv(FASE5_PHASE6_READY / "phase6_feature_matrix.csv")
    phase6_schema = pd.read_csv(FASE5_PHASE6_READY / "phase6_schema.csv")
    phase6_missing_cols = pd.read_csv(FASE5_PHASE6_READY / "phase6_missingness_by_column.csv")
    phase6_missing_rows = pd.read_csv(FASE5_PHASE6_READY / "phase6_missingness_by_country.csv")
    column_groups = yaml.safe_load((FASE5_PHASE6_READY / "phase6_column_groups.yaml").read_text(encoding="utf-8"))
    modeling_contract = yaml.safe_load((FASE5_PHASE6_READY / "phase6_modeling_contract.yaml").read_text(encoding="utf-8"))
    phase6_manifest = json.loads((FASE5_PHASE6_READY / "phase6_ready_manifest.json").read_text(encoding="utf-8"))

    assert phase6_feature_matrix.shape == feature_matrix.shape
    assert list(phase6_feature_matrix.columns) == list(feature_matrix.columns)
    assert phase6_schema.shape[0] == feature_matrix.shape[1]
    assert phase6_missing_cols.shape[0] == feature_matrix.shape[1]
    assert phase6_missing_rows.shape[0] == feature_matrix.shape[0]
    assert len(column_groups["observed_core_40"]) == 40
    assert len(column_groups["observed_core_46"]) == 46
    assert len(column_groups["observed_core_v2_added"]) == 6
    assert len(column_groups["candidate_numeric_model_features"]) > 0
    assert modeling_contract["contract"]["no_imputation"] is True
    assert modeling_contract["contract"]["phase6_should_not_recompute_phase5"] is True
    for name, metadata in phase6_manifest["files"].items():
        path = FASE5_PHASE6_READY / metadata["path"]
        assert path.exists(), name
        assert _sha256_file(path) == metadata["sha256"], name
    checks.append("phase6_ready_contract")

    workbook = load_workbook(FASE5_OUTPUTS / "MVP_AUDITABLE.xlsx", read_only=True)
    assert workbook.sheetnames == EXPECTED_EXCEL_SHEETS
    assert workbook["1_Hipotesis"].max_row == 16
    assert workbook["5_Variables_40"].max_row == 47
    assert workbook["5b_Variables_46_Detalle"].max_row == 7
    assert workbook["6_Matriz_40_Humana"].max_row == 44
    assert workbook["6_Matriz_40_Humana"].max_column == 50
    assert workbook["9_Normalizacion"].max_row >= 12
    assert workbook["11_Features_Fase6"].max_row == 44
    assert workbook["11_Features_Fase6"].max_column >= 138
    assert workbook["11b_Features_Fase6_v2"].max_row == 44
    assert workbook["11b_Features_Fase6_v2"].max_column >= 138
    assert workbook["12_Diccionario_Cols"].max_row >= 139
    checks.append("excel_contract")

    assert manifest["rules"]["phase3_phase4_immutable"] is True
    assert manifest["rules"]["no_imputation"] is True
    assert manifest["phase5_implementation_hashed"]
    for name, metadata in manifest["outputs_hashed"].items():
        path = MVP_ROOT / metadata["path"]
        assert path.exists(), name
        assert _sha256_file(path) == metadata["sha256"], name
    for rel_path, metadata in manifest["phase5_implementation_hashed"].items():
        path = MVP_ROOT / rel_path
        assert path.exists(), rel_path
        assert _sha256_file(path) == metadata["sha256"], rel_path
    for rel_path, metadata in manifest["inputs_hashed"].items():
        path = MVP_ROOT.parent / rel_path
        assert path.exists(), rel_path
        assert _sha256_file(path) == metadata["sha256"], rel_path
    checks.append("manifest_hashes")

    return checks


def main() -> None:
    checks = validate_phase5()
    print("Fase 5 MVP validation completed")
    for check in checks:
        print(f"- {check}: OK")


if __name__ == "__main__":
    main()
