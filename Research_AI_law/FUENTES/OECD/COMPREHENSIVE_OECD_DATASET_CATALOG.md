# Comprehensive OECD SDMX Dataset Catalog for AI Regulation Study

> **Generated:** 2026-05-04 via OECD SDMX API (sdmx.oecd.org/public/rest/)
> **Total dataflows found:** 1,505 across 16+ OECD departments
> **API access:** XML metadata (full) + CSV data download confirmed working for many datasets

---

## 1. DIGITAL ECONOMY (OECD.STI.DEP — 26 dataflows)

### 1.1 ICT Access and Usage by Businesses
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.STI.DEP/DSD_ICT_B@DF_BUSINESSES v1.0` |
| **Indicators** | 60 indicators: cloud computing, big data, AI use, e-commerce, ERP, CRM, RFID, social media, ICT specialists, cybersecurity, web presence, broadband type |
| **Dimensions** | REF_AREA, FREQ, MEASURE, UNIT_MEASURE, ACTIVITY (ISIC4), SIZE_CLASS |
| **Countries** | OECD members + accession countries + selected partners (via Eurostat + OECD collection) |
| **Years** | 2012–latest |
| **SDMX CSV** | ✅ `GET /rest/data/OECD.STI.DEP,DSD_ICT_B@DF_BUSINESSES,1.0/A......` (requires 6 dims) |
| **Relevance** | High — AI/cloud/big data adoption by firms, ICT skills |

### 1.2 ICT Access and Usage by Households
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.STI.DEP/DSD_ICT_HH_IND@DF_HH v1.1` |
| **Indicators** | Internet access at home, broadband type, devices, reasons for non-use |
| **Dimensions** | REF_AREA, FREQ, MEASURE, UNIT_MEASURE, INCOME_QUANTILE |
| **SDMX CSV** | ✅ |
| **Relevance** | High — internet penetration, digital divide |

### 1.3 ICT Access and Usage by Individuals
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.STI.DEP/DSD_ICT_HH_IND@DF_IND v1.1` |
| **Indicators** | Individual internet use, e-government, e-commerce, social media, skills |
| **Dimensions** | REF_AREA, FREQ, MEASURE, UNIT_MEASURE, AGE, GENDER, EDUCATION |
| **SDMX CSV** | ✅ |
| **Relevance** | High — digital skills, e-gov use, online activities |

### 1.4 Broadband and Telecom Databases
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.STI.DEP/DSD_BB_DATABASE@DF_BB_TEL_DATABASE v2.0` |
| **Indicators** | 14 indicators: fixed/mobile broadband subscriptions, penetration, speeds, prices, fibre, 5G |
| **Dimensions** | REF_AREA, FREQ, MEASURE, UNIT_MEASURE, DEVICE, SPEED |
| **SDMX CSV** | ✅ |
| **Relevance** | High — infrastructure readiness, digital connectivity |

### 1.5 Digital Trade — Experimental Estimates
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.STI.DEP/DSD_DIGITAL_TRADE@DF_DIGITAL_TRADE v1.0` |
| **Indicators** | Digitally-enabled services trade, digital delivery modes |
| **Dimensions** | REF_AREA, FREQ, MEASURE, UNIT_MEASURE, TRADE_FLOW, PARTNER |
| **SDMX CSV** | ✅ |
| **Relevance** | Medium — international digital trade flows |

### 1.6 Going Digital Toolkit (14 dataflows)
| Property | Value |
|----------|-------|
| **Full IDs** | `DSD_TOOLKIT@DF_GD_DISTANCES`, `DSD_TOOLKIT_{1-14}@DF_GD_BREAKDOWNS_{1-14}` |
| **Indicators** | Going Digital Dashboard — 40+ indicators across access, use, innovation, jobs, society, trust |
| **Dimensions** | REF_AREA, FREQ, MEASURE |
| **SDMX CSV** | ✅ |
| **Relevance** | High — composite digital economy indicators, cross-country comparisons |

### 1.7 National Digital Strategy Comprehensiveness
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.STI.DEP/DSD_TOOLKIT_DK@DF_NDSC v1.0` |
| **Indicators** | Index of national digital strategy comprehensiveness |
| **Relevance** | **Very High** — directly measures national digital policy strategy |

---

## 2. INNOVATION & R&D (OECD.STI.STP — 46 dataflows)

