"""Curaduria a las variables observadas core del MVP."""

from __future__ import annotations

import pandas as pd

from _common.load import load_dictionary, load_mvp_variables_config
from .config import META_COLS


EXPECTED_MVP_VARIABLES = 44


def get_mvp_variable_rows() -> list[dict]:
    return list(load_mvp_variables_config()["variables"])


def get_mvp_variables() -> list[str]:
    return [row["variable_matriz"] for row in get_mvp_variable_rows()]


def validate_mvp_variables_exist(dictionary: pd.DataFrame | None = None) -> None:
    if dictionary is None:
        dictionary = load_dictionary()
    mvp_vars = get_mvp_variables()
    if len(mvp_vars) != EXPECTED_MVP_VARIABLES:
        raise ValueError(f"Se esperaban {EXPECTED_MVP_VARIABLES} variables MVP, hay {len(mvp_vars)}")
    duplicated = sorted({v for v in mvp_vars if mvp_vars.count(v) > 1})
    if duplicated:
        raise ValueError(f"Variables MVP duplicadas: {duplicated}")
    missing = sorted(set(mvp_vars) - set(dictionary["variable_matriz"]))
    if missing:
        raise ValueError(f"Variables MVP no existen en diccionario Fase 3: {missing}")


def filter_to_mvp_variables(wide_mvp: pd.DataFrame) -> pd.DataFrame:
    validate_mvp_variables_exist()
    mvp_vars = get_mvp_variables()
    cols = [c for c in META_COLS if c in wide_mvp.columns] + mvp_vars
    return wide_mvp[cols].copy()


def build_variable_catalog(dictionary: pd.DataFrame | None = None) -> pd.DataFrame:
    if dictionary is None:
        dictionary = load_dictionary()
    cfg = pd.DataFrame(get_mvp_variable_rows())
    meta_cols = [
        "variable_matriz",
        "source_id",
        "table_id",
        "tipo_matriz",
        "unit",
        "direction",
        "bloque_tematico",
        "pct_complete",
        "n_countries_available",
        "fase4_role",
        "known_limitations",
    ]
    meta = dictionary[[c for c in meta_cols if c in dictionary.columns]].copy()
    return cfg.merge(meta, on="variable_matriz", how="left", suffixes=("_mvp", "_fase3"))


def validate_coverage(wide_curated: pd.DataFrame, min_pct: float = 30.0) -> pd.DataFrame:
    rows = []
    n = len(wide_curated)
    for var in get_mvp_variables():
        n_non_null = int(wide_curated[var].notna().sum()) if var in wide_curated.columns else 0
        pct = n_non_null / n * 100 if n else 0
        rows.append({
            "variable_matriz": var,
            "n_total": n,
            "n_non_null": n_non_null,
            "n_missing": n - n_non_null,
            "pct_complete": round(pct, 2),
            "below_threshold": pct < min_pct,
        })
    return pd.DataFrame(rows)
