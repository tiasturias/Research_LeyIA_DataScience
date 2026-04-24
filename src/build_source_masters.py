"""
Build per-source master datasets with explicit temporal policies.

Each source produces a single iso3-keyed master file with:
  - One row per study country (86 total)
  - Variables with documented year of reference
  - Source provenance metadata
  - NaN for structural absences

Outputs (data/interim/):
  - y_stanford_master.csv       (patents, investment, startups)
  - y_microsoft_master.csv      (ai_adoption_rate)
  - y_oxford_master.csv         (ai_readiness_score)
  - x2_wipo_master.csv          (gii_score, region_un)
  - x2_wb_master.csv            (WDI + WGI controls)
  - x1_master.csv               (regulatory variables, 2025 snapshot)
  - oecd_robustness_master.csv  (VC proxy + publications + OECD patents)
"""

import pandas as pd
import numpy as np
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
INTERIM = BASE / "data/interim"
RAW = BASE / "data/raw"

# Load the 86 study iso3 from IAPP baseline
STUDY_ISO3 = sorted(
    pd.read_csv(RAW / "IAPP/iapp_x1_core.csv", usecols=["iso3"])["iso3"].unique()
)


def _to_study(df, on="iso3"):
    """Left-join to study backbone to ensure exactly 86 rows."""
    backbone = pd.DataFrame({"iso3": STUDY_ISO3})
    return pd.merge(backbone, df, on=on, how="left")


# ═══════════════════════════════════════════════════════════════════════════════
# 1. STANFORD Y MASTER
# ═══════════════════════════════════════════════════════════════════════════════

def build_stanford_master():
    """
    Consolidate Stanford AI Index 2025 Y variables into one iso3-keyed file.

    Variables:
      ai_patents_per100k      - fig_1.2.4, year=2023, 54 countries
      ai_investment_usd_bn_cumulative - fig_4.3.9, cumulative 2013-2024, 84 countries
      ai_investment_usd_bn_2024       - fig_4.3.8, year=2024, 67 countries
      ai_startups_cumulative          - fig_4.3.13, cumulative 2013-2024, 84 countries
      ai_startups_2024                - fig_4.3.12, year=2024, 62 countries

    Decision: fig_4.3.8/4.3.9 is the PRIMARY source for country-level AI investment.
              fig_4.3.10 (USA/CHN/EU aggregate only) is NOT used.
    Decision: ai_vibrancy_score is EXCLUDED (Stanford Vibrancy Tool decommissioned).
    """
    pat = pd.read_csv(INTERIM / "stanford_ai_patents.csv",
                       usecols=["iso3", "ai_patents_per100k"])
    inv = pd.read_csv(INTERIM / "stanford_ai_investment.csv",
                       usecols=["iso3", "ai_investment_usd_bn_cumulative",
                                "ai_investment_usd_bn_2024"])
    su = pd.read_csv(INTERIM / "stanford_ai_startups.csv",
                      usecols=["iso3", "ai_startups_cumulative", "ai_startups_2024"])

    master = _to_study(pat)
    master = pd.merge(master, inv, on="iso3", how="left")
    master = pd.merge(master, su, on="iso3", how="left")

    # Temporal metadata
    master["patents_year"] = np.where(master["ai_patents_per100k"].notna(), 2023, np.nan)
    master["investment_year"] = np.where(
        master["ai_investment_usd_bn_cumulative"].notna(), 2024, np.nan
    )
    master["startups_year"] = np.where(
        master["ai_startups_cumulative"].notna(), 2024, np.nan
    )
    master["source"] = "Stanford_AI_Index_2025"

    out = INTERIM / "y_stanford_master.csv"
    master.to_csv(out, index=False)
    n_pat = master["ai_patents_per100k"].notna().sum()
    n_inv = master["ai_investment_usd_bn_cumulative"].notna().sum()
    n_su = master["ai_startups_cumulative"].notna().sum()
    print(f"[Stanford] {out.name}: 86 rows | patents={n_pat} investment={n_inv} startups={n_su}")
    return master


