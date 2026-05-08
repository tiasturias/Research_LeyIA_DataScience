"""Tarea 10: Construir DICCIONARIO de variables con metadata completa.
Incluye: bloque, variable, codigo_wb, nombre_wb, descripcion, tipo, unidad, URL.
"""
import requests
import csv
import os
from datetime import datetime

OUTPUT = "/Users/francoia/Documents/Research_AI_law/World Bank WDI/data_v2/DICCIONARIO.csv"
MATRIZ = "/Users/francoia/Documents/Research_AI_law/World Bank WDI/data_v2/MATRIZ_COMPLETA.csv"

# Definicion completa de los 37 indicadores
INDICATORS = [
    # Bloque Desarrollo (7 WDI)
    {"bloque": "Desarrollo", "canonical": "gdp_per_capita_ppp", "wb_code": "NY.GDP.PCAP.PP.CD", "wb_name": "GDP per capita, PPP (current international $)", "description": "PIB per capita ajustado por paridad de poder adquisitivo (PPA). Mide el nivel de desarrollo economico de un pais, controlando por diferencias en costo de vida. Variable de control fundamental en modelos de innovacion y adopcion tecnologica.", "unit": "USD internacionales corrientes", "scale": "Corriente"},
    {"bloque": "Desarrollo", "canonical": "gdp_current_usd", "wb_code": "NY.GDP.MKTP.CD", "wb_name": "GDP (current US$)", "description": "Producto Interno Bruto a precios de mercado en dolares estadounidenses corrientes. Indica el tamano absoluto de la economia.", "unit": "USD corrientes", "scale": "Corriente"},
    {"bloque": "Desarrollo", "canonical": "gdp_growth_annual_pct", "wb_code": "NY.GDP.MKTP.KD.ZG", "wb_name": "GDP growth (annual %)", "description": "Tasa de crecimiento anual del PIB a precios constantes. Control de dinamismo economico y ciclo de negocios.", "unit": "% anual", "scale": "Porcentaje"},
    {"bloque": "Desarrollo", "canonical": "inflation_consumer_prices", "wb_code": "FP.CPI.TOTL.ZG", "wb_name": "Inflation, consumer prices (annual %)", "description": "Cambio porcentual anual en el costo promedio de la canasta de bienes y servicios. Control de estabilidad macroeconomica.", "unit": "% anual", "scale": "Porcentaje"},
    {"bloque": "Desarrollo", "canonical": "unemployment_rate", "wb_code": "SL.UEM.TOTL.ZS", "wb_name": "Unemployment, total (% of total labor force)", "description": "Porcentaje de la fuerza laboral que esta sin trabajo pero busca empleo activamente. Control de condicion del mercado laboral.", "unit": "% fuerza laboral", "scale": "Porcentaje"},
    {"bloque": "Desarrollo", "canonical": "population", "wb_code": "SP.POP.TOTL", "wb_name": "Population, total", "description": "Poblacion total de mitad de ano. Util para normalizar variables en terminos per capita.", "unit": "Personas", "scale": "Absoluta"},
    {"bloque": "Desarrollo", "canonical": "labor_force", "wb_code": "SL.TLF.TOTL.IN", "wb_name": "Labor force, total", "description": "Tamano total de la fuerza laboral. Complementa unemployment_rate para evaluar el mercado de trabajo.", "unit": "Personas", "scale": "Absoluta"},
    
    # Bloque Apertura (5 WDI)
    {"bloque": "Apertura", "canonical": "exports_pct_gdp", "wb_code": "NE.EXP.GNFS.ZS", "wb_name": "Exports of goods and services (% of GDP)", "description": "Exportaciones totales como porcentaje del PIB. Mide el grado de apertura externa de la economia.", "unit": "% PIB", "scale": "Porcentaje"},
    {"bloque": "Apertura", "canonical": "trade_pct_gdp", "wb_code": "NE.TRD.GNFS.ZS", "wb_name": "Trade (% of GDP)", "description": "Suma de exportaciones e importaciones como porcentaje del PIB. Indicador integral de apertura comercial.", "unit": "% PIB", "scale": "Porcentaje"},
    {"bloque": "Apertura", "canonical": "fdi_net_inflows", "wb_code": "BX.KLT.DINV.CD.WD", "wb_name": "Foreign direct investment, net inflows (BoP, current US$)", "description": "Inversion extranjera directa neta en dolares corrientes. Mide la entrada de capital productivo internacional.", "unit": "USD corrientes", "scale": "Corriente"},
    {"bloque": "Apertura", "canonical": "fdi_pct_gdp", "wb_code": "BX.KLT.DINV.WD.GD.ZS", "wb_name": "Foreign direct investment, net inflows (% of GDP)", "description": "Inversion extranjera directa neta como porcentaje del PIB. Mejor para comparar paises que FDI en valores absolutos.", "unit": "% PIB", "scale": "Porcentaje"},
    {"bloque": "Apertura", "canonical": "gross_capital_formation_pct_gdp", "wb_code": "NE.GDI.TOTL.ZS", "wb_name": "Gross capital formation (% of GDP)", "description": "Formacion bruta de capital como porcentaje del PIB. Inversion agregada en la economia.", "unit": "% PIB", "scale": "Porcentaje"},
    
    # Bloque Digital (5 WDI)
    {"bloque": "Digital", "canonical": "internet_penetration", "wb_code": "IT.NET.USER.ZS", "wb_name": "Individuals using the Internet (% of population)", "description": "Porcentaje de la poblacion que utiliza Internet. Indicador clave de infraestructura digital basica.", "unit": "% poblacion", "scale": "Porcentaje"},
    {"bloque": "Digital", "canonical": "mobile_subscriptions_per100", "wb_code": "IT.CEL.SETS.P2", "wb_name": "Mobile cellular subscriptions (per 100 people)", "description": "Suscripciones a telefonia movil celular por cada 100 personas. Indicador de conectividad movil.", "unit": "por 100 personas", "scale": "Ratio"},
    {"bloque": "Digital", "canonical": "fixed_broadband_per100", "wb_code": "IT.NET.BBND.P2", "wb_name": "Fixed broadband subscriptions (per 100 people)", "description": "Suscripciones a banda ancha fija por cada 100 personas. Indicador de infraestructura digital avanzada.", "unit": "por 100 personas", "scale": "Ratio"},
    {"bloque": "Digital", "canonical": "secure_servers_per_1m", "wb_code": "IT.NET.SECR.P6", "wb_name": "Secure Internet servers (per 1 million people)", "description": "Servidores de Internet seguros por cada millon de personas. Proxy de madurez en ciberseguridad y servicios digitales.", "unit": "por 1M personas", "scale": "Ratio"},
    {"bloque": "Digital", "canonical": "electric_consumption_kwh_pc", "wb_code": "EG.USE.ELEC.KH.PC", "wb_name": "Electric power consumption (kWh per capita)", "description": "Consumo de energia electrica per capita en kWh. Proxy de capacidad energetica, relevante para infraestructura de IA y data centers.", "unit": "kWh per capita", "scale": "Ratio"},
    
    # Bloque Capital Humano (4 WDI)
    {"bloque": "Capital_Humano", "canonical": "tertiary_education_enrollment", "wb_code": "SE.TER.ENRR", "wb_name": "School enrollment, tertiary (% gross)", "description": "Tasa bruta de matricula en educacion terciaria. Indicador de capital humano avanzado.", "unit": "% bruto", "scale": "Porcentaje"},
    {"bloque": "Capital_Humano", "canonical": "education_expenditure_pct_gdp", "wb_code": "SE.XPD.TOTL.GD.ZS", "wb_name": "Government expenditure on education, total (% of GDP)", "description": "Gasto publico en educacion como porcentaje del PIB. Control de inversion en capital humano.", "unit": "% PIB", "scale": "Porcentaje"},
    {"bloque": "Capital_Humano", "canonical": "rd_expenditure_pct_gdp", "wb_code": "GB.XPD.RSDV.GD.ZS", "wb_name": "Research and development expenditure (% of GDP)", "description": "Gasto en investigacion y desarrollo como porcentaje del PIB. Indicador directo de capacidad cientifica nacional.", "unit": "% PIB", "scale": "Porcentaje"},
    {"bloque": "Capital_Humano", "canonical": "researchers_rd_per_million", "wb_code": "SP.POP.SCIE.RD.P6", "wb_name": "Researchers in R&D (per million people)", "description": "Investigadores en I+D por cada millon de personas. Indicador de intensidad de capital cientifico.", "unit": "por 1M personas", "scale": "Ratio"},
    
    # Bloque Innovacion (4 WDI)
    {"bloque": "Innovacion", "canonical": "patent_applications_residents", "wb_code": "IP.PAT.RESD", "wb_name": "Patent applications, residents", "description": "Solicitudes de patentes presentadas por residentes del pais. Indicador directo de produccion de innovacion domestica.", "unit": "Numero", "scale": "Absoluta"},
    {"bloque": "Innovacion", "canonical": "high_tech_exports_pct_manufactured", "wb_code": "TX.VAL.TECH.MF.ZS", "wb_name": "High-technology exports (% of manufactured exports)", "description": "Exportaciones de alta tecnologia como porcentaje de las exportaciones manufactureras. Indicador de sofisticacion tecnologica de la canasta exportadora.", "unit": "% exports manuf.", "scale": "Porcentaje"},
    {"bloque": "Innovacion", "canonical": "ict_goods_exports_pct", "wb_code": "TX.VAL.ICTG.ZS.UN", "wb_name": "ICT goods exports (% of total goods exports)", "description": "Exportaciones de bienes TIC como porcentaje del total de exportaciones de bienes. Indicador de especializacion en bienes tecnologicos.", "unit": "% exports bienes", "scale": "Porcentaje"},
    {"bloque": "Innovacion", "canonical": "ict_service_exports_pct", "wb_code": "BX.GSR.CCIS.ZS", "wb_name": "ICT service exports (% of service exports, BoP)", "description": "Exportaciones de servicios TIC como porcentaje de las exportaciones totales de servicios. Indicador de economia digital exportadora de servicios.", "unit": "% exports servicios", "scale": "Porcentaje"},
    
    # Bloque Gobernanza WGI (6 Estimates + 6 SE)
    {"bloque": "Gobernanza", "canonical": "control_of_corruption", "wb_code": "CC.EST", "wb_name": "Control of Corruption: Estimate", "description": "Percepcion sobre el grado en que el poder publico se ejerce para beneficio privado, incluyendo corrupcion menor y grave, y captura del Estado por elites. Escala aprox. -2.5 a +2.5. Fuente: WGI (Worldwide Governance Indicators).", "unit": "-2.5 a +2.5", "scale": "Indice estandarizado"},
    {"bloque": "Gobernanza", "canonical": "government_effectiveness", "wb_code": "GE.EST", "wb_name": "Government Effectiveness: Estimate", "description": "Percepcion sobre la calidad de los servicios publicos, la calidad del servicio civil y su grado de independencia de presiones politicas, la calidad de la formulacion e implementacion de politicas, y la credibilidad del compromiso gubernamental con dichas politicas. Fuente: WGI.", "unit": "-2.5 a +2.5", "scale": "Indice estandarizado"},
    {"bloque": "Gobernanza", "canonical": "political_stability", "wb_code": "PV.EST", "wb_name": "Political Stability and Absence of Violence/Terrorism: Estimate", "description": "Percepcion sobre la probabilidad de inestabilidad politica o violencia con motivacion politica, incluyendo terrorismo. Fuente: WGI.", "unit": "-2.5 a +2.5", "scale": "Indice estandarizado"},
    {"bloque": "Gobernanza", "canonical": "regulatory_quality", "wb_code": "RQ.EST", "wb_name": "Regulatory Quality: Estimate", "description": "Percepcion sobre la capacidad del gobierno de formular e implementar politicas y regulaciones solidas que permitan y promuevan el desarrollo del sector privado. ATENCION: este indicador mide calidad regulatoria GENERAL, no regulacion especifica de IA. Debe usarse como control institucional, no como proxy de regulacion de inteligencia artificial. Fuente: WGI.", "unit": "-2.5 a +2.5", "scale": "Indice estandarizado"},
    {"bloque": "Gobernanza", "canonical": "rule_of_law", "wb_code": "RL.EST", "wb_name": "Rule of Law: Estimate", "description": "Percepcion sobre el grado en que los agentes confian y respetan las reglas sociales, en particular la calidad del cumplimiento de contratos, derechos de propiedad, la policia y los tribunales, asi como la probabilidad de delito y violencia. Fuente: WGI.", "unit": "-2.5 a +2.5", "scale": "Indice estandarizado"},
    {"bloque": "Gobernanza", "canonical": "voice_accountability", "wb_code": "VA.EST", "wb_name": "Voice and Accountability: Estimate", "description": "Percepcion sobre el grado en que los ciudadanos pueden participar en la eleccion de su gobierno, asi como la libertad de expresion, de asociacion y de prensa. Fuente: WGI.", "unit": "-2.5 a +2.5", "scale": "Indice estandarizado"},
    
    # Standard Errors WGI (6)
    {"bloque": "Gobernanza", "canonical": "control_of_corruption_se", "wb_code": "CC.STD.ERR", "wb_name": "Control of Corruption: Standard Error", "description": "Error estandar de la estimacion de Control de Corrupcion. Permite construir intervalos de confianza y evaluar la precision de la medicion. Fuente: WGI.", "unit": "Error estandar", "scale": "Incertidumbre"},
    {"bloque": "Gobernanza", "canonical": "government_effectiveness_se", "wb_code": "GE.STD.ERR", "wb_name": "Government Effectiveness: Standard Error", "description": "Error estandar de la estimacion de Efectividad Gubernamental. Fuente: WGI.", "unit": "Error estandar", "scale": "Incertidumbre"},
    {"bloque": "Gobernanza", "canonical": "political_stability_se", "wb_code": "PV.STD.ERR", "wb_name": "Political Stability: Standard Error", "description": "Error estandar de la estimacion de Estabilidad Politica. Fuente: WGI.", "unit": "Error estandar", "scale": "Incertidumbre"},
    {"bloque": "Gobernanza", "canonical": "regulatory_quality_se", "wb_code": "RQ.STD.ERR", "wb_name": "Regulatory Quality: Standard Error", "description": "Error estandar de la estimacion de Calidad Regulatoria. Fuente: WGI.", "unit": "Error estandar", "scale": "Incertidumbre"},
    {"bloque": "Gobernanza", "canonical": "rule_of_law_se", "wb_code": "RL.STD.ERR", "wb_name": "Rule of Law: Standard Error", "description": "Error estandar de la estimacion de Estado de Derecho. Fuente: WGI.", "unit": "Error estandar", "scale": "Incertidumbre"},
    {"bloque": "Gobernanza", "canonical": "voice_accountability_se", "wb_code": "VA.STD.ERR", "wb_name": "Voice and Accountability: Standard Error", "description": "Error estandar de la estimacion de Voz y Rendicion de Cuentas. Fuente: WGI.", "unit": "Error estandar", "scale": "Incertidumbre"},
]

