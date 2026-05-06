"""Bloque E+F: Correlaciones Spearman/Pearson/Kendall, redundancia, inter-bloque con FDR."""

from __future__ import annotations

import warnings
from itertools import combinations

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.metrics import mutual_info_score

from .config import BLOCKS, OUTPUTS_DIR
from .load import get_block_var_cols, get_variable_cols, load_dictionary, load_wide


def _fdr_bh(pvalues: np.ndarray, alpha: float = 0.05) -> np.ndarray:
    """Benjamini-Hochberg FDR correction. Returns adjusted p-values."""
    n = len(pvalues)
    if n == 0:
        return pvalues
    pvalues = np.nan_to_num(pvalues.astype(float), nan=1.0, posinf=1.0, neginf=1.0)
    order = np.argsort(pvalues)
    ranked = np.empty(n)
    ranked[order] = np.arange(1, n + 1)
    adjusted = np.minimum(1.0, pvalues * n / ranked)
    # Enforce monotonicity (from right to left)
    for i in range(n - 2, -1, -1):
        adjusted[order[i]] = min(adjusted[order[i]], adjusted[order[i + 1]])
    return adjusted


def compute_pairwise_correlations(
    wide: pd.DataFrame,
    cols: list[str],
    min_n: int = 10,
    method: str = "spearman",
) -> pd.DataFrame:
    """Matriz de correlaciones pairwise para las columnas dadas."""
    data = wide[cols].apply(pd.to_numeric, errors="coerce")
    if data.shape[1] < 2:
        return pd.DataFrame(columns=["var_a", "var_b", "method", "rho", "pvalue_raw", "n_pairs"])
    corr = data.corr(method=method, min_periods=min_n)
    counts = data.notna().astype(int).T.dot(data.notna().astype(int))
    records = []
    for i, c1 in enumerate(cols[:-1]):
        for c2 in cols[i + 1:]:
            r = corr.loc[c1, c2]
            n = int(counts.loc[c1, c2])
            if n < min_n or pd.isna(r):
                continue
            r = float(max(min(r, 0.999999), -0.999999))
            if method in {"spearman", "pearson"} and n > 2:
                t = abs(r) * np.sqrt((n - 2) / max(1e-12, 1 - r * r))
                p = 2 * stats.t.sf(t, df=n - 2)
            elif method == "kendall" and n > 3:
                z = abs(r) / np.sqrt((2 * (2 * n + 5)) / (9 * n * (n - 1)))
                p = 2 * stats.norm.sf(z)
            else:
                p = 1.0
            records.append({
                "var_a": c1, "var_b": c2,
                "method": method, "rho": round(float(r), 4),
                "pvalue_raw": round(float(p), 6), "n_pairs": n,
            })
    return pd.DataFrame(records)

    # Slow exact fallback retained for reference if the vectorized path is
    # changed in the future.
    for c1, c2 in combinations(cols, 2):
        sub = wide[[c1, c2]].dropna()
        n = len(sub)
        if n < min_n:
            continue
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                if method == "spearman":
                    r, p = stats.spearmanr(sub[c1], sub[c2])
                elif method == "pearson":
                    r, p = stats.pearsonr(sub[c1], sub[c2])
                elif method == "kendall":
                    r, p = stats.kendalltau(sub[c1], sub[c2])
                else:
                    raise ValueError(f"Unknown method: {method}")
        except Exception:
            continue
        if np.isnan(r) or np.isnan(p):
            continue
        records.append({
            "var_a": c1, "var_b": c2,
            "method": method, "rho": round(float(r), 4),
            "pvalue_raw": round(float(p), 6), "n_pairs": n,
        })
    return pd.DataFrame(records)


def apply_fdr_holm(df: pd.DataFrame, alpha: float = 0.05) -> pd.DataFrame:
    """Añade columnas pvalue_fdr y pvalue_holm al DataFrame de correlaciones."""
    if df.empty or "pvalue_raw" not in df.columns:
        return df
    df = df.copy()
    pvals = np.nan_to_num(df["pvalue_raw"].astype(float).values, nan=1.0, posinf=1.0, neginf=1.0)
    df["pvalue_fdr"] = _fdr_bh(pvals, alpha).round(6)

    # Holm-Bonferroni
    n = len(pvals)
    order = np.argsort(pvals)
    holm = pvals.copy()
    for i, idx in enumerate(order):
        holm[idx] = min(1.0, pvals[idx] * (n - i))
    # Enforce monotonicity
    prev = 0.0
    for idx in order:
        holm[idx] = max(holm[idx], prev)
        prev = holm[idx]
    df["pvalue_holm"] = holm.round(6)

    df["survives_fdr_05"] = (df["pvalue_fdr"] < alpha)
    df["survives_holm_05"] = (df["pvalue_holm"] < alpha)
    df["significance"] = df.apply(
        lambda r: "survives_fdr_and_holm"
        if r["survives_fdr_05"] and r["survives_holm_05"]
        else ("survives_fdr_only" if r["survives_fdr_05"]
              else ("nominal_p05" if r["pvalue_raw"] < 0.05
                    else "not_significant")), axis=1
    )
    return df


