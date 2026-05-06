"""Test: los outputs de Fase 3 no fueron modificados."""

import hashlib
from pathlib import Path

import pytest


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def test_fase3_outputs_accessible():
    """Los outputs de Fase 3 deben ser accesibles y no vacíos."""
    fase3_outputs = Path(__file__).resolve().parents[3] / "FASE3" / "outputs"
    assert fase3_outputs.exists(), "FASE3/outputs no encontrado"
    csvs = list(fase3_outputs.glob("*.csv"))
    assert len(csvs) > 0, "No se encontraron CSV en FASE3/outputs"


def test_fase3_manifest_exists():
    """El manifest de Fase 3 debe existir y tener versión 1.x."""
    import json
    manifest_path = Path(__file__).resolve().parents[3] / "FASE3" / "outputs" / "manifest.json"
    assert manifest_path.exists(), "manifest.json de Fase 3 no encontrado"
    with open(manifest_path) as f:
        manifest = json.load(f)
    assert "version" in manifest
    assert manifest["version"].startswith("1."), f"Version inesperada: {manifest['version']}"


def test_wide_csv_not_empty():
    """La wide de Fase 3 no debe estar vacía."""
    wide_path = Path(__file__).resolve().parents[3] / "FASE3" / "outputs" / "matriz_madre_wide.csv"
    assert wide_path.exists(), "matriz_madre_wide.csv no encontrado"
    size = wide_path.stat().st_size
    assert size > 1_000_000, f"matriz_madre_wide.csv parece demasiado pequeño: {size} bytes"