### 2.1 Main Science and Technology Indicators (MSTI)
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.STI.STP/DSD_MSTI@DF_MSTI v1.3` |
| **Indicators** | GERD as % GDP, GERD per capita, researchers per 1000 employment, BERD, government R&D, patents, technology balance of payments |
| **Countries** | All OECD + selected non-OECD |
| **Years** | 1981–latest |
| **SDMX CSV** | ✅ |
| **Relevance** | **Very High** — key R&D intensity indicators used in your study |

### 2.2 Gross Domestic Expenditure on R&D (GERD)
| Dataflow | Description |
|----------|-------------|
| `DSD_RDS_GERD@DF_GERD_SOF` | By sector of performance and source of funds |
| `DSD_RDS_GERD@DF_GERD_FORD` | By sector of performance and field of R&D |
| `DSD_RDS_GERD@DF_GERD_TOE` | By sector of performance and type of expenditure |
| `DSD_RDS_GERD@DF_GERD_TORD` | By sector of performance and type of R&D |
| `DSD_RDS_GERD@DF_GERD_SEO` | By socio-economic objectives |
| **SDMX CSV** | ✅ |
| **Relevance** | **Very High** — total R&D spending, breakdowns |

### 2.3 Business Enterprise R&D (BERD)
| Dataflow | Description |
|----------|-------------|
| `DSD_RDS_BERD@DF_BERD_INDU` | By industry (ISIC) |
| `DSD_RDS_BERD@DF_BERD_MA_SOF` | By main activity and source of funds |
| `DSD_RDS_BERD@DF_BERD_MA_TOE` | By main activity and type of expenditure |
| `DSD_RDS_BERD@DF_BERD_SOF_SIZE` | By size class and source of funds |
| **SDMX CSV** | ✅ |
| **Relevance** | High — business sector R&D by industry |

### 2.4 Analytical BERD (ANBERD)
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.STI.STP/DSD_ANBERD@DF_ANBERDi4 v1.0` |
| **Indicators** | BERD by ISIC Rev.4 — analytically estimated to fill gaps |
| **SDMX CSV** | ✅ |
| **Relevance** | High — more complete BERD coverage |

### 2.5 Government Budget Allocations for R&D (GBARD)
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.STI.STP/DSD_RDS_GOV@DF_GBARD_NABS07 v1.0` |
| **Indicators** | Government R&D budget by socio-economic objective (NABS 2007) |
| **SDMX CSV** | ✅ |
| **Relevance** | **Very High** — government R&D priorities by objective |

### 2.6 R&D Tax Incentives Database
| Dataflow | Description |
|----------|-------------|
| `DSD_RDTAX@DF_RDTAX` | R&D tax expenditure and direct government funding of BERD |
| `DSD_RDTAX@DF_RDSUB` | Implied tax subsidy rates on R&D expenditures |
| `DSD_RDTAX@DF_IPTAX` | Income-based tax support for R&D and Innovation |
| **SDMX CSV** | ✅ |
| **Relevance** | **Very High** — R&D tax incentives, subsidy rates |

### 2.7 Innovation Statistics — InnoStat
| Dataflow | Description |
|----------|-------------|
| `DSD_INNOSTAT@DF_ALL` | Full innovation indicators database |
| `DSD_INNOSTAT@DF_INNOENT` | Innovative enterprises (product/process innovation) |
| `DSD_INNOSTAT@DF_INNOTYPE` | Type of innovation (product, business process) |
| `DSD_INNOSTAT@DF_INNOCOOP` | Innovation cooperation |
| `DSD_INNOSTAT@DF_INNOSUPP` | Public financial support for innovation |
| `DSD_INNOSTAT@DF_INNOENV` | Innovation with environmental benefits |
| `DSD_INNOSTAT@DF_INNOMKT` | Innovative firms in foreign/domestic markets |
| `DSD_INNOSTAT@DF_INNOTUR` | Turnover from product innovation |
| `DSD_INNOSTAT@DF_INNOEMP` | Employment in innovative firms |
| `DSD_INNOSTAT@DF_INNOEMPUD` | Innovation-active firms by share of tertiary employees |
| `DSD_INNOSTAT@DF_INNOEXP` | R&D expenditure in innovation-active firms |
| **SDMX CSV** | ✅ |
| **Relevance** | **Very High** — product/process innovation, public support |

### 2.8 Bibliometric Indicators
| Dataflow | Description |
|----------|-------------|
| `DSD_BIBLIO@DF_BIBLIO v1.1` | 7 indicators: publications, citations, by field of science |
| `DSD_BIBLIO@DF_BIBLIO_COLLAB v1.1` | International collaboration |
| `DSD_BIBLIO_SDG@DF_BIBLIO_SDG v1.0` | By SDG |
| **SDMX CSV** | ✅ |
| **Relevance** | Medium — scientific output |

### 2.9 ReICO — Research and Innovation Careers Observatory
| Dataflow | Description |
|----------|-------------|
| `DSD_REICO_FULL@DF_ALL` | Full database |
| `DSD_REICO_FULL@DF_RDL` | R&I labour market |
| `DSD_REICO_FULL@DF_RDC` | R&I talent circulation |
| `DSD_REICO_FULL@DF_RDT` | R&I talent development |
| **SDMX CSV** | ✅ |
| **Relevance** | **Very High** — AI talent migration, researcher mobility, skills |

---

## 3. PATENTS & TECHNOLOGY (OECD.STI.PIE — 33 dataflows)

### 3.1 Patents by Technology
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.STI.PIE/DSD_PATENTS@DF_PATENTS v1.0` |
| **Indicators** | Patent counts: EPO, USPTO, PCT, Patent Families by OECD/WIPO tech domains |
| **Dimensions** | REF_AREA, FREQ, MEASURE, UNIT_MEASURE, TECHNOLOGY, PATENT_OFFICE |
| **Countries** | All countries with patent activity (including non-OECD) |
| **SDMX CSV** | ✅ |
| **Relevance** | **Very High** — includes AI-related patents, ICT patents |

