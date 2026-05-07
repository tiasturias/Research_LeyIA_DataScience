"""Wrappers API-only sobre Fase 3 y Fase 4.

El codigo de Fase 5 no lee CSVs de Fase 3/4 para construir features. Las
lecturas directas quedan reservadas para trazabilidad/auditoria en Excel.
"""

from __future__ import annotations

import importlib.util
import sys
from functools import lru_cache
from pathlib import Path

import pandas as pd
import yaml

from .paths import FASE3_ROOT, FASE4_ROOT, FASE5_CONFIG


def _load_module_from_file(module_name: str, path: Path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"No se pudo cargar modulo desde {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


for p in (FASE3_ROOT, FASE3_ROOT / "src", FASE4_ROOT / "src"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

try:
    from src.fase3.api import (  # type: ignore  # noqa: E402
        current_version as _fase3_version,
        load_dictionary as _load_dictionary,
        load_wide as _load_wide,
    )
except ModuleNotFoundError:
    _fase3_api = _load_module_from_file("_fase3_api_for_mvp", FASE3_ROOT / "src" / "fase3" / "api.py")
    _load_wide = _fase3_api.load_wide
    _load_dictionary = _fase3_api.load_dictionary
    _fase3_version = _fase3_api.current_version

try:
    from fase4.api import (  # type: ignore  # noqa: E402
        load_candidates,
        load_eda_results,
        load_question_mapping,
        load_redundancy_report,
        load_submuestras,
        load_taxonomy,
    )
except ModuleNotFoundError:
    _fase4_api = _load_module_from_file("_fase4_api_for_mvp", FASE4_ROOT / "src" / "fase4" / "api.py")
    load_candidates = _fase4_api.load_candidates
    load_eda_results = _fase4_api.load_eda_results
    load_question_mapping = _fase4_api.load_question_mapping
    load_redundancy_report = _fase4_api.load_redundancy_report
    load_submuestras = _fase4_api.load_submuestras
    load_taxonomy = _fase4_api.load_taxonomy


@lru_cache(maxsize=1)
def load_wide() -> pd.DataFrame:
    return _load_wide()


@lru_cache(maxsize=1)
def load_dictionary() -> pd.DataFrame:
    return _load_dictionary()


def fase3_version() -> str:
    return str(_fase3_version())


def load_yaml_config(name: str) -> dict:
    with open(FASE5_CONFIG / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_mvp_sample_config() -> dict:
    return load_yaml_config("mvp_sample.yaml")


def load_mvp_variables_config() -> dict:
    return load_yaml_config("mvp_variables.yaml")


def load_mvp_pipeline_config() -> dict:
    return load_yaml_config("mvp_pipeline.yaml")


def load_fase4_decisions() -> dict:
    path = FASE4_ROOT / "outputs" / "eda_principal" / "eda_decisions_for_fase5.yaml"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_binding_taxonomy_config() -> dict:
    path = FASE4_ROOT / "config" / "fase4" / "binding_taxonomy.yaml"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)