# ═══════════════════════════════════════════════════════════════════════════════
# 2. MICROSOFT Y MASTER
# ═══════════════════════════════════════════════════════════════════════════════

def build_microsoft_master():
    """
    Microsoft AI Economy Institute — AI adoption rate.

    Variable: ai_adoption_rate (= ai_user_share_h2_2025, preferred over H1)
    Temporal policy: H2 2025 as canonical; H1 2025 as fallback if H2 missing.
    Coverage: 75/86 study countries.
    Structural absences (11): BHR, BLZ, BRB, CYP, EST, ISL, LUX, LVA, MLT, MUS, SYC.
    """
    ms = pd.read_csv(RAW / "Microsoft/microsoft_ai_diffusion_study.csv")
    ms = ms[["iso3", "ai_user_share_h1_2025", "ai_user_share_h2_2025"]].copy()

    # Canonical adoption rate: H2 preferred, H1 as fallback
    ms["ai_adoption_rate"] = ms["ai_user_share_h2_2025"].fillna(
        ms["ai_user_share_h1_2025"]
    )
    ms["adoption_period"] = np.where(
        ms["ai_user_share_h2_2025"].notna(), "H2_2025",
        np.where(ms["ai_user_share_h1_2025"].notna(), "H1_2025", None)
    )

    master = _to_study(ms[["iso3", "ai_adoption_rate", "adoption_period",
                           "ai_user_share_h1_2025", "ai_user_share_h2_2025"]])
    master["source"] = "Microsoft_AIEI_2025"

    out = INTERIM / "y_microsoft_master.csv"
    master.to_csv(out, index=False)
    n = master["ai_adoption_rate"].notna().sum()
    print(f"[Microsoft] {out.name}: 86 rows | ai_adoption_rate={n}/86")
    return master


# ═══════════════════════════════════════════════════════════════════════════════
# 3. OXFORD Y MASTER
# ═══════════════════════════════════════════════════════════════════════════════

def build_oxford_master():
    """
    Oxford Insights Government AI Readiness Index.

    Variable: ai_readiness_score (0-100 scale, harmonized)
    Temporal policy: 2025 edition as canonical; fallback to 2024 if 2025 missing.
    Coverage: 86/86 for 2025 (195 countries globally).
    Panel available 2019-2025 for extension analyses.
    """
    ox = pd.read_csv(RAW / "Oxford Insights/oxford_ai_readiness_snapshot_latest.csv")
    # Use 2025 snapshot first
    ox_2025 = ox[ox["year"] == 2025][["iso3", "ai_readiness_score"]].copy()
    ox_2025["readiness_year"] = 2025

    # Fallback: 2024 for any missing
    ox_2024 = ox[ox["year"] == 2024][["iso3", "ai_readiness_score"]].copy()
    ox_2024["readiness_year"] = 2024

    master = _to_study(ox_2025)
    # Fill gaps with 2024
    missing_mask = master["ai_readiness_score"].isna()
    if missing_mask.any():
        for idx in master[missing_mask].index:
            iso = master.loc[idx, "iso3"]
            row_2024 = ox_2024[ox_2024["iso3"] == iso]
            if len(row_2024) > 0:
                master.loc[idx, "ai_readiness_score"] = row_2024.iloc[0]["ai_readiness_score"]
                master.loc[idx, "readiness_year"] = 2024

    master["source"] = "Oxford_Insights_GAIRI_2025"

    out = INTERIM / "y_oxford_master.csv"
    master.to_csv(out, index=False)
    n = master["ai_readiness_score"].notna().sum()
    print(f"[Oxford] {out.name}: 86 rows | ai_readiness_score={n}/86")
    return master


# ═══════════════════════════════════════════════════════════════════════════════
# 4. WIPO X2 MASTER
# ═══════════════════════════════════════════════════════════════════════════════

