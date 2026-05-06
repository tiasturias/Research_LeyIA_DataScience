"""Orchestrator for the FASE3 Matriz Madre pipeline."""

from __future__ import annotations

from pathlib import Path
import warnings

import pandas as pd
from pandas.errors import PerformanceWarning

from .config import OUTPUT_DIR
from .extract import extract_all
from .export import write_outputs
from .geo import build_microsoft_crosswalk, build_universe
from .quality import traceability_issues
from .schemas import validate_core
from .transform import build_dictionary, build_snapshot, build_wide_and_traceability


def build_all(validate: bool = True) -> dict[str, pd.DataFrame]:
    warnings.filterwarnings("ignore", category=PerformanceWarning)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ms_crosswalk = build_microsoft_crosswalk()
    universe = build_universe(ms_crosswalk)
    panel = extract_all()
    snapshot = build_snapshot(panel)
    panel, snapshot = _apply_sample_verification(panel, snapshot)
    dictionary = build_dictionary(panel, snapshot, universe)

    allowed = set(dictionary["variable_matriz"])
    panel = panel[panel["variable_matriz"].isin(allowed)].reset_index(drop=True)
    snapshot = snapshot[snapshot["variable_matriz"].isin(allowed)].reset_index(drop=True)

    wide, trace = build_wide_and_traceability(snapshot, universe)

    if validate:
        validate_core(panel, snapshot, dictionary, trace)
        issues = traceability_issues(wide, panel, trace)
        if issues:
            raise ValueError("Blocking traceability issues: " + "; ".join(issues))
        _validate_dictionary_fk(panel, snapshot, wide, dictionary)
        _validate_wide_universe(wide)

    write_outputs(
        panel=panel,
        snapshot=snapshot,
        wide=wide,
        trace=trace,
        dictionary=dictionary,
        universe=universe,
        ms_crosswalk=ms_crosswalk,
    )
    return {
        "panel": panel,
        "snapshot": snapshot,
        "wide": wide,
        "traceability": trace,
        "dictionary": dictionary,
        "universe": universe,
        "microsoft_crosswalk": ms_crosswalk,
    }


def _validate_dictionary_fk(panel: pd.DataFrame, snapshot: pd.DataFrame, wide: pd.DataFrame, dictionary: pd.DataFrame) -> None:
    dict_vars = set(dictionary["variable_matriz"])
    panel_missing = set(panel["variable_matriz"]) - dict_vars
    snapshot_missing = set(snapshot["variable_matriz"]) - dict_vars
    id_cols = {
        "iso3", "country_name_canonical", "entity_type", "region", "income_group",
        "n_sources_present", "source_list", "n_variables_available", "pct_variables_available",
        "included_in_matrix", "included_in_dense_candidate", "inclusion_notes",
    }
    wide_vars = {c for c in wide.columns if c not in id_cols and not c.endswith("_confidence") and not c.endswith("_year_used")}
    wide_missing = wide_vars - dict_vars
    if panel_missing or snapshot_missing or wide_missing:
        raise ValueError(f"Dictionary FK failure: panel={len(panel_missing)}, snapshot={len(snapshot_missing)}, wide={len(wide_missing)}")


def _validate_wide_universe(wide: pd.DataFrame) -> None:
    bad_types = set(wide["entity_type"].dropna().unique()) - {"country_iso3"}
    if bad_types:
        raise ValueError(f"Wide contains non-country entity types: {bad_types}")
    if wide["iso3"].isin(["EU", "EUU", "WLD", "WORLD"]).any():
        raise ValueError("Wide contains EU/global aggregate")
    if "n_variables_available" in wide and wide["n_variables_available"].le(0).any():
        raise ValueError("Wide contains entities with zero analytical values")


def _apply_sample_verification(panel: pd.DataFrame, snapshot: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    verified_variables = {
        "ms_h2_2025_ai_diffusion_pct", "ms_h1_2025_ai_diffusion_pct", "ms_change_pp",
        "oxford_total_score", "wipo_gii_score", "wb_gdp_current_usd", "iapp_ley_ia_vigente",
    }
    mask = snapshot["iso3"].eq("CHL") & snapshot["variable_matriz"].isin(verified_variables)
    verified_ids = set(snapshot.loc[mask, "cell_id"])
    snapshot = snapshot.copy()
    panel = panel.copy()
    snapshot.loc[mask, "confidence_level"] = "verified"
    panel.loc[panel["cell_id"].isin(verified_ids), "confidence_level"] = "verified"
    return panel, snapshot


if __name__ == "__main__":
    outputs = build_all(validate=True)
    for key, df in outputs.items():
        print(f"{key}: {df.shape}")