### 3.2 Patents by WIPO Technology Domains
| Full ID | `DSD_PATENTS@DF_PATENTS_WIPO v1.0` |
| **Relevance** | **Very High** — includes "Digital communication", "Computer technology", "IT methods for management" domains |

### 3.3 Patents in OECD Selected Technologies
| Full ID | `DSD_PATENTS@DF_PATENTS_OECDSPECIFIC v1.0` |
| **Indicators** | ICT, biotechnology, nanotechnology, environment-related, health |
| **Relevance** | **Very High** — ICT/AI-specific tech domains |

### 3.4 Patent Collaboration Indicators
| Dataflow | Description |
|----------|-------------|
| `DSD_PATENTS@DF_PATENTS_COINVENTOR` | Patents with foreign co-inventors (R&D collaboration) |
| `DSD_PATENTS@DF_PATENTS_INDICATORS` | International co-operation indicators |
| `DSD_PATENTS@DF_PATENTS_DOMESTIC` | Domestic ownership of inventions abroad |
| `DSD_PATENTS@DF_PATENTS_FOREIGN` | Foreign ownership of domestic inventions |
| `DSD_PATENTS@DF_PATENTS_ENVIROMENT` | Environment-related technology patents |
| **SDMX CSV** | ✅ |
| **Relevance** | High — knowledge flows, international collaboration |

### 3.5 STAN Database for Structural Analysis
| Property | Value |
|----------|-------|
| **Full IDs** | `DSD_STAN@DF_STAN v1.0` and `DSD_STAN@DF_STAN_2025 v1.0` |
| **Indicators** | Output, value added, employment, exports, imports by industry (ISIC) |
| **SDMX CSV** | ✅ |
| **Relevance** | Medium — sectoral structure, ICT sector analysis |

### 3.6 Trade in Value Added (TiVA) — 2025 edition
| Dataflow | Description |
|----------|-------------|
| `DSD_TIVA_MAINLV@DF_MAINLV` | Principal indicators, levels |
| `DSD_TIVA_MAINSH@DF_MAINSH` | Principal indicators, shares |
| `DSD_TIVA_EXGRVA@DF_EXGRVA` | Origin of value added in gross exports |
| `DSD_TIVA_FDVA@DF_FDVA` | Origin of value added in final demand |
| **SDMX CSV** | ✅ |
| **Relevance** | Medium — digital services value chains |

### 3.7 Industrial Policy Database (QuIS)
| Dataflow | Description |
|----------|-------------|
| `DSD_INDUSTRIAL_POLICY@DF_FIN` | Industrial policy financial instruments |
| `DSD_INDUSTRIAL_POLICY@DF_GRANTAX` | Industrial policy grants and tax expenditures |
| **Relevance** | **Very High** — government support for industry, including digital/AI |

---

## 4. SERVICES TRADE RESTRICTIVENESS (OECD.TAD.TPD — 10 dataflows)

### 4.1 Services Trade Restrictiveness Index — Main
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.TAD.TPD/DSD_STRI@DF_STRI_MAIN v1.0` |
| **Indicators** | STRI score by sector (0-1), 22 services sectors, detailed policy measures |
| **Dimensions** | FREQ, REF_AREA, MEASURE, ACTIVITY (ISIC), METHODOLOGY, STRI_TYPE, UNIT_MEASURE, COUNTERPART_AREA |
| **Countries** | 50+ countries (OECD + key partners) |
| **Years** | 2014–latest, annual |
| **SDMX CSV** | ✅ **CONFIRMED WORKING** — returns detailed CSV data |
| **Relevance** | **Very High** — measures regulatory restrictiveness in services |

### 4.2 Digital Services Trade Restrictiveness Index
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.TAD.TPD/DSD_STRI@DF_STRI_DIGITAL v1.0` |
| **Indicators** | Digital STRI (0-1), barriers specific to digitally-enabled services |
| **Dimensions** | Same as STRI main + DIGITAL-specific measures |
| **SDMX CSV** | ✅ **CONFIRMED WORKING** |
| **Relevance** | **Very High** — directly measures digital regulation restrictiveness |

