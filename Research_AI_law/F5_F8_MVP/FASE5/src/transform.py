"""Transformaciones preregistradas para Fase 5 MVP."""

from __future__ import annotations

import numpy as np
import pandas as pd

from _common.load import load_mvp_pipeline_config


def _signed_log1p(series: pd.Series) -> pd.Series:
    return np.sign(series) * np.log1p(series.abs())


def get_log_variables() -> list[str]:
    cfg = load_mvp_pipeline_config()
    return list(cfg["transformaciones"]["log_transform"]["variables"])


def apply_log_transforms(df: pd.DataFrame, candidate_vars: list[str]) -> pd.DataFrame:
    out = df.copy()
    new_cols = {}
    for var in [v for v in candidate_vars if v in get_log_variables() and v in out.columns]:
        if not pd.api.types.is_numeric_dtype(out[var]):
            continue
        s = out[var]
        if (s.dropna() < 0).any():
            new_cols[f"{var}_log"] = _signed_log1p(s)
        else:
            new_cols[f"{var}_log"] = np.log1p(s)
    if new_cols:
        out = pd.concat([out, pd.DataFrame(new_cols, index=out.index)], axis=1)
    return out


def apply_robust_zscore(df: pd.DataFrame, candidate_vars: list[str]) -> pd.DataFrame:
    out = df.copy()
    new_cols = {}
    numeric_cols = []
    for var in candidate_vars:
        if var in out.columns and pd.api.types.is_numeric_dtype(out[var]):
            numeric_cols.append(var)
        log_var = f"{var}_log"
        if log_var in out.columns and pd.api.types.is_numeric_dtype(out[log_var]):
            numeric_cols.append(log_var)

    for var in numeric_cols:
        s = out[var]
        med = s.median(skipna=True)
        mad = (s - med).abs().median(skipna=True)
        z_col = f"{var}_z"
        if pd.notna(mad) and mad > 0:
            new_cols[z_col] = (s - med) / mad
        else:
            new_cols[z_col] = pd.Series(np.where(s.notna(), 0.0, np.nan), index=out.index)
    if new_cols:
        out = pd.concat([out, pd.DataFrame(new_cols, index=out.index)], axis=1)
    return out.copy()


def compute_transform_params(df: pd.DataFrame, candidate_vars: list[str]) -> pd.DataFrame:
    rows = []
    for var in candidate_vars:
        log_col = f"{var}_log"
        if log_col in df.columns and var in df.columns:
            method = "signed_log1p" if (df[var].dropna() < 0).any() else "log1p"
            rows.append({
                "source_variable": var,
                "derived_variable": log_col,
                "transform": "log_transform",
                "method": method,
                "center_median": np.nan,
                "scale_mad": np.nan,
                "n_non_null": int(df[log_col].notna().sum()),
                "status": "ok",
            })
        for col in [var, f"{var}_log"]:
            if col not in df.columns or not pd.api.types.is_numeric_dtype(df[col]):
                continue
            s = df[col]
            med = s.median(skipna=True)
            mad = (s - med).abs().median(skipna=True)
            rows.append({
                "source_variable": col,
                "derived_variable": f"{col}_z",
                "transform": "robust_zscore",
                "method": "median_mad",
                "center_median": med,
                "scale_mad": mad,
                "n_non_null": int(s.notna().sum()),
                "status": "ok" if pd.notna(mad) and mad > 0 else "zero_mad_or_not_estimable",
            })
    return pd.DataFrame(rows)


def apply_transforms(df: pd.DataFrame, candidate_vars: list[str]) -> pd.DataFrame:
    with_logs = apply_log_transforms(df, candidate_vars)
    return apply_robust_zscore(with_logs, candidate_vars)
