"""API pública de Fase 4 para consumo en Fase 5+."""

from __future__ import annotations

import pandas as pd
import yaml

from .config import CONFIG_DIR, OUTPUTS_DIR


def _load_csv(name: str) -> pd.DataFrame:
    path = OUTPUTS_DIR / f"{name}.csv"
    if not path.exists():
        raise FileNotFoundError(f"Output {name}.csv no existe. Ejecutar build-all primero.")
    return pd.read_csv(path)


def load_eda_results(name: str) -> pd.DataFrame:
    """Carga cualquier output de Fase 4 por nombre (sin .csv)."""
    return _load_csv(name)


def load_candidates() -> pd.DataFrame:
    """Variables candidatas clasificadas para Feature Engineering."""
    return _load_csv("eda_candidates_for_feature_engineering")


def load_submuestras() -> pd.DataFrame:
    """Resumen de las 6 submuestras candidatas."""
    return _load_csv("eda_submuestras_candidatas")


def load_submuestra_membership() -> pd.DataFrame:
    """Matriz pais × submuestra (1 = pertenece)."""
    return _load_csv("eda_submuestra_membership")


def load_country_profiles() -> pd.DataFrame:
    return _load_csv("eda_country_profiles")


def load_chile_profile() -> pd.DataFrame:
    return _load_csv("eda_chile_profile")


def load_chile_vs_peers() -> pd.DataFrame:
    return _load_csv("eda_chile_vs_peers")


def load_inter_block_correlations() -> pd.DataFrame:
    return _load_csv("eda_inter_block_correlations")


def load_redundancy_report() -> pd.DataFrame:
    return _load_csv("eda_redundancy_report")


def load_question_mapping(question: str | None = None) -> pd.DataFrame | dict:
    """Carga outputs de mapeo por sub-pregunta o el YAML preregistrado."""
    if question is None:
        path = CONFIG_DIR / "question_mapping.yaml"
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    mapping = {
        "Q1_investment": "eda_question_q1_investment",
        "Q2_adoption": "eda_question_q2_adoption",
        "Q3_innovation": "eda_question_q3_innovation",
        "Q4_content": "eda_question_q4_content",
        "viability": "eda_question_viability",
    }
    return _load_csv(mapping.get(question, question))


def load_taxonomy(kind: str = "binding") -> pd.DataFrame | dict:
    """Carga taxonomías exploratorias o sus clasificaciones generadas."""
    if kind == "binding":
        return _load_csv("eda_binding_classification")
    if kind == "enabling":
        return _load_csv("eda_enabling_classification")
    path = CONFIG_DIR / f"{kind}_taxonomy.yaml"
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    raise FileNotFoundError(f"Taxonomía desconocida: {kind}")


def list_versions() -> list[str]:
    from . import __version__
    return [__version__]
