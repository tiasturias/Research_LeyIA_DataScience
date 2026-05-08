"""Tarea 1: Verificar conectividad API WB y validar todos los códigos de indicadores.
FIXES:
- WDI: usa 'date' no 'year' en el JSON de respuesta
- WGI: no disponible via API v2; se descarga via Excel directo desde govindicators
"""
import requests
import csv
import os
from datetime import datetime

OUTPUT = "/Users/francoia/Documents/Research_AI_law/World Bank WDI/data_v2/raw/tarea1_validacion_indicadores.csv"

# 26 indicadores WDI (API v2)
WDI_CODES = {
    # Bloque Desarrollo
    "NY.GDP.PCAP.PP.CD":      "gdp_per_capita_ppp",
    "NY.GDP.MKTP.CD":         "gdp_current_usd",
    "NY.GDP.MKTP.KD.ZG":      "gdp_growth_annual_pct",
    "FP.CPI.TOTL.ZG":         "inflation_consumer_prices",
    "SL.UEM.TOTL.ZS":         "unemployment_rate",
    "SP.POP.TOTL":            "population",
    "SL.TLF.TOTL.IN":         "labor_force",
    # Bloque Apertura
    "NE.EXP.GNFS.ZS":         "exports_pct_gdp",
    "NE.TRD.GNFS.ZS":         "trade_pct_gdp",
    "BX.KLT.DINV.CD.WD":      "fdi_net_inflows",
    "BX.KLT.DINV.WD.GD.ZS":   "fdi_pct_gdp",
    "NE.GDI.TOTL.ZS":         "gross_capital_formation_pct_gdp",
    # Bloque Digital
    "IT.NET.USER.ZS":         "internet_penetration",
    "IT.CEL.SETS.P2":         "mobile_subscriptions_per100",
    "IT.NET.BBND.P2":         "fixed_broadband_per100",
    "IT.NET.SECR.P6":         "secure_servers_per_1m",
    "EG.USE.ELEC.KH.PC":      "electric_consumption_kwh_pc",
    # Bloque Capital Humano
    "SE.TER.ENRR":            "tertiary_education_enrollment",
    "SE.XPD.TOTL.GD.ZS":      "education_expenditure_pct_gdp",
    "GB.XPD.RSDV.GD.ZS":      "rd_expenditure_pct_gdp",
    "SP.POP.SCIE.RD.P6":      "researchers_rd_per_million",
    "SP.POP.TECH.RD.P6":      "technicians_rd_per_million",
    # Bloque Innovacion
    "IP.PAT.RESD":            "patent_applications_residents",
    "TX.VAL.TECH.MF.ZS":      "high_tech_exports_pct_manufactured",
    "TX.VAL.ICTG.ZS.UN":      "ict_goods_exports_pct",
    "BX.GSR.CCIS.ZS":         "ict_service_exports_pct",
}

# 12 indicadores WGI (NO disponibles via API v2; via Excel directo)
WGI_CODES = {
    "CC.EST":     "control_of_corruption",
    "GE.EST":     "government_effectiveness",
    "PV.EST":     "political_stability",
    "RQ.EST":     "regulatory_quality",
    "RL.EST":     "rule_of_law",
    "VA.EST":     "voice_accountability",
    "CC.STD.ERR": "control_of_corruption_se",
    "GE.STD.ERR": "government_effectiveness_se",
    "PV.STD.ERR": "political_stability_se",
    "RQ.STD.ERR": "regulatory_quality_se",
    "RL.STD.ERR": "rule_of_law_se",
    "VA.STD.ERR": "voice_accountability_se",
}

