"""Fixtures compartidos para tests Fase 4."""

import sys
from pathlib import Path

import pytest

# Asegurar paths correctos
FASE4_ROOT = Path(__file__).resolve().parents[2]
FASE3_ROOT = FASE4_ROOT.parent / "FASE3"

if str(FASE4_ROOT) not in sys.path:
    sys.path.insert(0, str(FASE4_ROOT))
if str(FASE3_ROOT) not in sys.path:
    sys.path.insert(0, str(FASE3_ROOT))

# Añadir src/ al path
sys.path.insert(0, str(FASE4_ROOT / "src"))


@pytest.fixture(scope="session")
def wide():
    from fase4.load import load_wide
    return load_wide()


@pytest.fixture(scope="session")
def dictionary():
    from fase4.load import load_dictionary
    return load_dictionary()


@pytest.fixture(scope="session")
def panel():
    from fase4.load import load_panel
    return load_panel()