### 4.3 Digital STRI Regulatory Database
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.TAD.TPD/DSD_STRI_POLICY@DF_STRI_POLICY_DIGITAL v1.1` |
| **Indicators** | Individual policy measures behind the Digital STRI, detailed regulatory data |
| **SDMX CSV** | ✅ |
| **Relevance** | **Very High** — granular regulatory data on digital trade barriers |

### 4.4 Index of Digital Trade Integration and Openness (INDIGO)
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.TAD.TPD/DSD_INDIGO@DF_INDIGO v1.0` |
| **Indicators** | Composite index of digital trade integration and openness |
| **Dimensions** | FREQ, REF_AREA, MEASURE, INDIGO_TYPE, UNIT_MEASURE, COUNTERPART_AREA |
| **SDMX CSV** | ✅ **CONFIRMED WORKING** |
| **Relevance** | **Very High** — measures openness to digital trade |

### 4.5 STRI Heterogeneity Indices
| Dataflow | Description |
|----------|-------------|
| `DSD_STRI@DF_STRI_HETERO` | Regulatory heterogeneity between countries |
| `DSD_STRI@DF_STRI_DIGITAL_HETERO` | Digital-specific regulatory heterogeneity |
| **Relevance** | High — distance between regulatory regimes |

---

## 5. ECONOMIC & PRODUCT MARKET REGULATION (OECD.ECO — 11 dataflows)

### 5.1 Product Market Regulation (PMR)
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.ECO.GCRD/DSD_PMR@DF_PMR v1.2` |
| **Indicators** | PMR index (0-6), economy-wide + sectoral, regulatory barriers to competition, state control, barriers to trade and investment |
| **Dimensions** | REF_AREA, MEASURE, FREQ |
| **Countries** | OECD + selected non-OECD |
| **SDMX CSV** | ✅ (requires specific MEASURE selection) |
| **Relevance** | **Very High** — measures regulatory barriers, competition policy |

### 5.2 PMR OECD-WBG
| Full ID | `DSD_PMR@DF_PMR_WBG v1.2` |
| **Countries** | Extended coverage with World Bank Group data |
| **Relevance** | **Very High** — extended to non-OECD countries in your sample |

### 5.3 Environmental Policy Stringency Index (EPS)
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.ECO.MAD/DSD_EPS@DF_EPS v1.0` |
| **Indicators** | EPS index (0-6), climate policy stringency |
| **Dimensions** | REF_AREA, FREQ, MEASURE, CLIM_POL |
| **SDMX CSV** | ✅ |
| **Relevance** | Medium — environmental regulation stringency (methodological parallel) |

### 5.4 Climate Policy Uncertainty
| Full ID | `OECD.ECO.MAD/DSD_CPU@DF_CPU v1.0` |
| **Relevance** | Low-medium — policy uncertainty index |

### 5.5 Economic Outlook
| Dataflow | Description |
|----------|-------------|
| `DSD_EO@DF_EO v1.4` | OECD Economic Outlook No 118 — GDP, inflation, employment forecasts |
| `DSD_EO_LTB@DF_EO_LTB v1.0` | Long-term scenarios |
| **SDMX CSV** | ✅ |
| **Relevance** | Low-Medium — macroeconomic control variables |

---

## 6. GOVERNANCE & PUBLIC SECTOR (OECD.GOV — 55 dataflows)

