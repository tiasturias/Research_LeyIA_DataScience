"""Construcción de grupos y submuestras para rankings comparativos."""

import pandas as pd


def assign_custom_groups(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    out = df.copy()
    for group_name, iso_list in config.get("country_groups", {}).items():
        if isinstance(iso_list, list):
            out[f"is_group_{group_name}"] = out["iso3"].isin(iso_list)
    return out


def build_group_membership(membership: pd.DataFrame, config: dict) -> pd.DataFrame:
    rows = []
    for _, r in membership.iterrows():
        iso3 = r["iso3"]
        rows.append({"iso3": iso3, "group_name": "global_43", "group_type": "global"})

        if pd.notna(r.get("region")):
            rows.append({"iso3": iso3, "group_name": str(r["region"]), "group_type": "region"})

        if pd.notna(r.get("income_group")):
            rows.append({"iso3": iso3, "group_name": str(r["income_group"]), "group_type": "income"})

    for group_name, iso_list in config.get("country_groups", {}).items():
        if isinstance(iso_list, list):
            for iso3 in iso_list:
                rows.append({"iso3": iso3, "group_name": group_name, "group_type": "custom"})

    return pd.DataFrame(rows).drop_duplicates()
