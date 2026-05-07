from __future__ import annotations

import pandas as pd

from FASE5.src.transform import get_log_variables
from FASE5.src.variables import get_mvp_variables


def _by_iso3(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values("iso3").set_index("iso3")


def test_original_mvp_variables_preserve_missingness(phase5_results):
    curated = _by_iso3(phase5_results["curated"])
    feature_matrix = _by_iso3(phase5_results["feature_matrix"])

    for variable in get_mvp_variables():
        assert variable in feature_matrix.columns
        assert feature_matrix[variable].isna().equals(curated[variable].isna()), variable


def test_log_and_zscore_features_preserve_source_missingness(phase5_results):
    feature_matrix = _by_iso3(phase5_results["feature_matrix"])

    for variable in get_log_variables():
        log_col = f"{variable}_log"
        if log_col in feature_matrix.columns:
            assert feature_matrix[log_col].isna().equals(feature_matrix[variable].isna()), log_col

    for source_col in list(feature_matrix.columns):
        z_col = f"{source_col}_z"
        if z_col in feature_matrix.columns:
            assert feature_matrix[z_col].isna().equals(feature_matrix[source_col].isna()), z_col


def test_feature_matrix_does_not_embed_transform_metadata_columns(phase5_results):
    feature_matrix = phase5_results["feature_matrix"]

    assert not any(col.endswith("_transform_method") for col in feature_matrix.columns)
