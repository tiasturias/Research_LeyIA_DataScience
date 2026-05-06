"""Bloques D y K: análisis intra-bloque y reducción dimensional exploratoria."""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import BLOCKS, OUTPUTS_DIR
from .load import get_block_var_cols, load_dictionary, load_wide


def _robust_scale(df: pd.DataFrame) -> pd.DataFrame:
    med = df.median(axis=0)
    mad = (df - med).abs().median(axis=0).replace(0, np.nan)
    return (df - med) / mad


def _safe_pca(matrix: pd.DataFrame, n_components: int = 5) -> tuple[pd.DataFrame, pd.DataFrame, list[float]]:
    try:
        from sklearn.decomposition import PCA
    except Exception:
        return pd.DataFrame(), pd.DataFrame(), []
    x = matrix.dropna(axis=0, how="any").dropna(axis=1, how="any")
    x = x.loc[:, x.nunique(dropna=True) > 1]
    if x.shape[0] < 5 or x.shape[1] < 2:
        return pd.DataFrame(), pd.DataFrame(), []
    z = _robust_scale(x).replace([np.inf, -np.inf], np.nan).dropna(axis=1)
    z = z.dropna(axis=0, how="any")
    if z.shape[0] < 5 or z.shape[1] < 2:
        return pd.DataFrame(), pd.DataFrame(), []
    n = min(n_components, z.shape[0] - 1, z.shape[1])
    pca = PCA(n_components=n, random_state=42)
    scores = pca.fit_transform(z)
    loadings = pd.DataFrame(
        pca.components_.T,
        index=z.columns,
        columns=[f"PC{i+1}" for i in range(n)],
    ).reset_index(names="variable_matriz")
    score_df = pd.DataFrame(
        scores,
        index=z.index,
        columns=[f"PC{i+1}" for i in range(n)],
    ).reset_index(names="row_index")
    return loadings, score_df, [round(float(v), 6) for v in pca.explained_variance_ratio_]


def compute_block_summary(wide: pd.DataFrame, dictionary: pd.DataFrame, block: str) -> pd.DataFrame:
    cols = get_block_var_cols(block, wide, dictionary)
    rows = []
    for col in cols:
        s = wide[col]
        drow = dictionary[dictionary["variable_matriz"] == col].iloc[0]
        rec = {
            "bloque_tematico": block,
            "variable_matriz": col,
            "tipo_matriz": drow.get("tipo_matriz", ""),
            "source_id": drow.get("source_id", ""),
            "unit": drow.get("unit", ""),
            "is_primary": drow.get("is_primary", ""),
            "n_non_null": int(s.notna().sum()),
            "pct_complete": round(float(s.notna().mean() * 100), 2),
            "n_unique": int(s.nunique(dropna=True)),
        }
        if pd.api.types.is_numeric_dtype(s):
            clean = s.dropna()
            rec.update({
                "median": round(float(clean.median()), 6) if len(clean) else np.nan,
                "iqr": round(float(clean.quantile(0.75) - clean.quantile(0.25)), 6) if len(clean) else np.nan,
                "min": round(float(clean.min()), 6) if len(clean) else np.nan,
                "max": round(float(clean.max()), 6) if len(clean) else np.nan,
            })
        rows.append(rec)
    return pd.DataFrame(rows)


