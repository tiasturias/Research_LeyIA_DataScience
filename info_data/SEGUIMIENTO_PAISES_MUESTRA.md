# Seguimiento De Paises - Muestra Del Estudio

## Proposito

Este documento registra el estado de cobertura de los 86 paises del estudio, usando como fuente de verdad el dataset `data/interim/sample_ready_cross_section.csv`.

## Resumen Ejecutivo (Actualizado 2026-04 — post Tarea A sub-tarea A.3-bis)

| Metrica | Valor |
|---|---|
| Total paises en muestra | 86 |
| **Muestra PRINCIPAL** (4Y + 5X1 + 5X2 core) | **72/86** |
| **Muestra CONFOUNDED** (+WGI_RQ + WGI_RL + GDPR-like) **[recomendada]** | **72/86** |
| Muestra DIGITAL (+ict_services + high_tech exports) | 69/86 |
| Muestra REGIME (+Freedom House score + democracy level) | 72/86 |
| **Muestra LEGAL_TRADITION** (+legal_origin La Porta) | **72/86** |
| Muestra EXTENDED (+R&D+educacion) | 62/86 |
| Muestra STRICT (+patents+gov_effectiveness) | 47/86 |
| Paises PARCIALES (no alcanzan PRINCIPAL) | 14 |
| Dataset definitivo | `data/interim/sample_ready_cross_section.csv` |
| Pipeline | `src/expand_wgi.py` → `src/expand_digital_economy.py` → `src/build_source_masters.py` → `src/build_sample_ready.py` |

### Fuentes integradas

| Fuente | Variable(s) | Cobertura | Master |
|---|---|---|---|
| **Stanford AI Index 2025** | ai_patents_per100k (54), ai_investment_cumulative (84), ai_startups_cumulative (84) | 54-84/86 | `y_stanford_master.csv` |
| **Microsoft AIEI 2025** | ai_adoption_rate | 75/86 | `y_microsoft_master.csv` |
| **Oxford Insights 2025** | ai_readiness_score | 86/86 | `y_oxford_master.csv` |
| **WIPO GII 2025** | gii_score | 84/86 | `x2_wipo_master.csv` |
| **World Bank WDI/WGI** | gdp_per_capita_ppp (85), internet_penetration (85), rd_expenditure (74), tertiary_education (82), **regulatory_quality (85)**, **rule_of_law (85)**, gov_effectiveness (85↑), control_of_corruption (85), **ict_service_exports_pct (83)**, **high_tech_exports_pct (83)** | 74-85/86 | `x2_wb_master.csv` |
| **DLA Piper 2025 + UNCTAD** (codificacion manual) | **has_gdpr_like_law (86)**, **gdpr_similarity_level (86)**, dp_law_year, has_dpa, eu_status, enforcement_active | 86/86 | `x2_gdpr_master.csv` |
| **Freedom House FITW 2025** (codificacion manual) | **fh_total_score (86)**, **fh_democracy_level (86)**, fh_pr_score, fh_cl_score, fh_status | 86/86 | `x2_fh_master.csv` |
| **La Porta et al. 2008** (codificacion manual) | **legal_origin (86)**, **is_common_law (86)** | 86/86 | `x2_legal_origin_master.csv` |
| **OECD + IAPP** | 5 vars X1 regulatorias | 86/86 | `x1_master.csv` |
| **OECD STI/MSTI** | VC proxy (32), publicaciones (60), patentes OECD | 32-60/86 | `oecd_robustness_master.csv` |

### Representacion regulatoria (Muestra PRINCIPAL, N=72)

| Grupo | Total (86) | En muestra principal (72) |
|---|---|---|
| binding_regulation | 32 | 27 |
| strategy_only | 39 | 34 |
| soft_framework | 10 | 9 |
| no_framework | 5 | 2 |

## Leyenda de estados

| Estado | Significado |
|---|---|
| PRINCIPAL | Tiene todas las variables del modelo principal (4Y + 5X1 + 5X2). Listo para modelamiento. |
| PARCIAL | Tiene al menos 1 variable faltante para el modelo principal. Disponible para subanalisis. |

