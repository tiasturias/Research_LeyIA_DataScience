"""Orquestador Fase 5 MVP: construye feature matrix y Excel auditable."""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from _common.load import fase3_version, load_dictionary, load_wide
from _common.paths import FASE3_ROOT, FASE4_ROOT, FASE5_OUTPUTS, FASE5_ROOT, MVP_ROOT
from .audit_excel import write_audit_excel
from .engineer import build_feature_matrix
from .phase6_bundle import write_phase6_bundle
from .sample import filter_to_mvp_sample, get_mvp_entities_detail, get_mvp_iso3
from .transform import apply_transforms, compute_transform_params
from .variables import (
    build_variable_catalog,
    filter_to_mvp_variables,
    get_mvp_variables,
    validate_coverage,
    validate_mvp_variables_exist,
)

AI_LEADERS = {"USA", "CHN", "SGP", "ARE", "IRL", "ISR", "KOR", "JPN"}
LARGE_AI_POWERS = {"USA", "CHN", "IND", "JPN"}
LATAM_PEERS = {"ARG", "BRA", "CHL", "COL", "CRI", "MEX", "PER", "URY"}
EU_LAGGARDS = {"GRC", "ROU", "HRV"}

FORBIDDEN_MEMBERSHIP_COLUMNS = {
    "split", "train", "test", "holdout", "fold", "partition", "set"
}

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def build_analysis_sample_membership(feature_matrix: pd.DataFrame) -> pd.DataFrame:
    """Documenta muestra primaria y flags de sensibilidad. No es split."""
    required = ["iso3", "country_name_canonical"]
    for col in required:
        if col not in feature_matrix.columns:
            raise ValueError(f"Missing required column for membership: {col}")

    optional = ["region", "income_group"]
    cols = required + [c for c in optional if c in feature_matrix.columns]
    membership = feature_matrix[cols].copy()

    membership["is_primary_analysis_sample"] = True
    membership["sample_inclusion_category"] = "mvp_preregistered"
    membership["inclusion_reason"] = "Included in preregistered 43-country MVP sample"
    membership["is_chile_focal"] = membership["iso3"].eq("CHL")
    membership["is_ai_leader_sensitivity"] = membership["iso3"].isin(AI_LEADERS)
    membership["is_large_ai_power_sensitivity"] = membership["iso3"].isin(LARGE_AI_POWERS)
    membership["is_latam_peer_sensitivity"] = membership["iso3"].isin(LATAM_PEERS)
    membership["is_eu_laggard_sensitivity"] = membership["iso3"].isin(EU_LAGGARDS)
    membership["is_eu_member_or_laggard_sensitivity"] = membership["is_eu_laggard_sensitivity"]

    if "region" not in membership.columns:
        membership["region"] = pd.NA
    if "income_group" not in membership.columns:
        membership["income_group"] = pd.NA

    membership["has_comparable_region_income"] = membership["region"].notna() & membership["income_group"].notna()
    membership["leave_group_region"] = membership["region"]
    membership["leave_group_income"] = membership["income_group"]
    membership["special_case_flag"] = "none"
    membership.loc[~membership["has_comparable_region_income"], "special_case_flag"] = "metadata_incomplete"
    membership["notes"] = "Primary analysis sample; sensitivity flags only; particiones predictivas eliminadas."

    forbidden = FORBIDDEN_MEMBERSHIP_COLUMNS.intersection(set(membership.columns))
    if forbidden:
        raise ValueError(f"Forbidden membership columns present: {sorted(forbidden)}")

    if len(membership) != 43:
        raise ValueError(f"Expected 43 countries, got {len(membership)}")
    if membership["iso3"].nunique() != 43:
        raise ValueError("Expected 43 unique ISO3 codes")
    if "CHL" not in set(membership["iso3"]):
        raise ValueError("CHL must be present in analysis sample membership")

    return membership

def _write_manifest(outputs: dict[str, Path]) -> None:
    try:
        git_sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(MVP_ROOT.parent), stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        git_sha = "unknown"

    n_observed = len(get_mvp_variables())
    manifest = {
        "version": "2.1",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "git_sha": git_sha,
        "fase3_version": fase3_version(),
        "fase5_version": "2.1",
        "methodology_version": "mvp-v0.2-methodology-correction-plus",
        "methodology": "inferential_comparative_observational",
        "primary_estimand": "adjusted_association",
        "n_primary_sample": 43,
        "n_observed_core_variables": 46,
        "train_test_split_created": False,
        "split_column_present": False,
        "holdout_used": False,
        "analysis_sample_membership_created": True,
        "phase6_ready_bundle_created": True,
        "non_estimable_transforms_flagged": True,
        "non_estimable_transforms_excluded_from_primary_groups": True,
        "workbook_holdout_language_removed": True,
        "no_imputation": True,
        "missing_values_preserved": True,
        "outliers_preserved": True,
        "inputs_hashed": {},
        "phase5_implementation_hashed": {},
        "outputs_hashed": {},
        "rules": {
            "phase3_phase4_immutable": True,
            "no_imputation": True,
            "n_mvp_entities": 43,
            "n_observed_core_variables": n_observed,
            "backwards_compatible_with_v1_0": True,
            "pca_included": False,
        },
    }
    for root in [FASE3_ROOT / "outputs", FASE4_ROOT / "outputs" / "eda_principal"]:
        for p in sorted(root.glob("*")):
            if p.is_file() and p.suffix.lower() in {".csv", ".json", ".yaml", ".md", ".xlsx", ".html"}:
                manifest["inputs_hashed"][str(p.relative_to(MVP_ROOT.parent))] = {
                    "sha256": sha256_file(p),
                    "bytes": p.stat().st_size,
                }
    for root in [FASE5_ROOT / "config", FASE5_ROOT / "src", FASE5_ROOT / "tests"]:
        for p in sorted(root.rglob("*")):
            if p.is_file() and p.suffix.lower() in {".py", ".yaml", ".yml"}:
                manifest["phase5_implementation_hashed"][str(p.relative_to(MVP_ROOT))] = {
                    "sha256": sha256_file(p),
                    "bytes": p.stat().st_size,
                }
    for name, path in outputs.items():
        manifest["outputs_hashed"][name] = {
            "path": str(path.relative_to(MVP_ROOT)),
            "sha256": sha256_file(path),
            "bytes": path.stat().st_size,
        }
    
    # Required top level outputs hash by instructions
    manifest["outputs"] = {
        name: metadata["sha256"] for name, metadata in manifest["outputs_hashed"].items()
    }

    for target in [FASE5_OUTPUTS / "fase5_manifest.json", MVP_ROOT / "manifest_mvp.json"]:
        with open(target, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)


