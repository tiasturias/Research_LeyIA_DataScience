from pathlib import Path
import sys

import pandas as pd
import pytest

PHASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PHASE_DIR / "src"))
OUTPUT_DIR = PHASE_DIR / "outputs"


@pytest.fixture(scope="session")
def output_dir():
    return OUTPUT_DIR


@pytest.fixture(scope="session")
def panel(output_dir):
    return pd.read_csv(output_dir / "matriz_larga_panel.csv")


@pytest.fixture(scope="session")
def snapshot(output_dir):
    return pd.read_csv(output_dir / "matriz_larga_snapshot.csv")


@pytest.fixture(scope="session")
def wide(output_dir):
    return pd.read_csv(output_dir / "matriz_madre_wide.csv")


@pytest.fixture(scope="session")
def dictionary(output_dir):
    return pd.read_csv(output_dir / "fase3_diccionario_variables.csv")


@pytest.fixture(scope="session")
def traceability(output_dir):
    return pd.read_csv(output_dir / "matriz_madre_trazabilidad.csv")


@pytest.fixture(scope="session")
def universe(output_dir):
    return pd.read_csv(output_dir / "fase3_universo_geografico.csv")
