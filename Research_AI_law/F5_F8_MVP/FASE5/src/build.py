"""Orquestador Fase 5 MVP: construye feature matrix y Excel auditable."""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

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


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _build_split(feature_matrix: pd.DataFrame) -> pd.DataFrame:
    split_df = feature_matrix[["iso3", "country_name_canonical", "region"]].copy()
    stratify = split_df["region"] if split_df["region"].value_counts().min() >= 2 else None
    train_idx, test_idx = train_test_split(
        split_df.index,
        test_size=0.20,
        random_state=42,
        stratify=stratify,
    )
    split_df["split"] = "train"
    split_df.loc[test_idx, "split"] = "test"
    return split_df


def _write_manifest(outputs: dict[str, Path]) -> None:
    try:
        git_sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(MVP_ROOT.parent), stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        git_sha = "unknown"

    n_observed = len(get_mvp_variables())
    manifest = {
        "version": "2.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "git_sha": git_sha,
        "fase3_version": fase3_version(),
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

    for target in [FASE5_OUTPUTS / "fase5_manifest.json", MVP_ROOT / "manifest_mvp.json"]:
        with open(target, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)


def build_phase5(save: bool = True) -> dict[str, pd.DataFrame | str]:
    FASE5_OUTPUTS.mkdir(parents=True, exist_ok=True)
    wide = load_wide()
    dictionary = load_dictionary()

    if wide.shape != (199, 1203):
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
    split = _build_split(feature_matrix)
    feature_matrix = feature_matrix.merge(split[["iso3", "split"]], on="iso3", how="left")

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
            "mvp_train_test_split.csv": FASE5_OUTPUTS / "mvp_train_test_split.csv",
        }
        feature_matrix.to_csv(paths["feature_matrix_mvp.csv"], index=False)
        coverage.to_csv(paths["coverage_report_mvp.csv"], index=False)
        countries.to_csv(paths["mvp_countries.csv"], index=False)
        variables_catalog.to_csv(paths["mvp_variables_catalog.csv"], index=False)
        transform_params.to_csv(paths["mvp_transform_params.csv"], index=False)
        split.to_csv(paths["mvp_train_test_split.csv"], index=False)
        excel_path = Path(write_audit_excel(wide_mvp, feature_matrix, coverage, transform_params))
        paths["MVP_AUDITABLE.xlsx"] = excel_path
        phase6_paths = write_phase6_bundle(
            feature_matrix=feature_matrix,
            coverage=coverage,
            variables_catalog=variables_catalog,
            transform_params=transform_params,
            split=split,
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
        "split": split,
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
