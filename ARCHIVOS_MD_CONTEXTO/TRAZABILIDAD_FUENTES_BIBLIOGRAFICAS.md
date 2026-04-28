# Auditoria De Trazabilidad De Fuentes Bibliograficas

## Proposito

Este documento audita, con criterio de trazabilidad estricta, donde queda almacenada hoy la referencia de origen de los datos usados en el estudio y deja centralizado el inventario verificado de enlaces, endpoints, PDFs, XLSX y activos oficiales de las **8 fuentes actualmente integradas**.

Su objetivo es responder cuatro preguntas operativas:
- si existe una columna o tabla donde ya se guarde el enlace de origen;
- que tan completa es esa trazabilidad por fuente;
- cuales fueron exactamente los activos oficiales usados en la recoleccion;
- donde queda la evidencia para futura bibliografia, cita metodologica y auditoria academica.

## Resultado De La Auditoria

**Respuesta corta:** no existe hoy una unica tabla maestra para las 8 fuentes. La trazabilidad esta distribuida entre manifests, columnas metadata en algunos CSV raw, el notebook `notebooks/01_recoleccion.ipynb` y la documentacion `info_data/`.

### Estado actual de persistencia por fuente

| fuente | existe tabla o columna con URL/origen | evidencia persistida actual | conclusion de auditoria |
|---|---|---|---|
| Stanford AI Index 2025 | Si | `data/raw/STANFORD AI INDEX 25/download_manifest.csv` con columna `href` | Trazabilidad fuerte por activo descargado |
| World Bank WDI | No en outputs raw | notebook + docs (`wbgapi`, codigos WB) | Trazabilidad documental, no tabular |
| World Bank WGI | Parcial | notebook + docs; output `wdi_governance_metadata.csv` sin URL | Trazabilidad documental, no tabular |
| OECD | Parcial | `oecd_all_indicators_long.csv` tiene `source`; `oecd_ai_visualizations_catalog.csv` tiene `iframe_url` | No existe registry unificado de URLs |
| Microsoft AIEI | Si, parcial | `microsoft_ai_diffusion_raw.csv` y `microsoft_ai_diffusion_study.csv` tienen `source`, `report_edition`, `report_url` | Trazabilidad aceptable, pero sin manifest |
| Oxford Insights | Si | `data/raw/Oxford Insights/download_manifest.csv` + `oxford_ai_readiness_all_raw.csv` con `source_dataset`, `report_url`, `data_asset_url`, `methodology_url`, `source_tier` | Trazabilidad muy fuerte |
| WIPO GII | Si, parcial-fuerte | `data/raw/WIPO Global Innovation Index/download_manifest.csv` + `wipo_gii_overall_panel.csv` con metadata de fuente | Trazabilidad fuerte en manifest; parcial en panel |
| IAPP | Si, parcial-fuerte | `data/raw/IAPP/download_manifest.csv`; outputs raw solo guardan `source` y `source_date` | Trazabilidad fuerte en manifest |

## Regla De Verificacion Aplicada

Solo se documentan aqui enlaces y endpoints que cumplen al menos una de estas condiciones:
- aparecen en un `download_manifest.csv` realmente existente en `data/raw/`;
- aparecen en columnas metadata de outputs raw realmente generados;
- aparecen en el notebook `notebooks/01_recoleccion.ipynb` como constantes o endpoints efectivamente usados por la extraccion ya implementada;
- aparecen en documentos operativos de `info_data/` que ya quedaron alineados con los outputs raw actuales.

No se documentan aqui enlaces inferidos sin evidencia en el repo o sin verificacion directa de la pagina oficial.

## Capa Externa Vs Capa Efectiva

En esta auditoria se distinguen dos niveles:
- `fuente externa/publica`: la pagina web publica desde la cual una persona empezaria razonablemente a navegar o descargar el dato;
- `fuente interna/efectiva`: el asset, endpoint, XLSX, PDF o API que realmente consumio el ETL.

Cuando el repo no preserva una landing superior unica para una subfuente, se registra la `fuente externa mas alta verificada` que hoy puede sostenerse con evidencia directa.

### Resumen ejecutivo: fuente externa vs fuente efectiva