def compute_mutual_information(
    wide: pd.DataFrame,
    cols: list[str],
    pairs: list[tuple[str, str]] | None = None,
    min_n: int = 15,
    n_bins: int = 8,
) -> pd.DataFrame:
    """Mutual information exploratoria usando discretización por cuantiles.

    Fase 4 solo la usa como señal no lineal descriptiva; no es modelo ni prueba
    de hipótesis.
    """
    records = []
    pair_iter = pairs if pairs is not None else list(combinations(cols, 2))
    for c1, c2 in pair_iter:
        sub = wide[[c1, c2]].dropna()
        n = len(sub)
        if n < min_n:
            continue
        if sub[c1].nunique() < 2 or sub[c2].nunique() < 2:
            continue
        try:
            x = pd.qcut(sub[c1], q=min(n_bins, sub[c1].nunique()), duplicates="drop").cat.codes
            y = pd.qcut(sub[c2], q=min(n_bins, sub[c2].nunique()), duplicates="drop").cat.codes
            mi = mutual_info_score(x, y)
        except Exception:
            continue
        records.append({
            "var_a": c1,
            "var_b": c2,
            "method": "mutual_information_quantile",
            "mi": round(float(mi), 6),
            "n_pairs": n,
            "n_bins": n_bins,
        })
    return pd.DataFrame(records).sort_values("mi", ascending=False).reset_index(drop=True) if records else pd.DataFrame(
        columns=["var_a", "var_b", "method", "mi", "n_pairs", "n_bins"]
    )


def compute_vif_diagnostics(wide: pd.DataFrame, dictionary: pd.DataFrame) -> pd.DataFrame:
    """VIF preliminar dentro de bloques de control, limitado a variables con buena cobertura."""
    try:
        from statsmodels.stats.outliers_influence import variance_inflation_factor
    except Exception:
        return pd.DataFrame([{
            "bloque_tematico": "all", "variable_matriz": "statsmodels_unavailable",
            "vif": np.nan, "n_obs": 0, "status": "dependency_unavailable",
        }])

    records = []
    for block in ["socioeconomic_control", "institutional_control", "tech_infrastructure_control"]:
        cols = get_block_var_cols(block, wide, dictionary)
        cols = [c for c in cols if pd.api.types.is_numeric_dtype(wide[c]) and wide[c].notna().mean() >= 0.70]
        # Mantener el diagnóstico liviano y estable.
        cols = cols[:12]
        if len(cols) < 2:
            continue
        x = wide[cols].dropna()
        if len(x) < max(20, len(cols) + 2):
            continue
        x = (x - x.mean()) / x.std(ddof=0).replace(0, np.nan)
        x = x.dropna(axis=1)
        if x.shape[1] < 2:
            continue
        for i, col in enumerate(x.columns):
            try:
                vif = float(variance_inflation_factor(x.values, i))
            except Exception:
                vif = np.nan
            records.append({
                "bloque_tematico": block,
                "variable_matriz": col,
                "vif": round(vif, 4) if np.isfinite(vif) else np.nan,
                "n_obs": len(x),
                "status": "ok" if np.isfinite(vif) else "not_estimable",
            })
    return pd.DataFrame(records) if records else pd.DataFrame(columns=[
        "bloque_tematico", "variable_matriz", "vif", "n_obs", "status",
    ])


