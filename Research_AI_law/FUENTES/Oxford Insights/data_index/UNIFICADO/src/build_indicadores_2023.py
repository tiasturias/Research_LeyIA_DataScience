"""
build_indicadores_2023.py — Paso 5.0
Hoja Indicadores_2023: los 39 indicadores individuales + iso3 + entity_type.
Lee DIRECTO del Excel fuente para maxima fidelidad.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd

YEAR = 2023
df_raw = read_sheet(YEAR, "Indicator scores", header=None)
df_iso = pd.read_csv(output_path("iso3_mapping.csv"))

# Same indicator mapping as extract_2023_indicators.py
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
for i in range(4, len(df_raw)):
    country_val = df_raw.iloc[i, 0]
    if pd.isna(country_val):
        continue
    entry = {"pais_original": clean_country(country_val)}
    for c in range(1, df_raw.shape[1]):
        indicator_raw = df_raw.iloc[2, c]
        if pd.isna(indicator_raw):
            continue
        raw_name = str(indicator_raw).strip()
        canonical = indicator_map.get(raw_name, raw_name)
        val = df_raw.iloc[i, c]
        try:
            entry[canonical] = float(val) if pd.notna(val) else None
        except (ValueError, TypeError):
            entry[canonical] = None
    rows.append(entry)

df_out = pd.DataFrame(rows)

# Also extract source row as metadata
source_row_data = {}
for c in range(1, df_raw.shape[1]):
    indicator_raw = df_raw.iloc[2, c]
    if pd.isna(indicator_raw):
        continue
    raw_name = str(indicator_raw).strip()
    canonical = indicator_map.get(raw_name, raw_name)
    src = df_raw.iloc[3, c]
    source_row_data[canonical] = str(src).strip() if pd.notna(src) else ""

# Add iso3
df_out = df_out.merge(df_iso[["pais_original", "iso3", "entity_type"]],
                      on="pais_original", how="left")

ordered = ["iso3", "entity_type", "pais_original"] + list(indicator_map.values())
df_out = df_out[ordered]

validate_row_count(df_out, 193, "Indicadores_2023")
print(f"  Columnas: {len(ordered)}")

out_path = output_path("indicadores_2023.csv")
df_out.to_csv(out_path, index=False)
print(f"Guardado: {out_path}")

# Also save sources metadata
src_path = output_path("indicadores_2023_sources.csv")
src_df = pd.DataFrame([{"variable": k, "source": v} for k, v in source_row_data.items()])
src_df.to_csv(src_path, index=False)
print(f"Fuentes guardadas: {src_path} ({len(src_df)} indicadores)")
