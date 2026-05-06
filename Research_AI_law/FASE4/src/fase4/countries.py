"""Bloque I: Perfiles de país, Chile focal, deep dives SGP/ARE/IRL."""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import BLOCKS, OUTPUTS_DIR
from .load import get_block_var_cols, load_dictionary, load_wide


def _robust_zscore(series: pd.Series) -> pd.Series:
    """Z-score robusto usando mediana y MAD."""
    s = series.copy()
    med = s.median()
    mad = (s - med).abs().median()
    if mad == 0:
        return pd.Series(np.where(s != med, np.nan, 0.0), index=s.index)
    return (s - med) / mad


def compute_country_profiles(
    wide: pd.DataFrame, dictionary: pd.DataFrame
) -> pd.DataFrame:
    """Z-scores robustos por bloque para cada país."""
    id_cols = ["iso3", "country_name_canonical", "region", "income_group",
               "n_sources_present", "included_in_dense_candidate"]
    profiles = wide[[c for c in id_cols if c in wide.columns]].copy()

    for block in BLOCKS:
        b_cols = get_block_var_cols(block, wide, dictionary)
        b_num = [c for c in b_cols if pd.api.types.is_numeric_dtype(wide[c])]
        if not b_num:
            profiles[f"zscore_{block}_mean"] = np.nan
            profiles[f"pct_coverage_{block}"] = 0.0
            continue

        # Z-score robusto por variable, luego promedio
        zscores = pd.DataFrame({c: _robust_zscore(wide[c]) for c in b_num})
        profiles[f"zscore_{block}_mean"] = zscores.mean(axis=1).round(4)
        profiles[f"pct_coverage_{block}"] = (wide[b_num].notna().sum(axis=1) / len(b_num) * 100).round(2)

    # Ranking global por bloque
    for block in BLOCKS:
        col = f"zscore_{block}_mean"
        if col in profiles:
            profiles[f"rank_{block}"] = profiles[col].rank(ascending=False, method="min").astype("Int64")

    return profiles.sort_values("zscore_ecosystem_outcome_mean", ascending=False, na_position="last").reset_index(drop=True)


def compute_chile_profile(
    wide: pd.DataFrame,
    dictionary: pd.DataFrame,
    country_profiles: pd.DataFrame,
) -> dict:
    """Perfil detallado de Chile: valores por bloque, rankings, fortalezas, debilidades."""
    chile_row = wide[wide["iso3"] == "CHL"]
    if chile_row.empty:
        return {}

    profile = {"iso3": "CHL", "country_name": "Chile"}
    chile_idx = chile_row.index[0]

    for block in BLOCKS:
        b_cols = get_block_var_cols(block, wide, dictionary)
        b_num = [c for c in b_cols if pd.api.types.is_numeric_dtype(wide[c])]
        if not b_num:
            continue

        # Percentiles de Chile en cada variable del bloque
        pcts = []
        for col in b_num:
            val = wide[col].iloc[chile_idx]
            if pd.isna(val):
                continue
            pct = (wide[col] <= val).sum() / wide[col].notna().sum() * 100
            pcts.append(pct)

        profile[f"n_vars_{block}"] = len(b_num)
        profile[f"n_data_{block}"] = int(wide.loc[chile_idx, b_num].notna().sum())
        profile[f"pct_coverage_{block}"] = round(profile[f"n_data_{block}"] / len(b_num) * 100, 2)
        profile[f"avg_percentile_{block}"] = round(float(np.mean(pcts)), 2) if pcts else np.nan

        z_col = f"zscore_{block}_mean"
        rank_col = f"rank_{block}"
        if z_col in country_profiles.columns:
            chile_cp = country_profiles[country_profiles["iso3"] == "CHL"]
            if not chile_cp.empty:
                profile[f"zscore_{block}"] = float(chile_cp[z_col].iloc[0])
                rank_val = chile_cp[rank_col].iloc[0] if rank_col in chile_cp else None
                profile[f"rank_{block}_of_{len(country_profiles)}"] = int(rank_val) if pd.notna(rank_val) else None

    return profile