| fuente | fuente externa/publica verificada | fuente interna/efectiva usada | relacion operativa |
|---|---|---|---|
| Stanford AI Index 2025 | `https://hai.stanford.edu/ai-index/2025-ai-index-report` | activos Google Drive publicados por Stanford y preservados por fila en `data/raw/STANFORD AI INDEX 25/download_manifest.csv` | la landing publica expone el reporte y el acceso a los datos; el ETL opero sobre los archivos Drive |
| World Bank WDI | `https://databank.worldbank.org/source/world-development-indicators` | consultas programaticas via `wbgapi` usando codigos WDI en `notebooks/01_recoleccion.ipynb` | la puerta publica es DataBank; el ETL no persistio un endpoint HTTP unico en raw |
| World Bank WGI | `https://www.worldbank.org/en/publication/worldwide-governance-indicators` | `https://www.worldbank.org/content/dam/sites/govindicators/doc/wgidataset_with_sourcedata-2025.xlsx` | la pagina WGI lleva al Excel oficial que fue el activo realmente consumido |
| OECD | `https://oecd.ai/en/` | `https://raw.githubusercontent.com/STIScoreboard/STI.Scoreboard/main/`; `https://sdmx.oecd.org/public/rest/data/OECD.STI.STP,DSD_MSTI@DF_MSTI/`; `https://oecd-ai.case-api.buddyweb.fr/policy-initiatives` | no existe una sola landing publica preservada para todas las subfuentes OECD; el ETL combinó portal publico y endpoints tecnicos |
| Microsoft AIEI | `https://www.microsoft.com/en-us/research/group/aiei/ai-diffusion/` | `https://www.microsoft.com/en-us/research/group/aiei/ai-diffusion/` + PDFs oficiales enlazados desde esa pagina | en Microsoft, la misma pagina publica fue tambien la fuente efectiva del scraping tabular |
| Oxford Insights | `https://oxfordinsights.com/ai-readiness/government-ai-readiness-index/` | activos anuales `XLSX`/`PDF` preservados en `download_manifest.csv` y en `oxford_ai_readiness_all_raw.csv` | la landing publica lleva a los datasets y reportes concretos usados por el ETL |
| WIPO GII | `https://www.wipo.int/en/web/global-innovation-index` | PDFs 2020-2023 + XLSX 2024-2025 preservados en `data/raw/WIPO Global Innovation Index/download_manifest.csv` | la landing publica de GII es la puerta de entrada; el ETL consumio activos de cada edicion |
| IAPP | `https://iapp.org/resources/article/global-ai-legislation-tracker/` | `https://assets.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt34a8e3844fb44942/global_ai_law_policy_tracker.pdf` | la pagina del tracker publica y contextualiza el PDF que sirvio como fuente primaria X1 |

## 1. Stanford AI Index 2025

### Donde queda guardada la trazabilidad hoy

- Tabla exhaustiva por activo: `data/raw/STANFORD AI INDEX 25/download_manifest.csv`
- Columnas auditadas: `type`, `path`, `title`, `id`, `href`
- Cobertura: 661 filas en el manifest

### Fuente base verificada

| capa | referencia verificada |
|---|---|
| fuente externa/publica | `https://hai.stanford.edu/ai-index/2025-ai-index-report` |
| fuente interna/efectiva | inventario de activos Google Drive publicados por Stanford AI Index 2025 y preservados en `download_manifest.csv` |

- La landing publica del AI Index 2025 expone el reporte y el acceso a los datos publicos.
- La evidencia exhaustiva de URLs por activo ya existe en `download_manifest.csv`.

### Activos efectivamente usados por variables del estudio

| variable / uso | archivo | URL verificada |
|---|---|---|
| `ai_patents` | `fig_1.2.4.csv` | `https://drive.google.com/file/d/1ChIwkm7ZSWsX_cHco-felIZpT5PoXodT/view?usp=drive_web` |
| `ai_startups` | `fig_4.3.12.csv` | `https://drive.google.com/file/d/1HuQM93e4TLPZB0egGg5uOrRqLipULp1X/view?usp=drive_web` |
| `ai_startups_cumul` | `fig_4.3.13.csv` | `https://drive.google.com/file/d/1_kv8F4Yi_yQWASCGLFUQsBr6Bu3Ni44k/view?usp=drive_web` |
| `ai_talent` | `fig_4.2.17.csv` | `https://drive.google.com/file/d/1fQ6bRkJL96Qg2vO5ABedJNTuoRjKNSLp/view?usp=drive_web` |
| `ai_skill` | `fig_4.2.15.csv` | `https://drive.google.com/file/d/1kfNpSkKJagns6bWJW9z-A4DVKH3odhHw/view?usp=drive_web` |
| `ai_investment` | `fig_4.3.10.csv` | `https://drive.google.com/file/d/13U0Ok9zyQ0xyUqPO7jJFrhPmQnpI0PKI/view?usp=drive_web` |
| `ai_job_postings` | `fig_4.2.1.csv` | `https://drive.google.com/file/d/1jqwpgP_Kn2891rp7nlyVMJ5Y54e_lGn4/view?usp=drive_web` |
| referencia inspeccionada pero no integrada como X1 | `fig_6.2.1.csv` | `https://drive.google.com/file/d/1OeAJqDeCFFFWnusis_laWnjPO8rzcMfq/view?usp=drive_web` |

