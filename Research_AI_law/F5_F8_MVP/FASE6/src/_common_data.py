"""Carga y validación de bundle phase6_ready desde Fase 5."""

from __future__ import annotations
import hashlib
import json
import sys
from functools import lru_cache
from pathlib import Path

import pandas as pd
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[3]
F5_F8_MVP = PROJECT_ROOT / "F5_F8_MVP"
FASE5_BUNDLE = F5_F8_MVP / "FASE5" / "outputs" / "phase6_ready"
FASE5_SRC = F5_F8_MVP / "FASE5"

# Asegurar import de FASE5.src.api
if str(FASE5_SRC) not in sys.path:
    sys.path.insert(0, str(FASE5_SRC))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_bundle_hash() -> dict:
    """Valida que cada archivo del bundle reproduce su sha256 según manifest."""
    with open(FASE5_BUNDLE / "phase6_ready_manifest.json") as f:
        manifest = json.load(f)
    errors = []
    for fname, meta in manifest.get("files", {}).items():
        p = FASE5_BUNDLE / fname
        if not p.exists():
            errors.append(f"missing: {fname}")
            continue
        actual = sha256_file(p)
        if actual != meta["sha256"]:
            errors.append(f"sha mismatch: {fname}")
    if errors:
        raise RuntimeError(f"Bundle integrity FAIL: {errors}")
    return {"status": "ok", "n_files": len(manifest["files"])}


@lru_cache(maxsize=1)
def load_bundle() -> dict:
    """Carga todos los componentes del bundle en un dict."""
    validate_bundle_hash()
    from FASE5.src.api import (
        load_phase6_feature_matrix,
        load_phase6_schema,
        load_phase6_column_groups,
        load_phase6_modeling_contract,
        load_phase6_ready_manifest,
        load_phase6_llm_context,
    )
    return {
        "feature_matrix": load_phase6_feature_matrix(),
        "schema": load_phase6_schema(),
        "column_groups": load_phase6_column_groups(),
        "contract": load_phase6_modeling_contract(),
        "manifest": load_phase6_ready_manifest(),
        "llm_context": load_phase6_llm_context(),
    }


def get_train_test_split() -> pd.DataFrame:
    return pd.read_csv(FASE5_BUNDLE / "phase6_train_test_split.csv")


def get_x2_controls() -> list[str]:
    """12 controles X2 según contrato."""
    bundle = load_bundle()
    return bundle["contract"]["variables_by_role"]["X2_control"]


def get_x1_aggregated() -> list[str]:
    """Variables agregadas regulatorias (0% missing en 43 países)."""
    return ["n_binding", "n_non_binding", "n_hybrid", "regulatory_intensity", "n_regulatory_mechanisms"]


def get_x1_iapp_raw() -> list[str]:
    """6 variables IAPP raw (cobertura 18/43)."""
    return [
        "iapp_ley_ia_vigente", "iapp_categoria_obligatoriedad",
        "iapp_proyecto_ley_ia", "iapp_modelo_gobernanza",
        "iapp_n_leyes_relacionadas", "iapp_n_autoridades",
    ]


def get_y_by_question(q: str) -> list[str]:
    """Y candidates por sub-pregunta. q ∈ {'Q1','Q2','Q3','Q5','Q6'}."""
    bundle = load_bundle()
    q_to_role = {
        "Q1": "Y_Q1_investment",
        "Q2": "Y_Q2_adoption",
        "Q3": "Y_Q3_innovation",
        "Q5": "Y_Q5_population_usage",
        "Q6": "Y_Q6_public_sector",
    }
    return bundle["contract"]["variables_by_role"][q_to_role[q]]
