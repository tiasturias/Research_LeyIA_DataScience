import pandas as pd
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "data" / "raw"
STANFORD = RAW / "STANFORD AI INDEX 25"
issues = []

def chk(path, label, id_col=None):
    p = Path(path) if Path(path).is_absolute() else BASE / path
    if not p.exists():
        issues.append(f"FALTA: {p}")
        print(f"  [X] FALTA  {label}")
        return None
    try:
        if str(p).endswith(".json"):
            data = json.loads(p.read_text())
            n = len(data) if isinstance(data, list) else (len(data) if isinstance(data, dict) else "?")
            print(f"  [V] {str(n):>6} entradas          {label}")
            return data
        df = pd.read_csv(p)
        r, c = df.shape
        matched_col = next((col for col in df.columns if id_col and col.lower() == id_col.lower()), None)
        nc = df[matched_col].nunique() if matched_col else "-"
        print(f"  [V] {r:>6}r x {c:>2}c  paises={str(nc):>4}  {label}")
        return df
    except Exception as e:
        issues.append(f"ERROR {p}: {e}")
        print(f"  [X] ERROR  {label}: {e}")
        return None

sep = "=" * 68

print(f"\n{sep}")
print("FUENTE 1 - STANFORD AI INDEX 2025  (Y)")
print(sep)
se = STANFORD / "4. Economy" / "Data"
sr = STANFORD / "1. Research and Development" / "Data"
# Stanford CSVs use "Geographic area" (not iso3/country/economy) as the country column
chk(se / "fig_4.2.1.csv",  "ai_job_postings",               "Geographic area")
chk(se / "fig_4.2.15.csv", "ai_skill",                      "Geographic area")
chk(se / "fig_4.2.17.csv", "ai_talent",                     "Geographic area")
chk(se / "fig_4.3.12.csv", "ai_startups (2024)",            "Geographic area")
chk(se / "fig_4.3.13.csv", "ai_startups_cumul (2013-2024)", "Geographic area")
chk(sr / "fig_1.2.4.csv",  "ai_patents (per 100k)",         "Geographic area")
chk(se / "fig_4.3.10.csv", "ai_investment",                 "Geographic area")
chk(STANFORD / "download_manifest.csv", "download_manifest")

print(f"\n{sep}")
print("FUENTE 2 - WORLD BANK WDI  (X2)")
print(sep)
wdi = RAW / "World Bank WDI"
chk(wdi / "wdi_all_indicators_long.csv", "wdi_all_indicators_long", "iso3")
chk(wdi / "wdi_all_indicators_wide.csv", "wdi_all_indicators_wide", "iso3")
chk(wdi / "wdi_core_controls.csv",       "wdi_core_controls",       "iso3")
chk(wdi / "wdi_governance.csv",          "wdi_governance",          "iso3")
chk(wdi / "wdi_governance_metadata.csv", "wdi_governance_metadata (SE+NSRC)", "iso3")
chk(wdi / "wdi_human_capital_infra.csv", "wdi_human_capital_infra", "iso3")
chk(wdi / "wdi_economic_structure.csv",  "wdi_economic_structure",  "iso3")

print(f"\n{sep}")
print("FUENTE 3 - OECD  (Y_proxy + X1 + X2)")
print(sep)
oecd = RAW / "OECD"
chk(oecd / "oecd_all_indicators_long.csv",         "oecd_all_indicators_long",         "iso3")
chk(oecd / "oecd_all_indicators_wide.csv",         "oecd_all_indicators_wide",         "iso3")
chk(oecd / "oecd_sti_scoreboard.csv",              "oecd_sti_scoreboard (Y_proxy)",    "iso3")
chk(oecd / "oecd_msti.csv",                        "oecd_msti (X2 I+D)",               "iso3")
chk(oecd / "oecd_ai_policy_initiatives_all.csv",   "oecd_ai_policy_initiatives_all",   "iso3")
chk(oecd / "oecd_ai_policy_initiatives_study.csv", "oecd_ai_policy_initiatives_study", "iso3")
chk(oecd / "oecd_x1_policy_variables.csv",         "oecd_x1_policy_variables (panel)", "iso3")
chk(oecd / "oecd_x1_core.csv",                     "oecd_x1_core (X1 6 vars)",         "iso3")
chk(oecd / "oecd_x1_snapshot_2024.csv",            "oecd_x1_snapshot_2024",            "iso3")