## Tabla De Seguimiento Por Pais

| iso3 | grupo_regulatorio | estado | variables_faltantes |
|---|---|---|---|
| ARE | strategy_only | PRINCIPAL | - |
| ARG | strategy_only | PRINCIPAL | - |
| ARM | soft_framework | PRINCIPAL | - |
| AUS | strategy_only | PRINCIPAL | - |
| AUT | binding_regulation | PRINCIPAL | - |
| BEL | binding_regulation | PRINCIPAL | - |
| BGD | strategy_only | PRINCIPAL | - |
| BGR | binding_regulation | PRINCIPAL | - |
| BHR | strategy_only | PARCIAL | ai_adoption_rate |
| BLR | soft_framework | PRINCIPAL | - |
| BLZ | no_framework | PARCIAL | ai_adoption_rate, gii_score |
| BRA | strategy_only | PRINCIPAL | - |
| BRB | no_framework | PARCIAL | ai_adoption_rate |
| CAN | strategy_only | PRINCIPAL | - |
| CHE | soft_framework | PRINCIPAL | - |
| CHL | strategy_only | PRINCIPAL | - |
| CHN | binding_regulation | PRINCIPAL | - |
| CMR | no_framework | PRINCIPAL | - |
| COL | strategy_only | PRINCIPAL | - |
| CRI | strategy_only | PRINCIPAL | - |
| CYP | binding_regulation | PARCIAL | ai_adoption_rate |
| CZE | binding_regulation | PRINCIPAL | - |
| DEU | binding_regulation | PRINCIPAL | - |
| DNK | binding_regulation | PRINCIPAL | - |
| ECU | soft_framework | PRINCIPAL | - |
| EGY | strategy_only | PRINCIPAL | - |
| ESP | binding_regulation | PRINCIPAL | - |
| EST | binding_regulation | PARCIAL | ai_adoption_rate |
| FIN | binding_regulation | PRINCIPAL | - |
| FRA | binding_regulation | PRINCIPAL | - |
| GBR | strategy_only | PRINCIPAL | - |
| GHA | strategy_only | PRINCIPAL | - |
| GRC | binding_regulation | PRINCIPAL | - |
| HRV | binding_regulation | PRINCIPAL | - |
| HUN | binding_regulation | PRINCIPAL | - |
| IDN | strategy_only | PRINCIPAL | - |
| IND | soft_framework | PRINCIPAL | - |
| IRL | binding_regulation | PRINCIPAL | - |
| ISL | soft_framework | PARCIAL | ai_adoption_rate |
| ISR | soft_framework | PRINCIPAL | - |
| ITA | binding_regulation | PRINCIPAL | - |
| JOR | strategy_only | PRINCIPAL | - |
| JPN | binding_regulation | PRINCIPAL | - |
| KAZ | strategy_only | PRINCIPAL | - |
| KEN | strategy_only | PRINCIPAL | - |
| KOR | binding_regulation | PRINCIPAL | - |
| LBN | no_framework | PRINCIPAL | - |
| LKA | soft_framework | PRINCIPAL | - |
| LTU | binding_regulation | PRINCIPAL | - |
| LUX | binding_regulation | PARCIAL | ai_adoption_rate |
| LVA | binding_regulation | PARCIAL | ai_adoption_rate |
| MAR | strategy_only | PARCIAL | ai_investment_usd_bn_cumulative, ai_startups_cumulative |
| MEX | strategy_only | PRINCIPAL | - |
| MLT | binding_regulation | PARCIAL | ai_adoption_rate |
| MNG | soft_framework | PRINCIPAL | - |
| MUS | strategy_only | PARCIAL | ai_adoption_rate |
| MYS | strategy_only | PRINCIPAL | - |
| NGA | strategy_only | PRINCIPAL | - |
| NLD | binding_regulation | PRINCIPAL | - |
| NOR | strategy_only | PRINCIPAL | - |
| NZL | strategy_only | PRINCIPAL | - |
| PAK | strategy_only | PARCIAL | ai_investment_usd_bn_cumulative, ai_startups_cumulative |
| PAN | strategy_only | PRINCIPAL | - |
| PER | binding_regulation | PRINCIPAL | - |
| PHL | strategy_only | PRINCIPAL | - |
| POL | binding_regulation | PRINCIPAL | - |
| PRT | binding_regulation | PRINCIPAL | - |
| ROU | binding_regulation | PRINCIPAL | - |
| RUS | binding_regulation | PRINCIPAL | - |
| SAU | strategy_only | PRINCIPAL | - |
| SGP | strategy_only | PRINCIPAL | - |
| SRB | strategy_only | PRINCIPAL | - |
| SVK | binding_regulation | PRINCIPAL | - |
| SVN | binding_regulation | PRINCIPAL | - |
| SWE | binding_regulation | PRINCIPAL | - |
| SYC | no_framework | PARCIAL | ai_adoption_rate |
| THA | strategy_only | PRINCIPAL | - |
| TUN | strategy_only | PRINCIPAL | - |
| TUR | strategy_only | PRINCIPAL | - |
| TWN | strategy_only | PARCIAL | gdp_per_capita_ppp, internet_penetration, gii_score |
| UGA | soft_framework | PRINCIPAL | - |
| UKR | strategy_only | PRINCIPAL | - |
| URY | strategy_only | PRINCIPAL | - |
| USA | strategy_only | PRINCIPAL | - |
| VNM | strategy_only | PRINCIPAL | - |
| ZAF | strategy_only | PRINCIPAL | - |