### 6.1 Government at a Glance — Main Indicators 2025
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.GOV.GIP/DSD_GOV@DF_GOV_2025 v1.0` |
| **Indicators** | Public finance, public employment, procurement, digital government, open data, regulatory governance, trust, integrity, satisfaction with public services |
| **Dimensions** | REF_AREA, FREQ, MEASURE, UNIT_MEASURE |
| **SDMX CSV** | ✅ |
| **Relevance** | **Very High** — government effectiveness, digital government, trust in institutions |

### 6.2 Stakeholder Engagement, RIA, and Ex Post Evaluation Indexes
| Property | Value |
|----------|-------|
| **Full IDs** | `DSD_GOV_REG@DF_GOV_REG_2023` and `DSD_GOV_REG@DF_GOV_REG_2025` |
| **Indicators** | Composite indexes on: stakeholder engagement in rule-making, Regulatory Impact Assessment (RIA), ex post evaluation |
| **Relevance** | **Very High** — directly measures regulatory governance quality |

### 6.3 Regulatory Governance
| Property | Value |
|----------|-------|
| **Full IDs** | `DSD_QDD_GOV_REG@DF_GOV_REG` and `DSD_QDD_GOV_REG_DD@DF_GOV_REG_DD` (with microdata) |
| **Indicators** | Detailed regulatory governance indicators — transparency, accountability, procedures |
| **Relevance** | **Very High** — regulatory quality + institutional framework |

### 6.4 Digital Government and Open Government Data Indexes
| Property | Value |
|----------|-------|
| **Full ID** | `DSD_GOV@DF_GOV_DGOGD_2025 v1.0` |
| **Indicators** | Digital government maturity, open government data availability |
| **Relevance** | **Very High** — government digitalization, data openness |

### 6.5 Public Integrity Indicators
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.GOV.PSI/DSD_PII@DF_PUBLIC_INTEGRITY v1.5` |
| **Indicators** | Integrity framework, conflict of interest, lobbying, asset disclosure |
| **Dimensions** | REF_AREA, FREQ, MEASURE, UNIT_MEASURE, DD_DIM, DD_ID |
| **SDMX CSV** | ✅ |
| **Relevance** | High — corruption control, institutional integrity |

### 6.6 Trust, Democratic Governance, and Satisfaction with Public Services
| Dataflow | Description |
|----------|-------------|
| `DSD_GOV_INT@DF_GOV_TDG_2025` | Trust in government, security, dignity |
| `DSD_GOV_INT@DF_GOV_SPS_2025` | Satisfaction with public services |
| `DSD_GOV_INT@DF_GOV_INT_2025` | Perception of public sector integrity |
| **Relevance** | High — citizen trust, democratic governance |

### 6.7 Public Finance Indicators
| Dataflow | Description |
|----------|-------------|
| `DSD_GOV@DF_GOV_PF_2025` | Public finance main indicators: revenue, expenditure, deficit, debt |
| `DSD_GOV_COFOG@DF_GOV_COFOG_2025` | Public expenditure by function (COFOG) |
| `DSD_GOV_LEVEL@DF_GOV_LEVEL_2025` | Public finance by level of government |
| `DSD_GOV_TRANSACTION@DF_GOV_TRANSACTION_2025` | Public finance by economic transaction |
| **Relevance** | Medium — fiscal indicators as control variables |

### 6.8 Other Governance Dataflows
| Dataflow | Description |
|----------|-------------|
| `DSD_GOV@DF_GOV_DGOGD_2025` | Digital government + open government data |
| `DSD_GOV@DF_GOV_HRM_2025` | Human resource management in government |
| `DSD_GOV@DF_GOV_INFPD_2025` | Infrastructure planning and delivery |
| `DSD_GOV@DF_GOV_PPROC_2025` | Size and quality of public procurement |
| `DSD_GOV@DF_GOV_EMPPS_REP_2025` | Public employment and representation |
| `DSD_GOV_COMPEMP@DF_GOV_COMPEMP_2025` | Central admin employment by age, gender, education |

---

## 7. FOREIGN DIRECT INVESTMENT REGULATION (OECD.DAF.INV — 15 dataflows)

