"""
extract_2023_indicators_to_consolidado.py — Paso 1.6
Extrae los 39 indicadores individuales de 2023.
Output: UNIFICADO/output/consolidado_2023_indicators.csv
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd
import numpy as np

YEAR = 2023
df = read_sheet(YEAR, "Indicator scores", header=None)

# Row 2 (index 2) = indicator names
# Row 3 (index 3) = sources
# Rows 4+ = data
# Col 0 = country name

indicator_names_raw = []
for c in range(1, df.shape[1]):
    name = df.iloc[2, c]
    if pd.notna(name):
        indicator_names_raw.append(str(name).strip())

# Clean names to canonical form
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

rows = []
for i in range(4, len(df)):
    country_val = df.iloc[i, 0]
    if pd.isna(country_val):
        continue
    entry = {"pais_original": clean_country(country_val)}
    for c in range(1, df.shape[1]):
        indicator_raw = df.iloc[2, c]
        if pd.isna(indicator_raw):
            continue
        raw_name = str(indicator_raw).strip()
        canonical = indicator_map.get(raw_name, raw_name)
        val = df.iloc[i, c]
        try:
            entry[canonical] = float(val) if pd.notna(val) else np.nan
        except (ValueError, TypeError):
            entry[canonical] = np.nan
    rows.append(entry)

df_out = pd.DataFrame(rows)

validate_row_count(df_out, EXPECTED_COUNTS[YEAR], f"{YEAR} indicators")
print(f"  Columnas: {len(df_out.columns)}")
print(f"  ind_ai_strategy NaN: {df_out['ind_ai_strategy'].isna().sum()}")

out_path = output_path(f"consolidado_{YEAR}_indicators.csv")
df_out.to_csv(out_path, index=False)
print(f"Guardado: {out_path}")
