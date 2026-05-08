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

if str(FASE5_SRC) not in sys.path:
    sys.path.insert(0, str(FASE5_SRC))


def get_analysis_sample_membership() -> pd.DataFrame:
    path = FASE5_BUNDLE / "phase6_analysis_sample_membership.csv"
    if not path.exists():
        raise FileNotFoundError("Falta phase6_analysis_sample_membership.csv. Cerrar Fase 5 v2.1 primero.")
    membership = pd.read_csv(path)
    forbidden = {"split", "train", "test", "holdout"}
    bad = forbidden.intersection(set(c.lower() for c in membership.columns))
    if bad:
        raise RuntimeError(f"Membership contiene columnas prohibidas: {bad}")
    return membership


def load_feature_matrix() -> pd.DataFrame:
    path = FASE5_BUNDLE / "phase6_feature_matrix.csv"
    if not path.exists():
        raise FileNotFoundError("Falta phase6_feature_matrix.csv")
    fm = pd.read_csv(path)
    if "split" in fm.columns:
        raise RuntimeError("Fase 6 v2.1+ no acepta columna split")
    return fm


def load_modeling_contract() -> dict:
    path = FASE5_BUNDLE / "phase6_modeling_contract.yaml"
    if not path.exists():
        raise FileNotFoundError("Falta phase6_modeling_contract.yaml")
    return yaml.safe_load(path.read_text())


def validate_inferential_contract() -> dict:
    if (FASE5_BUNDLE / "phase6_train_test_split.csv").exists():
        raise RuntimeError("Archivo prohibido: phase6_train_test_split.csv")

    fm = load_feature_matrix()
    membership = get_analysis_sample_membership()
    contract = load_modeling_contract()

    assert len(fm) == 43
    assert len(membership) == 43
    assert membership["is_primary_analysis_sample"].fillna(False).all()
    assert contract["methodology"] == "inferential_comparative_observational"
    assert contract["sample_policy"]["use_holdout_test_set"] is False
    assert contract["sample_policy"]["train_test_split_created"] is False
    assert contract["sample_policy"]["split_column_present"] is False

    return {
        "status": "ok",
        "methodology": contract["methodology"],
        "primary_estimand": contract.get("primary_estimand", "adjusted_association"),
        "n_feature_matrix": len(fm),
        "n_membership": len(membership),
        "holdout_used": False,
    }


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
        load_phase6_analysis_sample_membership,
    )
    return {
        "feature_matrix": load_phase6_feature_matrix(),
        "schema": load_phase6_schema(),
        "column_groups": load_phase6_column_groups(),
        "contract": load_phase6_modeling_contract(),
        "manifest": load_phase6_ready_manifest(),
        "llm_context": load_phase6_llm_context(),
        "analysis_sample_membership": load_phase6_analysis_sample_membership(),
    }


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