### Estado de trazabilidad

- Fuerte a nivel de activo completo gracias al manifest.
- Los CSV analiticos derivados no llevan `source_url` por fila.

## 2. World Bank WDI

### Donde queda guardada la trazabilidad hoy

- No hay `download_manifest.csv` para WDI.
- Los outputs raw `wdi_core_controls.csv`, `wdi_governance.csv`, `wdi_economic_structure.csv`, `wdi_human_capital_infra.csv` **no** guardan columnas de URL ni `source_dataset`.
- La trazabilidad real esta en `notebooks/01_recoleccion.ipynb` y en `info_data/VARIABLES_WORLD_BANK_WDI.md`.

### Metodo de acceso realmente usado

- Wrapper usado en el repo: `wbgapi`
- Fuente base documentada: World Bank - World Development Indicators (WDI)

### Variables WDI extraidas

| variable | codigo WB |
|---|---|
| `gdp_per_capita_ppp` | `NY.GDP.PCAP.PP.CD` |
| `rd_expenditure` | `GB.XPD.RSDV.GD.ZS` |
| `internet_penetration` | `IT.NET.USER.ZS` |
| `tertiary_education` | `SE.TER.ENRR` |
| `government_effectiveness` | `GE.EST` |
| `regulatory_quality` | `RQ.EST` |
| `rule_of_law` | `RL.EST` |
| `control_of_corruption` | `CC.EST` |
| `voice_accountability` | `VA.EST` |
| `political_stability` | `PV.EST` |
| `gdp_current_usd` | `NY.GDP.MKTP.CD` |
| `population` | `SP.POP.TOTL` |
| `labor_force` | `SL.TLF.TOTL.IN` |
| `fdi_net_inflows` | `BX.KLT.DINV.CD.WD` |
| `exports_pct_gdp` | `NE.EXP.GNFS.ZS` |
| `inflation_consumer_prices` | `FP.CPI.TOTL.ZG` |
| `unemployment_rate` | `SL.UEM.TOTL.ZS` |
| `education_expenditure_pct_gdp` | `SE.XPD.TOTL.GD.ZS` |
| `mobile_subscriptions_per100` | `IT.CEL.SETS.P2` |
| `patent_applications_residents` | `IP.PAT.RESD` |

### Referencias oficiales verificadas

| tipo | referencia |
|---|---|
| fuente externa/publica | `https://databank.worldbank.org/source/world-development-indicators` |
| fuente institucional | `World Bank - World Development Indicators (WDI)` |
| metodo usado en notebook | `wbgapi` |
| documentacion operativa interna | `info_data/VARIABLES_WORLD_BANK_WDI.md` |

### Estado de trazabilidad

- Correcta a nivel metodologico e indicador.
- Insuficiente a nivel tabular porque los outputs raw no guardan `source_url` ni `source_dataset`.
- La fuente externa/publica ya queda identificada, pero el ETL no preserva un endpoint HTTP unico equivalente al Excel WGI o a un manifest por descarga.

## 3. World Bank WGI

### Donde queda guardada la trazabilidad hoy

- `data/raw/World Bank WDI/wdi_governance_metadata.csv` no guarda URL ni metadata de fuente.
- La trazabilidad esta documentada en `notebooks/01_recoleccion.ipynb`, en `info_data/VARIABLES_WORLD_BANK_WDI.md` y en la memoria de repo `world_bank_wgi.md`.

### Fuente oficial realmente usada para metadata WGI

| tipo | URL verificada |
|---|---|
| pagina oficial WGI | `https://www.worldbank.org/en/publication/worldwide-governance-indicators` |
| Excel oficial usado para metadata (`STD.ERR` + `NO.SRC`) | `https://www.worldbank.org/content/dam/sites/govindicators/doc/wgidataset_with_sourcedata-2025.xlsx` |