## Analisis De Los 14 Paises PARCIALES

### Patron 1: Falta ai_adoption_rate (11 paises)

Estos paises no estan en el dataset Microsoft AIEI (147 paises globales). Es una **ausencia estructural** de la fuente, no un error de extraccion.

BHR, BLZ, BRB, CYP, EST, ISL, LUX, LVA, MLT, MUS, SYC

**Nota:** De estos, 5 son binding_regulation (CYP, EST, LUX, LVA, MLT) — su exclusion reduce ligeramente la representacion de ese grupo pero mantiene N=27 (suficiente).

### Patron 2: Falta ai_investment + ai_startups (2 paises)

MAR, PAK — no aparecen en Stanford fig_4.3.8/9/12/13. Ausencia estructural.

### Patron 3: Falta controles WB + GII (1 pais)

TWN — excluido de World Bank API y WIPO GII por status politico. Ver DATA_DECISIONS_LOG D-004.

## Cobertura Por Variable (86 paises)

| Variable | Cobertura | Rol | Fuente |
|---|---|---|---|
| has_ai_law | 86/86 | X1 principal | OECD + IAPP |
| regulatory_approach | 86/86 | X1 principal | OECD + IAPP |
| regulatory_intensity | 86/86 | X1 principal | OECD + IAPP |
| enforcement_level | 86/86 | X1 principal | OECD + IAPP |
| thematic_coverage | 86/86 | X1 principal | OECD + IAPP |
| ai_readiness_score | 86/86 | Y principal | Oxford Insights 2025 |
| oecd_member | 86/86 | X2 core | Derivado |
| region | 86/86 | X2 core | WIPO + manual |
| gdp_per_capita_ppp | 85/86 | X2 core | World Bank WDI |
| internet_penetration | 85/86 | X2 core | World Bank WDI |
| ai_investment_usd_bn_cumulative | 84/86 | Y principal | Stanford fig_4.3.9 |
| ai_startups_cumulative | 84/86 | Y principal | Stanford fig_4.3.13 |
| gii_score | 84/86 | X2 core | WIPO GII 2025 |
| tertiary_education | 82/86 | X2 extended | World Bank WDI |
| ai_adoption_rate | 75/86 | Y principal | Microsoft AIEI H2 2025 |
| rd_expenditure | 74/86 | X2 extended | World Bank WDI |
| **regulatory_quality** | **85/86** | **X2 confounder core** | World Bank WGI db=3 |
| **rule_of_law** | **85/86** | **X2 confounder core** | World Bank WGI db=3 |
| **has_gdpr_like_law** | **86/86** | **X2 confounder core (NEW 2026-04)** | DLA Piper 2025 + UNCTAD (manual) |
| **gdpr_similarity_level** | **86/86** | **X2 confounder core (NEW 2026-04)** | DLA Piper 2025 + EU adequacy list (manual) |
| **ict_service_exports_pct** | **83/86** | **X2 robustness digital economy (NEW 2026-04)** | World Bank WDI BX.GSR.CCIS.ZS |
| **high_tech_exports_pct** | **83/86** | **X2 robustness digital economy (NEW 2026-04)** | World Bank WDI TX.VAL.TECH.MF.ZS |
| **fh_total_score** | **86/86** | **X2 robustness regime politico (NEW 2026-04)** | Freedom House FITW 2025 (manual) |
| **fh_democracy_level** | **86/86** | **X2 robustness regime politico (NEW 2026-04)** | Freedom House FITW 2025 (manual, derivado) |
| **legal_origin** | **86/86** | **X2 robustness tradicion juridica (NEW 2026-04)** | La Porta et al. 2008 (manual, 5 familias) |
| **is_common_law** | **86/86** | **X2 robustness tradicion juridica (NEW 2026-04)** | Derivado de legal_origin |
| government_effectiveness | **85/86** (↑ desde 63) | X2 robustez | World Bank WGI db=3 |
| control_of_corruption | 85/86 (NEW) | X2 robustez | World Bank WGI db=3 |
| ai_patents_per100k | 54/86 | Y robustez | Stanford fig_1.2.4 |
| ai_investment_vc_proxy | 32/86 | X2 robustez | OECD VC |

