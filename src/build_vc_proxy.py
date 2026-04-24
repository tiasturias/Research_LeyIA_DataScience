"""
Build ai_investment_vc proxy from OECD VC variables.

OECD provides vc_seed_pct_gdp, vc_startup_pct_gdp, vc_later_pct_gdp for 33 countries.
We sum them into a single vc_total_pct_gdp as the proxy for ai_investment_vc.

NOTE: This is a *general* VC proxy, not AI-specific VC. Stanford fig_4.3.10 only covers
USA/China/Europe (aggregated) and cannot be used at country level.
The proxy is documented as `ai_investment_vc_proxy` (not exact).

Output: data/interim/ai_investment_vc_proxy.csv
"""

import pandas as pd
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent


def build():
    oecd = pd.read_csv(BASE / "data/raw/OECD/oecd_all_indicators_wide.csv")
    vc_cols = ["vc_seed_pct_gdp", "vc_startup_pct_gdp", "vc_later_pct_gdp"]

    # Keep only rows with VC data
    mask = oecd[vc_cols].notna().any(axis=1)
    vc = oecd.loc[mask, ["iso3", "year"] + vc_cols].copy()

    # Sum the three VC stages into a single proxy
    vc["vc_total_pct_gdp"] = vc[vc_cols].sum(axis=1)

    # The ai_investment_vc_proxy is the total VC as % of GDP
    vc["ai_investment_vc_proxy"] = vc["vc_total_pct_gdp"]

    out = vc[["iso3", "year", "vc_seed_pct_gdp", "vc_startup_pct_gdp",
              "vc_later_pct_gdp", "vc_total_pct_gdp", "ai_investment_vc_proxy"]].copy()

    out_path = BASE / "data/interim/ai_investment_vc_proxy.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_path, index=False)

    print(f"VC proxy: {len(out)} rows, {out['iso3'].nunique()} countries")
    print(f"Years: {sorted(out['year'].unique())}")
    print(f"Countries: {sorted(out['iso3'].unique())}")
    print(f"Saved to {out_path}")
    return out


if __name__ == "__main__":
    build()
