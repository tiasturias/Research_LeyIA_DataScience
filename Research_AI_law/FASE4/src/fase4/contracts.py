"""Bloque A: contrato de datos e inmutabilidad de Fase 3."""

from __future__ import annotations

import pandas as pd

from .config import BLOCKS, FASE3_OUTPUTS, OUTPUTS_DIR, sha256_file
from .load import current_version, load_dictionary, load_wide


def build_contract_check(wide: pd.DataFrame, dictionary: pd.DataFrame) -> pd.DataFrame:
    """Checks mínimos preregistrados para habilitar Fase 4."""
    checks = [
        {
            "check_id": "A001",
            "check": "fase3_current_version_1x",
            "expected": "1.x",
            "observed": current_version(),
            "passed": str(current_version()).startswith("1."),
        },
        {
            "check_id": "A002",
            "check": "wide_n_countries",
            "expected": "199",
            "observed": str(wide.shape[0]),
            "passed": wide.shape[0] == 199,
        },
        {
            "check_id": "A003",
            "check": "wide_n_columns",
            "expected": "1203",
            "observed": str(wide.shape[1]),
            "passed": wide.shape[1] == 1203,
        },
        {
            "check_id": "A004",
            "check": "all_entity_type_country_iso3",
            "expected": "all country_iso3",
            "observed": str(wide.get("entity_type", pd.Series(dtype=str)).dropna().unique().tolist()),
            "passed": "entity_type" in wide.columns and wide["entity_type"].eq("country_iso3").all(),
        },
        {
            "check_id": "A005",
            "check": "chile_present",
            "expected": "CHL present",
            "observed": str("CHL" in wide.get("iso3", pd.Series(dtype=str)).values),
            "passed": "iso3" in wide.columns and "CHL" in wide["iso3"].values,
        },
    ]
    for block in BLOCKS:
        checks.append({
            "check_id": f"A_BLOCK_{block}",
            "check": f"dictionary_has_{block}",
            "expected": "present",
            "observed": str((dictionary["bloque_tematico"] == block).sum()),
            "passed": bool((dictionary["bloque_tematico"] == block).any()),
        })
    return pd.DataFrame(checks)


def build_fase3_hashes() -> pd.DataFrame:
    """Hash de outputs Fase 3 sin modificar sus archivos."""
    rows = []
    for p in sorted(FASE3_OUTPUTS.glob("*")):
        if p.is_file() and p.suffix.lower() in {".csv", ".json", ".xlsx", ".md"}:
            rows.append({
                "file": p.name,
                "sha256": sha256_file(p),
                "bytes": p.stat().st_size,
            })
    return pd.DataFrame(rows)


def run_contracts(
    wide: pd.DataFrame | None = None,
    dictionary: pd.DataFrame | None = None,
    save: bool = True,
) -> dict[str, pd.DataFrame]:
    if wide is None:
        wide = load_wide()
    if dictionary is None:
        dictionary = load_dictionary()
    results = {
        "contract_check": build_contract_check(wide, dictionary),
        "fase3_input_hashes": build_fase3_hashes(),
    }
    if save:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        for name, df in results.items():
            df.to_csv(OUTPUTS_DIR / f"{name}.csv", index=False)
    return results
