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
    NON_ESTIMABLE_STATUSES = {
        "zero_mad_or_not_estimable",
        "constant_or_quasi_constant",
        "insufficient_non_missing_values",
        "source_missing",
    }
    
    for var in candidate_vars:
        log_col = f"{var}_log"
        if log_col in df.columns and var in df.columns:
            s_raw = df[var].dropna()
            s_log = df[log_col].dropna()
            
            if len(s_raw) == 0:
                status = "source_missing"
            elif len(s_raw) < 5:
                status = "insufficient_non_missing_values"
            elif s_raw.nunique() <= 1:
                status = "constant_or_quasi_constant"
            else:
                status = "ok"
                
            used = status not in NON_ESTIMABLE_STATUSES
            ex_reason = "Derived feature is non-estimable or unstable; preserve raw variable and exclude derived column from primary models." if not used else ""

            method = "signed_log1p" if (s_raw < 0).any() else "log1p"
            rows.append({
                "variable_original": var,
                "variable_derived": log_col,
                "transform_type": "log_transform",
                "method": method,
                "n_non_missing": int(len(s_log)),
                "median": s_log.median() if len(s_log) > 0 else np.nan,
                "mad": (s_log - s_log.median()).abs().median() if len(s_log) > 0 else np.nan,
                "mean": s_log.mean() if len(s_log) > 0 else np.nan,
                "std": s_log.std() if len(s_log) > 0 else np.nan,
                "min": s_log.min() if len(s_log) > 0 else np.nan,
                "max": s_log.max() if len(s_log) > 0 else np.nan,
                "status": status,
                "used_in_primary_modeling": used,
                "exclusion_reason": ex_reason,
                "notes": "",
            })
            
        for col in [var, f"{var}_log"]:
            if col not in df.columns or not pd.api.types.is_numeric_dtype(df[col]):
                continue
            s = df[col].dropna()
            
            med = s.median() if len(s) > 0 else np.nan
            mad = (s - med).abs().median() if len(s) > 0 else np.nan
            
            if len(s) == 0:
                status = "source_missing"
            elif len(s) < 5:
                status = "insufficient_non_missing_values"
            elif s.nunique() <= 1:
                status = "constant_or_quasi_constant"
            elif pd.isna(mad) or mad == 0:
                status = "zero_mad_or_not_estimable"
            else:
                status = "ok"

            used = status not in NON_ESTIMABLE_STATUSES
            ex_reason = "Derived feature is non-estimable or unstable; preserve raw variable and exclude derived column from primary models." if not used else ""

            rows.append({
                "variable_original": col,
                "variable_derived": f"{col}_z",
                "transform_type": "robust_zscore",
                "method": "median_mad",
                "n_non_missing": int(len(s)),
                "median": med,
                "mad": mad,
                "mean": s.mean() if len(s) > 0 else np.nan,
                "std": s.std() if len(s) > 0 else np.nan,
                "min": s.min() if len(s) > 0 else np.nan,
                "max": s.max() if len(s) > 0 else np.nan,
                "status": status,
                "used_in_primary_modeling": used,
                "exclusion_reason": ex_reason,
                "notes": "",
            })
            
    return pd.DataFrame(rows)


def apply_transforms(df: pd.DataFrame, candidate_vars: list[str]) -> pd.DataFrame:
    with_logs = apply_log_transforms(df, candidate_vars)
    return apply_robust_zscore(with_logs, candidate_vars)
