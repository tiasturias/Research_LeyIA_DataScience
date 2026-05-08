"""Artefactos tecnicos de Fase 5 para consumo directo por Fase 6."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
import yaml

from _common.paths import FASE5_PHASE6_READY
from .variables import get_mvp_variable_rows, get_mvp_variables


ID_COLS = ["iso3", "country_name_canonical"]
META_COLS = [
    "entity_type",
    "region",
    "income_group",
    "n_sources_present",
    "source_list",
    "n_variables_available",
    "pct_variables_available",
    "included_in_matrix",
    "included_in_dense_candidate",
    "inclusion_notes",
]
AUDIT_COLS = ["binding_variables_used", "non_binding_variables_used", "hybrid_variables_used"]
REGULATORY_AGGREGATES = [
    "n_binding",
    "n_non_binding",
    "n_hybrid",
    "regulatory_intensity",
    "n_regulatory_mechanisms",
]
LEGACY_V1_COUNT = 40
NEW_V2_Q6_VARIABLES = [
    "oxford_e_government_delivery",
    "oxford_government_digital_policy",
    "oxford_ind_data_governance",
    "oxford_governance_ethics",
    "oecd_2_indigo_oecd_indigo_score",
    "oecd_4_digital_gov_oecd_digital_gov_overall",
]
Y_Q5_POPULATION_USAGE = [
    "anthropic_usage_pct",
    "anthropic_collaboration_pct",
    "oxford_ind_adoption_emerging_tech",
]
Y_Q6_PUBLIC_SECTOR_PRIMARY = [
    "oxford_public_sector_adoption",
    "oxford_e_government_delivery",
    "oxford_government_digital_policy",
    "oxford_ind_data_governance",
    "oecd_2_indigo_oecd_indigo_score",
]
Y_Q6_PUBLIC_SECTOR_CONTEXT = [
    "oxford_governance_ethics",
]
Y_Q6_PUBLIC_SECTOR_AUX = [
    "oecd_4_digital_gov_oecd_digital_gov_overall",
]


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _json_default(value: Any):
    if pd.isna(value):
        return None
    return value


def _variable_config() -> pd.DataFrame:
    return pd.DataFrame(get_mvp_variable_rows())


def _column_dtype(series: pd.Series) -> str:
    if pd.api.types.is_bool_dtype(series):
        return "bool"
    if pd.api.types.is_integer_dtype(series):
        return "integer"
    if pd.api.types.is_float_dtype(series):
        return "float"
    if pd.api.types.is_numeric_dtype(series):
        return "numeric"
    return "string"


def _column_kind(column: str, observed: set[str]) -> str:
    if column in ID_COLS:
        return "id"
    if column in META_COLS:
        return "metadata"
    if column in observed:
        return "observed_core"
    if column.endswith("_log") and column[:-4] in observed:
        return "log_transform"
    if column.endswith("_z"):
        return "robust_zscore"
    if column in REGULATORY_AGGREGATES:
        return "regulatory_aggregate"
    if column.startswith("iapp_categoria_obligatoriedad_") or column.startswith("iapp_modelo_gobernanza_"):
        return "one_hot"
    if column in AUDIT_COLS:
        return "audit_trace"
    return "other"


def _source_column(column: str, observed: set[str], all_columns: set[str]) -> str | None:
    if column in observed:
        return column
    if column.endswith("_log") and column[:-4] in observed:
        return column[:-4]
    if column.endswith("_z"):
        raw = column[:-2]
        if raw in all_columns:
            return raw
    if column.startswith("iapp_categoria_obligatoriedad_"):
        return "iapp_categoria_obligatoriedad"
    if column.startswith("iapp_modelo_gobernanza_"):
        return "iapp_modelo_gobernanza"
    if column in REGULATORY_AGGREGATES or column in AUDIT_COLS:
        return "binding_taxonomy.yaml"
    return None


def build_phase6_column_groups(feature_matrix: pd.DataFrame, transform_params: pd.DataFrame) -> dict[str, list[str]]:
    observed = set(get_mvp_variables())
    observed_vars = [c for c in get_mvp_variables() if c in feature_matrix.columns]
    observed_core_40 = observed_vars[:LEGACY_V1_COUNT]
    all_columns = set(feature_matrix.columns)
    numeric_cols = [
        c for c in feature_matrix.columns
        if pd.api.types.is_numeric_dtype(feature_matrix[c])
    ]
    observed_numeric = [c for c in get_mvp_variables() if c in numeric_cols]
    observed_categorical = [c for c in get_mvp_variables() if c not in numeric_cols]
    log_cols = [c for c in feature_matrix.columns if _column_kind(c, observed) == "log_transform"]
    z_cols = [c for c in feature_matrix.columns if _column_kind(c, observed) == "robust_zscore"]
    one_hot_cols = [c for c in feature_matrix.columns if _column_kind(c, observed) == "one_hot"]
    regulatory_aggregate_cols = [c for c in REGULATORY_AGGREGATES if c in all_columns]
    metadata_cols = [c for c in ID_COLS + META_COLS if c in all_columns]
    audit_cols = [c for c in AUDIT_COLS if c in all_columns]
    
    non_estimable = []
    if transform_params is not None and not transform_params.empty:
        if "used_in_primary_modeling" in transform_params.columns:
            non_estimable = transform_params.loc[
                ~transform_params["used_in_primary_modeling"], "variable_derived"
            ].dropna().tolist()

    model_exclude = metadata_cols + audit_cols + observed_categorical + non_estimable
    candidate_numeric_model_features = [
        c for c in numeric_cols
        if c not in set(model_exclude)
    ]
    cfg = _variable_config()[["variable_matriz", "rol_mvp"]].to_dict("records")
    by_role: dict[str, list[str]] = {}
    for row in cfg:
        by_role.setdefault(row["rol_mvp"], []).append(row["variable_matriz"])
    by_role["Y_Q5_population_usage"] = Y_Q5_POPULATION_USAGE
    by_role["Y_Q6_public_sector"] = Y_Q6_PUBLIC_SECTOR_PRIMARY
    by_role["Y_Q6_public_sector_context"] = Y_Q6_PUBLIC_SECTOR_CONTEXT
    by_role["Y_Q6_public_sector_aux"] = Y_Q6_PUBLIC_SECTOR_AUX

    return {
        "id_cols": [c for c in ID_COLS if c in all_columns],
        "metadata_cols": metadata_cols,
        "methodology_cols": [],
        "observed_core_40": observed_core_40,
        "observed_core_46": observed_vars,
        "observed_core_v2_added": [c for c in NEW_V2_Q6_VARIABLES if c in all_columns],
        "observed_numeric": observed_numeric,
        "observed_categorical": observed_categorical,
        "log_transform_cols": log_cols,
        "robust_zscore_cols": z_cols,
        "regulatory_aggregate_cols": regulatory_aggregate_cols,
        "one_hot_cols": one_hot_cols,
        "audit_trace_cols": audit_cols,
        "non_estimable_derived_features": non_estimable,
        "candidate_numeric_model_features": candidate_numeric_model_features,
        "model_exclude_cols_default": model_exclude,
        "excluded_from_modeling": ["iso3", "country_name_canonical", "entity_type", "region", "income_group"],
        "X1_regulatory": by_role.get("X1_regulatory", []),
        "X2_controls": by_role.get("X2_control", []),
        "Y_Q1_investment": by_role.get("Y_Q1_investment", []),
        "Y_Q2_adoption": by_role.get("Y_Q2_adoption", []),
        "Y_Q3_innovation": by_role.get("Y_Q3_innovation", []),
        "Y_Q5_population_usage": by_role.get("Y_Q5_population_usage", []),
        "Y_Q6_public_sector": by_role.get("Y_Q6_public_sector", [])
    }


def build_phase6_schema(feature_matrix: pd.DataFrame) -> pd.DataFrame:
    cfg = _variable_config().set_index("variable_matriz").to_dict("index")
    observed = set(get_mvp_variables())
    all_columns = set(feature_matrix.columns)
    rows = []
    for idx, column in enumerate(feature_matrix.columns, start=1):
        source = _source_column(column, observed, all_columns)
        source_cfg = cfg.get(source, {}) if source else {}
        rows.append({
            "ordinal": idx,
            "column": column,
            "kind": _column_kind(column, observed),
            "dtype": _column_dtype(feature_matrix[column]),
            "source_column": source,
            "rol_mvp": source_cfg.get("rol_mvp"),
            "subpregunta": source_cfg.get("subpregunta"),
            "transform_config": source_cfg.get("transform"),
            "n_non_null": int(feature_matrix[column].notna().sum()),
            "n_null": int(feature_matrix[column].isna().sum()),
            "pct_null": round(float(feature_matrix[column].isna().mean() * 100), 4),
            "unique_non_null": int(feature_matrix[column].nunique(dropna=True)),
        })
    return pd.DataFrame(rows)


def build_phase6_missingness(feature_matrix: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    col_rows = []
    for column in feature_matrix.columns:
        col_rows.append({
            "column": column,
            "n_total": int(len(feature_matrix)),
            "n_non_null": int(feature_matrix[column].notna().sum()),
            "n_null": int(feature_matrix[column].isna().sum()),
            "pct_null": round(float(feature_matrix[column].isna().mean() * 100), 4),
        })
    row_rows = []
    observed = get_mvp_variables()
    observed_core_40 = [c for c in observed[:LEGACY_V1_COUNT] if c in feature_matrix.columns]
    observed_core_46 = [c for c in observed if c in feature_matrix.columns]
    for _, row in feature_matrix.iterrows():
        row_rows.append({
            "iso3": row["iso3"],
            "country_name_canonical": row["country_name_canonical"],
            "n_null_all_columns": int(row.isna().sum()),
            "n_null_observed_core_40": int(row[observed_core_40].isna().sum()),
            "pct_null_observed_core_40": round(float(row[observed_core_40].isna().mean() * 100), 4),
            "n_null_observed_core_46": int(row[observed_core_46].isna().sum()),
            "pct_null_observed_core_46": round(float(row[observed_core_46].isna().mean() * 100), 4),
        })
    return pd.DataFrame(col_rows), pd.DataFrame(row_rows)


def build_phase6_modeling_contract(
    feature_matrix: pd.DataFrame,
    coverage: pd.DataFrame,
    variables_catalog: pd.DataFrame,
    transform_params: pd.DataFrame,
) -> dict:
    groups = build_phase6_column_groups(feature_matrix, transform_params)
    cfg = variables_catalog[["variable_matriz", "rol_mvp", "subpregunta", "transform"]].to_dict("records")
    by_role: dict[str, list[str]] = {}
    by_question: dict[str, list[str]] = {}
    for row in cfg:
        by_role.setdefault(row["rol_mvp"], []).append(row["variable_matriz"])
        by_question.setdefault(row["subpregunta"], []).append(row["variable_matriz"])
    by_role["Y_Q5_population_usage"] = Y_Q5_POPULATION_USAGE
    by_role["Y_Q6_public_sector"] = Y_Q6_PUBLIC_SECTOR_PRIMARY
    by_role["Y_Q6_public_sector_context"] = Y_Q6_PUBLIC_SECTOR_CONTEXT
    by_role["Y_Q6_public_sector_aux"] = Y_Q6_PUBLIC_SECTOR_AUX
    by_question["Q5"] = Y_Q5_POPULATION_USAGE
    by_question["Q6"] = [
        "oxford_public_sector_adoption",
        *NEW_V2_Q6_VARIABLES,
    ]
    return {
        "version": "0.3",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "fase5_version": "2.1",
        "methodology_version": "mvp-v0.2-methodology-correction-plus",
        "methodology": "inferential_comparative_observational",
        "primary_estimand": "adjusted_association",
        "grain": "country_iso3",
        "primary_key": "iso3",
        "sample_policy": {
            "n_primary_sample": 43,
            "use_holdout_test_set": False,
            "train_test_split_created": False,
            "split_column_present": False,
            "effective_n_rule": "listwise_deletion_per_model_on_required_y_x",
            "primary_analysis_scope": "full_preregistered_sample_available_by_outcome",
        },
        "validation_policy": {
            "primary_uncertainty": "bootstrap_bca_confidence_intervals",
            "internal_validation": ["repeated_kfold_cv"],
            "loocv_reporting": "developer_only_when_metric_defined",
            "robustness_phase": "FASE7",
            "external_validation_available": False,
            "leave_group_out_is_external_test": False
        },
        "transform_policy": {
            "no_imputation": True,
            "missing_values_preserved": True,
            "preserve_raw_variables": True,
            "robust_zscore_method": "median_mad",
            "zero_mad_behavior": "flag_and_exclude_non_estimable_derived_cols_from_primary_models",
            "non_estimable_transform_status_values": [
                "zero_mad_or_not_estimable",
                "constant_or_quasi_constant",
                "insufficient_non_missing_values"
            ]
        },
        "feature_policy": {
            "pca_included": False,
            "outliers_preserved": True,
            "phase6_should_not_recompute_phase5": True,
            "phase6_should_validate_contract_on_startup": True
        },
        "contract": {
            "grain": "country_iso3",
            "primary_key": "iso3",
            "n_rows": int(feature_matrix.shape[0]),
            "n_columns": int(feature_matrix.shape[1]),
            "n_observed_core_variables": len(get_mvp_variables()),
            "n_observed_core_variables_v1_0": LEGACY_V1_COUNT,
            "n_observed_core_variables_v2_added": len(NEW_V2_Q6_VARIABLES),
            "no_imputation": True,
            "missing_values_preserved": True,
            "outliers_preserved": True,
            "phase6_should_not_recompute_phase5": True,
            "backwards_compatible": True,
            "pca_included": False,
            "variable_count_label_policy": "use_46_observed_variables; legacy_40_labels_must_be_disclaimed"
        },
        "special_cases": [
            {
                "iso3": "TWN",
                "metadata_comparability": "incomplete_region_income",
                "required_flag": "has_comparable_region_income",
                "sensitivity_policy": "document_and_optionally_exclude_from_group_leave_out"
            }
        ],
        "language_policy": {
            "allowed": [
                "association",
                "adjusted association",
                "internal validation",
                "sensitivity",
                "robustness",
                "effective_n",
                "descriptive in-sample score",
                "relative positioning"
            ],
            "forbidden_without_extra_design": [
                "causal effect",
                "impacto causal",
                "external validation",
                "test set independiente",
                "independent prediction",
                "train/test split",
                "holdout externo"
            ]
        },
        "required_phase6_inputs": [
            "phase6_feature_matrix.csv",
            "phase6_schema.csv",
            "phase6_schema.json",
            "phase6_variables_catalog.csv",
            "phase6_transform_params.csv",
            "phase6_column_groups.yaml",
            "phase6_missingness_by_column.csv",
            "phase6_missingness_by_country.csv",
            "phase6_analysis_sample_membership.csv",
            "phase6_modeling_contract.yaml",
            "phase6_ready_manifest.json"
        ],
        "questions": {
            "main": "regulatory_treatment_vs_ai_ecosystem_controls",
            "Q1": "investment",
            "Q2": "adoption_business",
            "Q3": "innovation",
            "Q4": "structured_regulatory_profile_no_nlp_mvp",
            "Q5": "population_usage",
            "Q6": "public_sector_usage",
        },
        "variables_by_role": by_role,
        "variables_by_subpregunta": by_question,
        "overlap_y_variables": {
            "anthropic_usage_pct": ["Q2", "Q5"],
            "anthropic_collaboration_pct": ["Q2", "Q5"],
            "oxford_ind_adoption_emerging_tech": ["Q2", "Q5"],
            "oxford_public_sector_adoption": ["Q2", "Q6"],
        },
        "column_groups": groups,
        "coverage": {
            "min_pct_complete_observed_core_46": float(coverage["pct_complete"].min()),
            "coverage_threshold_pct": 30.0,
            "all_observed_core_vars_above_threshold": bool((~coverage["below_threshold"]).all()),
        },
        "version_notes": "v0.3 (2026-05-08): No holdout, non estimable policy. Methodology correction v2.1+.",
    }


def build_phase6_llm_context() -> dict:
    return {
        "phase": "FASE5",
        "next_phase": "FASE6",
        "fase5_version": "2.1",
        "bundle_version": "0.3",
        "artifact_type": "machine_consumable_data_preparation_bundle",
        "primary_dataset": "phase6_feature_matrix.csv",
        "required_contracts": [
            "phase6_schema.json",
            "phase6_column_groups.yaml",
            "phase6_modeling_contract.yaml",
            "phase6_ready_manifest.json",
        ],
        "preferred_api": {
            "module": "FASE5.src.api",
            "load_matrix": "load_phase6_feature_matrix",
            "load_schema": "load_phase6_schema",
            "load_groups": "load_phase6_column_groups",
            "load_contract": "load_phase6_modeling_contract",
            "load_manifest": "load_phase6_ready_manifest",
        },
        "hard_rules": {
            "do_not_recompute_phase5": True,
            "do_not_impute_in_phase5": True,
            "do_not_mutate_phase3_or_phase4": True,
            "preserve_missingness_for_phase6_model_selection": True,
            "human_audit_excel_is_not_model_input": True,
            "do_not_run_pca_in_phase5_or_phase6": True,
        },
        "minimum_load_sequence": [
            "phase6_ready_manifest.json",
            "phase6_modeling_contract.yaml",
            "phase6_column_groups.yaml",
            "phase6_schema.json",
            "phase6_feature_matrix.csv",
        ],
    }


def write_phase6_bundle(
    feature_matrix: pd.DataFrame,
    coverage: pd.DataFrame,
    variables_catalog: pd.DataFrame,
    transform_params: pd.DataFrame,
    membership: pd.DataFrame,
    output_dir: Path | None = None,
) -> dict[str, Path]:
    if output_dir is None:
        output_dir = FASE5_PHASE6_READY
    output_dir.mkdir(parents=True, exist_ok=True)

    schema = build_phase6_schema(feature_matrix)
    missing_cols, missing_rows = build_phase6_missingness(feature_matrix)
    column_groups = build_phase6_column_groups(feature_matrix, transform_params)
    modeling_contract = build_phase6_modeling_contract(feature_matrix, coverage, variables_catalog, transform_params)

    paths = {
        "phase6_feature_matrix.csv": output_dir / "phase6_feature_matrix.csv",
        "phase6_schema.csv": output_dir / "phase6_schema.csv",
        "phase6_schema.json": output_dir / "phase6_schema.json",
        "phase6_column_groups.yaml": output_dir / "phase6_column_groups.yaml",
        "phase6_modeling_contract.yaml": output_dir / "phase6_modeling_contract.yaml",
        "phase6_missingness_by_column.csv": output_dir / "phase6_missingness_by_column.csv",
        "phase6_missingness_by_country.csv": output_dir / "phase6_missingness_by_country.csv",
        "phase6_variables_catalog.csv": output_dir / "phase6_variables_catalog.csv",
        "phase6_transform_params.csv": output_dir / "phase6_transform_params.csv",
        "phase6_analysis_sample_membership.csv": output_dir / "phase6_analysis_sample_membership.csv",
        "phase6_llm_context.json": output_dir / "phase6_llm_context.json",
    }

    feature_matrix.to_csv(paths["phase6_feature_matrix.csv"], index=False)
    schema.to_csv(paths["phase6_schema.csv"], index=False)
    paths["phase6_schema.json"].write_text(
        json.dumps(schema.to_dict("records"), indent=2, ensure_ascii=False, default=_json_default),
        encoding="utf-8",
    )
    paths["phase6_column_groups.yaml"].write_text(
        yaml.safe_dump(column_groups, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    paths["phase6_modeling_contract.yaml"].write_text(
        yaml.safe_dump(modeling_contract, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    missing_cols.to_csv(paths["phase6_missingness_by_column.csv"], index=False)
    missing_rows.to_csv(paths["phase6_missingness_by_country.csv"], index=False)
    variables_catalog.to_csv(paths["phase6_variables_catalog.csv"], index=False)
    transform_params.to_csv(paths["phase6_transform_params.csv"], index=False)
    membership.to_csv(paths["phase6_analysis_sample_membership.csv"], index=False)
    paths["phase6_llm_context.json"].write_text(
        json.dumps(build_phase6_llm_context(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    manifest = {
        "version": "0.3",
        "bundle_version": "0.3",
        "fase5_version": "2.1",
        "methodology": "inferential_comparative_observational",
        "n_rows": 43,
        "n_observed_core_variables": 46,
        "contains_train_test_split": False,
        "contains_split_column": False,
        "contains_analysis_sample_membership": True,
        "contract_file": "phase6_modeling_contract.yaml",
        "membership_file": "phase6_analysis_sample_membership.csv",
        "phase6_must_validate_contract_on_startup": True,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "bundle_type": "phase6_ready_technical",
        "rules": {
            "no_imputation": True,
            "phase6_should_consume_bundle_or_fase5_api": True,
            "human_audit_excel_excluded": True,
            "pca_included": False,
            "backwards_compatible": True,
        },
        "files": {
            name: {
                "path": str(path.relative_to(output_dir)),
                "sha256": _sha256_file(path),
                "bytes": path.stat().st_size,
            }
            for name, path in paths.items()
        },
    }
    manifest_path = output_dir / "phase6_ready_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    paths["phase6_ready_manifest.json"] = manifest_path

    # Anti-regression checks on phase6 outputs directly
    for k in ["phase6_feature_matrix.csv", "phase6_schema.csv", "phase6_column_groups.yaml"]:
        p = paths[k]
        content = p.read_text().lower()
        if "split" in content:
             # Ensure the word 'split' is not used as a column or artifact
             if k == "phase6_feature_matrix.csv" and "split" in pd.read_csv(p).columns:
                 raise ValueError("Forbidden column 'split' found in phase6 feature matrix.")
             if k == "phase6_column_groups.yaml" and "split_col" in content:
                 raise ValueError("Forbidden 'split' artifacts in column groups.")

    return paths