### Indicadores metadata extraidos

| variable | codigo WGI |
|---|---|
| `government_effectiveness_se` | `GE.STD.ERR` |
| `regulatory_quality_se` | `RQ.STD.ERR` |
| `rule_of_law_se` | `RL.STD.ERR` |
| `control_of_corruption_se` | `CC.STD.ERR` |
| `voice_accountability_se` | `VA.STD.ERR` |
| `political_stability_se` | `PV.STD.ERR` |
| `government_effectiveness_nsrc` | `GE.NO.SRC` |
| `regulatory_quality_nsrc` | `RQ.NO.SRC` |
| `rule_of_law_nsrc` | `RL.NO.SRC` |
| `control_of_corruption_nsrc` | `CC.NO.SRC` |
| `voice_accountability_nsrc` | `VA.NO.SRC` |
| `political_stability_nsrc` | `PV.NO.SRC` |

### Nota de auditoria

- Los `.STD.ERR` y `.NO.SRC` **no** se obtuvieron por la API WDI estandar source 2.
- Se documenta como fuente efectiva el Excel oficial WGI 2025 revision.

## 4. OECD

### Donde queda guardada la trazabilidad hoy

- No existe un manifest unico OECD.
- `data/raw/OECD/oecd_all_indicators_long.csv` guarda solo la subfuente en columna `source` (`OECD_STI_Scoreboard`, `OECD_MSTI_SDMX`).
- `data/raw/OECD/oecd_ai_visualizations_catalog.csv` guarda `iframe_url`, pero no un registry bibliografico integral.
- La trazabilidad detallada real esta en `notebooks/01_recoleccion.ipynb` y `info_data/VARIABLES_OECD.md`.

### Fuente externa/publica vs fuente efectiva

| capa | referencia verificada |
|---|---|
| fuente externa/publica mas alta verificada | `https://oecd.ai/en/` |
| fuentes internas/efectivas | `https://raw.githubusercontent.com/STIScoreboard/STI.Scoreboard/main/`; `https://sdmx.oecd.org/public/rest/data/OECD.STI.STP,DSD_MSTI@DF_MSTI/`; `https://wp.oecd.ai/wp-json/wp/v2/visualizations?per_page=100&page={page}`; `https://oecd-ai.case-api.buddyweb.fr/policy-initiatives` |

- OECD no entra al proyecto por una sola puerta tecnica.
- La `fuente externa/publica` verificable para el bloque AI/policy es el portal OECD.AI.
- Para STI Scoreboard y MSTI, el repo conserva la raiz tecnica efectiva, no una landing publica superior unica por subfuente.

### 4.1 OECD STI Scoreboard (GitHub raw)

Base verificada en notebook:
- `https://raw.githubusercontent.com/STIScoreboard/STI.Scoreboard/main/`

Archivos efectivamente usados:

| variable(s) | archivo | URL verificada |
|---|---|---|
| `ai_publications_frac` | `AIPUBS_NBFRAC_V8.txt` | `https://raw.githubusercontent.com/STIScoreboard/STI.Scoreboard/main/AIPUBS_NBFRAC_V8.txt` |
| `ai_publications_top10_frac` | `TOP10_AI_NBFRAC_V8.txt` | `https://raw.githubusercontent.com/STIScoreboard/STI.Scoreboard/main/TOP10_AI_NBFRAC_V8.txt` |
| `ai_publications_scopus_frac` | `FPUBS_1702_NBFRAC_V8.txt` | `https://raw.githubusercontent.com/STIScoreboard/STI.Scoreboard/main/FPUBS_1702_NBFRAC_V8.txt` |
| `ai_patents_pct` | `PCTAI_NB_V8.txt` | `https://raw.githubusercontent.com/STIScoreboard/STI.Scoreboard/main/PCTAI_NB_V8.txt` |
| `ai_patents_ip5` | `IP5AI_NB_V8.txt` | `https://raw.githubusercontent.com/STIScoreboard/STI.Scoreboard/main/IP5AI_NB_V8.txt` |
| `vc_seed_pct_gdp` | `VCSEED_XGDP_V8.txt` | `https://raw.githubusercontent.com/STIScoreboard/STI.Scoreboard/main/VCSEED_XGDP_V8.txt` |
| `vc_startup_pct_gdp` | `VCSTART_XGDP_V8.txt` | `https://raw.githubusercontent.com/STIScoreboard/STI.Scoreboard/main/VCSTART_XGDP_V8.txt` |
| `vc_later_pct_gdp` | `VCLATE_XGDP_V8.txt` | `https://raw.githubusercontent.com/STIScoreboard/STI.Scoreboard/main/VCLATE_XGDP_V8.txt` |
| `researchers_per_1000_employed` | `TP_RSXEM_V8.txt` | `https://raw.githubusercontent.com/STIScoreboard/STI.Scoreboard/main/TP_RSXEM_V8.txt` |

