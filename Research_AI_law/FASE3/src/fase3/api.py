"""Public API for Fase 4-8 consumers.

Downstream phases should import these functions instead of reading CSV files
directly. The files remain the authoritative artifacts; this API is the stable
access contract.
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

PHASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_DIR = PHASE_DIR / "outputs"


def load_wide(version: str = "1.0") -> pd.DataFrame:
    _assert_version(version)
    return pd.read_csv(OUTPUT_DIR / "matriz_madre_wide.csv")


def load_panel(version: str = "1.0") -> pd.DataFrame:
    _assert_version(version)
    return pd.read_csv(OUTPUT_DIR / "matriz_larga_panel.csv")


def load_snapshot(version: str = "1.0") -> pd.DataFrame:
    _assert_version(version)
    return pd.read_csv(OUTPUT_DIR / "matriz_larga_snapshot.csv")


def load_dictionary(version: str = "1.0") -> pd.DataFrame:
    _assert_version(version)
    return pd.read_csv(OUTPUT_DIR / "fase3_diccionario_variables.csv")


def get_block(block: str, version: str = "1.0") -> pd.DataFrame:
    wide = load_wide(version=version)
    dictionary = load_dictionary(version=version)
    variables = dictionary.loc[dictionary["bloque_tematico"].eq(block), "variable_matriz"].tolist()
    aux = [f"{v}_{suffix}" for v in variables for suffix in ["year_used", "confidence"]]
    id_cols = [
        "iso3", "country_name_canonical", "entity_type", "region", "income_group",
        "n_sources_present", "source_list", "n_variables_available", "pct_variables_available",
        "included_in_matrix", "included_in_dense_candidate", "inclusion_notes",
    ]
    cols = [c for c in id_cols + variables + aux if c in wide.columns]
    return wide[cols].copy()


def get_chile_snapshot(version: str = "1.0") -> pd.DataFrame:
    snapshot = load_snapshot(version=version)
    return snapshot[snapshot["iso3"].eq("CHL")].copy()


def list_versions() -> list[str]:
    manifest = _manifest()
    versions = [str(manifest.get("version", "1.0"))]
    archive_dir = OUTPUT_DIR / "_archive"
    if archive_dir.exists():
        versions.extend(sorted(p.name for p in archive_dir.iterdir() if p.is_dir()))
    return versions


def _manifest() -> dict:
    return json.loads((OUTPUT_DIR / "manifest.json").read_text(encoding="utf-8"))


def _assert_version(version: str) -> None:
    current = str(_manifest().get("version", "1.0"))
    if version != current:
        raise ValueError(f"Requested version {version!r}, available current version is {current!r}.")