def compute_partial_correlations(
    wide: pd.DataFrame,
    inter_block: pd.DataFrame,
    max_pairs: int = 100,
) -> pd.DataFrame:
    """Correlaciones parciales descriptivas controlando por GDP y efectividad gubernamental si existen."""
    if inter_block.empty:
        return pd.DataFrame(columns=[
            "var_a", "var_b", "controls", "partial_r_spearman", "pvalue_raw",
            "n_pairs", "status",
        ])
    cols_lower = {c.lower(): c for c in wide.columns}
    gdp = next((c for k, c in cols_lower.items() if "gdp" in k and "per_capita" in k), None)
    gov = next((c for k, c in cols_lower.items() if "gov" in k and "effectiveness" in k), None)
    controls = [c for c in [gdp, gov] if c and pd.api.types.is_numeric_dtype(wide[c])]
    if not controls:
        return pd.DataFrame([{
            "var_a": "", "var_b": "", "controls": "",
            "partial_r_spearman": np.nan, "pvalue_raw": np.nan,
            "n_pairs": 0, "status": "controls_not_available",
        }])

    records = []
    candidates = inter_block.head(max_pairs)
    for _, row in candidates.iterrows():
        va, vb = row["var_a"], row["var_b"]
        sub = wide[[va, vb, *controls]].dropna()
        if len(sub) < len(controls) + 15:
            continue
        ranked = sub.rank()
        x_ctrl = np.column_stack([np.ones(len(ranked)), ranked[controls].values])
        try:
            resid_a = ranked[va].values - x_ctrl @ np.linalg.lstsq(x_ctrl, ranked[va].values, rcond=None)[0]
            resid_b = ranked[vb].values - x_ctrl @ np.linalg.lstsq(x_ctrl, ranked[vb].values, rcond=None)[0]
            r, p = stats.pearsonr(resid_a, resid_b)
        except Exception:
            continue
        if np.isnan(r) or np.isnan(p):
            continue
        records.append({
            "var_a": va,
            "var_b": vb,
            "controls": "|".join(controls),
            "partial_r_spearman": round(float(r), 4),
            "pvalue_raw": round(float(p), 6),
            "n_pairs": len(sub),
            "status": "exploratory_not_inferential",
        })
    return pd.DataFrame(records) if records else pd.DataFrame(columns=[
        "var_a", "var_b", "controls", "partial_r_spearman", "pvalue_raw",
        "n_pairs", "status",
    ])


def compute_redundancy(
    spearman_df: pd.DataFrame,
    dictionary: pd.DataFrame,
    threshold: float = 0.85,
) -> pd.DataFrame:
    """Identifica pares con |rho| > threshold y cruza con diccionario."""
    if spearman_df.empty:
        return pd.DataFrame()
    high = spearman_df[spearman_df["rho"].abs() >= threshold].copy()
    if high.empty:
        return high

    def _is_primary(var: str) -> bool | None:
        row = dictionary[dictionary["variable_matriz"] == var]
        if len(row):
            return bool(row["is_primary"].iloc[0])
        return None

    def _block(var: str) -> str:
        row = dictionary[dictionary["variable_matriz"] == var]
        if len(row):
            return str(row["bloque_tematico"].iloc[0])
        return ""

    high["is_primary_a"] = high["var_a"].apply(_is_primary)
    high["is_primary_b"] = high["var_b"].apply(_is_primary)
    high["bloque_a"] = high["var_a"].apply(_block)
    high["bloque_b"] = high["var_b"].apply(_block)
    high["same_block"] = high["bloque_a"] == high["bloque_b"]
    high["recommendation"] = high.apply(
        lambda r: f"keep_{r['var_a']}_drop_{r['var_b']}"
        if r["is_primary_a"] and not r["is_primary_b"]
        else (
            f"keep_{r['var_b']}_drop_{r['var_a']}"
            if r["is_primary_b"] and not r["is_primary_a"]
            else "human_review_needed"
        ),
        axis=1,
    )
    return high.sort_values("rho", key=abs, ascending=False).reset_index(drop=True)