### 4.2 OECD MSTI (SDMX API)

Endpoint root verificado en notebook:
- `https://sdmx.oecd.org/public/rest/data/OECD.STI.STP,DSD_MSTI@DF_MSTI/`

Indicadores efectivamente usados:

| variable | concepto / seleccion verificada |
|---|---|
| `gerd_pct_gdp` | `GERD`, `unit=PT_B1GQ` |
| `berd_pct_gdp` | `BERD`, `unit=PT_B1GQ` |
| `herd_pct_gdp` | `HERD`, `unit=PT_B1GQ` |
| `goverd_pct_gdp` | `GOVERD`, `unit=PT_B1GQ` |

### 4.3 OECD.AI Visualizations catalog

Endpoint verificado en notebook:
- `https://wp.oecd.ai/wp-json/wp/v2/visualizations?per_page=100&page={page}`

Uso real:
- metadata/catalogo de 191 visualizaciones;
- no fue la fuente directa de variables tabulares finales del estudio;
- el output `oecd_ai_visualizations_catalog.csv` conserva `iframe_url` cuando el portal lo expone.

### 4.4 EC-OECD AI Policy Database

Endpoints verificados en notebook:
- `https://oecd-ai.case-api.buddyweb.fr/policy-initiatives`
- `https://oecd-ai.case-api.buddyweb.fr/policy-initiatives?page={page}`
- `https://oecd-ai.case-api.buddyweb.fr/countries`
- `https://oecd-ai.case-api.buddyweb.fr/countries/s/{slug}`

Variables X1 obtenidas desde esta API:
- `has_ai_law`
- `regulatory_approach`
- `regulatory_intensity`
- `year_enacted`
- `enforcement_level`
- `thematic_coverage`
- complementarias: `n_total_initiatives`, `n_binding`, `n_nonbinding`, `n_strategies`, `n_regulations`, `n_sectors_covered`, `n_policy_instruments`

### Estado de trazabilidad

- Buena a nivel documental y de endpoint.
- Debil a nivel de raw final porque no existe un manifest OECD con URLs exactas por activo descargado.

## 5. Microsoft AI Economy Institute (AIEI)

### Donde queda guardada la trazabilidad hoy

- `data/raw/Microsoft/microsoft_ai_diffusion_raw.csv` guarda `source`, `report_edition`, `report_url`
- `data/raw/Microsoft/microsoft_ai_diffusion_study.csv` guarda `source`, `report_edition`, `report_url`
- `data/raw/Microsoft/microsoft_ai_diffusion_snapshot.csv` **no** guarda URL

### Fuente y activos verificados

| tipo | URL verificada | uso real |
|---|---|---|
| landing HTML principal | `https://www.microsoft.com/en-us/research/group/aiei/ai-diffusion/` | fuente efectiva del scraping tabular |
| PDF H1 2025 | `https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/Microsoft-AI-Diffusion-Report.pdf` | verificacion documental |
| PDF H2 2025 | `https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/Microsoft-AI-Diffusion-Report-2025-H2.pdf` | verificacion documental |

### Variable obtenida

| variable | origen real |
|---|---|
| `ai_adoption_rate` | tablas HTML publicas del landing AIEI; `report_url` persistido en raw |

### Estado de trazabilidad

- Aceptable: existe `report_url` en tablas raw principales.
- Mejorable: no existe `download_manifest.csv` propio para Microsoft.

## 6. Oxford Insights

### Donde queda guardada la trazabilidad hoy

- Manifest central: `data/raw/Oxford Insights/download_manifest.csv`
- Metadata por fila en `data/raw/Oxford Insights/oxford_ai_readiness_all_raw.csv`
- Columnas auditadas presentes en raw: `source_name`, `source_dataset`, `report_url`, `data_asset_url`, `methodology_url`, `source_tier`

