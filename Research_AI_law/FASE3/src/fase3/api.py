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


def load_wide(version: str | None = None) -> pd.DataFrame:
    _assert_version(version)
    return pd.read_csv(OUTPUT_DIR / "matriz_madre_wide.csv")


def load_panel(version: str | None = None) -> pd.DataFrame:
    _assert_version(version)
    return pd.read_csv(OUTPUT_DIR / "matriz_larga_panel.csv")


def load_snapshot(version: str | None = None) -> pd.DataFrame:
    _assert_version(version)
    return pd.read_csv(OUTPUT_DIR / "matriz_larga_snapshot.csv")


def load_dictionary(version: str | None = None) -> pd.DataFrame:
    _assert_version(version)
    return pd.read_csv(OUTPUT_DIR / "fase3_diccionario_variables.csv")


def get_block(block: str, version: str | None = None) -> pd.DataFrame:
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


def get_chile_snapshot(version: str | None = None) -> pd.DataFrame:
    snapshot = load_snapshot(version=version)
    return snapshot[snapshot["iso3"].eq("CHL")].copy()


def list_versions() -> list[str]:
    manifest = _manifest()
    versions = [str(manifest.get("version", "1.0"))]
    archive_dir = OUTPUT_DIR / "_archive"
    if archive_dir.exists():
        versions.extend(sorted(p.name for p in archive_dir.iterdir() if p.is_dir()))
    return versions


def current_version() -> str:
    return str(_manifest().get("version", "1.0"))


def _manifest() -> dict:
    return json.loads((OUTPUT_DIR / "manifest.json").read_text(encoding="utf-8"))


def _assert_version(version: str | None) -> None:
    """Accept None (any current 1.x), exact match, or any compatible 1.x version.

    Quality fixes that preserve schema and semantics bump minor (1.0 -> 1.1).
    Schema-breaking changes would bump major (1.x -> 2.0).
    """
    current = current_version()
    if version is None:
        return
    # exact match always ok
    if version == current:
        return
    # accept any 1.x when current is 1.x (backward-compatible quality fixes)
    try:
        req_major = version.split(".")[0]
        cur_major = current.split(".")[0]
        if req_major == cur_major:
            return
    except (AttributeError, IndexError):
        pass
    raise ValueError(
        f"Requested version {version!r} is incompatible with current {current!r}. "
        f"Pass version=None to accept the current major version."
    )
