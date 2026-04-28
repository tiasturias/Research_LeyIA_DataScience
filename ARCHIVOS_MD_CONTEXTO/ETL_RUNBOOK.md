# ETL Runbook — Proyecto Regulacion IA

## Proposito

Este documento define el orden oficial de ejecucion del pipeline ETL, las dependencias entre scripts, los outputs esperados y las condiciones de exito. Cualquier ejecucion del pipeline debe seguir este orden exacto.

## Prerequisitos

- Python 3.9+ con entorno virtual `.venv` activado
- Todas las fuentes raw presentes en `data/raw/` (no se descargan automaticamente)
- Paquetes: `pandas`, `numpy`, `requests` (ver `requirements.txt`)

## Pipeline de Ejecucion

### Paso 0: Scripts ETL originales (raw → interim por fuente)

Estos scripts transforman datos raw en archivos interim individuales. Deben ejecutarse solo si los raw han cambiado o si los interim no existen.

| Orden | Script | Input | Output | Paises |
|-------|--------|-------|--------|--------|
| 0.1 | `src/consolidate_x1.py` | `data/raw/OECD/oecd_x1_core.csv` + `data/raw/IAPP/iapp_x1_core.csv` | `data/interim/x1_consolidated.csv` | 86 (902 rows panel) |
| 0.2 | `src/build_stanford_y.py` | `data/raw/STANFORD AI INDEX 25/...` (5 CSV figs) | `data/interim/stanford_ai_patents.csv`, `stanford_ai_investment.csv`, `stanford_ai_startups.csv` | 54-84 |
| 0.3 | `src/expand_wdi.py` | `data/raw/World Bank WDI/wdi_all_indicators_wide.csv` + World Bank API v2 | `data/interim/wdi_all_86.csv` | 85 |
| 0.3b | `src/expand_wgi.py` | World Bank DataBank API (db=3, `GOV_WGI_*.EST`) | `data/raw/World Bank WDI/wgi_expansion_22.csv` | 22 (expansion) |
| 0.4 | `src/build_derived_controls.py` | `data/raw/IAPP/iapp_x1_core.csv` + `data/raw/WIPO.../wipo_gii_snapshot_latest.csv` | `data/interim/derived_controls.csv` | 86 |
| 0.5 | `src/build_vc_proxy.py` | `data/raw/OECD/oecd_all_indicators_wide.csv` | `data/interim/ai_investment_vc_proxy.csv` | 33 |
| 0.6 | `data/raw/GDPR_coding/gdpr_like_coding.csv` | (codificacion manual) | consumido directo por `build_source_masters.py::build_gdpr_master()` | 86 |
| 0.7 | `src/expand_digital_economy.py` | World Bank WDI API (`wbgapi`) | `data/raw/World Bank WDI/digital_economy_86.csv` | 85 (TWN excluido per D-004) |
| 0.8 | `data/raw/FreedomHouse/freedom_in_the_world_2025.csv` | (codificacion manual) | consumido directo por `build_source_masters.py::build_fh_master()` | 86 |
| 0.9 | `data/raw/LegalOrigin/legal_origin_coding.csv` | (codificacion manual) | consumido directo por `build_source_masters.py::build_legal_origin_master()` | 86 |

**Nota:** Los pasos 0.3, 0.3b y 0.7 requieren acceso a internet. `expand_wgi.py` (agregado 2026-04 per Tarea A) descarga WGI (regulatory_quality, rule_of_law, government_effectiveness, control_of_corruption) para los 22 paises que la API v2 no devuelve. Usa DataBank `db=3` con prefijo `GOV_WGI_*` (la API v2 con codigos `RQ.EST`/`RL.EST` esta deprecada; ver DATA_DECISIONS_LOG D-013). **Debe ejecutarse ANTES de `build_source_masters.py`** porque este ultimo mergea `wgi_expansion_22.csv` con `wdi_all_86.csv` para construir `x2_wb_master.csv`.

**Paso 0.6 (agregado 2026-04 per Tarea A sub-tarea A.4):** `gdpr_like_coding.csv` es una codificacion manual de 86 paises basada en DLA Piper *Data Protection Laws of the World 2025*, UNCTAD Data Protection Tracker y EU Commission adequacy decisions list. No requiere internet ni scripts intermedios. Si se actualiza, solo se necesita re-ejecutar `build_source_masters.py`. Ver `info_data/METODOLOGIA_GDPR_CODING.md` y DATA_DECISIONS_LOG D-014.

