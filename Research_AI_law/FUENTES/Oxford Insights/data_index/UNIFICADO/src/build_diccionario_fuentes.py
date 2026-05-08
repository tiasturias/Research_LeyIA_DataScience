"""
build_diccionario_fuentes.py — Pasos 7.1 + 7.2 + 8.1 + 8.2 + 9.0
Construye las hojas de documentacion a partir del schema y los contextos.
Outputs:
  - UNIFICADO/output/diccionario_variables.csv  (Hoja 7)
  - UNIFICADO/output/fuentes_directas.csv        (Hoja 8)
  - UNIFICADO/output/fuentes_directas.csv ya incluye todo
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd
import numpy as np

# --- 7.1: Compile dictionary from schema ---
df_schema = pd.read_csv(output_path("schema_consolidado.csv"))

# Add extra columns for the dictionary
desc_adicional = {
    "iso3": "Codigo ISO 3166-1 alpha-3 de tres letras. Permite cruzar con datasets externos.",
    "entity_type": "Tipo de entidad geografica: 'pais' para la mayoria, 'region' para algunas entradas en 2019.",
    "pais_original": "Nombre del pais exactamente como aparece en el archivo Excel fuente de ese ano. No normalizado.",
    "year": "Ano de la edicion del Government AI Readiness Index.",
    "scale": "Escala del total_score. '0-10' para 2019, '0-100' para 2020-2025.",
    "framework": "Framework conceptual usado ese ano: '4_clusters' (2019), '3_pillars_10_dims' (2020-2024), '6_pillars_14_dims' (2025).",
    "total_score": "Puntaje indice de preparacion gubernamental para IA. No es porcentaje absoluto, es score comparativo.",
}

fuentes = []

for _, row in df_schema.iterrows():
    var = row["variable"]
    anos = row["anos"]
    fw = row["framework"]
    desc = row["descripcion"]
    tipo = row["tipo"]
    
    # Extra scale info
    escala_info = ""
    if "scale" in desc.lower() or "0-" in desc:
        # extract from description
        import re
        m = re.search(r'\(([^)]*)\)', desc)
        if m:
            escala_info = m.group(1)
    
    # Determine source file and sheet
    if "2019" in anos and "4_clusters" in fw:
        src_file = "SHARED_-2019-Index-data-for-report.xlsx"
        src_sheet = "Data"
        src_col_hint = f"Ver contexto_2019.md para columna exacta de {var}"
    elif "2020" in anos or "2021" in anos or "2022" in anos or "2023" in anos or "2024" in anos:
        if var.startswith("ind_"):
            src_file = "2023-Government-AI-Readiness-Index-Public-Indicator-Data.xlsx"
            src_sheet = "Indicator scores"
            src_col_hint = f"Fila 3 (Indicator names), columna del indicador. Ver contexto_2023.md"
        elif var in ["ranking_detail"]:
            src_file = "2024-GAIRI-data.xlsx"
            src_sheet = "Scores per pillar and dimension"
            src_col_hint = "Columna C (Ranking)"
        else:
            src_file = "varios: 2020-2024/*.xlsx"
            src_sheet = "Detailed scores o equivalente"
            src_col_hint = f"Ver contexto_2020.md para {var}"
    elif "2025" in anos:
        src_file = "2025-Government-AI-Readiness-Index-data-1.xlsx"
        src_sheet = "Dimensions-Pillars"
        src_col_hint = f"Fila 2 (headers). Ver contexto_2025.md para columna exacta de {var}"
    else:
        src_file = ""
        src_sheet = ""
        src_col_hint = ""
    
    # For rankings_2019 variables
    if var.startswith("rank_") or var.startswith("score_") or var == "region_pertenece":
        src_file = "SHARED_-2019-Index-data-for-report.xlsx"
        src_sheet = "Rankings"
        src_col_hint = "Regiones en bloques de 3 columnas. Ver contexto_2019.md"
    
    # Entity columns from mapping
    if var in ["iso3", "entity_type"]:
        src_file = "UNIFICADO/src/iso3_mapping.py"
        src_sheet = "Derivado del mapping manual"
        src_col_hint = "Construido a partir de los nombres en los 7 Excels fuente"
    
    if var == "pais_original":
        src_file = "todos"
        src_sheet = "variable"
        src_col_hint = "Nombre exacto del pais en el Excel de cada ano"
    
    if var == "year":
        src_file = "todos"
        src_sheet = "variable"
        src_col_hint = "Ano de la edicion del indice"
    
    if var in ["scale", "framework"]:
        src_file = "UNIFICADO/src/"
        src_sheet = "Metadato agregado"
        src_col_hint = "Anadido durante el proceso de consolidacion"
    
    dic_entry = {
        "variable": var,
        "hoja_destino": "Consolidado",
        "descripcion": desc,
        "entidad": "pais",
        "tipo_valor": tipo,
        "escala": escala_info if escala_info else ("0-100" if "2020" in anos or "2025" in anos else ("0-10" if "2019" in anos else "")),
        "rango_teorico": "",
        "anos_disponibles": anos,
        "framework": fw,
    }
    
    src_entry = {
        "variable": var,
        "anos": anos,
        "archivo_origen": src_file,
        "hoja_origen": src_sheet,
        "columna_origen": src_col_hint,
        "header_origen": var,
        "notas": "",
    }
    
    fuentes.append(src_entry)

df_dicc = pd.DataFrame([{
    "variable": r["variable"], "hoja_destino": r["hoja_destino"],
    "descripcion": r["descripcion"], "entidad": r["entidad"],
    "tipo_valor": r["tipo_valor"], "escala": r["escala"],
    "anos_disponibles": r["anos_disponibles"], "framework": r["framework"]
} for r in [dict(zip(["variable","hoja_destino","descripcion","entidad","tipo_valor","escala","anos_disponibles","framework"],
                     ["iso3","Consolidado","","pais","string","","todos","todos"]))] ])  # dummy init

# Actually build properly:
dicc_rows = []
for _, srow in df_schema.iterrows():
    dicc_rows.append({
        "variable": srow["variable"],
        "hoja_destino": "Consolidado (principal) + hojas de detalle especificas",
        "descripcion": srow["descripcion"],
        "entidad": "pais",
        "tipo_valor": srow["tipo"],
        "escala": ("0-100" if ("2020" in str(srow["anos"]) or "2025" in str(srow["anos"])) else
                   "0-10" if "2019" in str(srow["anos"]) and "2020" not in str(srow["anos"]) else
                   "0-1" if "norm_" in str(srow["variable"]) else
                   "binario 0/1" if "privacy_laws" in str(srow["variable"]) else
                   "ordinal 0-2" if "ai_strategy" in str(srow["variable"]) and not str(srow["variable"]).startswith("ind_") else
                   "conteo" if "ai_startups" == str(srow["variable"]) else
                   "string" if srow["tipo"] == "string" else
                   "0-100"),
        "rango_teorico": "",
        "anos_disponibles": srow["anos"],
        "framework": srow["framework"],
        "notas": "",
    })

df_dicc = pd.DataFrame(dicc_rows)

# Build fuentes with more precision
fuente_rows = []
for _, srow in df_schema.iterrows():
    var = srow["variable"]
    anos = str(srow["anos"])
    fw = str(srow["framework"])
    
    if var in ["iso3", "entity_type"]:
        archivo = "UNIFICADO/src/iso3_mapping.py"
        hoja = "Derivado del mapeo manual"
        col_orig = "Ver ISO3_Mapping sheet"
        header = "Variable derivada"
    elif var in ["pais_original", "year", "scale", "framework"]:
        archivo = "N/A (metadato)"
        hoja = "N/A"
        col_orig = "Variable contextual agregada durante consolidacion"
        header = "N/A"
    elif "4_clusters" in fw:
        if var.startswith("rank_") or var.startswith("score_") or var == "region_pertenece":
            archivo = "SHARED_-2019-Index-data-for-report.xlsx"
            hoja = "Rankings"
            col_orig = "Bloques de 3 cols por region (Rank/Country/Score)"
            header = var.replace("rank_","Rank ").replace("score_","Score ").replace("_"," ").title()
        else:
            archivo = "SHARED_-2019-Index-data-for-report.xlsx"
            hoja = "Data"
            if var == "total_score":
                col_orig = "Col 26 (INDEX SCORE)"
                header = "INDEX SCORE"
            elif var.startswith("norm_"):
                raw_name = var.replace("norm_","").replace("_"," ").title()
                col_orig = f"Col 14-24 (NORMALISED)"
                header = f"NORMALISED: {raw_name}"
            elif var.startswith("avg_"):
                col_orig = "Col 29-32"
                header = var.replace("_"," ").title()
            else:
                col_orig = f"Col 1-12 (raw indicators)"
                header = var.replace("_"," ").title()
    elif "3_pillars_10_dims" in fw:
        if var.startswith("ind_"):
            archivo = "2023-Government-AI-Readiness-Index-Public-Indicator-Data.xlsx"
            hoja = "Indicator scores"
            col_orig = "Fila 3 (Indicator names). Col 1-39."
            header = var.replace("ind_","").replace("_"," ").title()
        elif var == "ranking_detail":
            archivo = "2024-GAIRI-data.xlsx"
            hoja = "Scores per pillar and dimension"
            col_orig = "Col C (Ranking)"
            header = "Ranking"
        else:
            archivo = "2020-2024 (varios archivos, misma estructura)"
            hoja = "Detailed scores / Pillar & dimension scores / Scores per pillar and dimension"
            col_orig = f"Columna '{var.replace('_',' ').title()}' en el Excel correspondiente"
            header = var.replace("_"," ").title()
    elif "6_pillars_14_dims" in fw:
        archivo = "2025-Government-AI-Readiness-Index-data-1.xlsx"
        hoja = "Dimensions-Pillars"
        # Map back to original header
        hdr_map = {
            "rank": "Ranking", "total_score": "Total Score",
            "policy_capacity": "Policy Capacity", "ai_infrastructure": "AI Infrastructure",
            "governance_2025": "Governance", "public_sector_adoption": "Public Sector Adoption",
            "development_diffusion": "Development & Diffusion", "resilience": "Resilience",
            "policy_vision": "Policy vision", "policy_commitment": "Policy commitment",
            "compute_capacity": "Compute capacity",
            "enabling_technical_infrastructure": "Enabling technical infrastructure",
            "data_quality": "Data quality", "governance_principles": "Governance principles",
            "regulatory_compliance": "Regulatory compliance",
            "government_digital_policy": "Government digital policy",
            "e_government_delivery": "e-Government delivery",
            "human_capital_2025": "Human capital", "ai_sector_maturity": "AI sector maturity",
            "ai_technology_diffusion": "AI technology diffusion",
            "societal_transition": "Societal transition", "safety_security": "Safety and security",
        }
        header = hdr_map.get(var, var)
        col_orig = f"Columna '{header}' en Dimensions-Pillars (fila 2)"
    else:
        archivo = ""
        hoja = ""
        col_orig = ""
        header = ""
    
    fuente_rows.append({
        "variable": var,
        "anos": anos,
        "archivo_origen": archivo,
        "hoja_origen": hoja,
        "header_origen": header,
        "columna_origen": col_orig,
        "notas": "",
    })

df_fuentes = pd.DataFrame(fuente_rows)

# --- 9.0: ISO3 Mapping sheet ---
df_iso = pd.read_csv(output_path("iso3_mapping.csv"))

# Save all
df_dicc.to_csv(output_path("diccionario_variables.csv"), index=False)
df_fuentes.to_csv(output_path("fuentes_directas.csv"), index=False)
# ISO3 mapping already exists, just rename for clarity
df_iso.to_csv(output_path("iso3_mapping_sheet.csv"), index=False)

print(f"Diccionario: {len(df_dicc)} variables")
print(f"Fuentes: {len(df_fuentes)} entradas")
print(f"ISO3 Mapping: {len(df_iso)} paises")
print("Guardados en output/")