def build_wipo_master():
    """
    WIPO Global Innovation Index — gii_score + region_un.

    Variable: gii_score (composite innovation index)
    Temporal policy: 2025 edition as canonical; 2024 fallback.
    Coverage: 84/86 for 2025 (BLZ, TWN structurally absent from WIPO).
    region_un used as input for derived `region` control.
    """
    wipo = pd.read_csv(RAW / "WIPO Global Innovation Index/wipo_gii_snapshot_latest.csv")

    # 2025 snapshot
    w25 = wipo[wipo["year"] == 2025][["iso3", "gii_score", "region_un"]].copy()
    w25["gii_year"] = 2025

    # Try panel for fallback years
    try:
        panel = pd.read_csv(RAW / "WIPO Global Innovation Index/wipo_gii_overall_panel.csv")
        w24 = panel[panel["year"] == 2024][["iso3", "gii_score"]].copy()
        w24["gii_year"] = 2024
        # Also get region_un from snapshot if not in panel
        if "region_un" not in w24.columns:
            region_map = wipo.drop_duplicates("iso3")[["iso3", "region_un"]]
            w24 = pd.merge(w24, region_map, on="iso3", how="left")
    except Exception:
        w24 = pd.DataFrame(columns=["iso3", "gii_score", "region_un", "gii_year"])

    master = _to_study(w25)
    # Fill missing with 2024
    missing_mask = master["gii_score"].isna()
    if missing_mask.any() and len(w24) > 0:
        for idx in master[missing_mask].index:
            iso = master.loc[idx, "iso3"]
            row_24 = w24[w24["iso3"] == iso]
            if len(row_24) > 0:
                master.loc[idx, "gii_score"] = row_24.iloc[0]["gii_score"]
                master.loc[idx, "gii_year"] = 2024
                if pd.isna(master.loc[idx, "region_un"]):
                    master.loc[idx, "region_un"] = row_24.iloc[0].get("region_un")

    master["source"] = "WIPO_GII_2025"

    out = INTERIM / "x2_wipo_master.csv"
    master.to_csv(out, index=False)
    n_gii = master["gii_score"].notna().sum()
    n_reg = master["region_un"].notna().sum()
    print(f"[WIPO] {out.name}: 86 rows | gii_score={n_gii}/86 region_un={n_reg}/86")
    return master


# ═══════════════════════════════════════════════════════════════════════════════
# 5. WORLD BANK X2 MASTER
# ═══════════════════════════════════════════════════════════════════════════════

