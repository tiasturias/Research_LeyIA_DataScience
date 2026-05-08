"""API publica de Fase 6 v2.1+ para consumo en Fase 7 y 8."""

from __future__ import annotations
import json
from pathlib import Path
import pandas as pd
import yaml

FASE6_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = FASE6_ROOT / "outputs"

def load_fase6_manifest() -> dict:
    return json.loads((OUTPUTS / "fase6_manifest.json").read_text(encoding="utf-8"))

def load_primary_results() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "primary_results_long.csv")

def load_effective_n() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "phase6_effective_n_by_outcome.csv")

def load_q1_results() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q1_results.csv")

def load_q2_results() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q2_results.csv")

def load_q2_scores() -> pd.DataFrame:
    """Scores descriptivos in-sample para adopción. No son predicciones independientes."""
    return pd.read_csv(OUTPUTS / "q2_scores_per_country.csv")

def load_q3_results() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q3_results.csv")

def load_q4_clusters() -> pd.DataFrame:
    """Clustering descriptivo de perfiles regulatorios."""
    return pd.read_csv(OUTPUTS / "q4_clusters.csv")

def load_q5_results() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q5_results.csv")

def load_q5_scores() -> pd.DataFrame:
    """Scores descriptivos in-sample para uso poblacional."""
    return pd.read_csv(OUTPUTS / "q5_scores_per_country.csv")

def load_q6_results() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q6_results.csv")

def load_q6_scores() -> pd.DataFrame:
    """Scores descriptivos in-sample para sector público."""
    return pd.read_csv(OUTPUTS / "q6_scores_per_country.csv")