def compute_block_pca_loadings(wide: pd.DataFrame, dictionary: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for block in BLOCKS:
        cols = get_block_var_cols(block, wide, dictionary)
        cols = [c for c in cols if pd.api.types.is_numeric_dtype(wide[c]) and wide[c].notna().mean() >= 0.70]
        loadings, _, explained = _safe_pca(wide[cols], n_components=5) if cols else (pd.DataFrame(), pd.DataFrame(), [])
        if loadings.empty:
            rows.append({
                "bloque_tematico": block,
                "variable_matriz": "NO_PCA_ESTIMABLE",
                "component": "NA",
                "loading": np.nan,
                "explained_variance_ratio": np.nan,
                "status": "insufficient_complete_cases_or_variables",
            })
            continue
        for _, r in loadings.iterrows():
            for pc in [c for c in loadings.columns if c.startswith("PC")]:
                idx = int(pc[2:]) - 1
                rows.append({
                    "bloque_tematico": block,
                    "variable_matriz": r["variable_matriz"],
                    "component": pc,
                    "loading": round(float(r[pc]), 6),
                    "explained_variance_ratio": explained[idx] if idx < len(explained) else np.nan,
                    "status": "exploratory_not_feature",
                })
    return pd.DataFrame(rows)


def compute_global_pca(wide: pd.DataFrame, dictionary: pd.DataFrame) -> pd.DataFrame:
    cols = dictionary.loc[dictionary["pct_complete"].ge(70), "variable_matriz"].tolist()
    cols = [c for c in cols if c in wide.columns and pd.api.types.is_numeric_dtype(wide[c])]
    loadings, scores, explained = _safe_pca(wide[cols], n_components=10)
    rows = []
    for _, r in loadings.iterrows():
        for pc in [c for c in loadings.columns if c.startswith("PC")]:
            idx = int(pc[2:]) - 1
            rows.append({
                "record_type": "loading",
                "iso3": "",
                "variable_matriz": r["variable_matriz"],
                "component": pc,
                "value": round(float(r[pc]), 6),
                "explained_variance_ratio": explained[idx] if idx < len(explained) else np.nan,
            })
    if not scores.empty:
        score_map = wide.loc[scores["row_index"], ["iso3", "country_name_canonical"]].reset_index(drop=True)
        score_values = scores.drop(columns=["row_index"]).reset_index(drop=True)
        for idx, r in score_values.iterrows():
            for pc in score_values.columns:
                rows.append({
                    "record_type": "score",
                    "iso3": score_map.loc[idx, "iso3"],
                    "variable_matriz": "",
                    "component": pc,
                    "value": round(float(r[pc]), 6),
                    "explained_variance_ratio": np.nan,
                })
    return pd.DataFrame(rows) if rows else pd.DataFrame([{
        "record_type": "diagnostic", "iso3": "", "variable_matriz": "",
        "component": "NA", "value": np.nan, "explained_variance_ratio": np.nan,
    }])


def compute_country_clustering(wide: pd.DataFrame, dictionary: pd.DataFrame) -> pd.DataFrame:
    out = wide[["iso3", "country_name_canonical", "region", "income_group"]].copy()
    reg_cols = get_block_var_cols("regulatory_treatment", wide, dictionary)
    reg_cols = [c for c in reg_cols if c in wide.columns and wide[c].notna().any()]
    out["regulatory_cluster_k4"] = pd.NA
    out["cluster_status"] = "not_regulated_or_no_iapp_record"
    if len(reg_cols) >= 2:
        try:
            from sklearn.cluster import AgglomerativeClustering
            mask = wide[reg_cols].notna().any(axis=1)
            x = wide.loc[mask, reg_cols].copy()
            for col in x.columns:
                if not pd.api.types.is_numeric_dtype(x[col]):
                    x[col] = pd.Categorical(x[col]).codes.replace(-1, 0)
            x = x.fillna(0)
            n_clusters = min(4, max(2, len(x) // 3))
            labels = AgglomerativeClustering(n_clusters=n_clusters).fit_predict(x)
            out.loc[mask, "regulatory_cluster_k4"] = labels + 1
            out.loc[mask, "cluster_status"] = "exploratory_regulatory_hca"
        except Exception as exc:
            out["cluster_status"] = f"clustering_error: {type(exc).__name__}"
    return out


def compute_umap_coords(wide: pd.DataFrame, dictionary: pd.DataFrame) -> pd.DataFrame:
    cols = dictionary.loc[dictionary["pct_complete"].ge(70), "variable_matriz"].tolist()
    cols = [c for c in cols if c in wide.columns and pd.api.types.is_numeric_dtype(wide[c])]
    base = wide[["iso3", "country_name_canonical", "region", "income_group"]].copy()
    base["umap_x"] = np.nan
    base["umap_y"] = np.nan
    base["method"] = "not_estimated"
    x = wide[cols].dropna(axis=0, how="any").dropna(axis=1, how="any") if cols else pd.DataFrame()
    x = x.loc[:, x.nunique(dropna=True) > 1] if not x.empty else x
    if x.shape[0] < 10 or x.shape[1] < 2:
        base["method"] = "insufficient_complete_cases"
        return base
    z = _robust_scale(x).replace([np.inf, -np.inf], np.nan).dropna(axis=1)
    # UMAP puede activar compilación JIT costosa en entornos limpios. Para que
    # build-all sea determinista y rápido, Fase 4 deja este slot como
    # visualización 2D reproducible basada en PCA; Fase 5 puede recalcular UMAP
    # si se decide usarlo como figura exploratoria.
    from sklearn.decomposition import PCA
    coords = PCA(n_components=2, random_state=42).fit_transform(z)
    method = "pca_2d_fallback_for_umap_slot"
    base.loc[z.index, "umap_x"] = coords[:, 0]
    base.loc[z.index, "umap_y"] = coords[:, 1]
    base.loc[z.index, "method"] = method
    return base


def run_block_analysis(
    wide: pd.DataFrame | None = None,
    dictionary: pd.DataFrame | None = None,
    save: bool = True,
) -> dict[str, pd.DataFrame]:
    if wide is None:
        wide = load_wide()
    if dictionary is None:
        dictionary = load_dictionary()
    results = {f"eda_block_{block}_summary": compute_block_summary(wide, dictionary, block) for block in BLOCKS}
    results["eda_block_pca_loadings"] = compute_block_pca_loadings(wide, dictionary)
    results["eda_pca_global"] = compute_global_pca(wide, dictionary)
    results["eda_clustering_countries"] = compute_country_clustering(wide, dictionary)
    results["eda_umap_coords"] = compute_umap_coords(wide, dictionary)
    if save:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        for name, df in results.items():
            df.to_csv(OUTPUTS_DIR / f"{name}.csv", index=False)
    return results
