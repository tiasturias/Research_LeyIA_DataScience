"""Wrapper sobre src.fase3.api con cache en memoria y validaciones de contrato."""

from __future__ import annotations

import importlib.util
import sys
from functools import lru_cache
from pathlib import Path

import pandas as pd

# Asegurar que FASE3 está en el path. En ejecución desde FASE4, el paquete
# ``src`` de Fase 4 puede ocultar ``src.fase3``; por eso mantenemos un fallback
# al paquete instalable ``fase3`` sin leer CSVs directamente.
_FASE3 = Path(__file__).resolve().parents[3] / "FASE3"
_FASE3_SRC = _FASE3 / "src"
for _path in (str(_FASE3), str(_FASE3_SRC)):
    if _path not in sys.path:
        sys.path.insert(0, _path)

try:  # layout documentado en el plan
    from src.fase3.api import (  # type: ignore  # noqa: E402
        get_block as _get_block,
        get_chile_snapshot as _get_chile_snapshot,
        load_dictionary as _load_dictionary,
        load_panel as _load_panel,
        load_snapshot as _load_snapshot,
        load_wide as _load_wide,
        list_versions as _list_versions,
        current_version as _current_version,
    )
except ModuleNotFoundError:  # layout local cuando FASE4 se ejecuta como src.fase4
    _api_path = _FASE3_SRC / "fase3" / "api.py"
    _spec = importlib.util.spec_from_file_location("_fase3_public_api_for_fase4", _api_path)
    if _spec is None or _spec.loader is None:
        raise
    _fase3_api = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_fase3_api)
    _get_block = _fase3_api.get_block
    _get_chile_snapshot = _fase3_api.get_chile_snapshot
    _load_dictionary = _fase3_api.load_dictionary
    _load_panel = _fase3_api.load_panel
    _load_snapshot = _fase3_api.load_snapshot
    _load_wide = _fase3_api.load_wide
    _list_versions = _fase3_api.list_versions
    _current_version = _fase3_api.current_version

from .config import AUX_SUFFIXES, BLOCKS, META_COLS  # noqa: E402


@lru_cache(maxsize=1)
def load_wide() -> pd.DataFrame:
    """Carga la Matriz Madre wide desde Fase 3. Resultado en caché."""
    return _load_wide()


@lru_cache(maxsize=1)
def load_panel() -> pd.DataFrame:
    return _load_panel()


@lru_cache(maxsize=1)
def load_snapshot() -> pd.DataFrame:
    return _load_snapshot()


@lru_cache(maxsize=1)
def load_dictionary() -> pd.DataFrame:
    return _load_dictionary()


def get_block(block: str) -> pd.DataFrame:
    if block not in BLOCKS:
        raise ValueError(f"Bloque desconocido: {block}. Bloques válidos: {BLOCKS}")
    return _get_block(block)


@lru_cache(maxsize=1)
def get_chile_snapshot() -> pd.DataFrame:
    return _get_chile_snapshot()


def list_versions() -> list[str]:
    return _list_versions()


def current_version() -> str:
    return _current_version()


def get_variable_cols(wide: pd.DataFrame, dictionary: pd.DataFrame) -> list[str]:
    """Retorna columnas que son variables analíticas (no meta, no aux)."""
    var_names = set(dictionary["variable_matriz"].tolist())
    return [c for c in wide.columns if c in var_names]


def get_meta_cols(wide: pd.DataFrame) -> list[str]:
    return [c for c in META_COLS if c in wide.columns]


def get_numeric_var_cols(wide: pd.DataFrame, dictionary: pd.DataFrame) -> list[str]:
    """Variables analíticas de tipo numérico (no binario, no categórico, no texto)."""
    d = dictionary[dictionary["tipo_matriz"].isin(["numeric", "score", "index", "count", "rank"])]
    valid = set(d["variable_matriz"].tolist())
    all_var = get_variable_cols(wide, dictionary)
    numeric_cols = [c for c in all_var if c in valid]
    # Filtro adicional: la columna debe ser numérica en el DataFrame
    numeric_cols = [c for c in numeric_cols if pd.api.types.is_numeric_dtype(wide[c])]
    return numeric_cols


def get_block_var_cols(block: str, wide: pd.DataFrame, dictionary: pd.DataFrame) -> list[str]:
    """Variables de un bloque que existen en wide."""
    d = dictionary[dictionary["bloque_tematico"] == block]
    block_vars = set(d["variable_matriz"].tolist())
    return [c for c in wide.columns if c in block_vars]
