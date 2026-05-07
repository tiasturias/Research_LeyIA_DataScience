"""Filtrado a las 43 entidades preregistradas del MVP."""

from __future__ import annotations

import pandas as pd

from _common.load import load_mvp_sample_config, load_wide


def get_mvp_iso3() -> list[str]:
    return list(load_mvp_sample_config()["entities"])


def get_mvp_entities_detail() -> pd.DataFrame:
    return pd.DataFrame(load_mvp_sample_config()["entities_detail"])


def filter_to_mvp_sample(wide: pd.DataFrame | None = None) -> pd.DataFrame:
    if wide is None:
        wide = load_wide()
    iso3_list = get_mvp_iso3()
    mvp = wide[wide["iso3"].isin(iso3_list)].copy()
    missing = sorted(set(iso3_list) - set(mvp["iso3"]))
    if missing:
        raise ValueError(f"Entidades MVP ausentes en wide: {missing}")
    if len(mvp) != 43:
        raise ValueError(f"Expected 43 entities, got {len(mvp)}")
    if "CHL" not in mvp["iso3"].values:
        raise ValueError("Chile must be present")
    if not mvp["entity_type"].eq("country_iso3").all():
        bad = mvp.loc[~mvp["entity_type"].eq("country_iso3"), ["iso3", "entity_type"]]
        raise ValueError(f"Entidades no country_iso3 en MVP:\n{bad}")
    order = {iso3: i for i, iso3 in enumerate(iso3_list)}
    return mvp.assign(_mvp_order=mvp["iso3"].map(order)).sort_values("_mvp_order").drop(columns="_mvp_order").reset_index(drop=True)