def compute_chile_vs_peers(
    wide: pd.DataFrame,
    dictionary: pd.DataFrame,
    peer_iso3: list[str],
) -> pd.DataFrame:
    """Comparativa Chile vs países peer en métricas por bloque."""
    all_iso3 = ["CHL"] + [p for p in peer_iso3 if p in wide["iso3"].values]
    subset = wide[wide["iso3"].isin(all_iso3)].copy()

    rows = []
    for _, country_row in subset.iterrows():
        rec = {
            "iso3": country_row["iso3"],
            "country_name": country_row.get("country_name_canonical", country_row["iso3"]),
            "region": country_row.get("region", ""),
            "income_group": country_row.get("income_group", ""),
        }
        for block in BLOCKS:
            b_cols = get_block_var_cols(block, wide, dictionary)
            b_num = [c for c in b_cols if pd.api.types.is_numeric_dtype(wide[c])]
            if b_num:
                vals = country_row[b_num].dropna()
                rec[f"n_data_{block}"] = len(vals)
                rec[f"pct_coverage_{block}"] = round(len(vals) / len(b_num) * 100, 2)
                # Z-scores relativos al universo completo (para comparación)
                z_block = pd.DataFrame({c: _robust_zscore(wide[c]) for c in b_num})
                chile_z = z_block.loc[country_row.name]
                rec[f"zscore_mean_{block}"] = round(float(chile_z.mean()), 4)
        rows.append(rec)

    return pd.DataFrame(rows)


def compute_deep_dive_profiles(
    wide: pd.DataFrame,
    dictionary: pd.DataFrame,
    target_iso3: list[str] = None,
) -> pd.DataFrame:
    """Perfil expandido de Singapur, UAE, Irlanda (o los targets indicados)."""
    if target_iso3 is None:
        target_iso3 = ["SGP", "ARE", "IRL", "CHL"]

    rows = []
    for iso3 in target_iso3:
        country_rows = wide[wide["iso3"] == iso3]
        if country_rows.empty:
            continue
        country_row = country_rows.iloc[0]
        rec = {
            "iso3": iso3,
            "country_name": country_row.get("country_name_canonical", iso3),
            "region": country_row.get("region", ""),
            "income_group": country_row.get("income_group", ""),
        }
        for block in BLOCKS:
            b_cols = get_block_var_cols(block, wide, dictionary)
            b_num = [c for c in b_cols if pd.api.types.is_numeric_dtype(wide[c])]
            if b_num:
                vals = country_row[b_num].dropna()
                rec[f"pct_coverage_{block}"] = round(len(vals) / len(b_num) * 100, 2)
                # Ranking del país en cada variable del bloque
                ranks = []
                for col in b_num:
                    val = country_row[col]
                    if pd.isna(val):
                        continue
                    r = (wide[col].dropna() >= val).sum()
                    ranks.append(r / wide[col].notna().sum() * 100)
                rec[f"avg_pct_rank_{block}"] = round(float(np.mean(ranks)), 2) if ranks else np.nan
        rows.append(rec)

    return pd.DataFrame(rows)


def run_country_analysis(
    wide: pd.DataFrame | None = None,
    dictionary: pd.DataFrame | None = None,
    peer_iso3: list[str] | None = None,
    save: bool = True,
) -> dict[str, object]:
    if wide is None:
        wide = load_wide()
    if dictionary is None:
        dictionary = load_dictionary()
    if peer_iso3 is None:
        peer_iso3 = ["ARG", "BRA", "COL", "MEX", "PER", "URY", "SGP", "ARE", "IRL", "EST", "USA", "GBR", "KOR"]

    profiles = compute_country_profiles(wide, dictionary)
    chile_profile = compute_chile_profile(wide, dictionary, profiles)
    chile_vs_peers = compute_chile_vs_peers(wide, dictionary, peer_iso3)
    deep_dives = compute_deep_dive_profiles(wide, dictionary)

    results = {
        "eda_country_profiles": profiles,
        "eda_chile_vs_peers": chile_vs_peers,
        "eda_singapore_uae_ireland_profiles": deep_dives,
        "chile_profile_dict": chile_profile,
    }

    if save:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        for name, df in results.items():
            if isinstance(df, pd.DataFrame):
                df.to_csv(OUTPUTS_DIR / f"{name}.csv", index=False)
        # Chile profile como CSV de una fila
        if chile_profile:
            pd.DataFrame([chile_profile]).to_csv(OUTPUTS_DIR / "eda_chile_profile.csv", index=False)

    return results
