"""Feature engineering agregado y categórico para Fase 5 MVP."""

from __future__ import annotations

import numpy as np
import pandas as pd

from _common.load import load_binding_taxonomy_config


def _binary_presence(series: pd.Series) -> pd.Series:
    if pd.api.types.is_numeric_dtype(series):
        return series.fillna(0).astype(float).gt(0).astype(int)
    return series.notna().astype(int)


def build_regulatory_aggregates(raw_wide_mvp: pd.DataFrame, base: pd.DataFrame) -> pd.DataFrame:
    taxonomy = load_binding_taxonomy_config()
    out = base.copy()
    for kind in ("binding", "non_binding", "hybrid"):
        cols = [c for c in taxonomy.get(kind, []) if c in raw_wide_mvp.columns]
        if cols:
            flags = pd.DataFrame({c: _binary_presence(raw_wide_mvp[c]) for c in cols}, index=raw_wide_mvp.index)
            out[f"n_{kind}"] = flags.sum(axis=1).astype(int).values
            out[f"{kind}_variables_used"] = "|".join(cols)
        else:
            out[f"n_{kind}"] = 0
            out[f"{kind}_variables_used"] = ""
    den = (out["n_binding"] + out["n_non_binding"]).replace(0, np.nan)
    out["regulatory_intensity"] = (out["n_binding"] / den).fillna(0.0)
    out["n_regulatory_mechanisms"] = out["n_binding"] + out["n_non_binding"] + out["n_hybrid"]
    return out


def one_hot_categorical_regulatory(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in ["iapp_categoria_obligatoriedad", "iapp_modelo_gobernanza"]:
        if col not in out.columns:
            continue
        dummies = pd.get_dummies(out[col], prefix=col, dummy_na=False, dtype=int)
        if not dummies.empty:
            out = pd.concat([out, dummies], axis=1)
    return out


def build_feature_matrix(raw_wide_mvp: pd.DataFrame, curated: pd.DataFrame, transformed: pd.DataFrame) -> pd.DataFrame:
    with_aggregates = build_regulatory_aggregates(raw_wide_mvp, transformed)
    return one_hot_categorical_regulatory(with_aggregates)
