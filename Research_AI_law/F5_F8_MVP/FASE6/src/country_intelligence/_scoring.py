"""Funciones de scoring, percentiles, rankings y etiquetado interpretativo."""

import pandas as pd
import numpy as np


def percentile_rank(series: pd.Series, higher_is_better: bool = True) -> pd.Series:
    s = pd.to_numeric(series, errors="coerce")
    if higher_is_better:
        return s.rank(pct=True, method="average")
    return 1 - s.rank(pct=True, method="average")


def descending_rank(series: pd.Series, higher_is_better: bool = True) -> pd.Series:
    s = pd.to_numeric(series, errors="coerce")
    return s.rank(ascending=not higher_is_better, method="min")


def zscore(series: pd.Series) -> pd.Series:
    s = pd.to_numeric(series, errors="coerce")
    if s.std(skipna=True) == 0 or pd.isna(s.std(skipna=True)):
        return pd.Series([pd.NA] * len(s), index=s.index)
    return (s - s.mean(skipna=True)) / s.std(skipna=True)


def label_from_percentile(p):
    if pd.isna(p):
        return "not_ranked_missing"
    if p >= 0.90:
        return "top_pioneer"
    if p >= 0.75:
        return "high_performer"
    if p >= 0.40:
        return "middle_performer"
    if p >= 0.20:
        return "low_performer"
    return "bottom_laggard"


def strength_weakness_label(p):
    if pd.isna(p):
        return "missing"
    if p >= 0.75:
        return "strength"
    if p <= 0.25:
        return "weakness"
    return "neutral"