def build_phase5(save: bool = True) -> dict[str, pd.DataFrame | str]:
    FASE5_OUTPUTS.mkdir(parents=True, exist_ok=True)
    wide = load_wide()
    dictionary = load_dictionary()

    if wide.shape != (199, 1218):
        raise ValueError(f"Wide shape inesperado: {wide.shape}")
    if not wide["entity_type"].eq("country_iso3").all():
        raise ValueError("Wide contiene entidades no country_iso3")
    validate_mvp_variables_exist(dictionary)

    wide_mvp = filter_to_mvp_sample(wide)
    curated = filter_to_mvp_variables(wide_mvp)
    coverage = validate_coverage(curated)
    transformed = apply_transforms(curated, get_mvp_variables())
    transform_params = compute_transform_params(transformed, get_mvp_variables())
    feature_matrix = build_feature_matrix(wide_mvp, curated, transformed)
    
    assert "split" not in feature_matrix.columns
    assert len(feature_matrix) == 43
    assert feature_matrix["iso3"].nunique() == 43

    membership = build_analysis_sample_membership(feature_matrix)

    countries = get_mvp_entities_detail().merge(
        wide_mvp[["iso3", "country_name_canonical", "region", "income_group"]],
        on="iso3",
        how="left",
    )
    variables_catalog = build_variable_catalog(dictionary)

    if coverage["below_threshold"].any():
        below = coverage.loc[coverage["below_threshold"], ["variable_matriz", "pct_complete"]]
        raise ValueError(f"Variables bajo 30% cobertura en muestra MVP:\n{below}")

    outputs: dict[str, Path] = {}
    if save:
        paths = {
            "feature_matrix_mvp.csv": FASE5_OUTPUTS / "feature_matrix_mvp.csv",
            "coverage_report_mvp.csv": FASE5_OUTPUTS / "coverage_report_mvp.csv",
            "mvp_countries.csv": FASE5_OUTPUTS / "mvp_countries.csv",
            "mvp_variables_catalog.csv": FASE5_OUTPUTS / "mvp_variables_catalog.csv",
            "mvp_transform_params.csv": FASE5_OUTPUTS / "mvp_transform_params.csv",
            "analysis_sample_membership.csv": FASE5_OUTPUTS / "analysis_sample_membership.csv",
        }
        feature_matrix.to_csv(paths["feature_matrix_mvp.csv"], index=False)
        coverage.to_csv(paths["coverage_report_mvp.csv"], index=False)
        countries.to_csv(paths["mvp_countries.csv"], index=False)
        variables_catalog.to_csv(paths["mvp_variables_catalog.csv"], index=False)
        transform_params.to_csv(paths["mvp_transform_params.csv"], index=False)
        membership.to_csv(paths["analysis_sample_membership.csv"], index=False)
        
        excel_path = Path(write_audit_excel(wide_mvp, feature_matrix, coverage, transform_params, membership=membership))
        paths["MVP_AUDITABLE.xlsx"] = excel_path
        
        phase6_paths = write_phase6_bundle(
            feature_matrix=feature_matrix,
            coverage=coverage,
            variables_catalog=variables_catalog,
            transform_params=transform_params,
            membership=membership,
        )
        paths.update({f"phase6_ready/{name}": path for name, path in phase6_paths.items()})
        outputs = paths
        _write_manifest(outputs)

    return {
        "wide_mvp": wide_mvp,
        "curated": curated,
        "coverage": coverage,
        "feature_matrix": feature_matrix,
        "countries": countries,
        "variables_catalog": variables_catalog,
        "transform_params": transform_params,
        "membership": membership,
        "excel_path": str(FASE5_OUTPUTS / "MVP_AUDITABLE.xlsx"),
    }


def main() -> None:
    results = build_phase5(save=True)
    fm = results["feature_matrix"]
    print("Fase 5 MVP build completed")
    print(f"feature_matrix_mvp.csv: {fm.shape[0]} filas x {fm.shape[1]} columnas")
    print(f"Excel auditable: {results['excel_path']}")


if __name__ == "__main__":
    main()