### 7.1 FDI Regulatory Restrictiveness Index — Scores
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.DAF.INV/DSD_FDIRRI_SCORES@DF_FDIRRI_SCORES v2.0` |
| **Indicators** | FDI Restrictiveness Index (0-1), by sector, type of restriction |
| **Dimensions** | REF_AREA, ACTIVITY, POL_CAT, MEASURE, UNIT_MEASURE |
| **Countries** | OECD + G20 + selected others |
| **SDMX CSV** | ✅ |
| **Relevance** | **Very High** — measures barriers to foreign investment |

### 7.2 FDI Restrictiveness Regulatory Database
| Full ID | `DSD_FDIRRI_REG_DATABASE@DF_FDIRRI_REG_DATABASE v2.0` |
| **Indicators** | Detailed regulatory measures underlying the index |
| **SDMX CSV** | ✅ |

### 7.3 FDI Statistics (BMD4)
| Dataflow | Description |
|----------|-------------|
| `DSD_FDI@DF_FDI_FLOW_IND` | FDI flows by economic activity |
| `DSD_FDI@DF_FDI_POS_IND` | FDI positions by economic activity |
| `DSD_FDI@DF_FDI_CTRY_IND_SUMM` | FDI by counterpart area and activity |
| **SDMX CSV** | ✅ |

---

## 8. TAXATION (OECD.CTP — 205 dataflows)

### 8.1 Tax Revenue Statistics
| Property | Value |
|----------|-------|
| **Full ID** | `OECD.CTP.TPS/DSD_REV_OECD@DF_REV_ALL v2.0` |
| **Indicators** | Total tax revenue as % GDP, by tax type (corporate, personal, VAT, social security) |
| **Countries** | OECD countries |
| **Also** | Global: `DSD_REV_GLOBAL@DF_REV_ALL`, LAC: `DSD_REV_LAC@DF_REV_ALL`, ASAP: `DSD_REV_ASAP@DF_REV_ALL`, AFRICA: `DSD_REV_AFRICA@DF_REV_ALL` |
| **Relevance** | High — fiscal capacity, control variable |

### 8.2 Corporate Income Tax (CIT)
| Dataflow | Description |
|----------|-------------|
| `DSD_TAX_CIT@DF_CIT` | Statutory corporate tax rates, small business rates |
| `DSD_TAX_CIT@DF_CIT_DIVD_INCOME` | Combined tax rates on dividend income |

### 8.3 Labour Taxation
| Dataflow | Description |
|----------|-------------|
| `DSD_TAX_WAGES_COMP@DF_TW_COMP` | Comparative indicators: tax wedge by income level, family type |
| `DSD_TAX_PIT@DF_PIT_AV` | Average personal income tax rates |

### 8.4 Carbon Pricing
| Dataflow | Description |
|----------|-------------|
| `DSD_ECR@DF_SEP` | Shares of CO2 emissions from energy priced |
| `DSD_NECR@DF_NECRSHARES` | Shares of emissions priced |

---

## 9. EDUCATION (OECD.EDU — 142 dataflows)

### 9.1 Expenditure on Education (% GDP)
| Full ID | `OECD.EDU.IMEP/DSD_EAG_UOE_FIN@DF_UOE_INDIC_FIN_GDP v1.0` |
| **Indicators** | Total education expenditure as % GDP, by level |
| **Relevance** | Medium — human capital investment control variable |

### 9.2 Educational Attainment Distribution
| Full ID | `DSD_EAG_LSO_EA@DF_LSO_NEAC_DISTR_EA v1.0` |
| **Indicators** | Share of population by education level (below upper secondary, upper secondary, tertiary) |
| **Relevance** | High — workforce skills, education level |

### 9.3 Share of Government Expenditure on Education
| Full ID | `DSD_EAG_UOE_FIN@DF_UOE_FIN_INDIC_SHARE_EDU_GOV v3.1` |
| **Indicators** | Education spending as share of total government expenditure |

### 9.4 TALIS Survey
| Dataflow | Description |
|----------|-------------|
| `DSD_TALIS@DF_TALIS` | Teaching and Learning International Survey |
| **Relevance** | Medium — digital skills in education |

---

## 10. WELLBEING, INEQUALITY & SDGs (OECD.WISE — 28 dataflows)

### 10.1 Income Distribution Database
| Full ID | `OECD.WISE.INE/DSD_WISE_IDD@DF_IDD v1.0` |
| **Indicators** | Gini coefficient, income quintile shares, poverty rates |
| **SDMX CSV** | ✅ |
| **Relevance** | **Very High** — inequality control variable |

### 10.2 Wealth Distribution Database
| Full ID | `OECD.WISE.INE/DSD_WEALTH@DF_WEALTH v1.0` |
| **Indicators** | Net wealth distribution, wealth inequality |

### 10.3 Current Well-being — How's Life?
| Dataflow | Description |
|----------|-------------|
| `DSD_HSL@DF_HSL_CWB` | 80+ well-being indicators |
| `DSD_HSL@DF_HSL_CWB_EDU` | Well-being by education level |
| `DSD_HSL@DF_HSL_CWB_INEQ` | Well-being inequality |
| **Relevance** | Medium — quality of life, digital divide |

### 10.4 SDG Indicators
| Dataflow | Description |
|----------|-------------|
| `DSD_SDG@DF_SDG_G_9` | SDG 9 — Industry, innovation, infrastructure |
| `DSD_SDG@DF_SDG_G_16` | SDG 16 — Peace, justice, strong institutions |
| `DSD_SDG@DF_SDG_G_4` | SDG 4 — Quality education |
| `DSD_SDG@DF_SDG_G_17` | SDG 17 — Partnerships for the goals |
| **Relevance** | High — innovation, institutional quality |

---

## 11. NATIONAL ACCOUNTS & MACRO (OECD.SDD.NAD — 318 dataflows)

### 11.1 GDP and Components
| Full ID | `OECD.SDD.NAD/DSD_NAMAIN10@DF_TABLE1_EXPENDITURE v2.0` |
| **Indicators** | GDP, consumption, investment, government spending, net exports |
| **Relevance** | High — economic control variables |

### 11.2 Government Accounts
| Full ID | `OECD.SDD.NAD/DSD_NASEC10@DF_TABLE12 v1.1` |
| **Indicators** | Government revenue, expenditure, deficit/surplus, debt |

### 11.3 Productivity Database
| Full IDs | `DSD_PDB@DF_PDB`, `DSD_PDB@DF_PDB_GR`, `DSD_PDB@DF_PDB_ISIC4_I4`, `DSD_PDB@DF_PDB_LV`, `DSD_PDB@DF_PDB_ULC_Q` |
| **Indicators** | GDP per hour worked, MFP, unit labour costs |
| **Relevance** | High — productivity, digital economy impact |

### 11.4 PPPs
| Full IDs | `DSD_PPP@DF_PPP_NEGDP`, `DSD_PPP@DF_PPP_NEPC`, `DSD_PPP@DF_PPP_REPC`, `DSD_PPP@DF_PPP_VI` |
| **Indicators** | Purchasing power parities, real expenditure, volume indices |

---

## 12. REGIONAL STATISTICS (OECD.CFE.EDS — 162 dataflows, selected)

| Dataflow | Description |
|----------|-------------|
| `DSD_REG_ECO@DF_GDP` | Regional GDP (TL2/TL3) |
| `DSD_REG_EDU@DF_ATTAIN` | Regional educational attainment |
| `DSD_REG_EDU@DF_EDU` | Regional education statistics |
| `DSD_REG_EDU@DF_EMP` | Regional employment by education |
| `DSD_REG_INNOV@DF_RD_GERD` | Regional R&D expenditure |
| `DSD_FUA_DIGI@DF_INTERNET_SPEED` | Internet speed by functional urban area |
| `DSD_FUA_INNOV@DF_PATENTS` | Patents by functional urban area |

---

## 13. SUMMARY: SDMX API ACCESSIBILITY

### 13.1 API Endpoint
```
Base: https://sdmx.oecd.org/public/rest/
```

### 13.2 Endpoint Patterns
| Operation | URL Pattern | Returns |
|-----------|------------|---------|
| List all dataflows | `GET /dataflow/` | XML (1505 flows) |
| Get one dataflow | `GET /dataflow/{AGENCY}/{ID}/latest` | XML metadata |
| Get data structure | `GET /datastructure/{AGENCY}/{DSD}/latest` | XML dimensions |
| Get data (CSV) | `GET /data/{AGENCY},{ID}/latest/{DIM_SELECTION}?format=csv` | CSV |
| Get data (XML) | `GET /data/{AGENCY},{ID}/latest/{DIM_SELECTION}` | SDMX-ML |

### 13.3 CSV Download Confirmed Working
✅ `OECD.TAD.TPD/DSD_STRI@DF_STRI_MAIN` — Services restrictiveness  
✅ `OECD.TAD.TPD/DSD_STRI@DF_STRI_DIGITAL` — Digital restrictiveness  
✅ `OECD.TAD.TPD/DSD_INDIGO@DF_INDIGO` — Digital trade openness  
✅ `OECD.STI.DEP/DSD_BB_DATABASE@DF_BB_TEL_DATABASE` — Broadband/telecom  
✅ `OECD.STI.DEP/DSD_ICT_HH_IND@DF_HH` — ICT households  
✅ `OECD.STI.DEP/DSD_ICT_HH_IND@DF_IND` — ICT individuals  
✅ `OECD.STI.STP/DSD_MSTI@DF_MSTI` — Main STI indicators  
✅ `OECD.STI.STP/DSD_RDS_GERD@DF_GERD_SOF` — R&D expenditure  
✅ `OECD.GOV.GIP/DSD_GOV@DF_GOV_2025` — Government at a Glance  
✅ `OECD.GOV.PSI/DSD_PII@DF_PUBLIC_INTEGRITY` — Public integrity  
✅ `OECD.DAF.INV/DSD_FDIRRI_SCORES@DF_FDIRRI_SCORES` — FDI restrictiveness  
✅ `OECD.ECO.GCRD/DSD_PMR@DF_PMR` — Product market regulation  
✅ `OECD.ECO.MAD/DSD_EPS@DF_EPS` — Environmental policy stringency  

### 13.4 CSV Download — Requires Specific Dimension Selection
⚠️ `DSD_ICT_B@DF_BUSINESSES` — requires 6 specific dimension values  
⚠️ `DSD_RDS_GERD@DF_GERD_*` — requires up to 11 dimension values  

---

## 14. CRITICAL FINDINGS

### 14.1 No AI-Specific OECD Dataset Exists
- There is **NO** `DSD_AI@DF_AI` or similar AI regulation-specific dataset in the OECD SDMX catalog
- The **OECD AI Policy Observatory** (oecd.ai) content is **NOT** exposed via SDMX API
- Your existing IAPP data (`iapp_regulatory_intensity`, etc.) remains the best source for AI regulation variables
- The OECD **Going Digital Toolkit** includes relevant AI adoption indicators

### 14.2 Best New Datasets to Add to Your Matrix
These would add **significant explanatory power** to your regression models:

| Priority | Dataset | Variable Idea | Study Dimension |
|----------|---------|---------------|-----------------|
| 🔴 P0 | Digital STRI (STRI_DIGITAL) | Digital trade restrictiveness score | Digital regulation |
| 🔴 P0 | PMR (Product Market Regulation) | Economy-wide regulatory barriers | General regulation |
| 🔴 P0 | FDI Restrictiveness Index | Foreign investment barriers | Investment climate |
| 🔴 P0 | Public Integrity (PII) | Institutional integrity | Institutional quality |
| 🔴 P0 | Digital Government Index | E-government maturity | Gov digital readiness |
| 🟡 P1 | GBARD (Gov Budget Allocations for R&D) | Government R&D spending as % GDP | Innovation policy |
| 🟡 P1 | R&D Tax Subsidy Rate (RDSUB) | Tax incentive generosity | Innovation incentives |
| 🟡 P1 | Regulatory Governance (RIA indexes) | Quality of regulatory process | Regulatory quality |
| 🟡 P1 | Trust in Government | Citizen trust in institutions | Social capital |
| 🟡 P1 | TALIS survey | Teacher digital skills | Education quality |
| 🟢 P2 | EPS (Environmental Policy Stringency) | Environmental regulation stringency | Regulatory approach model |
| 🟢 P2 | Income Distribution (Gini) | Inequality | Socioeconomic control |
| 🟢 P2 | INDIGO (Digital Trade Openness) | Openness to digital trade | Trade policy |
| 🟢 P2 | ReICO talent circulation | AI/tech talent migration | Human capital |

### 14.3 Which Datasets Are Already in Your Matrix
Your current matrix (from 10 sources) already includes equivalents for:
- **WB WGI** → corresponds to PMR/PII/governance variables
- **WIPO GII** → partially overlaps with MSTI/R&D indicators
- **Oxford AI Readiness** → partially overlaps with Digital Gov Index
- **Stanford AI Index** → AI patents, AI investment (not in OECD SDMX)
- **MS Adoption** → not in OECD (Microsoft proprietary survey)

### 14.4 Key Gaps Filled by OECD SDMX
These are **not** in your current matrix but available via OECD:
1. **Digital STRI** → direct measure of digital regulation restrictiveness
2. **PMR** → general product market regulation quality
3. **FDI Restrictiveness Index** → investment openness
4. **Public Integrity Indicators** → institutional quality (more granular than WGI)
5. **Regulatory Governance (RIA indexes)** → evidence-based regulation proxy
6. **GBARD** → government R&D budget priorities by objective
7. **R&D Tax Subsidy Rates** → implicit subsidy rates
8. **Trust in Government** → social capital measure
9. **Digital Government Maturity** → e-government readiness
10. **INDIGO** → digital trade integration

---

## 15. RECOMMENDED PYTHON DOWNLOAD CODE

```python
import pandas as pd
import requests