print(f"\n{sep}")
print("FUENTE 4 - WIPO GII  (X2 panel 2020-2025)")
print(sep)
wipo = RAW / "WIPO Global Innovation Index"
chk(wipo / "wipo_gii_all_raw.csv",         "wipo_gii_all_raw",           "iso3")
chk(wipo / "wipo_gii_overall_panel.csv",   "wipo_gii_overall_panel",     "iso3")
chk(wipo / "wipo_gii_study.csv",           "wipo_gii_study (86 paises)", "iso3")
chk(wipo / "wipo_gii_wide.csv",            "wipo_gii_wide",              "iso3")
chk(wipo / "wipo_gii_pillars_study.csv",   "wipo_gii_pillars_study",     "iso3")
chk(wipo / "wipo_gii_snapshot_latest.csv", "wipo_gii_snapshot_latest",   "iso3")
chk(wipo / "download_manifest.csv",        "download_manifest")

print(f"\n{sep}")
print("FUENTE 5 - MICROSOFT AI Diffusion  (Y)")
print(sep)
ms = RAW / "Microsoft"
chk(ms / "microsoft_ai_diffusion_raw.csv",      "microsoft_ai_diffusion_raw",      "iso3")
chk(ms / "microsoft_ai_diffusion_study.csv",    "microsoft_ai_diffusion_study",    "iso3")
chk(ms / "microsoft_ai_adoption_panel.csv",     "microsoft_ai_adoption_panel",     "iso3")
chk(ms / "microsoft_ai_diffusion_snapshot.csv", "microsoft_ai_diffusion_snapshot", "iso3")

print(f"\n{sep}")
print("FUENTE 6 - OXFORD INSIGHTS  (Y readiness 2019-2025)")
print(sep)
ox = RAW / "Oxford Insights"
chk(ox / "oxford_ai_readiness_all_raw.csv",          "oxford_ai_readiness_all_raw",          "iso3")
chk(ox / "oxford_ai_readiness_study.csv",            "oxford_ai_readiness_study",            "iso3")
chk(ox / "oxford_ai_readiness_long.csv",             "oxford_ai_readiness_long",             "iso3")
chk(ox / "oxford_ai_readiness_wide.csv",             "oxford_ai_readiness_wide",             "iso3")
chk(ox / "oxford_ai_readiness_pillars_long.csv",     "oxford_ai_readiness_pillars_long",     "iso3")
chk(ox / "oxford_ai_readiness_dimensions_long.csv",  "oxford_ai_readiness_dimensions_long",  "iso3")
chk(ox / "oxford_ai_readiness_snapshot_latest.csv",  "oxford_ai_readiness_snapshot_latest",  "iso3")
chk(ox / "download_manifest.csv",                    "download_manifest")

print(f"\n{sep}")
print("FUENTE 7 - IAPP Tracker  (X1 regulacion IA, crudo)")
print(sep)
iapp = RAW / "IAPP"
chk(iapp / "iapp_tracker_structured_raw.csv", "iapp_tracker_structured_raw (29 jurisdicciones)")
chk(iapp / "iapp_all_coded.csv",  "iapp_all_coded (todas jurisdicciones)", "iso3")
chk(iapp / "iapp_x1_core.csv",    "iapp_x1_core (86 paises del estudio)",  "iso3")
chk(RAW  / "iapp_regulatory.csv", "iapp_regulatory.csv (flat metodologia)", "iso3")
chk(iapp / "download_manifest.csv", "download_manifest")
chk(RAW  / "iapp_tracker_raw_extracted.json", "iapp_tracker_raw_extracted.json (PDF raw)")

print(f"\n{sep}")
print("VERIFICACION ETL - no debe haber archivos Transform en data/raw/")
print(sep)
forbidden = [
    "IAPP/iapp_oecd_reconciliation.csv",
    "IAPP/iapp_x1_consolidated.csv",
    "IAPP/snapshots/iapp_x1_snapshot_2026.csv",
]
clean = True
for f in forbidden:
    if (RAW / f).exists():
        issues.append(f"ARCHIVO TRANSFORM EN RAW: {f}")
        print(f"  [X] ENCONTRADO (debe moverse a interim/): {f}")
        clean = False
if clean:
    print("  [V] Ningun archivo Transform encontrado en data/raw/ - CORRECTO")

print(f"\n{sep}")
if issues:
    print(f"RESUMEN: {len(issues)} PROBLEMA(S) DETECTADO(S)")
    for i in issues:
        print(f"  [X] {i}")
else:
    print("RESUMEN: TODO EN ORDEN - 7 fuentes, 0 problemas detectados")
print(sep)