def compute_inter_block_correlations(
    wide: pd.DataFrame,
    dictionary: pd.DataFrame,
    min_coverage: float = 0.30,
    min_n: int = 15,
) -> pd.DataFrame:
    """Correlaciones Spearman entre variables de distintos bloques, con FDR."""
    # Bloques prioritarios según el plan
    priority_pairs = [
        ("regulatory_treatment", "ecosystem_outcome"),
        ("regulatory_treatment", "adoption_diffusion"),
        ("regulatory_treatment", "tech_infrastructure_control"),
        ("institutional_control", "ecosystem_outcome"),
        ("socioeconomic_control", "ecosystem_outcome"),
        ("tech_infrastructure_control", "ecosystem_outcome"),
        ("adoption_diffusion", "ecosystem_outcome"),
    ]

    d_filtered = dictionary[dictionary["pct_complete"] >= min_coverage * 100] if "pct_complete" in dictionary.columns else dictionary
    all_records = []

    for block_a, block_b in priority_pairs:
        cols_a = get_block_var_cols(block_a, wide, d_filtered)
        cols_b = get_block_var_cols(block_b, wide, d_filtered)
        cols_a = [c for c in cols_a if pd.api.types.is_numeric_dtype(wide[c])]
        cols_b = [c for c in cols_b if pd.api.types.is_numeric_dtype(wide[c])]
        if not cols_a or not cols_b:
            continue
        for ca in cols_a:
            for cb in cols_b:
                sub = wide[[ca, cb]].dropna()
                n = len(sub)
                if n < min_n:
                    continue
                try:
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore")
                        r, p = stats.spearmanr(sub[ca], sub[cb])
                except Exception:
                    continue
                if np.isnan(r) or np.isnan(p):
                    continue
                all_records.append({
                    "block_a": block_a, "block_b": block_b,
                    "var_a": ca, "var_b": cb,
                    "rho_spearman": round(float(r), 4),
                    "pvalue_raw": round(float(p), 6),
                    "n_pairs": n,
                })

    if not all_records:
        return pd.DataFrame()

    df = pd.DataFrame(all_records)
    df = apply_fdr_holm(df, alpha=0.05)
    return df.sort_values("rho_spearman", key=abs, ascending=False).reset_index(drop=True)


def run_bivariate_analysis(
    wide: pd.DataFrame | None = None,
    dictionary: pd.DataFrame | None = None,
    save: bool = True,
) -> dict[str, pd.DataFrame]:
    if wide is None:
        wide = load_wide()
    if dictionary is None:
        dictionary = load_dictionary()

    # Variables numéricas con ≥30% cobertura
    d_num = dictionary[
        dictionary["tipo_matriz"].isin(["numeric", "score", "index", "count", "rank", "pct"]) &
        (dictionary.get("pct_complete", pd.Series(100, index=dictionary.index)) >= 30)
    ]
    num_cols = [c for c in wide.columns
                if c in d_num["variable_matriz"].values
                and pd.api.types.is_numeric_dtype(wide[c])]

    print(f"  Calculando correlaciones Spearman para {len(num_cols)} variables...")
    spearman = compute_pairwise_correlations(wide, num_cols, method="spearman")
    spearman = apply_fdr_holm(spearman)
    pearson = apply_fdr_holm(compute_pairwise_correlations(wide, num_cols, method="pearson"))
    kendall = apply_fdr_holm(compute_pairwise_correlations(wide, num_cols, method="kendall"))

    print(f"  Calculando redundancia (|rho| ≥ 0.85)...")
    redundancy = compute_redundancy(spearman, dictionary, threshold=0.85)

    print("  Calculando mutual information exploratoria...")
    top_pairs = []
    if not spearman.empty:
        top_pairs = list(
            spearman.assign(abs_rho=spearman["rho"].abs())
            .sort_values("abs_rho", ascending=False)
            .head(5000)[["var_a", "var_b"]]
            .itertuples(index=False, name=None)
        )
    mutual_info = compute_mutual_information(wide, num_cols, pairs=top_pairs)

    print(f"  Calculando correlaciones inter-bloque...")
    inter_block = compute_inter_block_correlations(wide, dictionary)
    inter_block_fdr = inter_block[[
        c for c in ["block_a", "block_b", "var_a", "var_b", "rho_spearman",
                  "pvalue_raw", "pvalue_fdr", "pvalue_holm", "significance", "n_pairs"]
        if c in inter_block.columns
    ]].copy() if not inter_block.empty else pd.DataFrame(columns=[
        "block_a", "block_b", "var_a", "var_b", "rho_spearman",
        "pvalue_raw", "pvalue_fdr", "pvalue_holm", "significance", "n_pairs",
    ])
    partial = compute_partial_correlations(wide, inter_block)
    vif = compute_vif_diagnostics(wide, dictionary)

    results = {
        "eda_correlations_spearman": spearman,
        "eda_correlations_pearson": pearson,
        "eda_correlations_kendall": kendall,
        "eda_mutual_information": mutual_info,
        "eda_redundancy_report": redundancy,
        "eda_inter_block_correlations": inter_block,
        "eda_inter_block_fdr": inter_block_fdr,
        "eda_partial_correlations": partial,
        "eda_vif_diagnostics": vif,
    }

    if save:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        for name, df in results.items():
            df.to_csv(OUTPUTS_DIR / f"{name}.csv", index=False)

    return results
