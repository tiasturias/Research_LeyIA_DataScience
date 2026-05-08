"""Tarea 3: Extraer Bloque Desarrollo - 7 indicadores WDI.
Extract ALL countries with data from WB API v2, filter aggregates, save long-format CSV.
"""
import requests
import csv
import os
import json
from datetime import datetime

BASE_URL = "https://api.worldbank.org/v2"
OUTPUT_DIR = "/Users/francoia/Documents/Research_AI_law/World Bank WDI/data_v2/raw"
AUDIT_FILE = "/Users/francoia/Documents/Research_AI_law/World Bank WDI/data_v2/raw/tarea3_audit_desarrollo.csv"
COUNTRIES_FILE = "/Users/francoia/Documents/Research_AI_law/World Bank WDI/data_v2/raw/tarea2_paises_metadata.csv"

# 7 indicadores del Bloque Desarrollo
INDICATORS = {
    "NY.GDP.PCAP.PP.CD":  "gdp_per_capita_ppp",
    "NY.GDP.MKTP.CD":     "gdp_current_usd",
    "NY.GDP.MKTP.KD.ZG":  "gdp_growth_annual_pct",
    "FP.CPI.TOTL.ZG":     "inflation_consumer_prices",
    "SL.UEM.TOTL.ZS":     "unemployment_rate",
    "SP.POP.TOTL":        "population",
    "SL.TLF.TOTL.IN":     "labor_force",
}

def load_valid_countries():
    """Load country list, return set of valid ISO3 codes (excl aggregates)."""
    valid = set()
    with open(COUNTRIES_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            valid.add(row["iso3"])
    return valid

def fetch_indicator(code, canonical, valid_iso3):
    """Fetch all data for one WDI indicator from WB API v2."""
    url = f"{BASE_URL}/country/all/indicator/{code}"
    params = {
        "date": "2018:2025",
        "format": "json",
        "per_page": 20000,
        "source": 2,
    }
    
    print(f"  Fetching {code} ({canonical})...", end=" ")
    
    r = requests.get(url, params=params, timeout=120)
    if r.status_code != 200:
        print(f"HTTP {r.status_code}")
        return None, {"code": code, "error": f"HTTP {r.status_code}"}
    
    data = r.json()
    if not data or len(data) < 2 or not data[1]:
        print("Empty response")
        return None, {"code": code, "error": "Empty response"}
    
    meta = data[0]
    records = data[1]
    
    # Filter: only real countries, only non-null values
    rows = []
    n_aggregates = 0
    n_null = 0
    for d in records:
        iso3 = d.get("countryiso3code", "")
        val = d.get("value")
        year = d.get("date", "")
        
        if iso3 not in valid_iso3:
            n_aggregates += 1
            continue
        if val is None:
            n_null += 1
            continue
        
        rows.append({
            "iso3": iso3,
            "year": year,
            "country_name": d.get("country", {}).get("value", ""),
            "value": val,
            "wb_indicator": code,
            "canonical_name": canonical,
        })
    
    # Metadata
    name = meta.get("name", "")
    last_updated = meta.get("lastupdated", "")
    total_api = meta.get("total", 0)
    
    years_found = sorted(set(r["year"] for r in rows))
    countries_found = sorted(set(r["iso3"] for r in rows))
    
    print(f"OK | {len(rows)} rows | {len(countries_found)} countries | years: {years_found}")
    
    # Save CSV
    out_path = os.path.join(OUTPUT_DIR, f"tarea3_{canonical}.csv")
    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["iso3", "year", "country_name", "value", "wb_indicator", "canonical_name"])
        writer.writeheader()
        writer.writerows(rows)
    
    # Audit entry
    audit = {
        "bloque": "Desarrollo",
        "canonical_name": canonical,
        "wb_code": code,
        "wb_name": name,
        "last_updated_wb": last_updated,
        "total_records_api": total_api,
        "n_aggregates_filtered": n_aggregates,
        "n_null_filtered": n_null,
        "n_rows_final": len(rows),
        "n_countries": len(countries_found),
        "years_data": ", ".join(years_found),
        "output_file": out_path,
        "extraction_timestamp": datetime.now().isoformat(),
        "api_url": f"{url}?date=2018:2025&format=json&per_page=20000&source=2",
    }
    
    return rows, audit

def main():
    print("=" * 80)
    print("TAREA 3: Extraccion Bloque Desarrollo (7 indicadores WDI)")
    print(f"Hora: {datetime.now().isoformat()}")
    print("=" * 80)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    valid_iso3 = load_valid_countries()
    print(f"Valid countries loaded: {len(valid_iso3)}")
    print()
    
    all_audit = []
    total_rows = 0
    
    for i, (code, canonical) in enumerate(INDICATORS.items(), 1):
        print(f"[{i}/7]", end=" ")
        rows, audit = fetch_indicator(code, canonical, valid_iso3)
        if audit:
            all_audit.append(audit)
            if rows:
                total_rows += len(rows)
    
    # Save audit log
    audit_fieldnames = [
        "bloque", "canonical_name", "wb_code", "wb_name", "last_updated_wb",
        "total_records_api", "n_aggregates_filtered", "n_null_filtered",
        "n_rows_final", "n_countries", "years_data", "output_file",
        "extraction_timestamp", "api_url"
    ]
    with open(AUDIT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=audit_fieldnames)
        writer.writeheader()
        writer.writerows(all_audit)
    
    print(f"\n{'='*80}")
    print(f"BLOQUE DESARROLLO COMPLETADO")
    print(f"  Indicadores: {len(all_audit)}/7")
    print(f"  Total rows extracted: {total_rows}")
    print(f"  Audit log: {AUDIT_FILE}")
    print(f"  CSVs in: {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
