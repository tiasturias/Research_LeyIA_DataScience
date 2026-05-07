from __future__ import annotations

import sys
from pathlib import Path

import pytest


MVP_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = MVP_ROOT.parent
for path in (MVP_ROOT, PROJECT_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))


@pytest.fixture(scope="session")
def phase5_results():
    from FASE5.src.build import build_phase5

    return build_phase5(save=True)
