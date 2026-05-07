"""Test Q4 Clustering outputs."""


def test_q4_clusters_n43_complete(q4_clusters):
    assert len(q4_clusters) == 43
    assert q4_clusters["cluster_kmeans_n43"].notna().all()
    assert q4_clusters["cluster_hca_n43"].notna().all()


def test_q4_clusters_n18_subset(q4_clusters):
    n18 = q4_clusters["cluster_kmeans_n18"].notna().sum()
    assert n18 == q4_clusters["in_iapp_subset"].sum()


def test_q4_chile_in_clusters(q4_clusters):
    chile = q4_clusters[q4_clusters["iso3"] == "CHL"]
    assert len(chile) == 1
    import pandas as pd
    assert pd.notna(chile["cluster_kmeans_n43"].iloc[0])


def test_q4_silhouette_in_range(q4_silhouette):
    assert q4_silhouette["silhouette_score"].between(-1, 1).all()
