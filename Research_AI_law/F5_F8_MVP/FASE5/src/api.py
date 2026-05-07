"""API publica para consumir artefactos de Fase 5 v2.0 desde Fases 6-8."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import yaml

from _common.paths import FASE5_OUTPUTS, FASE5_PHASE6_READY
from .build import build_phase5


def output_path(filename: str) -> Path:
    return FASE5_OUTPUTS / filename


def phase6_ready_path(filename: str) -> Path:
    return FASE5_PHASE6_READY / filename


def load_feature_matrix() -> pd.DataFrame:
    """Carga la matriz tecnica canonica v2.0: 43 paises x 138 columnas."""
    return pd.read_csv(output_path("feature_matrix_mvp.csv"))


def load_coverage_report() -> pd.DataFrame:
    return pd.read_csv(output_path("coverage_report_mvp.csv"))


def load_mvp_countries() -> pd.DataFrame:
    return pd.read_csv(output_path("mvp_countries.csv"))


def load_mvp_variables_catalog() -> pd.DataFrame:
    """Carga el catalogo de 46 variables observadas reales, incluyendo las 6 v2.0."""
    return pd.read_csv(output_path("mvp_variables_catalog.csv"))


def load_transform_params() -> pd.DataFrame:
    return pd.read_csv(output_path("mvp_transform_params.csv"))


def load_train_test_split() -> pd.DataFrame:
    return pd.read_csv(output_path("mvp_train_test_split.csv"))


def load_manifest() -> dict:
    """Carga el manifiesto Fase 5 v2.0 con hashes de entradas y outputs."""
    return json.loads(output_path("fase5_manifest.json").read_text(encoding="utf-8"))


def load_phase6_feature_matrix() -> pd.DataFrame:
    """Carga la copia tecnica que Fase 6 debe usar como input principal."""
    return pd.read_csv(phase6_ready_path("phase6_feature_matrix.csv"))


def load_phase6_schema() -> pd.DataFrame:
    return pd.read_csv(phase6_ready_path("phase6_schema.csv"))


def load_phase6_column_groups() -> dict:
    """Carga grupos de columnas, incluyendo observed_core_40 y observed_core_46."""
    return yaml.safe_load(phase6_ready_path("phase6_column_groups.yaml").read_text(encoding="utf-8"))


def load_phase6_modeling_contract() -> dict:
    """Carga el contrato v0.2 con mapeos Q1-Q6, Q5/Q6 y solapes Y."""
    return yaml.safe_load(phase6_ready_path("phase6_modeling_contract.yaml").read_text(encoding="utf-8"))


def load_phase6_ready_manifest() -> dict:
    """Carga el manifiesto del bundle phase6_ready v0.2."""
    return json.loads(phase6_ready_path("phase6_ready_manifest.json").read_text(encoding="utf-8"))


def load_phase6_llm_context() -> dict:
    return json.loads(phase6_ready_path("phase6_llm_context.json").read_text(encoding="utf-8"))


__all__ = [
    "build_phase5",
    "load_coverage_report",
    "load_feature_matrix",
    "load_manifest",
    "load_mvp_countries",
    "load_mvp_variables_catalog",
    "load_phase6_column_groups",
    "load_phase6_feature_matrix",
    "load_phase6_modeling_contract",
    "load_phase6_llm_context",
    "load_phase6_ready_manifest",
    "load_phase6_schema",
    "load_train_test_split",
    "load_transform_params",
    "output_path",
    "phase6_ready_path",
]
