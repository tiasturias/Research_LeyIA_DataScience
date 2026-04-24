"""
Build and audit the complete-case matrix for the study.

Merges all interim datasets into a single iso3-level matrix and counts
how many countries are complete under different variable definitions.

Output: data/interim/completeness_audit.csv  (country × variable coverage)
        Prints summary to console.
"""

import pandas as pd
import numpy as np
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent


def load_all():
    """Load and merge all interim datasets into a single 2025/latest snapshot."""
    # ── X1 (consolidated, use 2025 snapshot) ─────────────────────────────────
    x1 = pd.read_csv(BASE / "data/interim/x1_consolidated.csv")
    x1_snap = x1[x1["year"] == 2025].copy()
    x1_cols = ["iso3", "has_ai_law", "regulatory_approach", "regulatory_intensity",
               "year_enacted", "enforcement_level", "thematic_coverage",
               "regulatory_status_group"]

    # ── Derived controls ─────────────────────────────────────────────────────
    dc = pd.read_csv(BASE / "data/interim/derived_controls.csv")  # oecd_member, region

    # ── WDI (use latest available year per country) ──────────────────────────
    wdi = pd.read_csv(BASE / "data/interim/wdi_all_86.csv")
    wdi_core_cols = ["gdp_per_capita_ppp", "rd_expenditure", "internet_penetration",
                     "tertiary_education", "government_effectiveness"]
    # For each country, take the most recent non-null value for each variable
    wdi_latest = []
    for iso3 in wdi["iso3"].unique():
        cdf = wdi[wdi["iso3"] == iso3].sort_values("year", ascending=False)
        row = {"iso3": iso3}
        for col in wdi_core_cols:
            if col in cdf.columns:
                vals = cdf[cdf[col].notna()]
                row[col] = vals[col].iloc[0] if len(vals) > 0 else np.nan
                row[f"{col}_year"] = int(vals["year"].iloc[0]) if len(vals) > 0 else np.nan
            else:
                row[col] = np.nan
        wdi_latest.append(row)
    wdi_snap = pd.DataFrame(wdi_latest)

    # ── WIPO GII (use latest year) ──────────────────────────────────────────
    wipo = pd.read_csv(BASE / "data/raw/WIPO Global Innovation Index/wipo_gii_snapshot_latest.csv",
                        usecols=["iso3", "year", "gii_score"])
    wipo_latest = wipo.sort_values("year", ascending=False).drop_duplicates("iso3")
    wipo_snap = wipo_latest[["iso3", "gii_score"]].copy()

    # ── Oxford (use latest year) ─────────────────────────────────────────────
    try:
        oxford = pd.read_csv(BASE / "data/raw/Oxford Insights/oxford_ai_readiness_snapshot_latest.csv")
        ox_score_col = [c for c in oxford.columns if "readiness" in c.lower() or "score" in c.lower()]
        if ox_score_col:
            oxford_snap = oxford.sort_values("year", ascending=False).drop_duplicates("iso3")
            oxford_snap = oxford_snap[["iso3", ox_score_col[0]]].rename(
                columns={ox_score_col[0]: "ai_readiness_score"})
        else:
            oxford_snap = pd.DataFrame(columns=["iso3", "ai_readiness_score"])
    except Exception:
        oxford_snap = pd.DataFrame(columns=["iso3", "ai_readiness_score"])

    # ── Microsoft (latest snapshot) ──────────────────────────────────────────
    try:
        ms = pd.read_csv(BASE / "data/raw/Microsoft/microsoft_ai_diffusion_study.csv")
        adopt_col = [c for c in ms.columns if "adoption" in c.lower() or "share" in c.lower() or "ai_user" in c.lower()]
        if adopt_col:
            ms_snap = ms[["iso3", adopt_col[0]]].rename(
                columns={adopt_col[0]: "ai_adoption_rate"}).drop_duplicates("iso3")
        else:
            ms_snap = pd.DataFrame(columns=["iso3", "ai_adoption_rate"])
    except Exception:
        ms_snap = pd.DataFrame(columns=["iso3", "ai_adoption_rate"])

    # ── Stanford patents ─────────────────────────────────────────────────────
    pat = pd.read_csv(BASE / "data/interim/stanford_ai_patents.csv", usecols=["iso3", "ai_patents_per100k"])

    # ── Stanford investment ──────────────────────────────────────────────────
    inv = pd.read_csv(BASE / "data/interim/stanford_ai_investment.csv",
                       usecols=["iso3", "ai_investment_usd_bn_cumulative", "ai_investment_usd_bn_2024"])

    # ── Stanford startups ────────────────────────────────────────────────────
    su = pd.read_csv(BASE / "data/interim/stanford_ai_startups.csv",
                      usecols=["iso3", "ai_startups_cumulative", "ai_startups_2024"])

    # ── Merge everything on iso3 ─────────────────────────────────────────────
    master = x1_snap[x1_cols].copy()
    for right in [dc, wdi_snap, wipo_snap, oxford_snap, ms_snap, pat, inv, su]:
        if len(right) > 0 and "iso3" in right.columns:
            master = pd.merge(master, right, on="iso3", how="left")

    return master


