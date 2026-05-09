"""Q4: Perfiles regulatorios estructurados (Clustering descriptivo)."""

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.metrics import silhouette_score
import scipy.spatial.distance as dist


def run_q4(fm: pd.DataFrame, config: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    # We use binding taxonomy or IAPP direct raw variables for clustering
    # Since NLP is out of scope, we use the structured variables.
    
    # Selecting binary Techieray variables
    tr_vars = [
        "tr_ley_ia_vigente",
        "tr_proyecto_ley_ia",
        "tr_estrategia_nacional_ia",
        "tr_tiene_guia_softlaw",
        "tr_tiene_autoridad_dedicada",
    ]
    cols = [c for c in tr_vars if c in fm.columns]
    
    sub = fm[["iso3", "country_name_canonical"] + cols].dropna().copy()
    
    if len(sub) < 15 or not cols:
        return pd.DataFrame(), pd.DataFrame()
        
    X = sub[cols].values.astype(float)
    
    # Primary: Hierarchical Clustering with Jaccard
    jaccard_dist = dist.pdist(X, metric='jaccard')
    if not np.any(np.isnan(jaccard_dist)):
        hca = AgglomerativeClustering(n_clusters=4, metric='precomputed', linkage='average')
        sub["cluster_hca"] = hca.fit_predict(dist.squareform(jaccard_dist))
        sil_hca = silhouette_score(dist.squareform(jaccard_dist), sub["cluster_hca"], metric='precomputed')
    else:
        sub["cluster_hca"] = np.nan
        sil_hca = np.nan
        
    # Sensitivity: KMeans
    kmeans = KMeans(n_clusters=4, random_state=20260508, n_init=10)
    sub["cluster_kmeans"] = kmeans.fit_predict(X)
    sil_kmeans = silhouette_score(X, sub["cluster_kmeans"])
    
    sub["analysis_scope"] = "full_preregistered_sample_unsupervised"
    sub["validation_scope"] = "cluster_internal_silhouette_not_external_test"
    sub["holdout_used"] = False
    
    # Distance matrix output
    dist_df = pd.DataFrame(
        dist.squareform(jaccard_dist), 
        index=sub["iso3"], 
        columns=sub["iso3"]
    ) if not np.any(np.isnan(jaccard_dist)) else pd.DataFrame()
    
    return sub, dist_df