### Endpoints y activos oficiales verificados

| tipo | URL verificada |
|---|---|
| landing principal | `https://oxfordinsights.com/ai-readiness/government-ai-readiness-index/` |
| landing 2025 | `https://oxfordinsights.com/ai-readiness/government-ai-readiness-index-2025/` |
| discovery media API | `https://oxfordinsights.com/wp-json/wp/v2/media?search=Government%20AI%20Readiness&per_page=100` |
| discovery media API complementaria | `https://oxfordinsights.com/wp-json/wp/v2/media?search=public%20data&per_page=100` |

### Activos por anio realmente usados

| anio | dataset / activo principal | URL verificada |
|---|---|---|
| 2019 | dataset XLSX | `https://oxfordinsights.com/wp-content/uploads/2024/01/SHARED_-2019-Index-data-for-report.xlsx` |
| 2019 | reporte PDF | `https://oxfordinsights.com/wp-content/uploads/2023/12/ai-gov-readiness-report_v08.pdf` |
| 2020 | dataset XLSX | `https://oxfordinsights.com/wp-content/uploads/2023/12/2020-Government-AI-Readiness-Index-public-dataset.xlsx` |
| 2020 | reporte PDF | `https://oxfordinsights.com/wp-content/uploads/2023/11/AIReadinessReport.pdf` |
| 2021 | dataset XLSX | `https://oxfordinsights.com/wp-content/uploads/2023/12/2021-Government-AI-Readiness-Index-public-dataset.xlsx` |
| 2021 | reporte PDF | `https://oxfordinsights.com/wp-content/uploads/2023/11/Government_AI_Readiness_21.pdf` |
| 2022 | dataset XLSX | `https://oxfordinsights.com/wp-content/uploads/2023/12/2022-Government-AI-Readiness-Index-public-data.xlsx` |
| 2022 | reporte PDF | `https://oxfordinsights.com/wp-content/uploads/2023/11/Government_AI_Readiness_2022_FV.pdf` |
| 2023 | dataset XLSX | `https://oxfordinsights.com/wp-content/uploads/2023/12/2023-AI-Readiness-Index-public-dataset.xlsx` |
| 2023 | reporte PDF | `https://oxfordinsights.com/wp-content/uploads/2023/12/2023-Government-AI-Readiness-Index.pdf` |
| 2024 | reporte PDF usado para extraccion | `https://oxfordinsights.com/wp-content/uploads/2024/12/2024-Government-AI-Readiness-Index-1.pdf` |
| 2025 | dataset XLSX canonico final | `https://oxfordinsights.com/wp-content/uploads/2026/01/2025-Government-AI-Readiness-Index-data-1.xlsx` |
| 2025 | dataset XLSX archivado | `https://oxfordinsights.com/wp-content/uploads/2026/01/2025-Government-AI-Readiness-Index-data.xlsx` |
| 2025 | methodology PDF | `https://oxfordinsights.com/wp-content/uploads/2026/01/Methodology-Report-2025.pdf` |
| 2025 | reporte PDF | `https://oxfordinsights.com/wp-content/uploads/2025/12/2025-Government-AI-Readiness-Index.pdf` |

### Estado de trazabilidad

- Muy fuerte: manifest + metadata por fila en raw.
- Es la fuente mejor documentada del proyecto en terminos bibliograficos.

## 7. WIPO Global Innovation Index (GII)

### Donde queda guardada la trazabilidad hoy

- Manifest central: `data/raw/WIPO Global Innovation Index/download_manifest.csv`
- Metadata parcial por fila en `data/raw/WIPO Global Innovation Index/wipo_gii_overall_panel.csv`
- Columnas auditadas presentes en panel: `source_name`, `source_dataset`, `source_variable_original`, `report_url`, `data_asset_url`, `source_tier`

### Activos y URLs verificadas

