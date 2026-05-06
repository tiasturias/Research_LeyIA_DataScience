"""Bloque L: Generador de 6 submuestras candidatas (multiverse analysis)."""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import BLOCKS, OUTPUTS_DIR, get_peer_groups, get_thresholds
from .load import get_block_var_cols, get_variable_cols, load_dictionary, load_wide


def _gower_distance_to_chile(
    wide: pd.DataFrame,
    dictionary: pd.DataFrame,
    control_blocks: list[str],
) -> pd.Series:
    """Distancia simplificada de Gower entre cada país y Chile en los bloques de control."""
    b_cols = []
    for block in control_blocks:
        b_cols += get_block_var_cols(block, wide, dictionary)
    b_num = [c for c in b_cols if pd.api.types.is_numeric_dtype(wide[c])]

    if not b_num or "CHL" not in wide["iso3"].values:
        return pd.Series(np.nan, index=wide.index)

    # Normalizar variables al rango [0,1] por variable
    sub = wide[b_num].copy()
    for col in b_num:
        mn, mx = sub[col].min(), sub[col].max()
        if mx > mn:
            sub[col] = (sub[col] - mn) / (mx - mn)
        else:
            sub[col] = 0.0

    chile_idx = wide[wide["iso3"] == "CHL"].index[0]
    chile_row = sub.loc[chile_idx]

    distances = sub.apply(
        lambda row: (row - chile_row).abs().mean(), axis=1
    )
    return distances


def build_submuestras(
    wide: pd.DataFrame,
    dictionary: pd.DataFrame,
    coverage_by_country: pd.DataFrame | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Construye las 6 submuestras candidatas.

    Returns (summary_df, membership_df)
    """
    thresholds = get_thresholds()
    peers = get_peer_groups()
    densa_80 = thresholds["submuestras"]["densa_80"]
    densa_60 = thresholds["submuestras"]["densa_60"]
    k_chile = thresholds["submuestras"]["comparable_chile_top_k"]

    var_cols = get_variable_cols(wide, dictionary)
    n_vars = len(var_cols)

    # Cobertura por país
    pct_avail = wide[var_cols].notna().sum(axis=1) / n_vars

    # IAPP variables para submuestra "regulada"
    iapp_vars = [c for c in var_cols if c.startswith("iapp_")]

    # Distancia de Gower a Chile
    control_blocks = ["socioeconomic_control", "institutional_control", "tech_infrastructure_control"]
    distances = _gower_distance_to_chile(wide, dictionary, control_blocks)

    # 1. densa_80
    mask_80 = pct_avail >= densa_80
    # 2. densa_60
    mask_60 = pct_avail >= densa_60
    # 3. regulada (al menos 1 IAPP no nulo)
    if iapp_vars:
        mask_reg = wide[iapp_vars].notna().any(axis=1)
    else:
        mask_reg = pd.Series(False, index=wide.index)
    # 4. comparable_chile (top-K por distancia de Gower)
    sorted_dist = distances.sort_values()
    top_k_idx = sorted_dist.iloc[:k_chile].index
    mask_chile = pd.Series(False, index=wide.index)
    mask_chile.loc[top_k_idx] = True
    # 5. oecd_plus_latam
    oecd_iso3 = set(peers.get("oecd_subset", []))
    latam_iso3 = set(peers.get("latam", []))
    oecd_latam = oecd_iso3 | latam_iso3
    mask_oecd = wide["iso3"].isin(oecd_latam)
    # 6. full
    mask_full = pd.Series(True, index=wide.index)

    submuestras = {
        "densa_80": mask_80,
        "densa_60": mask_60,
        "regulada": mask_reg,
        "comparable_chile": mask_chile,
        "oecd_plus_latam": mask_oecd,
        "full": mask_full,
    }

    key_countries = peers.get("key_countries_must_be_present", ["USA", "CHL", "SGP", "ARE", "IRL"])

    # Membership matrix
    membership = wide[["iso3", "country_name_canonical", "region", "income_group"]].copy()
    for name, mask in submuestras.items():
        membership[name] = mask.astype(int)

    # Summary
    summary_rows = []
    for name, mask in submuestras.items():
        sub_iso3 = wide.loc[mask, "iso3"].tolist()
        n = len(sub_iso3)
        # Cobertura por bloque en la submuestra
        block_cov = {}
        for block in BLOCKS:
            b_cols = get_block_var_cols(block, wide, dictionary)
            b_num = [c for c in b_cols if pd.api.types.is_numeric_dtype(wide[c])]
            if b_num:
                bc = wide.loc[mask, b_num].notna().mean().mean() * 100
            else:
                bc = 0.0
            block_cov[f"cov_{block}"] = round(bc, 2)

        summary_rows.append({
            "submuestra": name,
            "n_countries": n,
            "chile_present": "CHL" in sub_iso3,
            "key_countries_present": sum(k in sub_iso3 for k in key_countries),
            "key_countries_total": len(key_countries),
            "pct_coverage_mean": round(pct_avail[mask].mean() * 100, 2),
            "criterion": _describe_criterion(name, densa_80, densa_60, k_chile),
            **block_cov,
        })

    return pd.DataFrame(summary_rows), membership


def _describe_criterion(name: str, d80: float, d60: float, k: int) -> str:
    return {
        "densa_80": f"pct_variables_available >= {d80*100:.0f}%",
        "densa_60": f"pct_variables_available >= {d60*100:.0f}%",
        "regulada": "al menos 1 variable IAPP no nula",
        "comparable_chile": f"top-{k} países por distancia de Gower a Chile (bloques de control)",
        "oecd_plus_latam": "OECD + LATAM (lista cerrada preregistrada)",
        "full": "todos los países soberanos (country_iso3)",
    }.get(name, "")


def run_submuestras_analysis(
    wide: pd.DataFrame | None = None,
    dictionary: pd.DataFrame | None = None,
    save: bool = True,
) -> dict[str, pd.DataFrame]:
    if wide is None:
        wide = load_wide()
    if dictionary is None:
        dictionary = load_dictionary()

    summary, membership = build_submuestras(wide, dictionary)
    results = {
        "eda_submuestras_candidatas": summary,
        "eda_submuestra_membership": membership,
    }

    if save:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        for name, df in results.items():
            df.to_csv(OUTPUTS_DIR / f"{name}.csv", index=False)

    return results