def build_wb_master():
    """
    World Bank WDI + WGI controls.

    Temporal policy: For each variable × country, take the latest available value
    within the window [2019, 2024]. Values older than 2019 are excluded to maintain
    contemporaneity with the 2025 cross-section. WGI variables use [2019, 2023]
    since 2023 is the latest WGI publication as of 2026-04.

    Core variables (WDI):
      gdp_per_capita_ppp     - 85/86 (TWN excluded from WB API)
      internet_penetration   - 85/86
      rd_expenditure         - 78/86 (structural gaps in small/developing countries)
      tertiary_education     - 84/86

    Confounder core variables (WGI, added 2026-04 per audit Tarea A):
      regulatory_quality     - 85/86 target (merge raw 63 + expansion 22)
      rule_of_law            - 85/86 target (merge raw 63 + expansion 22)

    Robustness variables (WGI):
      government_effectiveness - 85/86 (expanded from 63 via expand_wgi.py)
      control_of_corruption    - 85/86 (expanded from 63 via expand_wgi.py)

    Exception: TWN structurally excluded from WB API per D-004.
    """
    wdi = pd.read_csv(INTERIM / "wdi_all_86.csv")

    # Merge WGI expansion for the 22 countries missing from the original raw
    wgi_exp_path = RAW / "World Bank WDI/wgi_expansion_22.csv"
    if wgi_exp_path.exists():
        wgi_exp = pd.read_csv(wgi_exp_path)
        # For each (iso3, year) in wgi_exp, override wdi WGI columns if wdi has NaN
        wgi_cols = ["regulatory_quality", "rule_of_law",
                    "government_effectiveness", "control_of_corruption"]
        for col in wgi_cols:
            if col not in wdi.columns:
                wdi[col] = np.nan
        wdi = wdi.set_index(["iso3", "year"])
        wgi_exp = wgi_exp.set_index(["iso3", "year"])
        for col in wgi_cols:
            if col in wgi_exp.columns:
                wdi[col] = wdi[col].combine_first(wgi_exp[col])
        wdi = wdi.reset_index()

    # Merge digital economy indicators for 85 countries (Tarea A sub-task A.5)
    digital_path = RAW / "World Bank WDI/digital_economy_86.csv"
    if digital_path.exists():
        digital = pd.read_csv(digital_path)
        digital_cols = ["ict_service_exports_pct", "high_tech_exports_pct"]
        for col in digital_cols:
            if col not in wdi.columns:
                wdi[col] = np.nan
        wdi = wdi.set_index(["iso3", "year"])
        digital = digital.set_index(["iso3", "year"])
        for col in digital_cols:
            if col in digital.columns:
                wdi[col] = wdi[col].combine_first(digital[col])
        wdi = wdi.reset_index()

    WINDOW_START = 2019
    WINDOW_END = 2024

    core_vars = [
        "gdp_per_capita_ppp", "rd_expenditure", "internet_penetration",
        "tertiary_education",
    ]
    # WGI confounder vars (new) + robustness vars
    confounder_vars = ["regulatory_quality", "rule_of_law"]
    robustness_vars = ["government_effectiveness", "control_of_corruption"]
    # Digital economy proxies (added 2026-04 Tarea A sub-task A.5)
    # Clasificadas como EXTENDED (no core) por cobertura 83/86 y por ser
    # proxies del constructo "economia digital" en vez de medicion directa.
    digital_vars = ["ict_service_exports_pct", "high_tech_exports_pct"]
    extra_vars = [
        "population", "gdp_current_usd", "unemployment_rate", "labor_force",
    ]
    all_vars = (core_vars + confounder_vars + robustness_vars
                + digital_vars + extra_vars)

    rows = []
    for iso3 in STUDY_ISO3:
        cdf = wdi[(wdi["iso3"] == iso3) &
                   (wdi["year"] >= WINDOW_START) &
                   (wdi["year"] <= WINDOW_END)].sort_values("year", ascending=False)
        row = {"iso3": iso3}
        for var in all_vars:
            if var in cdf.columns:
                vals = cdf[cdf[var].notna()]
                if len(vals) > 0:
                    row[var] = vals[var].iloc[0]
                    row[f"{var}_year"] = int(vals["year"].iloc[0])
                else:
                    row[var] = np.nan
                    row[f"{var}_year"] = np.nan
            else:
                row[var] = np.nan
                row[f"{var}_year"] = np.nan
        rows.append(row)

    master = pd.DataFrame(rows)
    master["source"] = "World_Bank_WDI_WGI"
    master["temporal_window"] = f"{WINDOW_START}-{WINDOW_END}"

    out = INTERIM / "x2_wb_master.csv"
    master.to_csv(out, index=False)

    print(f"[World Bank] {out.name}: {len(master)} rows | window={WINDOW_START}-{WINDOW_END}")
    print(f"  -- WDI core --")
    for var in core_vars:
        n = master[var].notna().sum()
        print(f"  {var}: {n}/86")
    print(f"  -- WGI confounders (added 2026-04 Tarea A) --")
    for var in confounder_vars:
        n = master[var].notna().sum()
        print(f"  {var}: {n}/86")
    print(f"  -- WGI robustness --")
    for var in robustness_vars:
        n = master[var].notna().sum()
        print(f"  {var}: {n}/86")
    print(f"  -- Digital economy proxies (added 2026-04 Tarea A A.5) --")
    for var in digital_vars:
        n = master[var].notna().sum()
        print(f"  {var}: {n}/86")
    return master


# ═══════════════════════════════════════════════════════════════════════════════
# 6. X1 MASTER (regulatory, 2025 cross-section)
# ═══════════════════════════════════════════════════════════════════════════════