| anio | activo | URL verificada | estado de uso |
|---|---|---|---|
| base | landing / public page | `https://www.wipo.int/en/web/global-innovation-index` | fuente externa/publica principal |
| 2019 | landing / publication page | `https://www.wipo.int/publications/en/details.jsp?id=4435` | descubierto pero excluido del ETL por no contener tabla completa util |
| 2020 | reporte PDF | `https://www.wipo.int/documents/d/global-innovation-index/docs-en-2020-wipo_pub_gii_2020.pdf` | usado |
| 2021 | reporte PDF | `https://www.wipo.int/documents/d/global-innovation-index/docs-en-2021-wipo_pub_gii_2021.pdf` | usado |
| 2022 | reporte PDF | `https://www.wipo.int/documents/d/global-innovation-index/docs-en-wipo-pub-2000-2022-en-main-report-global-innovation-index-2022-15th-edition.pdf` | usado |
| 2023 | reporte PDF | `https://www.wipo.int/documents/d/global-innovation-index/docs-en-wipo-pub-2000-2023-en-main-report-global-innovation-index-2023-16th-edition.pdf` | usado |
| 2024 | dataset XLSX | `https://www.wipo.int/edocs/pubdocs/en/wipo-pub-2000-2024-tech1.xlsx` | usado |
| 2024 | reporte PDF | `https://www.wipo.int/edocs/pubdocs/en/wipo-pub-2000-2024-en-global-innovation-index-2024.pdf` | usado |
| 2025 | dataset XLSX | `https://www.wipo.int/edocs/pubdocs/en/wipo-pub-2000-2025-tech1.xlsx` | usado |
| 2025 | reporte PDF oficial bloqueado por challenge HTML | `https://www.wipo.int/web-publications/global-innovation-index-2025/assets/80937/global-innovation-index-2025-en.pdf` | URL oficial verificada; descarga automatica no valida |

### Nota de auditoria sobre 2025 PDF

- El manifest conserva la URL oficial 2025 del PDF, pero la descarga automatica desde terminal devolvio HTML/no PDF valido.
- El repo conserva ademas una copia manual local del PDF 2025, pero esa fila tiene `url=manual_download`, por lo que **no** se documenta como enlace externo verificable adicional.

### Variable usada en el estudio

| variable | origen real |
|---|---|
| `gii_score` | PDFs oficiales 2020-2023 + XLSX oficiales 2024-2025 |

## 8. IAPP

### Donde queda guardada la trazabilidad hoy

- Manifest central: `data/raw/IAPP/download_manifest.csv`
- `iapp_x1_core.csv` e `iapp_tracker_structured_raw.csv` guardan `source` y `source_date`, pero no URL.

### Activos y URLs verificadas

| activo | URL verificada | uso real |
|---|---|---|
| landing del tracker | `https://iapp.org/resources/article/global-ai-legislation-tracker/` | referencia oficial |
| PDF principal | `https://assets.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt34a8e3844fb44942/global_ai_law_policy_tracker.pdf` | fuente primaria X1 |
| PDF complementario 2025 | `https://assets.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt03a98a47faf09eb7/global_ai_governance_law_policy_series_2025.pdf` | apoyo de codificacion |

### Variables usadas en el estudio

| variables X1 | origen real |
|---|---|
| `has_ai_law`, `regulatory_approach`, `regulatory_intensity`, `year_enacted`, `enforcement_level`, `thematic_coverage` | PDF principal IAPP + codificacion directa en `src/iapp_coding.py` |

### Estado de trazabilidad

- Fuerte a nivel bibliografico: la fuente externa/publica y el PDF efectivo estan claramente separados.
- Mejorable en raw final: los CSV IAPP guardan `source` y `source_date`, pero no la URL del PDF por fila.

## Conclusiones Operativas

1. **Si existen tablas/columnas con trazabilidad**, pero estan fragmentadas por fuente.
2. **Las fuentes mejor resueltas bibliograficamente hoy** son Stanford, Oxford, WIPO e IAPP, porque tienen manifests explicitos.
3. **Microsoft tiene trazabilidad tabular parcial** en raw (`report_url`), suficiente para auditoria basica.
4. **OECD y World Bank son las fuentes mas debiles en persistencia tabular de enlaces**: la evidencia esta en notebook y docs, no en los CSV raw finales.
5. **Este documento pasa a ser la referencia central en `info_data/`** para futura bibliografia del estudio, porque consolida lo que antes estaba disperso.

## Recomendacion Profesional Para La Siguiente Iteracion

Para cerrar definitivamente la brecha de trazabilidad, conviene crear en una futura iteracion un registry tabular unico, por ejemplo:

- `data/raw/source_bibliography_registry.csv`

Con columnas minimas:
- `source_family`
- `subsource`
- `canonical_variable`
- `source_dataset`
- `source_url`
- `source_type`
- `access_method`
- `downloaded_at`
- `used_in_output`
- `evidence_file`

Eso permitiria pasar de trazabilidad documental distribuida a trazabilidad tabular unificada.