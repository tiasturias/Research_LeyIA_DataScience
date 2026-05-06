"""Bloque C: Estadística univariada robusta para cada variable."""

from __future__ import annotations

import warnings

import numpy as np
import pandas as pd
from scipy import stats

from .config import OUTPUTS_DIR
from .load import get_variable_cols, load_dictionary, load_wide


def _mad(series: pd.Series) -> float:
    return float(np.median(np.abs(series.dropna() - series.dropna().median())))


def _robust_cv(series: pd.Series) -> float:
    med = series.dropna().median()
    mad = _mad(series)
    if med == 0:
        return np.nan
    return float(mad / abs(med))


def _count_iqr_outliers(series: pd.Series, k: float = 1.5) -> int:
    s = series.dropna()
    if len(s) < 4:
        return 0
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    return int(((s < q1 - k * iqr) | (s > q3 + k * iqr)).sum())


def _count_robust_z_outliers(series: pd.Series, threshold: float = 3.5) -> int:
    s = series.dropna()
    if len(s) < 4:
        return 0
    med = s.median()
    mad = _mad(s)
    if mad == 0:
        return 0
    z = (s - med).abs() / mad
    return int((z > threshold).sum())


def _normality_test(series: pd.Series) -> tuple[float, float, str]:
    s = series.dropna()
    n = len(s)
    if n < 8:
        return np.nan, np.nan, "insufficient_n"
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            if n < 5000:
                stat, p = stats.shapiro(s)
                test = "shapiro"
            else:
                result = stats.anderson(s, dist="norm")
                # Anderson-Darling: stat vs critical values at 5%
                stat = float(result.statistic)
                p = np.nan
                test = "anderson"
        return float(stat), float(p) if not np.isnan(p) else np.nan, test
    except Exception:
        return np.nan, np.nan, "error"


def compute_numeric_summary(
    wide: pd.DataFrame, dictionary: pd.DataFrame, min_n: int = 5
) -> pd.DataFrame:
    """Estadísticos robustos y clásicos para cada variable numérica."""
    d_num = dictionary[
        dictionary["tipo_matriz"].isin(["numeric", "score", "index", "count", "rank", "pct"])
    ]
    var_cols = set(d_num["variable_matriz"].tolist())
    cols = [c for c in wide.columns if c in var_cols and pd.api.types.is_numeric_dtype(wide[c])]

    records = []
    for col in cols:
        s = wide[col]
        s_clean = s.dropna()
        n = len(s_clean)
        n_miss = int(s.isna().sum())
        row_d = d_num[d_num["variable_matriz"] == col]

        if n < min_n:
            records.append({
                "variable_matriz": col,
                "bloque_tematico": row_d["bloque_tematico"].iloc[0] if len(row_d) else "",
                "source_id": row_d["source_id"].iloc[0] if len(row_d) else "",
                "unit": row_d["unit"].iloc[0] if len(row_d) else "",
                "direction": row_d["direction"].iloc[0] if len(row_d) else "",
                "n": n, "n_missing": n_miss,
                "pct_complete": round(n / len(wide) * 100, 2),
                "status": "insufficient_data",
            })
            continue

        percs = np.nanpercentile(s_clean, [1, 5, 10, 25, 75, 90, 95, 99])
        norm_stat, norm_p, norm_test = _normality_test(s_clean)

        records.append({
            "variable_matriz": col,
            "bloque_tematico": row_d["bloque_tematico"].iloc[0] if len(row_d) else "",
            "source_id": row_d["source_id"].iloc[0] if len(row_d) else "",
            "unit": row_d["unit"].iloc[0] if len(row_d) else "",
            "direction": row_d["direction"].iloc[0] if len(row_d) else "",
            "is_primary": row_d["is_primary"].iloc[0] if len(row_d) else None,
            "n": n,
            "n_missing": n_miss,
            "pct_complete": round(n / len(wide) * 100, 2),
            "mean": round(float(s_clean.mean()), 6),
            "median": round(float(s_clean.median()), 6),
            "std": round(float(s_clean.std()), 6),
            "mad": round(_mad(s_clean), 6),
            "min": round(float(s_clean.min()), 6),
            "p01": round(float(percs[0]), 6),
            "p05": round(float(percs[1]), 6),
            "p10": round(float(percs[2]), 6),
            "p25": round(float(percs[3]), 6),
            "p75": round(float(percs[4]), 6),
            "p90": round(float(percs[5]), 6),
            "p95": round(float(percs[6]), 6),
            "p99": round(float(percs[7]), 6),
            "max": round(float(s_clean.max()), 6),
            "iqr": round(float(percs[4] - percs[3]), 6),
            "cv_robust": round(_robust_cv(s_clean), 4),
            "skewness": round(float(stats.skew(s_clean)), 4),
            "kurtosis": round(float(stats.kurtosis(s_clean)), 4),
            "n_zero": int((s_clean == 0).sum()),
            "n_negative": int((s_clean < 0).sum()),
            "n_outliers_iqr_1_5": _count_iqr_outliers(s_clean, 1.5),
            "n_outliers_iqr_3_0": _count_iqr_outliers(s_clean, 3.0),
            "n_outliers_z_robust": _count_robust_z_outliers(s_clean),
            "normality_test": norm_test,
            "normality_stat": round(norm_stat, 4) if not np.isnan(norm_stat) else np.nan,
            "normality_p": round(norm_p, 6) if not np.isnan(norm_p) else np.nan,
            "suggest_log_transform": abs(float(stats.skew(s_clean))) > 2.0,
            "status": "ok",
        })

    return pd.DataFrame(records)