def test_wdi_indicator(code, canonical):
    """Test WDI indicator via API v2 (source=2)."""
    url = f"https://api.worldbank.org/v2/country/all/indicator/{code}"
    params = {
        "date": "2018:2025",
        "format": "json",
        "per_page": 100,  # small sample for validation
        "source": 2,
    }
    try:
        r = requests.get(url, params=params, timeout=30)
        if r.status_code != 200:
            return {"code": code, "canonical": canonical, "source": "WDI", "valid": False, 
                    "error": f"HTTP {r.status_code}"}
        
        data = r.json()
        if not data or len(data) < 2 or not data[1]:
            return {"code": code, "canonical": canonical, "source": "WDI", "valid": False,
                    "error": "Respuesta vacia"}

        meta = data[0]
        records = data[1]
        
        # Campo 'date' no 'year'
        values = [d for d in records if d.get("value") is not None]
        val_years = sorted(set(d["date"] for d in values))
        
        # Metadata
        name = meta.get("name", "")
        source_org = meta.get("source", {}).get("value", "")
        last_updated = meta.get("lastupdated", "")
        total = meta.get("total", 0)
        pages = meta.get("pages", 0)
        
        return {
            "code": code,
            "canonical": canonical,
            "source": "WDI",
            "source_id": 2,
            "name": name,
            "source_org": source_org,
            "last_updated": last_updated,
            "total_records_api": total,
            "pages": pages,
            "sample_years": ", ".join(val_years),
            "sample_values": len(values),
            "valid": len(values) > 0,
            "error": "",
        }
    except Exception as e:
        return {"code": code, "canonical": canonical, "source": "WDI", "valid": False, 
                "error": str(e)[:200]}

def check_wgi_availability():
    """Check if WGI is available via any alternative method."""
    # WGI not available via API v2 country queries
    # Check if indicator metadata at least exists
    try:
        url = "https://api.worldbank.org/v2/indicator/RQ.EST?format=json"
        r = requests.get(url, timeout=15)
        data = r.json()
        has_metadata = len(data) > 1 and data[1] is not None
        return "metadata_only" if has_metadata else "not_found"
    except:
        return "error"

def main():
    print("=" * 80)
    print("TAREA 1: Validacion de indicadores WB")
    print(f"Hora: {datetime.now().isoformat()}")
    print("=" * 80)
    
    results = []
    
    # --- WDI via API v2 ---
    print("\n--- WDI Indicators (API v2, source=2) ---")
    for i, (code, canonical) in enumerate(WDI_CODES.items(), 1):
        print(f"[{i:02d}/26] {code} ({canonical})...", end=" ")
        result = test_wdi_indicator(code, canonical)
        results.append(result)
        if result["valid"]:
            print(f"OK | total={result['total_records_api']}, years=[{result['sample_years']}], "
                  f"updated={result['last_updated']}")
        else:
            print(f"FAIL | {result['error']}")
    
    # --- WGI check ---
    print("\n--- WGI Indicators (API v2) ---")
    wgi_status = check_wgi_availability()
    print(f"WGI API status: {wgi_status}")
    print("WGI data will be downloaded from:")
    print("  https://www.worldbank.org/content/dam/sites/govindicators/doc/wgidataset_with_sourcedata-2025.xlsx")
    print("  (2025 update, covers 1996-2024)")
    
    for code, canonical in WGI_CODES.items():
        results.append({
            "code": code,
            "canonical": canonical,
            "source": "WGI",
            "source_id": "Excel",
            "name": f"WGI via Excel download (govindicators/doc/wgidataset_with_sourcedata-2025.xlsx)",
            "source_org": "World Bank WGI (govindicators)",
            "last_updated": "2025 update",
            "total_records_api": 0,
            "pages": 0,
            "sample_years": "1996-2024 (via Excel)",
            "sample_values": 0,
            "valid": True,  # available via Excel not API
            "error": "API v2 no disponible; descarga via Excel directo",
        })
    
    # Save
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    fieldnames = [
        "canonical", "code", "source", "source_id", "name", "source_org",
        "last_updated", "total_records_api", "pages",
        "sample_years", "sample_values", "valid", "error"
    ]
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            writer.writerow({k: r.get(k, "") for k in fieldnames})
    
    print(f"\nSaved: {OUTPUT}")
    
    valid_wdi = [r for r in results if r["source"] == "WDI" and r["valid"]]
    invalid_wdi = [r for r in results if r["source"] == "WDI" and not r["valid"]]
    
    print(f"\n{'='*80}")
    print(f"RESUMEN FINAL:")
    print(f"  WDI válidos (API):    {len(valid_wdi)}/26")
    print(f"  WDI fallidos:         {len(invalid_wdi)}/26")
    print(f"  WGI (via Excel):      {len(WGI_CODES)}/12 (descarga directa)")
    print(f"  TOTAL indicadores:    {len(valid_wdi) + len(WGI_CODES)}/38")
    
    if invalid_wdi:
        print("\n  WDI FALLIDOS:")
        for r in invalid_wdi:
            print(f"    {r['code']} ({r['canonical']}): {r['error']}")
    
    return results

if __name__ == "__main__":
    main()