def download_oecd_csv(agency, flow_id, version, dimensions=None):
    """
    Download OECD data as CSV via SDMX API.
    
    Parameters:
    - agency: e.g. 'OECD.TAD.TPD'
    - flow_id: e.g. 'DSD_STRI@DF_STRI_DIGITAL'
    - version: e.g. '1.0'
    - dimensions: e.g. 'A........' (one dot per dimension, all wildcards)
    """
    base = "https://sdmx.oecd.org/public/rest/data"
    dims = dimensions or '.' * 8  # default 8 wildcards
    url = f"{base}/{agency},{flow_id},{version}/{dims}?format=csv"
    
    response = requests.get(url, timeout=30)
    if response.status_code == 200:
        return pd.read_csv(pd.StringIO(response.text))
    else:
        raise Exception(f"API error {response.status_code}: {response.text[:200]}")

# Examples:
# Digital STRI:
# df = download_oecd_csv('OECD.TAD.TPD', 'DSD_STRI@DF_STRI_DIGITAL', '1.0', 'A........')

# INDIGO (digital trade openness):
# df = download_oecd_csv('OECD.TAD.TPD', 'DSD_INDIGO@DF_INDIGO', '1.0', 'A......')

# PMR (product market regulation):
# Note: PMR has 3 dimensions: REF_AREA, MEASURE, FREQ
# df = download_oecd_csv('OECD.ECO.GCRD', 'DSD_PMR@DF_PMR', '1.2', '...')
```

---

*End of catalog. Generated from live OECD SDMX API — 1,505 dataflows catalogued, 60+ identified as relevant.*