**Paso 0.7 (agregado 2026-04 per Tarea A sub-tarea A.5):** `expand_digital_economy.py` descarga via `wbgapi` dos indicadores de proxy de economia digital: `ict_service_exports_pct` (BX.GSR.CCIS.ZS) y `high_tech_exports_pct` (TX.VAL.TECH.MF.ZS) para los 85 paises fetcheables (TWN excluido per D-004), ventana 2019-2024. Output raw consumido por `build_wb_master()`, que lo integra con `wdi_all_86.csv` y produce `x2_wb_master.csv`. UNCTAD DER no publica "digital_economy_gdp_pct" a nivel pais; estos son los proxies reproducibles via WDI. Ver DATA_DECISIONS_LOG D-015.

**Paso 0.8 (agregado 2026-04 per Tarea A sub-tarea A.6):** `freedom_in_the_world_2025.csv` es una codificacion manual de los 86 paises basada en Freedom House *Freedom in the World 2025* (data ano 2024). Columnas: fh_total_score (0-100), fh_status (F/PF/NF), fh_pr_score, fh_cl_score. Variables derivadas: `fh_democracy_level` (0-2 ordinal). Los scores exactos deben validarse contra el Excel oficial "All Data, FIW 2013-2025.xlsx" antes de publicacion academica. Ver `info_data/METODOLOGIA_FREEDOM_HOUSE.md` y DATA_DECISIONS_LOG D-016.

**Paso 0.9 (agregado 2026-04 per Tarea A sub-tarea A.3-bis):** `legal_origin_coding.csv` es una codificacion manual exhaustiva de los 86 paises en las 5 familias legales de La Porta-Lopez-de-Silanes-Shleifer (2008): English, French, German, Scandinavian, Socialist. Columnas: `legal_origin` (categorica 5 niveles), `is_common_law` (binaria). Casos ambiguos (SAU, JOR, IDN, PHL, TUR, MUS, CMR, CHN, VNM) desambiguados por criterio del codigo comercial de origen. Codificacion estable historicamente; no requiere updates. Ver `info_data/METODOLOGIA_LEGAL_ORIGIN.md` y DATA_DECISIONS_LOG D-017.

### Paso 1: Source Masters (interim por fuente → masters consolidados)

```bash
python src/build_source_masters.py
```

| Output | Descripcion | Paises |
|--------|-------------|--------|
| `data/interim/y_stanford_master.csv` | Patentes + inversion + startups | 86 (54-84 con datos) |
| `data/interim/y_microsoft_master.csv` | Adopcion IA | 86 (75 con datos) |
| `data/interim/y_oxford_master.csv` | AI Readiness | 86 (86 con datos) |
| `data/interim/x2_wipo_master.csv` | GII score + region | 86 (84 con datos) |
| `data/interim/x2_wb_master.csv` | Controles socioeconomicos + WGI confounders + digital economy proxies | 86 (74-85 por variable; 83 digital) |
| `data/interim/x2_gdpr_master.csv` | GDPR-like confounder (manual coding) | 86 (86 con datos) |
| `data/interim/x1_master.csv` | Variables regulatorias 2025 | 86 (86 con datos) |
| `data/interim/oecd_robustness_master.csv` | VC proxy + publicaciones | 86 (32-60 con datos) |

**Dependencias:** Requiere que todos los outputs del Paso 0 existan.

### Paso 2: Sample-Ready Dataset (masters → dataset definitivo para limpieza)

```bash
python src/build_sample_ready.py
```

| Output | Descripcion |
|--------|-------------|
| `data/interim/sample_ready_cross_section.csv` | **Dataset definitivo**: 86 paises × todas las variables + flags de completitud |
| `data/interim/coverage_matrix.csv` | Matriz variable × pais en formato largo para auditoria |

**Dependencias:** Requiere que todos los masters del Paso 1 existan + `derived_controls.csv`.

### Paso 3 (opcional): Auditoria de completitud

```bash
python src/audit_completeness.py
```

Genera `data/interim/completeness_audit.csv`. Este archivo queda como diagnostico historico; el canon para limpieza es `sample_ready_cross_section.csv`.

## Ejecucion Completa (de cero)

```bash
cd "/Users/francoia/Documents/MIA/Proyecto Data-Science/research"
source .venv/bin/activate

# Paso 0: ETL por fuente (solo si raw cambiaron)
python src/consolidate_x1.py
python src/build_stanford_y.py
python src/build_derived_controls.py
python src/build_vc_proxy.py
# python src/expand_wdi.py  # Solo si necesitas re-fetch de World Bank API v2
# python src/expand_wgi.py  # Solo si necesitas re-fetch de WGI (DataBank db=3)
# python src/expand_digital_economy.py  # Solo si necesitas re-fetch proxies de economia digital

# Paso 1: Source masters
python src/build_source_masters.py

# Paso 2: Sample-ready
python src/build_sample_ready.py
```

