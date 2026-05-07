"""API estable de Fase 6 para consumo en Fase 7-8."""

from __future__ import annotations
import json
from pathlib import Path

import pandas as pd

from ._common_data import F5_F8_MVP

OUTPUTS = F5_F8_MVP / "FASE6" / "outputs"


def load_q1_results() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q1_results.csv")


def load_q1_consistency() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q1_consistency.csv")


def load_q1_psm_pairs() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q1_psm_matched_pairs.csv")


def load_q1_psm_balance() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q1_psm_balance_diagnostics.csv")


def load_q2_results() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q2_results.csv")


def load_q2_predictions() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q2_predictions_per_country.csv")


def load_q3_results() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q3_results.csv")


def load_q3_consistency() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q3_consistency.csv")


def load_q4_clusters() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q4_clusters.csv")


def load_q4_silhouette() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q4_silhouette_scores.csv")


def load_fase6_manifest() -> dict:
    with open(OUTPUTS / "fase6_manifest.json") as f:
        return json.load(f)


def load_q5_results() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q5_results.csv")


def load_q5_consistency() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q5_consistency.csv")


def load_q5_predictions() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q5_predictions_per_country.csv")


def load_q6_results() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q6_results.csv")


def load_q6_consistency() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q6_consistency.csv")


def load_q6_predictions() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "q6_predictions_per_country.csv")
