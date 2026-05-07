"""Q4: Clustering de países por perfil regulatorio.
Doble clustering: N=43 oficial (Gower) + N=18 complementario (Jaccard binario)."""

from __future__ import annotations
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import squareform
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

from ._common_data import load_bundle, F5_F8_MVP

OUTPUTS = F5_F8_MVP / "FASE6" / "outputs"


def get_features_n43(fm: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    """Features mixtas para clustering N=43: 9 one-hots + 5 agregados."""
    one_hots = [c for c in fm.columns if (
        c.startswith("iapp_categoria_obligatoriedad_") or
        c.startswith("iapp_modelo_gobernanza_")
    )]
    aggregates = ["n_binding", "n_non_binding", "n_hybrid",
                  "regulatory_intensity", "n_regulatory_mechanisms"]
    cols = one_hots + aggregates
    cols = [c for c in cols if c in fm.columns]
    sub = fm[["iso3"] + cols].copy()
    return sub, cols


def get_features_n18(fm: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    """Vector binario IAPP para subset de 18 con datos."""
    iapp_binary_cols = [
        "iapp_ley_ia_vigente", "iapp_proyecto_ley_ia",
    ]
    one_hots = [c for c in fm.columns if (
        c.startswith("iapp_categoria_obligatoriedad_") or
        c.startswith("iapp_modelo_gobernanza_")
    )]
    cols = iapp_binary_cols + one_hots
    cols = [c for c in cols if c in fm.columns]
    sub = fm[fm["iapp_ley_ia_vigente"].notna()][["iso3"] + cols].copy()
    return sub, cols


def jaccard_distance_matrix(X: np.ndarray) -> np.ndarray:
    """Jaccard distance entre filas (binario)."""
    n = X.shape[0]
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            inter = np.sum(np.logical_and(X[i] == 1, X[j] == 1))
            union = np.sum(np.logical_or(X[i] == 1, X[j] == 1))
            d = 1 - inter / union if union > 0 else 0.0
            D[i, j] = D[j, i] = d
    return D


def euclidean_standardized_distance(X: np.ndarray) -> np.ndarray:
    """Euclidean sobre features estandarizadas (z-score)."""
    Xs = StandardScaler().fit_transform(X)
    n = Xs.shape[0]
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            d = float(np.linalg.norm(Xs[i] - Xs[j]))
            D[i, j] = D[j, i] = d
    return D


def hca_clusters(D: np.ndarray, k: int = 4) -> np.ndarray:
    cond = squareform(D, checks=False)
    Z = linkage(cond, method="ward")
    return fcluster(Z, t=k, criterion="maxclust")


def kmeans_clusters(X: np.ndarray, k: int = 4, seed: int = 42) -> np.ndarray:
    return KMeans(n_clusters=k, random_state=seed, n_init=20).fit_predict(X)


def run_q4(seed: int = 42, k: int = 4) -> dict:
    bundle = load_bundle()
    fm = bundle["feature_matrix"]

    # ===== N=43 OFICIAL =====
    sub43, cols43 = get_features_n43(fm)
    X43 = sub43[cols43].values.astype(float)
    D43 = euclidean_standardized_distance(X43)
    hca43 = hca_clusters(D43, k=k)
    km43 = kmeans_clusters(StandardScaler().fit_transform(X43), k=k, seed=seed)
    sil_hca43 = silhouette_score(D43, hca43, metric="precomputed") if len(set(hca43)) > 1 else np.nan
    sil_km43 = silhouette_score(StandardScaler().fit_transform(X43), km43) if len(set(km43)) > 1 else np.nan

    # ===== N=18 COMPLEMENTARIO =====
    sub18, cols18 = get_features_n18(fm)
    X18 = sub18[cols18].fillna(0).astype(int).values
    D18 = jaccard_distance_matrix(X18)
    hca18 = hca_clusters(D18, k=min(k, max(2, X18.shape[0] // 4)))
    km18 = kmeans_clusters(X18.astype(float), k=min(k, max(2, X18.shape[0] // 4)), seed=seed)
    sil_hca18 = silhouette_score(D18, hca18, metric="precomputed") if len(set(hca18)) > 1 else np.nan
    sil_km18 = silhouette_score(X18.astype(float), km18) if len(set(km18)) > 1 else np.nan

    # ===== ENSAMBLAR clusters.csv =====
    clusters_df = fm[["iso3", "country_name_canonical", "region"]].copy()
    clusters_df["cluster_kmeans_n43"] = km43
    clusters_df["cluster_hca_n43"] = hca43
    clusters_df["in_iapp_subset"] = clusters_df["iso3"].isin(sub18["iso3"]).astype(int)
    clusters_df["cluster_kmeans_n18"] = np.nan
    clusters_df["cluster_hca_n18"] = np.nan
    iso_to_km18 = dict(zip(sub18["iso3"], km18))
    iso_to_hca18 = dict(zip(sub18["iso3"], hca18))
    clusters_df["cluster_kmeans_n18"] = clusters_df["iso3"].map(iso_to_km18)
    clusters_df["cluster_hca_n18"] = clusters_df["iso3"].map(iso_to_hca18)

    OUTPUTS.mkdir(parents=True, exist_ok=True)
    clusters_df.to_csv(OUTPUTS / "q4_clusters.csv", index=False)

    # Distance matrices long-format
    def matrix_to_long(D, isos, metric, scope):
        rows = []
        for i, a in enumerate(isos):
            for j, b in enumerate(isos):
                if i < j:
                    rows.append({
                        "iso3_a": a, "iso3_b": b,
                        "distance": float(D[i, j]),
                        "distance_metric": metric, "scope": scope,
                    })
        return pd.DataFrame(rows)

    matrix_to_long(D43, sub43["iso3"].tolist(), "euclidean_standardized", "n43_mixed").to_csv(
        OUTPUTS / "q4_distance_matrix_n43.csv", index=False)
    matrix_to_long(D18, sub18["iso3"].tolist(), "jaccard", "n18_binary").to_csv(
        OUTPUTS / "q4_distance_matrix_n18.csv", index=False)

    # Silhouette
    pd.DataFrame([
        {"method": "kmeans", "scope": "n43_mixed", "k": k, "silhouette_score": sil_km43, "n_observations": 43},
        {"method": "hca",    "scope": "n43_mixed", "k": k, "silhouette_score": sil_hca43, "n_observations": 43},
        {"method": "kmeans", "scope": "n18_binary", "k": min(k, max(2, X18.shape[0]//4)), "silhouette_score": sil_km18, "n_observations": 18},
        {"method": "hca",    "scope": "n18_binary", "k": min(k, max(2, X18.shape[0]//4)), "silhouette_score": sil_hca18, "n_observations": 18},
    ]).to_csv(OUTPUTS / "q4_silhouette_scores.csv", index=False)

    # Centroides KMeans n43 (para deep-dive Chile)
    centroids = pd.DataFrame(
        StandardScaler().fit(X43).inverse_transform(
            KMeans(n_clusters=k, random_state=seed, n_init=20)
            .fit(StandardScaler().fit_transform(X43)).cluster_centers_
        ),
        columns=cols43,
    )
    centroids.insert(0, "cluster_label", range(k))
    centroids.to_csv(OUTPUTS / "q4_centroids.csv", index=False)

    return {
        "n43_kmeans_silhouette": sil_km43,
        "n43_hca_silhouette": sil_hca43,
        "n18_kmeans_silhouette": sil_km18,
        "n18_hca_silhouette": sil_hca18,
        "k": k,
    }
