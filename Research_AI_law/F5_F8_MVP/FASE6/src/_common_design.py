from dataclasses import dataclass
import pandas as pd

@dataclass(frozen=True)
class ModelDesign:
    question: str
    outcome: str
    predictors: list[str]
    controls: list[str]
    model_family: str
    analysis_role: str = "primary"
    scale: str | None = None


def build_model_frame(
    fm: pd.DataFrame,
    design: ModelDesign,
    min_n: int = 15,
) -> tuple[pd.DataFrame, dict]:
    """Construye la muestra efectiva por outcome sin imputación y sin split."""
    if "split" in fm.columns:
        raise RuntimeError("Fase 6 no acepta columna split.")

    required = ["iso3", design.outcome] + list(design.predictors) + list(design.controls)
    missing_cols = [c for c in required if c not in fm.columns]
    if missing_cols:
        return pd.DataFrame(), {
            "question": design.question,
            "outcome": design.outcome,
            "status": "missing_required_columns",
            "missing_columns": ";".join(missing_cols),
            "n_effective": 0,
        }

    raw = fm[required].copy()
    n_primary = len(raw)
    n_missing_outcome = raw[design.outcome].isna().sum()
    n_missing_predictors = raw[design.predictors + design.controls].isna().any(axis=1).sum()

    sub = raw.dropna(subset=[design.outcome] + design.predictors + design.controls).copy()
    n_effective = len(sub)

    meta = {
        "question": design.question,
        "outcome": design.outcome,
        "model_family": design.model_family,
        "analysis_role": design.analysis_role,
        "n_primary_sample": n_primary,
        "n_effective": n_effective,
        "n_missing_outcome": int(n_missing_outcome),
        "n_missing_predictors": int(n_missing_predictors),
        "missingness_policy": "listwise_deletion_on_required_y_x_no_imputation",
        "analysis_scope": "full_preregistered_sample_available_by_outcome",
        "validation_scope": "internal_resampling_not_external_test",
        "holdout_used": False,
        "status": "ok" if n_effective >= min_n else "low_n_exploratory_only",
    }
    return sub, meta
