import pandas as pd
from pathlib import Path
OUTPUTS = Path(__file__).resolve().parents[1] / "outputs"

def test_q4_clustering():
    if not (OUTPUTS / "q4_clusters.csv").exists():
        return
    df = pd.read_csv(OUTPUTS / "q4_clusters.csv")
    assert "analysis_scope" in df.columns
    assert "cluster_kmeans" in df.columns
