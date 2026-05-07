"""Fixtures compartidos para tests Fase 6."""

import json
import pandas as pd
import pytest
from pathlib import Path

import sys
FASE6_ROOT = Path(__file__).resolve().parents[1]
if str(FASE6_ROOT.parent) not in sys.path:
    sys.path.insert(0, str(FASE6_ROOT.parent))

OUTPUTS = FASE6_ROOT / "outputs"
FASE5_BUNDLE = FASE6_ROOT.parent / "FASE5" / "outputs" / "phase6_ready"


@pytest.fixture
def q1_results():
    return pd.read_csv(OUTPUTS / "q1_results.csv")


@pytest.fixture
def q1_consistency():
    return pd.read_csv(OUTPUTS / "q1_consistency.csv")


@pytest.fixture
def q1_psm_pairs():
    return pd.read_csv(OUTPUTS / "q1_psm_matched_pairs.csv")


@pytest.fixture
def q1_psm_balance():
    return pd.read_csv(OUTPUTS / "q1_psm_balance_diagnostics.csv")


@pytest.fixture
def q2_results():
    return pd.read_csv(OUTPUTS / "q2_results.csv")


@pytest.fixture
def q2_predictions():
    return pd.read_csv(OUTPUTS / "q2_predictions_per_country.csv")


@pytest.fixture
def q3_results():
    return pd.read_csv(OUTPUTS / "q3_results.csv")


@pytest.fixture
def q3_consistency():
    return pd.read_csv(OUTPUTS / "q3_consistency.csv")


@pytest.fixture
def q4_clusters():
    return pd.read_csv(OUTPUTS / "q4_clusters.csv")


@pytest.fixture
def q4_silhouette():
    return pd.read_csv(OUTPUTS / "q4_silhouette_scores.csv")


@pytest.fixture
def q5_results():
    return pd.read_csv(OUTPUTS / "q5_results.csv")


@pytest.fixture
def q5_consistency():
    return pd.read_csv(OUTPUTS / "q5_consistency.csv")


@pytest.fixture
def q5_predictions():
    return pd.read_csv(OUTPUTS / "q5_predictions_per_country.csv")


@pytest.fixture
def q6_results():
    return pd.read_csv(OUTPUTS / "q6_results.csv")


@pytest.fixture
def q6_consistency():
    return pd.read_csv(OUTPUTS / "q6_consistency.csv")


@pytest.fixture
def q6_predictions():
    return pd.read_csv(OUTPUTS / "q6_predictions_per_country.csv")


@pytest.fixture
def fase6_manifest():
    with open(OUTPUTS / "fase6_manifest.json") as f:
        return json.load(f)