def build_x1_master():
    """
    Regulatory variables — 2025 cross-sectional snapshot from consolidated X1.

    Source: x1_consolidated.csv (OECD panel + IAPP 2025 snapshot)
    Uses the year=2025 row as the canonical regulatory state per country.
    Derives regulatory_status_group for comparative analysis.
    """
    x1 = pd.read_csv(INTERIM / "x1_consolidated.csv")
    snap = x1[x1["year"] == 2025].copy()

    cols = ["iso3", "has_ai_law", "regulatory_approach", "regulatory_intensity",
            "year_enacted", "enforcement_level", "thematic_coverage",
            "regulatory_status_group", "x1_source"]
    master = snap[cols].copy()
    master["year"] = 2025
    master["source"] = "OECD_IAPP_consolidated"

    # Ensure all 86 study countries present
    master = _to_study(master)

    out = INTERIM / "x1_master.csv"
    master.to_csv(out, index=False)

    n = master["has_ai_law"].notna().sum()
    groups = master["regulatory_status_group"].value_counts().to_dict()
    print(f"[X1] {out.name}: {len(master)} rows | has_ai_law={n}/86")
    print(f"  Groups: {groups}")
    return master


# ═══════════════════════════════════════════════════════════════════════════════
# 7. OECD ROBUSTNESS MASTER
# ═══════════════════════════════════════════════════════════════════════════════

def build_oecd_robustness_master():
    """
    OECD variables for robustness analyses (NOT for the main model).

    Variables (latest available within 2019-2024 window):
      ai_investment_vc_proxy     - 33 countries (VC total as % GDP)
      ai_publications_frac       - 63 countries
      ai_publications_top10_frac - 63 countries
      ai_patents_pct             - OECD patent families under PCT
      ai_patents_ip5             - OECD patent families at IP5

    These are SECONDARY/ROBUSTNESS variables, not part of the main model.
    """
    oecd = pd.read_csv(RAW / "OECD/oecd_all_indicators_wide.csv")
    vc = pd.read_csv(INTERIM / "ai_investment_vc_proxy.csv")

    WINDOW_START = 2019
    WINDOW_END = 2024

    robustness_vars = [
        "ai_publications_frac", "ai_publications_top10_frac",
        "ai_publications_scopus_frac", "ai_patents_pct", "ai_patents_ip5",
        "gerd_pct_gdp", "berd_pct_gdp", "researchers_per_1000_employed",
    ]

    # Get latest available per country within window
    rows = []
    for iso3 in STUDY_ISO3:
        cdf = oecd[(oecd["iso3"] == iso3) &
                    (oecd["year"] >= WINDOW_START) &
                    (oecd["year"] <= WINDOW_END)].sort_values("year", ascending=False)
        row = {"iso3": iso3}
        for var in robustness_vars:
            if var in cdf.columns:
                vals = cdf[cdf[var].notna()]
                if len(vals) > 0:
                    row[var] = vals[var].iloc[0]
                    row[f"{var}_year"] = int(vals["year"].iloc[0])
                else:
                    row[var] = np.nan
                    row[f"{var}_year"] = np.nan
            else:
                row[var] = np.nan
                row[f"{var}_year"] = np.nan
        rows.append(row)

    master = pd.DataFrame(rows)

    # Add VC proxy (latest available)
    vc_latest = []
    for iso3 in STUDY_ISO3:
        cdf = vc[(vc["iso3"] == iso3) &
                  (vc["year"] >= WINDOW_START) &
                  (vc["year"] <= WINDOW_END)].sort_values("year", ascending=False)
        if len(cdf) > 0:
            vc_latest.append({
                "iso3": iso3,
                "ai_investment_vc_proxy": cdf.iloc[0]["ai_investment_vc_proxy"],
                "vc_proxy_year": int(cdf.iloc[0]["year"]),
            })
        else:
            vc_latest.append({
                "iso3": iso3,
                "ai_investment_vc_proxy": np.nan,
                "vc_proxy_year": np.nan,
            })

    vc_df = pd.DataFrame(vc_latest)
    master = pd.merge(master, vc_df, on="iso3", how="left")
    master["source"] = "OECD_STI_MSTI"
    master["role"] = "robustness"

    out = INTERIM / "oecd_robustness_master.csv"
    master.to_csv(out, index=False)

    n_vc = master["ai_investment_vc_proxy"].notna().sum()
    n_pub = master["ai_publications_frac"].notna().sum()
    print(f"[OECD Robustness] {out.name}: {len(master)} rows")
    print(f"  ai_investment_vc_proxy={n_vc}/86 ai_publications_frac={n_pub}/86")
    return master