def compute_ranges():
    """Read MATRIZ_COMPLETA and compute min/max for each variable."""
    import pandas as pd
    df = pd.read_csv(MATRIZ)
    ranges = {}
    for col in df.columns:
        if col in ["iso3", "country_name", "wb_region", "wb_income_group"]:
            continue
        base_var = "_".join(col.split("_")[:-1])
        if base_var not in ranges:
            ranges[base_var] = {"min": float("inf"), "max": float("-inf")}
        col_min = df[col].min()
        col_max = df[col].max()
        if pd.notna(col_min) and col_min < ranges[base_var]["min"]:
            ranges[base_var]["min"] = col_min
        if pd.notna(col_max) and col_max > ranges[base_var]["max"]:
            ranges[base_var]["max"] = col_max
    return ranges

def main():
    print("=" * 80)
    print("TAREA 10: Construir DICCIONARIO de variables")
    print(f"Hora: {datetime.now().isoformat()}")
    print("=" * 80)
    
    ranges = compute_ranges()
    print(f"Computed ranges for {len(ranges)} variables")
    
    rows = []
    for ind in INDICATORS:
        source = "WDI" if ind["bloque"] in ["Desarrollo","Apertura","Digital","Capital_Humano","Innovacion"] else "WGI"
        wb_code = ind["wb_code"]
        
        # URL for auditability
        if source == "WDI":
            url_api = f"https://api.worldbank.org/v2/country/all/indicator/{wb_code}?date=2018:2025&format=json&source=2"
            url_web = f"https://data.worldbank.org/indicator/{wb_code}"
            extraction = "API v2 (source=2)"
        else:
            url_api = "WGI no disponible via API. Descargado de: https://www.worldbank.org/content/dam/sites/govindicators/doc/wgidataset_with_sourcedata-2025.xlsx"
            url_web = "https://www.worldbank.org/en/publication/worldwide-governance-indicators"
            extraction = "Excel directo (govindicators/doc/wgidataset_with_sourcedata-2025.xlsx)"
        
        # Range
        var_range = ranges.get(ind["canonical"], {"min": "N/A", "max": "N/A"})
        rmin = round(var_range["min"], 4) if isinstance(var_range["min"], (int, float)) else var_range["min"]
        rmax = round(var_range["max"], 4) if isinstance(var_range["max"], (int, float)) else var_range["max"]
        
        rows.append({
            "bloque": ind["bloque"],
            "variable": ind["canonical"],
            "codigo_wb": wb_code,
            "nombre_wb": ind["wb_name"],
            "descripcion": ind["description"],
            "unidad": ind["unit"],
            "escala": ind["scale"],
            "rango_min": rmin,
            "rango_max": rmax,
            "fuente": source,
            "metodo_extraccion": extraction,
            "url_api": url_api,
            "url_web": url_web,
        })
    
    # Save
    fieldnames = [
        "bloque", "variable", "codigo_wb", "nombre_wb", "descripcion",
        "unidad", "escala", "rango_min", "rango_max",
        "fuente", "metodo_extraccion", "url_api", "url_web"
    ]
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Guardado: {OUTPUT}")
    print(f"  Variables: {len(rows)}")
    
    # Summary per block
    blocks = {}
    for r in rows:
        b = r["bloque"]
        blocks[b] = blocks.get(b, 0) + 1
    print("\nResumen por bloque:")
    for b, c in blocks.items():
        print(f"  {b}: {c} variables")

if __name__ == "__main__":
    main()