def compute_outlier_list(
    wide: pd.DataFrame, dictionary: pd.DataFrame, k: float = 3.0
) -> pd.DataFrame:
    """Lista pais-variable con outliers extremos (IQR × k)."""
    d_num = dictionary[dictionary["tipo_matriz"].isin(["numeric", "score", "index", "count", "rank", "pct"])]
    var_cols = set(d_num["variable_matriz"].tolist())
    cols = [c for c in wide.columns if c in var_cols and pd.api.types.is_numeric_dtype(wide[c])]

    records = []
    for col in cols:
        s = wide[col]
        s_clean = s.dropna()
        if len(s_clean) < 4:
            continue
        q1, q3 = s_clean.quantile(0.25), s_clean.quantile(0.75)
        iqr = q3 - q1
        low, high = q1 - k * iqr, q3 + k * iqr
        outlier_mask = (s < low) | (s > high)
        if not outlier_mask.any():
            continue
        row_d = d_num[d_num["variable_matriz"] == col]
        block = row_d["bloque_tematico"].iloc[0] if len(row_d) else ""
        for idx in wide.index[outlier_mask & s.notna()]:
            val = float(s.iloc[idx])
            records.append({
                "iso3": wide["iso3"].iloc[idx],
                "country_name_canonical": wide["country_name_canonical"].iloc[idx],
                "variable_matriz": col,
                "bloque_tematico": block,
                "value": round(val, 6),
                "q1": round(float(q1), 6),
                "q3": round(float(q3), 6),
                "iqr": round(float(iqr), 6),
                "lower_fence": round(float(low), 6),
                "upper_fence": round(float(high), 6),
                "direction": "above" if val > high else "below",
                "iqr_k": k,
            })
    if not records:
        return pd.DataFrame(columns=[
            "iso3", "country_name_canonical", "variable_matriz", "bloque_tematico",
            "value", "q1", "q3", "iqr", "lower_fence", "upper_fence",
            "direction", "iqr_k",
        ])
    return pd.DataFrame(records).sort_values(["variable_matriz", "direction"]).reset_index(drop=True)


def compute_categorical_summary(
    wide: pd.DataFrame, dictionary: pd.DataFrame
) -> pd.DataFrame:
    """Distribución de variables categóricas y binarias."""
    d_cat = dictionary[dictionary["tipo_matriz"].isin(["binary", "categorical", "text"])]
    cat_cols = [c for c in wide.columns if c in d_cat["variable_matriz"].values]

    records = []
    for col in cat_cols:
        s = wide[col].dropna().astype(str)
        n = len(s)
        if n == 0:
            continue
        vc = s.value_counts()
        row_d = d_cat[d_cat["variable_matriz"] == col]
        records.append({
            "variable_matriz": col,
            "bloque_tematico": row_d["bloque_tematico"].iloc[0] if len(row_d) else "",
            "source_id": row_d["source_id"].iloc[0] if len(row_d) else "",
            "unit": row_d["unit"].iloc[0] if len(row_d) else "",
            "n_non_null": n,
            "n_missing": len(wide) - n,
            "pct_complete": round(n / len(wide) * 100, 2),
            "n_categories": len(vc),
            "modal_category": str(vc.index[0]),
            "modal_freq": int(vc.iloc[0]),
            "modal_pct": round(vc.iloc[0] / n * 100, 2),
            "n_rare_categories_lt5pct": int((vc / n < 0.05).sum()),
            "top3_categories": " | ".join(vc.index[:3].tolist()),
        })
    if not records:
        return pd.DataFrame(columns=[
            "variable_matriz", "bloque_tematico", "source_id", "unit", "n_non_null",
            "n_missing", "pct_complete", "n_categories", "modal_category",
            "modal_freq", "modal_pct", "n_rare_categories_lt5pct", "top3_categories",
        ])
    return pd.DataFrame(records)


def compute_numeric_distributions(variable_summary: pd.DataFrame) -> pd.DataFrame:
    """Tabla compacta de distribuciones numéricas para reporte y Fase 5."""
    if variable_summary.empty:
        return pd.DataFrame(columns=[
            "variable_matriz", "bloque_tematico", "n", "pct_complete", "mean",
            "median", "std", "mad", "min", "p05", "p25", "p75", "p95",
            "max", "iqr", "skewness", "kurtosis", "suggest_log_transform",
        ])
    cols = [
        "variable_matriz", "bloque_tematico", "n", "pct_complete", "mean",
        "median", "std", "mad", "min", "p05", "p25", "p75", "p95",
        "max", "iqr", "skewness", "kurtosis", "suggest_log_transform",
    ]
    existing = [c for c in cols if c in variable_summary.columns]
    return variable_summary[existing].copy()


def run_univariate_analysis(
    wide: pd.DataFrame | None = None,
    dictionary: pd.DataFrame | None = None,
    save: bool = True,
) -> dict[str, pd.DataFrame]:
    if wide is None:
        wide = load_wide()
    if dictionary is None:
        dictionary = load_dictionary()

    variable_summary = compute_numeric_summary(wide, dictionary)
    results = {
        "eda_variable_summary": variable_summary,
        "eda_numeric_distributions": compute_numeric_distributions(variable_summary),
        "eda_outliers": compute_outlier_list(wide, dictionary),
        "eda_categorical_distributions": compute_categorical_summary(wide, dictionary),
    }

    if save:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        for name, df in results.items():
            df.to_csv(OUTPUTS_DIR / f"{name}.csv", index=False)

    return results