def audit(master):
    """Compute completeness under different variable definitions."""

    # ── Definition 1: STRICT (all Y + all X1 + all X2) ──────────────────────
    y_vars = ["ai_readiness_score", "ai_adoption_rate", "ai_patents_per100k",
              "ai_startups_cumulative", "ai_investment_usd_bn_cumulative"]
    x1_vars = ["has_ai_law", "regulatory_approach", "regulatory_intensity",
                "enforcement_level", "thematic_coverage"]
    x2_vars = ["gdp_per_capita_ppp", "rd_expenditure", "internet_penetration",
               "tertiary_education", "gii_score", "government_effectiveness",
               "oecd_member", "region"]

    # year_enacted is conditional: only required when has_ai_law == 1
    master["year_enacted_ok"] = master.apply(
        lambda r: True if r["has_ai_law"] == 0 else pd.notna(r.get("year_enacted")),
        axis=1,
    )

    all_vars = y_vars + x1_vars + x2_vars

    # Per-variable coverage
    print("=" * 70)
    print("VARIABLE COVERAGE (86 study countries)")
    print("=" * 70)
    for var in all_vars + ["year_enacted_ok"]:
        if var == "year_enacted_ok":
            cov = master["year_enacted_ok"].sum()
        elif var in master.columns:
            cov = master[var].notna().sum()
        else:
            cov = 0
        bar = "█" * int(cov / 86 * 40)
        print(f"  {var:<40s} {cov:>3d}/86  {bar}")

    # ── Complete-case counts under different definitions ─────────────────────
    print("\n" + "=" * 70)
    print("COMPLETE-CASE ANALYSIS")
    print("=" * 70)

    def count_complete(var_list, name, extra_cond=None):
        mask = pd.Series(True, index=master.index)
        for v in var_list:
            if v in master.columns:
                mask &= master[v].notna()
            else:
                mask = pd.Series(False, index=master.index)
                break
        if extra_cond is not None:
            mask &= extra_cond
        n = mask.sum()
        countries = sorted(master.loc[mask, "iso3"].tolist())
        return n, countries, mask

    # A: Strict (all Y + X1 + X2, no vibrancy)
    n, countries, mask_a = count_complete(
        all_vars, "STRICT (5Y + 5X1 + 8X2, no vibrancy)",
        extra_cond=master["year_enacted_ok"],
    )
    print(f"\n  A. STRICT (5Y + 5X1 + 8X2, no vibrancy): {n}/86")
    if n <= 60:
        print(f"     Countries: {countries}")

    # B: Without gov_effectiveness (known gap)
    vars_b = [v for v in all_vars if v != "government_effectiveness"]
    n_b, countries_b, mask_b = count_complete(
        vars_b, "Without gov_effectiveness",
        extra_cond=master["year_enacted_ok"],
    )
    print(f"\n  B. Without government_effectiveness (5Y + 5X1 + 7X2): {n_b}/86")
    if n_b <= 60:
        print(f"     Countries: {countries_b}")

    # C: Without gov_effectiveness and without patents
    vars_c = [v for v in vars_b if v != "ai_patents_per100k"]
    n_c, countries_c, mask_c = count_complete(
        vars_c, "Without GE and patents",
        extra_cond=master["year_enacted_ok"],
    )
    print(f"\n  C. Without GE & patents (4Y + 5X1 + 7X2): {n_c}/86")
    if n_c <= 60:
        print(f"     Countries: {countries_c}")

    # D: Core only (readiness + adoption + investment + startups + X1 + core X2)
    vars_d = ["ai_readiness_score", "ai_adoption_rate",
              "ai_investment_usd_bn_cumulative", "ai_startups_cumulative",
              "has_ai_law", "regulatory_approach", "regulatory_intensity",
              "enforcement_level", "thematic_coverage",
              "gdp_per_capita_ppp", "internet_penetration", "gii_score",
              "oecd_member", "region"]
    n_d, countries_d, mask_d = count_complete(
        vars_d, "CORE (4Y + 5X1 + 5X2)",
        extra_cond=master["year_enacted_ok"],
    )
    print(f"\n  D. CORE (4Y + 5X1 + 5X2): {n_d}/86")
    if n_d <= 70:
        print(f"     Countries: {countries_d}")

    # E: Same as D but add rd_expenditure and tertiary_education
    vars_e = vars_d + ["rd_expenditure", "tertiary_education"]
    n_e, countries_e, mask_e = count_complete(
        vars_e, "CORE + RD + EDUC",
        extra_cond=master["year_enacted_ok"],
    )
    print(f"\n  E. CORE + rd_expenditure + tertiary_education (4Y + 5X1 + 7X2): {n_e}/86")
    if n_e <= 70:
        print(f"     Countries: {countries_e}")

    # ── Regulatory group representation ──────────────────────────────────────
    print("\n" + "=" * 70)
    print("REGULATORY REPRESENTATION (Definition E)")
    print("=" * 70)
    if n_e > 0:
        complete_e = master[mask_e]
        group_dist = complete_e["regulatory_status_group"].value_counts()
        for g, cnt in group_dist.items():
            print(f"  {g:<25s}: {cnt}")

    # ── Missing analysis for bottleneck variables ────────────────────────────
    print("\n" + "=" * 70)
    print("BOTTLENECK: Countries that would become complete if variable X were filled")
    print("=" * 70)
    bottleneck_vars = ["ai_adoption_rate", "ai_patents_per100k", "rd_expenditure",
                       "government_effectiveness", "tertiary_education"]
    for bv in bottleneck_vars:
        # How many are only missing THIS variable (from definition B)?
        mask_all_but = pd.Series(True, index=master.index)
        for v in vars_b:
            if v == bv:
                continue
            if v in master.columns:
                mask_all_but &= master[v].notna()
        mask_all_but &= master["year_enacted_ok"]
        missing_only_this = mask_all_but & (master[bv].isna() if bv in master.columns else True)
        n_unblock = missing_only_this.sum()
        if n_unblock > 0:
            blocked = sorted(master.loc[missing_only_this, "iso3"].tolist())
            print(f"  {bv}: filling it would unblock {n_unblock} countries -> {blocked}")

    # ── Save full audit matrix ───────────────────────────────────────────────
    out = master.copy()
    for v in all_vars:
        out[f"has_{v}"] = out[v].notna().astype(int) if v in out.columns else 0
    out["has_year_enacted_ok"] = out["year_enacted_ok"].astype(int)
    out["complete_strict"] = mask_a.astype(int)
    out["complete_no_ge"] = mask_b.astype(int)
    out["complete_core"] = mask_d.astype(int)
    out["complete_core_plus"] = mask_e.astype(int)

    out_path = BASE / "data/interim/completeness_audit.csv"
    out.to_csv(out_path, index=False)
    print(f"\nFull audit saved to {out_path}")

    return out


if __name__ == "__main__":
    master = load_all()
    audit(master)