## Verificacion Post-Ejecucion

Despues de ejecutar el pipeline completo, verificar:

1. `sample_ready_cross_section.csv` tiene exactamente 86 filas
2. `complete_principal` >= 70 (actualmente 72)
3. `complete_confounded` >= 70 (actualmente 72) — modelo recomendado post-Tarea A
4. Los 4 grupos regulatorios estan representados en la muestra principal
5. No hay iso3 duplicados en ningun master
6. No hay valores negativos en `ai_investment_usd_bn_cumulative` o `ai_startups_cumulative`
7. `regulatory_quality` y `rule_of_law` tienen cobertura 85/86 (solo TWN missing per D-004)
8. `has_gdpr_like_law` y `gdpr_similarity_level` tienen cobertura 86/86 (manual exhaustive coding)
9. `ict_service_exports_pct` y `high_tech_exports_pct` tienen cobertura ~83/86 (BGD, SRB, VNM sin datos); `complete_digital` >= 65 (actualmente 69)
10. `fh_total_score` y `fh_democracy_level` tienen cobertura 86/86 (manual exhaustive coding); `complete_regime` = `complete_confounded` (actualmente 72)
11. `legal_origin` y `is_common_law` tienen cobertura 86/86 (La Porta 2008 manual coding); `complete_legal_tradition` = `complete_confounded` (actualmente 72); distribucion: French=30, English=24, Socialist=19, German=8, Scandinavian=5

## Manifiesto de Outputs

| Archivo | Tipo | Rol |
|---------|------|-----|
| `data/interim/x1_consolidated.csv` | Panel 2013-2025 | Insumo historico |
| `data/interim/stanford_ai_patents.csv` | Snapshot | Insumo para Stanford master |
| `data/interim/stanford_ai_investment.csv` | Snapshot | Insumo para Stanford master |
| `data/interim/stanford_ai_startups.csv` | Snapshot | Insumo para Stanford master |
| `data/interim/wdi_all_86.csv` | Panel 2013-2024 | Insumo para WB master (WDI core + WGI original 63) |
| `data/raw/World Bank WDI/wgi_expansion_22.csv` | Panel 2019-2023 | Insumo para WB master (WGI expansion 22 paises) |
| `data/raw/World Bank WDI/digital_economy_86.csv` | Panel 2019-2024 | Insumo para WB master (digital economy proxies, 85 paises) |
| `data/raw/GDPR_coding/gdpr_like_coding.csv` | Codificacion manual | Insumo para x2_gdpr_master (86 paises) |
| `data/raw/FreedomHouse/freedom_in_the_world_2025.csv` | Codificacion manual | Insumo para x2_fh_master (86 paises) |
| `data/interim/derived_controls.csv` | Snapshot | Insumo para sample-ready |
| `data/interim/ai_investment_vc_proxy.csv` | Panel | Insumo para OECD robustness |
| `data/interim/y_stanford_master.csv` | Master | Source master oficial |
| `data/interim/y_microsoft_master.csv` | Master | Source master oficial |
| `data/interim/y_oxford_master.csv` | Master | Source master oficial |
| `data/interim/x2_wipo_master.csv` | Master | Source master oficial |
| `data/interim/x2_wb_master.csv` | Master | Source master oficial |
| `data/interim/x2_gdpr_master.csv` | Master | Source master oficial (GDPR-like confounder) |
| `data/interim/x2_fh_master.csv` | Master | Source master oficial (Freedom House regimen politico) |
| `data/raw/LegalOrigin/legal_origin_coding.csv` | Codificacion manual | Insumo para x2_legal_origin_master (86 paises) |
| `data/interim/x2_legal_origin_master.csv` | Master | Source master oficial (Legal origin La Porta 2008) |
| `data/interim/x1_master.csv` | Master | Source master oficial |
| `data/interim/oecd_robustness_master.csv` | Master | Source master oficial |
| **`data/interim/sample_ready_cross_section.csv`** | **Definitivo** | **Entrada a 02_limpieza** |
| `data/interim/coverage_matrix.csv` | Auditoria | Diagnostico de cobertura |
| `data/interim/completeness_audit.csv` | Auditoria | Diagnostico historico |
