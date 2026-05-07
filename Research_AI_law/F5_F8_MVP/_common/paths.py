"""Paths canonicos del MVP."""

from __future__ import annotations

from pathlib import Path

MVP_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = MVP_ROOT.parent
FASE3_ROOT = PROJECT_ROOT / "FASE3"
FASE4_ROOT = PROJECT_ROOT / "FASE4"
FASE5_ROOT = MVP_ROOT / "FASE5"
FASE5_OUTPUTS = FASE5_ROOT / "outputs"
FASE5_PHASE6_READY = FASE5_OUTPUTS / "phase6_ready"
FASE5_CONFIG = FASE5_ROOT / "config"