# ═══════════════════════════════════════════════════════════════════════════════
# 8. GDPR MASTER (added 2026-04 per Tarea A sub-task A.4)
# ═══════════════════════════════════════════════════════════════════════════════

def build_gdpr_master():
    """
    Consolidate GDPR-like law coding into one iso3-keyed file.

    Source: manual coding from DLA Piper Data Protection Laws of the World (2025)
    cross-checked with UNCTAD Data Protection Tracker and national DPA registries.

    Variables:
      has_gdpr_like_law (0/1):        binary indicator of comprehensive DP law
      gdpr_similarity_level (0-3):    ordinal level of GDPR alignment
        0 = no comprehensive law
        1 = basic / sectoral only
        2 = comprehensive GDPR-like law (no EU adequacy)
        3 = EU/EEA member OR current EU adequacy decision
      dp_law_year (int):              year the main DP law was enacted / last major amended
      has_dpa (0/1):                  operational independent Data Protection Authority
      eu_status (str):                eu_member / eea_member / adequacy / none
      enforcement_active (0/1):       has the law been actively enforced (fines / decisions)?

    Coverage: 86/86 (exhaustive manual coding).
    Cutoff date: 2026-03.

    See info_data/METODOLOGIA_GDPR_CODING.md for full coding rules and rationale.
    """
    src = pd.read_csv(RAW / "GDPR_coding/gdpr_like_coding.csv")

    cols = ["iso3", "has_gdpr_like_law", "gdpr_similarity_level",
            "dp_law_name", "dp_law_year", "has_dpa", "eu_status",
            "enforcement_active"]
    master = src[cols].copy()
    master = _to_study(master)

    out = INTERIM / "x2_gdpr_master.csv"
    master.to_csv(out, index=False)

    n_has = int(master["has_gdpr_like_law"].sum())
    n_l3 = int((master["gdpr_similarity_level"] == 3).sum())
    n_l2 = int((master["gdpr_similarity_level"] == 2).sum())
    n_l1 = int((master["gdpr_similarity_level"] == 1).sum())
    print(f"[GDPR] {out.name}: {len(master)} rows | has_gdpr_like_law={n_has}/86")
    print(f"  Levels: L1={n_l1} | L2={n_l2} | L3={n_l3}")
    return master


# ═══════════════════════════════════════════════════════════════════════════════
# 9. FREEDOM HOUSE MASTER (added 2026-04 per Tarea A sub-task A.6)
# ═══════════════════════════════════════════════════════════════════════════════

