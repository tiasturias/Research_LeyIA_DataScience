"""Paths, constants and config loader for Fase 4."""

from __future__ import annotations

import hashlib
from pathlib import Path

import yaml

# Root paths
FASE4_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = FASE4_ROOT.parent
FASE3_ROOT = PROJECT_ROOT / "FASE3"
FASE3_OUTPUTS = FASE3_ROOT / "outputs"

OUTPUTS_DIR = FASE4_ROOT / "outputs" / "eda_principal"
CONFIG_DIR = FASE4_ROOT / "config" / "fase4"


def _load_yaml(name: str) -> dict:
    path = CONFIG_DIR / name
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_thresholds() -> dict:
    return _load_yaml("thresholds.yaml")


def get_peer_groups() -> dict:
    return _load_yaml("peer_groups.yaml")


def get_binding_taxonomy() -> dict:
    return _load_yaml("binding_taxonomy.yaml")


def get_question_mapping() -> dict:
    return _load_yaml("question_mapping.yaml")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# Columnas de identidad en la wide (no son variables analíticas)
META_COLS = [
    "iso3", "country_name_canonical", "entity_type", "region", "income_group",
    "n_sources_present", "source_list", "n_variables_available",
    "pct_variables_available", "included_in_matrix", "included_in_dense_candidate",
    "inclusion_notes",
]

# Sufijos auxiliares que acompañan a cada variable
AUX_SUFFIXES = ("_confidence", "_year_used")

BLOCKS = [
    "regulatory_treatment",
    "ecosystem_outcome",
    "adoption_diffusion",
    "socioeconomic_control",
    "institutional_control",
    "tech_infrastructure_control",
]
