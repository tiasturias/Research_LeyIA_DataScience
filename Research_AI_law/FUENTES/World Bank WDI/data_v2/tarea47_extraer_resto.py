"""Tareas 4-7: Extraer Bloques Apertura, Digital, Capital Humano, Innovacion.
Extrae 18 indicadores WDI restantes en una sola pasada.
"""
import requests
import csv
import os
from datetime import datetime

BASE_URL = "https://api.worldbank.org/v2"
OUTPUT_DIR = "/Users/francoia/Documents/Research_AI_law/World Bank WDI/data_v2/raw"
COUNTRIES_FILE = "/Users/francoia/Documents/Research_AI_law/World Bank WDI/data_v2/raw/tarea2_paises_metadata.csv"

BLOCKS = {
    "Apertura": {
        "NE.EXP.GNFS.ZS":       "exports_pct_gdp",
        "NE.TRD.GNFS.ZS":       "trade_pct_gdp",
        "BX.KLT.DINV.CD.WD":    "fdi_net_inflows",
        "BX.KLT.DINV.WD.GD.ZS": "fdi_pct_gdp",
        "NE.GDI.TOTL.ZS":       "gross_capital_formation_pct_gdp",
    },
    "Digital": {
        "IT.NET.USER.ZS":       "internet_penetration",
        "IT.CEL.SETS.P2":       "mobile_subscriptions_per100",
        "IT.NET.BBND.P2":       "fixed_broadband_per100",
        "IT.NET.SECR.P6":       "secure_servers_per_1m",
        "EG.USE.ELEC.KH.PC":    "electric_consumption_kwh_pc",
    },
    "Capital_Humano": {
        "SE.TER.ENRR":          "tertiary_education_enrollment",
        "SE.XPD.TOTL.GD.ZS":    "education_expenditure_pct_gdp",
        "GB.XPD.RSDV.GD.ZS":    "rd_expenditure_pct_gdp",
        "SP.POP.SCIE.RD.P6":    "researchers_rd_per_million",
    },
    "Innovacion": {
        "IP.PAT.RESD":          "patent_applications_residents",
        "TX.VAL.TECH.MF.ZS":    "high_tech_exports_pct_manufactured",
        "TX.VAL.ICTG.ZS.UN":    "ict_goods_exports_pct",
        "BX.GSR.CCIS.ZS":       "ict_service_exports_pct",
    },
}

def load_valid_countries():
    valid = set()
    with open(COUNTRIES_FILE, "r") as f:
        for row in csv.DictReader(f):
            valid.add(row["iso3"])
    return valid

def fetch_indicator(code, canonical, valid_iso3):
    url = f"{BASE_URL}/country/all/indicator/{code}"
    params = {"date": "2018:2025", "format": "json", "per_page": 20000, "source": 2}
    
    r = requests.get(url, params=params, timeout=120)
    if r.status_code != 200:
        return None, {"code": code, "error": f"HTTP {r.status_code}"}
    
    data = r.json()
    if not data or len(data) < 2 or not data[1]:
        return None, {"code": code, "error": "Empty response"}
    
    meta = data[0]
    records = data[1]
    
    rows = []
    n_agg = 0
    n_null = 0
    for d in records:
        iso3 = d.get("countryiso3code", "")
        val = d.get("value")
        year = d.get("date", "")
        if iso3 not in valid_iso3:
            n_agg += 1
            continue
        if val is None:
            n_null += 1
            continue
        rows.append({
            "iso3": iso3, "year": year,
            "country_name": d.get("country", {}).get("value", ""),
            "value": val, "wb_indicator": code,
            "canonical_name": canonical,
        })
    
    name = meta.get("name", "")
    last_updated = meta.get("lastupdated", "")
    years = sorted(set(r["year"] for r in rows))
    countries = sorted(set(r["iso3"] for r in rows))
    
    audit = {
        "canonical_name": canonical, "wb_code": code, "wb_name": name,
        "last_updated_wb": last_updated, "total_records_api": meta.get("total", 0),
        "n_aggregates_filtered": n_agg, "n_null_filtered": n_null,
        "n_rows_final": len(rows), "n_countries": len(countries),
        "years_data": ", ".join(years),
        "extraction_timestamp": datetime.now().isoformat(),
        "api_url": f"{url}?date=2018:2025&format=json&per_page=20000&source=2",
    }
    return rows, audit

def main():
    print("=" * 80)
    print("TAREAS 4-7: Extraccion Bloques Apertura, Digital, Capital Humano, Innovacion")
    print(f"Hora: {datetime.now().isoformat()}")
    print("=" * 80)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    valid_iso3 = load_valid_countries()
    print(f"Valid countries: {len(valid_iso3)}\n")
    
    total_indicators = 0
    total_rows = 0
    
    for block_name, indicators in BLOCKS.items():
        print(f"--- BLOQUE: {block_name} ---")
        block_audit = []
        block_rows = 0
        
        for i, (code, canonical) in enumerate(indicators.items(), 1):
            print(f"  [{i}/{len(indicators)}] {code} ({canonical})...", end=" ")
            rows, audit = fetch_indicator(code, canonical, valid_iso3)
            
            if rows:
                # Save CSV
                out_path = os.path.join(OUTPUT_DIR, f"tarea47_{canonical}.csv")
                with open(out_path, "w", newline="") as f:
                    w = csv.DictWriter(f, fieldnames=["iso3","year","country_name","value","wb_indicator","canonical_name"])
                    w.writeheader()
                    w.writerows(rows)
                
                block_rows += len(rows)
                audit["bloque"] = block_name
                audit["output_file"] = out_path
                block_audit.append(audit)
                print(f"OK | {len(rows)} rows | {audit['n_countries']} countries | years: {audit['years_data']}")
            else:
                print(f"FAIL | {audit.get('error','')}")
        
        total_indicators += len(block_audit)
        total_rows += block_rows
        
        # Save block audit
        audit_path = os.path.join(OUTPUT_DIR, f"tarea47_audit_{block_name}.csv")
        fieldnames = [
            "bloque","canonical_name","wb_code","wb_name","last_updated_wb",
            "total_records_api","n_aggregates_filtered","n_null_filtered",
            "n_rows_final","n_countries","years_data","output_file",
            "extraction_timestamp","api_url"
        ]
        with open(audit_path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(block_audit)
        
        print(f"  -> {len(indicators)} indicadores, {block_rows} rows total, audit: {audit_path}\n")
    
    print("=" * 80)
    print(f"TAREAS 4-7 COMPLETADAS")
    print(f"  Bloques: 4/4")
    print(f"  Indicadores: {total_indicators}/18 extraidos")
    print(f"  Total rows: {total_rows}")

if __name__ == "__main__":
    main()