def build_fh_master():
    """
    Consolidate Freedom in the World 2025 (data year 2024) scores for 86 countries.

    Source: manual coding from Freedom House "Freedom in the World 2025" (released
    March 2025, covers 2024 events). Scores should be verified against the official
    FH Excel "All Data, FIW 2013-2025" before publication.

    Variables:
      fh_total_score (int):  aggregate freedom score (0-100)
      fh_status (str):       F (Free, >=70), PF (Partly Free, 35-69), NF (Not Free, <=34)
      fh_pr_score (int):     Political Rights subscore (range -4 to 40)
      fh_cl_score (int):     Civil Liberties subscore (0-60)
      fh_democracy_level (int ordinal 0-2):  derived: 0=NF, 1=PF, 2=F

    Coverage: 86/86 (exhaustive manual coding).
    Cutoff: FITW 2025 (data year 2024).

    See info_data/METODOLOGIA_FREEDOM_HOUSE.md for coding rationale and validation notes.
    """
    src = pd.read_csv(RAW / "FreedomHouse/freedom_in_the_world_2025.csv")

    src["fh_democracy_level"] = src["fh_status"].map({"NF": 0, "PF": 1, "F": 2})

    cols = ["iso3", "fh_status", "fh_total_score", "fh_pr_score", "fh_cl_score",
            "fh_democracy_level", "fh_year"]
    master = src[cols].copy()
    master = _to_study(master)

    out = INTERIM / "x2_fh_master.csv"
    master.to_csv(out, index=False)

    n_f = int((master["fh_status"] == "F").sum())
    n_pf = int((master["fh_status"] == "PF").sum())
    n_nf = int((master["fh_status"] == "NF").sum())
    print(f"[FH]   {out.name}: {len(master)} rows | F={n_f} | PF={n_pf} | NF={n_nf}")
    print(f"  Mean score: {master['fh_total_score'].mean():.1f} (range {master['fh_total_score'].min()}-{master['fh_total_score'].max()})")
    return master


# ═══════════════════════════════════════════════════════════════════════════════
# 10. LEGAL ORIGIN MASTER (added 2026-04 per Tarea A sub-task A.3-bis)
# ═══════════════════════════════════════════════════════════════════════════════

def build_legal_origin_master():
    """
    Consolidate legal origin classification per La Porta, Lopez-de-Silanes &
    Shleifer (2008) "The Economic Consequences of Legal Origins" (JEL 46(2)).

    Source: manual coding of 86 countries into the 5 La Porta legal families
    (English, French, German, Scandinavian, Socialist) based on the commercial /
    civil code lineage criterion. Reference tables: La Porta et al. 2008
    Appendix; Djankov-La Porta-Lopez-de-Silanes-Shleifer datasets; CBR
    Leximetric dataset for ambiguous cases.

    Variables:
      legal_origin (str):   one of {English, French, German, Scandinavian, Socialist}
      is_common_law (0/1):  derived binary (1 if English legal origin)

    Coverage: 86/86 (exhaustive manual coding).
    Cutoff: 2008 La Porta classification (stable over time).

    See info_data/METODOLOGIA_LEGAL_ORIGIN.md for coding rationale and edge cases
    (SAU, CHN, VNM, PHL, JOR mixed systems).
    """
    src = pd.read_csv(RAW / "LegalOrigin/legal_origin_coding.csv")

    cols = ["iso3", "legal_origin", "is_common_law"]
    master = src[cols].copy()
    master = _to_study(master)

    out = INTERIM / "x2_legal_origin_master.csv"
    master.to_csv(out, index=False)

    dist = master["legal_origin"].value_counts().to_dict()
    n_cl = int(master["is_common_law"].sum())
    print(f"[LegalOrig] {out.name}: {len(master)} rows | common_law={n_cl}/86")
    print(f"  Distribution: {dist}")
    return master


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def build_all():
    print("=" * 70)
    print("BUILDING PER-SOURCE MASTER DATASETS")
    print("=" * 70)
    print()

    stanford = build_stanford_master()
    microsoft = build_microsoft_master()
    oxford = build_oxford_master()
    wipo = build_wipo_master()
    wb = build_wb_master()
    x1 = build_x1_master()
    oecd_rob = build_oecd_robustness_master()
    gdpr = build_gdpr_master()
    fh = build_fh_master()
    legal = build_legal_origin_master()

    print()
    print("=" * 70)
    print("ALL SOURCE MASTERS BUILT SUCCESSFULLY")
    print("=" * 70)

    return {
        "stanford": stanford,
        "microsoft": microsoft,
        "oxford": oxford,
        "wipo": wipo,
        "wb": wb,
        "x1": x1,
        "oecd_robustness": oecd_rob,
        "gdpr": gdpr,
        "fh": fh,
        "legal": legal,
    }


if __name__ == "__main__":
    build_all()
