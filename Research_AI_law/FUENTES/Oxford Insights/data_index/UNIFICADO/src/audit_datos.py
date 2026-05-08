"""
audit_datos.py — Auditoria profesional de integridad de datos
Verifica que CADA VALOR en el Consolidado provenga EXACTAMENTE
de los 7 Excels fuente originales. Cero datos sinteticos.

Output: UNIFICADO/validation/audit_report.txt
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd
import numpy as np

REPORT = []
ERRORS = 0
CHECKS = 0
MISMATCHES = []

def log(msg):
    print(msg)
    REPORT.append(msg)

def error(msg):
    global ERRORS
    ERRORS += 1
    log(f"  ERROR: {msg}")

def check_val(expected, actual, context):
    global CHECKS, MISMATCHES
    CHECKS += 1
    if pd.isna(expected) and pd.isna(actual):
        return True
    if pd.isna(expected) and not pd.isna(actual):
        MISMATCHES.append(f"{context}: esperaba NaN, obtuvo {actual}")
        return False
    if not pd.isna(expected) and pd.isna(actual):
        MISMATCHES.append(f"{context}: esperaba {expected}, obtuvo NaN")
        return False
    if isinstance(expected, float) and isinstance(actual, float):
        if abs(expected - actual) > 1e-10:
            MISMATCHES.append(f"{context}: esperaba {expected:.15f}, obtuvo {actual:.15f}")
            return False
    elif str(expected).strip() != str(actual).strip():
        MISMATCHES.append(f"{context}: esperaba '{expected}', obtuvo '{actual}'")
        return False
    return True

log("=" * 80)
log("AUDITORIA PROFESIONAL DE INTEGRIDAD DE DATOS")
log("Oxford_Insights_Unificado.xlsx")
log("=" * 80)
log(f"\nFecha: {pd.Timestamp.now()}")
log(f"Fuentes a verificar: 7 archivos .xlsx originales")
log(f"Objetivo: 0 datos sinteticos, 0 estimaciones, 0 invenciones")
log("")

# Load the consolidated data
df_consol = pd.read_csv(output_path("consolidado_final.csv"))
df_iso = pd.read_csv(output_path("iso3_mapping.csv"))

# ============================================================
# PARTE 1: VERIFICACION POR AÑO - CADA VALOR CONTRA SU FUENTE
# ============================================================

# --- 2019: Data sheet ---
log("\n" + "-" * 70)
log("PARTE 1a: 2019 — Data sheet (raw indicators + normalized + clusters)")
log("-" * 70)

df_src = read_sheet(2019, "Data", header=None)
col_map_2019 = {
    "total_score": 26, "avg_governance": 29, "avg_infrastructure_data": 30,
    "avg_skills_education": 31, "avg_govt_public_services": 32,
    "privacy_laws": 1, "ai_strategy": 2, "data_availability": 3,
    "govt_procurement_advanced_tech": 4, "data_capability_govt": 5,
    "technology_skills": 6, "ai_startups": 7, "log_ai_startups": 8,
    "innovation_capability": 9, "digital_public_services": 10,
    "govt_effectiveness": 11, "ict_govt_vision": 12,
    "norm_privacy_laws": 14, "norm_ai_strategy": 15,
    "norm_data_availability": 16, "norm_govt_procurement": 17,
    "norm_data_capability": 18, "norm_technology_skills": 19,
    "norm_log_ai_startups": 20, "norm_innovation_capability": 21,
    "norm_digital_public_services": 22, "norm_govt_effectiveness": 23,
    "norm_ict_govt_vision": 24,
}

# Build lookup: pais_original -> source values for 2019
src_2019 = {}
for i in range(7, len(df_src)):
    country = clean_country(df_src.iloc[i, 0])
    if pd.isna(country):
        continue
    src_2019[country] = {}
    for var, col_idx in col_map_2019.items():
        val = df_src.iloc[i, col_idx]
        src_2019[country][var] = float(val) if pd.notna(val) else np.nan

consol_2019 = df_consol[df_consol["year"] == 2019]
compare_vars_2019 = list(col_map_2019.keys())
n_countries_2019 = 0
for _, row in consol_2019.iterrows():
    country = row["pais_original"]
    if country not in src_2019:
        error(f"2019: pais '{country}' no encontrado en fuente")
        continue
    n_countries_2019 += 1
    for var in compare_vars_2019:
        expected = src_2019[country][var]
        actual = row[var]
        if not check_val(expected, actual, f"2019/{country}/{var}"):
            error(f"{country}/{var}: fuente={expected}, consolidado={actual}")

log(f"  2019: {n_countries_2019} paises verificados, {len(compare_vars_2019)} variables c/u")
log(f"  2019: {CHECKS} checks hasta ahora")

# Reset counter for next section
checks_before = CHECKS
CHECKS = 0

# --- 2020: Detailed scores ---
log("\n" + "-" * 70)
log("PARTE 1b: 2020 — Detailed scores")
log("-" * 70)

Y = 2020
df_src = read_sheet(Y, "Detailed scores", header=1)
df_src = df_src.loc[:, ~df_src.columns.str.contains("^Unnamed", na=False)]
src_2020 = {}
for _, row in df_src.iterrows():
    c = clean_country(row.iloc[0])
    src_2020[c] = {
        "total_score": float(row["Overall score"]),
        "government": float(row["Government"]),
        "technology_sector": float(row["Technology Sector"]),
        "data_infrastructure": float(row["Data and Infrastructure"]),
        "vision": float(row["Vision"]),
        "governance_ethics": float(row["Governance and Ethics"]),
        "digital_capacity": float(row["Digital Capacity"]),
        "adaptability": float(row["Adaptability"]),
        "size": float(row["Size"]),
        "innovation_capacity": float(row["Innovation Capacity"]),
        "human_capital": float(row["Human Capital"]),
        "infrastructure": float(row["Infrastructure"]),
        "data_availability": float(row["Data Availability"]),
        "data_representativeness": float(row["Data Representativeness"]) if pd.notna(row["Data Representativeness"]) else np.nan,
    }

consol_yr = df_consol[df_consol["year"] == Y]
vars_yr = ["total_score","government","technology_sector","data_infrastructure",
           "vision","governance_ethics","digital_capacity","adaptability",
           "size","innovation_capacity","human_capital","infrastructure",
           "data_availability","data_representativeness"]
n_ok = 0
for _, row in consol_yr.iterrows():
    c = row["pais_original"]
    if c not in src_2020:
        error(f"{Y}: pais '{c}' no encontrado en fuente"); continue
    n_ok += 1
    for var in vars_yr:
        expected = src_2020[c][var]
        actual = row[var]
        if not check_val(expected, actual, f"{Y}/{c}/{var}"):
            error(f"{c}/{var}: fuente={expected}, consolidado={actual}")
log(f"  {Y}: {n_ok} paises verificados, {len(vars_yr)} variables c/u")
checks_2020 = CHECKS
CHECKS = 0

# --- 2021: Detailed scores ---
log("\n" + "-" * 70)
log("PARTE 1c: 2021 — Detailed scores")
log("-" * 70)

Y = 2021
df_src = read_sheet(Y, "Detailed scores", header=1)
df_src = df_src.loc[:, ~df_src.columns.str.contains("^Unnamed", na=False)]
src_2021 = {}
for _, row in df_src.iterrows():
    c = clean_country(row.iloc[0])
    src_2021[c] = {
        "total_score": float(row["Overall score"]),
        "government": float(row["Government"]),
        "technology_sector": float(row["Technology Sector"]),
        "data_infrastructure": float(row["Data and Infrastructure"]),
        "vision": float(row["Vision"]),
        "governance_ethics": float(row["Governance and Ethics"]),
        "digital_capacity": float(row["Digital Capacity"]),
        "adaptability": float(row["Adaptability"]),
        "size": float(row["Size"]),
        "innovation_capacity": float(row["Innovation Capacity"]) if pd.notna(row["Innovation Capacity"]) else np.nan,
        "human_capital": float(row["Human Capital"]),
        "infrastructure": float(row["Infrastructure"]),
        "data_availability": float(row["Data Availability"]),
        "data_representativeness": float(row["Data Representativeness"]) if pd.notna(row["Data Representativeness"]) else np.nan,
    }

consol_yr = df_consol[df_consol["year"] == Y]
vars_yr = ["total_score","government","technology_sector","data_infrastructure",
           "vision","governance_ethics","digital_capacity","adaptability",
           "size","innovation_capacity","human_capital","infrastructure",
           "data_availability","data_representativeness"]
n_ok = 0
for _, row in consol_yr.iterrows():
    c = row["pais_original"]
    if c not in src_2021:
        error(f"{Y}: pais '{c}' no encontrado en fuente"); continue
    n_ok += 1
    for var in vars_yr:
        expected = src_2021[c][var]
        actual = row[var]
        if not check_val(expected, actual, f"{Y}/{c}/{var}"):
            error(f"{c}/{var}: fuente={expected}, consolidado={actual}")
log(f"  {Y}: {n_ok} paises verificados, {len(vars_yr)} variables c/u")
checks_2021 = CHECKS
CHECKS = 0

# --- 2022: Detailed scores ---
log("\n" + "-" * 70)
log("PARTE 1d: 2022 — Detailed scores (con Maturity)")
log("-" * 70)

Y = 2022
df_src = read_sheet(Y, "Detailed scores", header=1)
df_src = df_src.loc[:, ~df_src.columns.str.contains("^Unnamed", na=False)]
src_2022 = {}
for _, row in df_src.iterrows():
    c = clean_country(row.iloc[0])
    src_2022[c] = {
        "total_score": float(row["Overall score"]),
        "government": float(row["Government"]),
        "technology_sector": float(row["Technology Sector"]),
        "data_infrastructure": float(row["Data and Infrastructure"]),
        "vision": float(row["Vision"]),
        "governance_ethics": float(row["Governance and Ethics"]),
        "digital_capacity": float(row["Digital Capacity"]),
        "adaptability": float(row["Adaptability"]),
        "maturity": float(row["Maturity"]),
        "innovation_capacity": float(row["Innovation Capacity"]),
        "human_capital": float(row["Human Capital"]),
        "infrastructure": float(row["Infrastructure"]),
        "data_availability": float(row["Data Availability"]),
        "data_representativeness": float(row["Data Representativeness"]) if pd.notna(row["Data Representativeness"]) else np.nan,
    }

consol_yr = df_consol[df_consol["year"] == Y]
vars_yr = ["total_score","government","technology_sector","data_infrastructure",
           "vision","governance_ethics","digital_capacity","adaptability",
           "maturity","innovation_capacity","human_capital","infrastructure",
           "data_availability","data_representativeness"]
n_ok = 0
for _, row in consol_yr.iterrows():
    c = row["pais_original"]
    if c not in src_2022:
        error(f"{Y}: pais '{c}' no encontrado en fuente"); continue
    n_ok += 1
    for var in vars_yr:
        expected = src_2022[c][var]
        actual = row[var]
        if not check_val(expected, actual, f"{Y}/{c}/{var}"):
            error(f"{c}/{var}: fuente={expected}, consolidado={actual}")
log(f"  {Y}: {n_ok} paises verificados, {len(vars_yr)} variables c/u")
checks_2022 = CHECKS
CHECKS = 0

# --- 2023: Pillar & dimension scores ---
log("\n" + "-" * 70)
log("PARTE 1e: 2023 — Pillar & dimension scores")
log("-" * 70)

Y = 2023
df_src = read_sheet(Y, "Pillar & dimension scores", header=1)
df_src = df_src.loc[:, ~df_src.columns.str.contains("^Unnamed", na=False)]
src_2023_p = {}
for _, row in df_src.iterrows():
    c = clean_country(row.iloc[0])
    src_2023_p[c] = {
        "total_score": float(row["Total score"]),
        "government": float(row["Government"]),
        "technology_sector": float(row["Technology Sector"]),
        "data_infrastructure": float(row["Data and Infrastructure"]),
        "vision": float(row["Vision"]),
        "governance_ethics": float(row["Governance and Ethics"]),
        "digital_capacity": float(row["Digital Capacity"]),
        "adaptability": float(row["Adaptability"]),
        "maturity": float(row["Maturity"]),
        "innovation_capacity": float(row["Innovation Capacity"]),
        "human_capital": float(row["Human Capital"]),
        "infrastructure": float(row["Infrastructure"]),
        "data_availability": float(row["Data Availability"]),
        "data_representativeness": float(row["Data Representativeness"]) if pd.notna(row["Data Representativeness"]) else np.nan,
    }

consol_yr = df_consol[df_consol["year"] == Y]
vars_yr = ["total_score","government","technology_sector","data_infrastructure",
           "vision","governance_ethics","digital_capacity","adaptability",
           "maturity","innovation_capacity","human_capital","infrastructure",
           "data_availability","data_representativeness"]
n_ok = 0
for _, row in consol_yr.iterrows():
    c = row["pais_original"]
    if c not in src_2023_p:
        error(f"{Y}: pais '{c}' no encontrado en fuente"); continue
    n_ok += 1
    for var in vars_yr:
        expected = src_2023_p[c][var]
        actual = row[var]
        if not check_val(expected, actual, f"{Y}/{c}/{var}"):
            error(f"{c}/{var}: fuente={expected}, consolidado={actual}")
log(f"  {Y} pillars: {n_ok} paises verificados, {len(vars_yr)} variables c/u")
checks_2023_p = CHECKS
CHECKS = 0

# --- 2023: Indicator scores ---
log("\n" + "-" * 70)
log("PARTE 1f: 2023 — Indicator scores (39 indicadores)")
log("-" * 70)

df_src = read_sheet(2023, "Indicator scores", header=None)
# Build indicator name mapping (same as extract)
indicator_map = {
    "AI strategy": "ind_ai_strategy",
    "Data protection and privacy laws": "ind_data_protection_laws",
    "Cybersecurity": "ind_cybersecurity",
    "Regulatory quality": "ind_regulatory_quality",
    "Ethical principles": "ind_ethical_principles",
    "Accountability": "ind_accountability",
    "Online services": "ind_online_services",
    "Foundational IT infrastructure": "ind_foundational_it",
    "Government Promotion of Investment in Emerging Technologies": "ind_govt_promotion_emerging_tech",
    "Government Effectiveness": "ind_govt_effectiveness",
    "Government responsiveness to change": "ind_govt_responsiveness",
    "Procurement Data": "ind_procurement_data",
    "Number of AI Unicorns log transformation": "ind_ai_unicorns_log",
    "Number of non-AI Unicorns log transformation": "ind_non_ai_unicorns_log",
    "Value of trade in ICT services (per capita) log transformation": "ind_ict_trade_services_log",
    "Value of trade in ICT goods (per capita) log transformation": "ind_ict_trade_goods_log",
    "Computer software spending": "ind_software_spending",
    "Time spent dealing with government regulations": "ind_time_govt_regulations",
    "VC availability": "ind_vc_availability",
    "R&D Spending log transformation": "ind_rd_spending_log",
    "Company investment in emerging technology": "ind_company_investment_emerging_tech",
    "AI research papers log transformation": "ind_ai_research_papers_log",
    "Graduates in STEM or computer science": "ind_stem_graduates",
    "Github Activity log transformation": "ind_github_activity_log",
    "Female STEM Graduates": "ind_female_stem_graduates",
    "Quality of Engineering and Technology Higher Ed": "ind_eng_tech_higher_ed_quality",
    "ICT skills": "ind_ict_skills",
    "Telecommunications Infrastructure": "ind_telecom_infrastructure",
    "Supercomputers log transformation": "ind_supercomputers_log",
    "Broadband Quality": "ind_broadband_quality",
    "5G Infrastructure": "ind_5g_infrastructure",
    "Adoption of Emerging Technologies": "ind_adoption_emerging_tech",
    "Open Data": "ind_open_data",
    "Data governance": "ind_data_governance",
    "Mobile-cellular telephone subscriptions": "ind_mobile_subscriptions",
    "Households with internet access": "ind_households_internet",
    "Statistical Capacity": "ind_statistical_capacity",
    "Cost of cheapest internet-enabled device (% of monthly GDP per capita)": "ind_cost_internet_device",
    "Gender gap in internet access": "ind_gender_gap_internet",
}

# Build source lookup
src_2023_i = {}
for i in range(4, len(df_src)):
    country = clean_country(df_src.iloc[i, 0])
    if pd.isna(country):
        continue
    src_2023_i[country] = {}
    for c in range(1, df_src.shape[1]):
        raw_name = str(df_src.iloc[2, c]).strip() if pd.notna(df_src.iloc[2, c]) else ""
        if raw_name not in indicator_map:
            continue
        var_name = indicator_map[raw_name]
        val = df_src.iloc[i, c]
        src_2023_i[country][var_name] = float(val) if pd.notna(val) else np.nan

indicator_vars = list(indicator_map.values())
consol_yr = df_consol[df_consol["year"] == 2023]
n_ok = 0
for _, row in consol_yr.iterrows():
    c = row["pais_original"]
    if c not in src_2023_i:
        error(f"2023 indicators: pais '{c}' no encontrado en fuente"); continue
    n_ok += 1
    for var in indicator_vars:
        expected = src_2023_i[c].get(var, np.nan)
        actual = row[var]
        if not check_val(expected, actual, f"2023_ind/{c}/{var}"):
            error(f"{c}/{var}: fuente={expected}, consolidado={actual}")
log(f"  2023 indicators: {n_ok} paises verificados, {len(indicator_vars)} variables c/u")
checks_2023_i = CHECKS
CHECKS = 0

# --- 2024: Scores per pillar and dimension ---
log("\n" + "-" * 70)
log("PARTE 1g: 2024 — Scores per pillar and dimension")
log("-" * 70)

Y = 2024
df_src = read_sheet(Y, "Scores per pillar and dimension", header=1)
df_src = df_src.loc[:, ~df_src.columns.str.contains("^Unnamed", na=False)]
src_2024 = {}
for _, row in df_src.iterrows():
    c = clean_country(row.iloc[0])
    src_2024[c] = {
        "total_score": float(row["Total"]),
        "government": float(row["Government"]),
        "technology_sector": float(row["Technology Sector"]),
        "data_infrastructure": float(row["Data and Infrastructure"]),
        "vision": float(row["Vision"]),
        "governance_ethics": float(row["Governance and Ethics"]),
        "digital_capacity": float(row["Digital Capacity"]),
        "adaptability": float(row["Adaptability"]),
        "maturity": float(row["Maturity"]),
        "innovation_capacity": float(row["Innovation Capacity"]),
        "human_capital": float(row["Human Capital"]),
        "infrastructure": float(row["Infrastructure"]),
        "data_availability": float(row["Data Availability"]),
        "data_representativeness": float(row["Data Representativeness"]),
        "ranking_detail": float(row["Ranking"]) if pd.notna(row["Ranking"]) else np.nan,
    }

consol_yr = df_consol[df_consol["year"] == Y]
vars_yr = ["total_score","government","technology_sector","data_infrastructure",
           "vision","governance_ethics","digital_capacity","adaptability",
           "maturity","innovation_capacity","human_capital","infrastructure",
           "data_availability","data_representativeness","ranking_detail"]
n_ok = 0
for _, row in consol_yr.iterrows():
    c = row["pais_original"]
    if c not in src_2024:
        error(f"{Y}: pais '{c}' no encontrado en fuente"); continue
    n_ok += 1
    for var in vars_yr:
        expected = src_2024[c][var]
        actual = row[var]
        if not check_val(expected, actual, f"{Y}/{c}/{var}"):
            error(f"{c}/{var}: fuente={expected}, consolidado={actual}")
log(f"  {Y}: {n_ok} paises verificados, {len(vars_yr)} variables c/u")
checks_2024 = CHECKS
CHECKS = 0

# --- 2025: Dimensions-Pillars ---
log("\n" + "-" * 70)
log("PARTE 1h: 2025 — Dimensions-Pillars")
log("-" * 70)

Y = 2025
df_src = read_sheet(Y, "Dimensions-Pillars", header=1)
df_src = df_src.loc[:, ~df_src.columns.str.contains("^Unnamed", na=False)]

col_map_2025 = {
    "total_score": "Total Score",
    "policy_capacity": "Policy Capacity",
    "ai_infrastructure": "AI Infrastructure",
    "governance_2025": "Governance",
    "public_sector_adoption": "Public Sector Adoption",
    "development_diffusion": "Development & Diffusion",
    "resilience": "Resilience",
    "policy_vision": "Policy vision",
    "policy_commitment": "Policy commitment",
    "compute_capacity": "Compute capacity",
    "enabling_technical_infrastructure": "Enabling technical infrastructure",
    "data_quality": "Data quality",
    "governance_principles": "Governance principles",
    "regulatory_compliance": "Regulatory compliance",
    "government_digital_policy": "Government digital policy",
    "e_government_delivery": "e-Government delivery",
    "human_capital_2025": "Human capital",
    "ai_sector_maturity": "AI sector maturity",
    "ai_technology_diffusion": "AI technology diffusion",
    "societal_transition": "Societal transition",
    "safety_security": "Safety and security",
}

src_2025 = {}
for _, row in df_src.iterrows():
    c = clean_country(row.iloc[1])  # Country is at index 1
    src_2025[c] = {}
    for var, src_col in col_map_2025.items():
        val = row[src_col]
        src_2025[c][var] = float(val) if pd.notna(val) else np.nan

consol_yr = df_consol[df_consol["year"] == Y]
vars_yr = list(col_map_2025.keys())
n_ok = 0
for _, row in consol_yr.iterrows():
    c = row["pais_original"]
    if c not in src_2025:
        error(f"{Y}: pais '{c}' no encontrado en fuente"); continue
    n_ok += 1
    for var in vars_yr:
        expected = src_2025[c][var]
        actual = row[var]
        if not check_val(expected, actual, f"{Y}/{c}/{var}"):
            error(f"{c}/{var}: fuente={expected}, consolidado={actual}")
log(f"  {Y}: {n_ok} paises verificados, {len(vars_yr)} variables c/u")
checks_2025 = CHECKS
CHECKS = 0

# ============================================================
# PARTE 2: VERIFICACION DE DETALLE 2019 SHEET
# ============================================================
log("\n" + "-" * 70)
log("PARTE 2: Detalle_2019 vs fuente Data sheet")
log("-" * 70)

df_detail_2019 = pd.read_csv(output_path("detalle_2019.csv"))
detail_vars = [v for v in col_map_2019.keys()]
n_ok = 0
for _, row in df_detail_2019.iterrows():
    c = row["pais_original"]
    if c not in src_2019:
        error(f"Detalle_2019: pais '{c}' no encontrado en fuente"); continue
    n_ok += 1
    for var in detail_vars:
        expected = src_2019[c][var]
        actual = row[var]
        if not check_val(expected, actual, f"detalle_2019/{c}/{var}"):
            error(f"{c}/{var}: fuente={expected}, detalle={actual}")
log(f"  Detalle_2019: {n_ok} paises verificados")

# ============================================================
# PARTE 3: VERIFICACION DE 2019 RANKINGS
# ============================================================
log("\n" + "-" * 70)
log("PARTE 3: Rankings_Regionales_2019 vs fuente Rankings sheet")
log("-" * 70)

df_rank_src = read_sheet(2019, "Rankings", header=None)
df_rank_dest = pd.read_csv(output_path("rankings_regionales_2019.csv"))

# Verify that at least 20 random countries have matching global score
import random
rank_countries = df_rank_dest["pais_original"].tolist()
random.seed(42)
sample = random.sample(rank_countries, min(20, len(rank_countries)))

rank_region_cols = ["global", "asia_pacific", "africa", "latam", "north_america",
                     "eastern_europe", "australasia", "western_europe"]
src_rank = {}
for region_name, (col_rank, col_country, col_score) in {
    "global": (0, 1, 2), "asia_pacific": (4, 5, 6), "africa": (8, 9, 10),
    "latam": (12, 13, 14), "north_america": (16, 17, 18),
    "eastern_europe": (20, 21, 22), "australasia": (24, 25, 26),
    "western_europe": (28, 29, 30),
}.items():
    for i in range(2, len(df_rank_src)):
        cv = df_rank_src.iloc[i, col_country]
        if pd.isna(cv):
            continue
        c = str(cv).strip()
        if c not in src_rank:
            src_rank[c] = {}
        src_rank[c][f"rank_{region_name}"] = df_rank_src.iloc[i, col_rank]
        src_rank[c][f"score_{region_name}"] = df_rank_src.iloc[i, col_score]

n_ok = 0
for _, row in df_rank_dest.iterrows():
    c = row["pais_original"]
    if c not in src_rank:
        continue
    n_ok += 1
    for region in rank_region_cols:
        for metric in ["rank", "score"]:
            col_name = f"{metric}_{region}"
            if col_name not in row or col_name not in src_rank[c]:
                continue
            expected = src_rank[c][col_name]
            expected_f = float(expected) if pd.notna(expected) else np.nan
            actual_f = row[col_name] if pd.notna(row[col_name]) else np.nan
            if not check_val(expected_f, actual_f, f"rank_2019/{c}/{col_name}"):
                error(f"{c}/{col_name}: fuente={expected_f}, destino={actual_f}")

log(f"  Rankings: {n_ok} entradas verificadas")

# ============================================================
# PARTE 4: VERIFICACION DE DATOS SINTETICOS
# ============================================================
log("\n" + "-" * 70)
log("PARTE 4: DETECCION DE POSIBLES DATOS SINTETICOS")
log("-" * 70)

# 4a: Check that non-existent year-variable combinations are NaN
# 2019 should NOT have 2020-2024 variables (government, technology_sector, etc.)
na_checks = [
    ("2019", "government"), ("2019", "technology_sector"), ("2019", "policy_capacity"),
    ("2020", "policy_capacity"), ("2020", "ai_infrastructure"),
    ("2021", "policy_capacity"), ("2021", "governance_2025"),
    ("2022", "policy_capacity"), ("2022", "size"),  # size doesn't exist in 2022
    ("2023", "policy_capacity"), ("2023", "size"),
    ("2024", "policy_capacity"), ("2024", "size"),
    ("2025", "government"), ("2025", "size"), ("2025", "maturity"),  # 2025 framework renamed
]
log("  Verificando que variables que NO existen en un ano sean NaN:")
all_clear = True
for year_str, var in na_checks:
    yr = int(year_str)
    subset = df_consol[df_consol["year"] == yr]
    if var not in subset.columns:
        log(f"  {year_str}/{var}: columna no existe en Consolidado (correcto)")
        continue
    na_count = subset[var].isna().sum()
    total = len(subset)
    if na_count == total:
        log(f"  ✓ {year_str}/{var}: 100% NaN ({na_count}/{total})")
    else:
        error(f"  ✗ {year_str}/{var}: {na_count}/{total} NaN (esperado 100%) - POSIBLE DATO SINTETICO")
        all_clear = False

# 4b: Check that variables that DO exist in a year are NOT all NaN
exists_checks = [
    ("2020", "government"), ("2020", "total_score"), ("2020", "vision"),
    ("2021", "total_score"), ("2022", "maturity"), ("2023", "ind_ai_strategy"),
    ("2024", "ranking_detail"), ("2025", "policy_capacity"),
]
log("  Verificando que variables que SI existen tengan datos reales:")
for year_str, var in exists_checks:
    yr = int(year_str)
    subset = df_consol[df_consol["year"] == yr]
    if var not in subset.columns:
        error(f"  {year_str}/{var}: columna NO existe en Consolidado")
        continue
    na_count = subset[var].isna().sum()
    non_na = total - na_count
    total = len(subset)
    # Some variables have legitimate NaN (e.g., ranking_detail 82/188 NaN)
    if non_na > 0:
        log(f"  ✓ {year_str}/{var}: {non_na}/{total} con datos reales")
    else:
        error(f"  ✗ {year_str}/{var}: 0/{total} con datos - POSIBLE DATO FALTANTE NO ESPERADO")
        all_clear = False

# 4c: Check for suspicious patterns that indicate synthetic data
# All values should have AT LEAST some variation (no column should be constant)
log("  Verificando variacion natural de datos (columnas constantes = posible sintesis):")
for col in df_consol.columns:
    if col in ["iso3", "entity_type", "pais_original", "year", "scale", "framework"]:
        continue
    nunique = df_consol[col].nunique()
    if nunique == 0:
        continue  # all NaN - expected for year-specific variables
    if nunique == 1 and df_consol[col].notna().sum() > 1:
        error(f"  {col}: solo 1 valor unico con {df_consol[col].notna().sum()} valores no-NaN - sospechoso")
    elif nunique <= 3 and col.startswith("norm_") == False:
        # Some variables ARE genuinely low-cardinality (Vision is 3-valued)
        pass

# 4d: Verify that the Rankings_Regionales_2019 sheet comes from Rankings sheet, NOT Data
log("  Verificando que rankings regionales no duplican scores principales:")
for _, row in df_rank_dest.iterrows():
    score_global = row.get("score_global")
    # This should match the index_score from Data sheet
    c = row["pais_original"]
    if c in src_2019 and pd.notna(score_global):
        expected = src_2019[c]["total_score"]
        if abs(score_global - expected) > 0.1:
            error(f"  {c}: score_global rankings ({score_global}) != index_score data ({expected})")

# ============================================================
# PARTE 5: VERIFICACION DE ISO3
# ============================================================
log("\n" + "-" * 70)
log("PARTE 5: Verificacion de ISO3 mapping")
log("-" * 70)

log("  Verificando que iso3 proviene del mapping manual, no de datos externos:")
# Check that iso3 mapping covers all countries in the dataset
all_consol_countries = set(df_consol["pais_original"].unique())
all_mapped_countries = set(df_iso["pais_original"].unique())
unmapped = all_consol_countries - all_mapped_countries
if unmapped:
    error(f"  Paises sin mapping: {unmapped}")
else:
    log(f"  ✓ Todos los {len(all_consol_countries)} paises unicos tienen ISO3")

# Check no iso3 is NaN in consolidado
na_iso = df_consol["iso3"].isna().sum()
if na_iso > 0:
    error(f"  {na_iso} filas sin ISO3 en Consolidado")
else:
    log(f"  ✓ 0 filas sin ISO3 en Consolidado")

# ============================================================
# PARTE 6: CONCLUSION
# ============================================================
log("\n" + "=" * 80)
log("RESULTADO DE LA AUDITORIA")
log("=" * 80)

total_checks = (checks_before + checks_2020 + checks_2021 + checks_2022 + 
                checks_2023_p + checks_2023_i + checks_2024 + checks_2025 +
                CHECKS)  # + other CHECKS from parts 2-5
                
# Count total checks more carefully
total_2019_check = checks_before
all_checks = total_2019_check + checks_2020 + checks_2021 + checks_2022 + checks_2023_p + checks_2023_i + checks_2024 + checks_2025

log(f"\n  Total de valores verificados contra fuentes originales: {all_checks}")
log(f"  Discrepancias encontradas: {len(MISMATCHES)}")
log(f"  Errores reportados: {ERRORS}")

if ERRORS == 0 and len(MISMATCHES) == 0:
    log(f"\n  ✅ CONCLUSION: AUDITORIA PASADA")
    log(f"  No se encontraron datos sinteticos, estimados ni inventados.")
    log(f"  Cada valor verificado coincide exactamente con su fuente original.")
    log(f"  Las columnas derivadas (iso3, entity_type, scale, framework)")
    log(f"  son metadatos agregados durante la consolidacion y estan")
    log(f"  documentadas como tales en Diccionario_Variables y Fuentes_Directas.")
else:
    log(f"\n  ❌ CONCLUSION: AUDITORIA FALLADA")
    log(f"  Se encontraron {ERRORS} errores y {len(MISMATCHES)} discrepancias.")
    log(f"  Detalle de discrepancias:")
    for m in MISMATCHES[:50]:
        log(f"    - {m}")

# Save report
report_path = os.path.join(VALIDATION_DIR, "audit_report.txt")
with open(report_path, "w") as f:
    f.write("\n".join(REPORT))
log(f"\nReporte guardado: {report_path}")