## Historial De Actualizaciones

| Fecha | Accion |
|---|---|
| 2025-04 | Creacion pipeline completo: source masters + sample-ready cross-section. 72/86 PRINCIPAL. |
| 2026-04 | **Tarea A (auditoria Problema #6):** agregados regulatory_quality y rule_of_law como X2 confounders core; ampliada cobertura government_effectiveness de 63 → 85; agregado control_of_corruption (85) via `src/expand_wgi.py`. Ver DATA_DECISIONS_LOG D-012/D-013. |
| 2026-04 | **Tarea A sub-tarea A.4:** agregados has_gdpr_like_law y gdpr_similarity_level (86/86) como X2 confounders legal-regulatorios mediante codificacion manual de 86 paises basada en DLA Piper 2025. Metodologia en `info_data/METODOLOGIA_GDPR_CODING.md`. Ver D-014. |
| 2026-04 | **Tarea A sub-tarea A.5:** agregados ict_service_exports_pct y high_tech_exports_pct (83/86) como proxies de economia digital via WDI (`src/expand_digital_economy.py`). UNCTAD DER no publica datos country-level reproducibles. Nueva tier `complete_digital` = 69/86 para robustness. Ver D-015. |
| 2026-04 | **Tarea A sub-tarea A.6:** agregados fh_total_score y fh_democracy_level (86/86) como confounders politico-regimen via Freedom House FITW 2025 (codificacion manual). Correlacion con WGI r=0.68 confirma no-redundancia. Nueva tier `complete_regime` = 72/86 para robustness. Ver D-016 y `info_data/METODOLOGIA_FREEDOM_HOUSE.md`. |
| 2026-04 | **Tarea A sub-tarea A.3-bis:** agregados legal_origin y is_common_law (86/86) como confounder de tradicion juridica via La Porta-LS (2008). Gradiente 13.3x en binding_regulation (English 5.6% vs Scandinavian 75%). Correlacion con WGI r=0.10 confirma no-redundancia. Nueva tier `complete_legal_tradition` = 72/86 (sin perdida de N). Ver D-017 y `info_data/METODOLOGIA_LEGAL_ORIGIN.md`. |
