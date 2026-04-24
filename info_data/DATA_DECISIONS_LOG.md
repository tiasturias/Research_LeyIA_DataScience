# Data Decisions Log — Proyecto Regulacion IA

## Proposito

Este documento registra todas las decisiones metodologicas tomadas durante la recoleccion y preparacion de datos. Cada decision debe estar justificada y ser rastreable.

---

## D-001: Exclusion de ai_vibrancy_score

**Fecha:** 2025-04  
**Variable:** ai_vibrancy_score  
**Decision:** Excluida del estudio  
**Razon:** La fuente oficial (Stanford HAI Global AI Vibrancy Tool) fue descomisionada. La alternativa (Tortoise Global AI Index) esta detras de paywall. No existe fuente publica reproducible para un score compuesto de vitalidad del ecosistema de IA.  
**Compensacion:** Los outcomes observables (investment, startups, patents, readiness, adoption) cubren las dimensiones que vibrancy agregaba como indice compuesto.  
**Impacto:** Ningun — las 4Y principales son directamente observables y mas transparentes que un indice compuesto opaco.

---

## D-002: fig_4.3.8/4.3.9 como fuente primaria de inversion IA por pais

**Fecha:** 2025-04  
**Variable:** ai_investment_usd_bn_cumulative, ai_investment_usd_bn_2024  
**Decision:** Usar fig_4.3.8 (annual 2024) y fig_4.3.9 (cumulative 2013-2024) como fuentes primarias  
**Razon:** fig_4.3.10 solo reporta USA, China y EU como agregado. fig_4.3.8/9 reportan ~90 paises individualmente.  
**Cobertura resultado:** 84/86 paises del estudio  
**Fuente descartada:** fig_4.3.10 (no usable a nivel pais)

---

## D-003: Ventana temporal para controles socioeconomicos (WDI/WGI)

**Fecha:** 2025-04  
**Variable:** gdp_per_capita_ppp, rd_expenditure, internet_penetration, tertiary_education, government_effectiveness  
**Decision:** Para cada variable × pais, tomar el valor mas reciente disponible dentro de la ventana [2019, 2024]  
**Razon:** El corte transversal principal es 2025. Los controles deben reflejar condiciones contemporaneas. Valores anteriores a 2019 serian demasiado distantes para una cross-section de regulacion vigente.  
**Impacto:** Reduce ligeramente la cobertura de rd_expenditure (74/86) y government_effectiveness (63/86), pero mejora la coherencia temporal.

---

## D-004: TWN (Taiwan) — excepciones de cobertura

**Fecha:** 2025-04  
**Pais:** TWN  
**Decision:** TWN se mantiene en la muestra (86 paises) pero con ausencias estructurales documentadas  
**Variables afectadas:**
- gdp_per_capita_ppp: NaN (excluido de World Bank API)
- internet_penetration: NaN (excluido de World Bank API)  
- gii_score: NaN (excluido de WIPO GII por status politico)
**Razon:** TWN tiene regulacion IA documentada y es relevante para el analisis regulatorio. Excluirlo eliminaria un caso valido. Se acepta como observacion incompleta para el modelo principal, pero disponible para subanalisis.  
**Impacto:** TWN no entra en la muestra principal (complete_principal=0) pero queda disponible para analisis descriptivos y NLP.

---

## D-005: government_effectiveness como variable de robustez, no principal

**Fecha:** 2025-04  
**Variable:** government_effectiveness  
**Decision:** Reclasificada de X2 core a X2 robustness  
**Razon:** Solo cubre 63/86 paises. Los 22 paises de la expansion WDI (API v2) no retornaron datos para el indicador GE.EST. Incluirla como core reduciria la muestra principal de 72 a ~48.  
**Impacto:** El modelo principal no controla por efectividad gubernamental. Se usa en modelos de robustez como sensibilidad.

---

## D-006: ai_patents_per100k como variable de robustez

**Fecha:** 2025-04  
**Variable:** ai_patents_per100k  
**Decision:** Reclasificada de Y principal a Y robustness  
**Razon:** Solo cubre 54/86 paises (Stanford fig_1.2.4, 2023). Incluirla como Y principal eliminaria 32 paises de la muestra. Los paises faltantes son principalmente economias emergentes con regulatory_status_group diverso.  
**Impacto:** La subpregunta de innovacion (Q3) se responde con ai_startups como Y principal; ai_patents se analiza en submodelo separado con N≈54.

---

## D-007: Microsoft H2 2025 como periodo canonico de adopcion

**Fecha:** 2025-04  
**Variable:** ai_adoption_rate  
**Decision:** Usar ai_user_share_h2_2025 como valor canonico; H1 2025 como fallback  
**Razon:** H2 es mas reciente y contemporaneo con el corte transversal 2025. Microsoft publica ambos semestres.  
**Cobertura:** 75/86 (11 paises estructuralmente ausentes del estudio Microsoft)

---

## D-008: ai_investment_vc_proxy como robustez financiera

**Fecha:** 2025-04  
**Variable:** ai_investment_vc_proxy (OECD VC total como % PIB)  
**Decision:** Clasificada como robustness, no outcome principal  
**Razon:** (1) Solo cubre 32/86 paises. (2) Es VC general, no IA-especifico. (3) Stanford fig_4.3.8/9 provee inversion IA directa para 84/86.  
**Impacto:** Se usa en modelos de sensibilidad para validar que los resultados de inversion no dependen de la medida.

---

## D-009: Muestra principal como cross-section 2025

**Fecha:** 2025-04  
**Decision:** La muestra principal es un corte transversal con:
- Variables regulatorias (X1): snapshot 2025 (IAPP + OECD panel year=2025)
- Variables Y: edicion mas reciente disponible (2024-2025 segun fuente)
- Variables X2: valor mas reciente dentro de ventana 2019-2024  
**Razon:** No todas las fuentes Y tienen panel comparable. El objetivo es maximizar comparabilidad contemporanea, no longitudinalidad.  
**Extension panel:** Disponible para analisis de sensibilidad via x1_consolidated.csv (2013-2025) y paneles de Oxford/WIPO.

---

## D-010: Taxonomia regulatoria de 4 niveles

**Fecha:** 2025-04  
**Variable:** regulatory_status_group  
**Decision:** 4 niveles derivados de regulatory_approach:
- `no_framework` ← none (5 paises)
- `soft_framework` ← light_touch (10 paises)
- `strategy_only` ← strategy_led (39 paises)
- `binding_regulation` ← regulation_focused + comprehensive (32 paises)  
**Razon:** Colapsar los 5 niveles OECD/IAPP en 4 grupos permite comparacion significativa con tamanos de grupo suficientes para inferencia.  
**Nota:** El conteo (5/10/39/32) corresponde a los 86 paises completos. En la muestra principal (72), los conteos son 2/9/34/27.

---

## D-011: Inclusion de todo el espectro regulatorio

**Fecha:** 2025-04  
**Decision:** La muestra incluye paises sin regulacion IA (no_framework). `has_ai_law=0` no es criterio de exclusion.  
**Razon:** La pregunta de investigacion es si "existe asociacion entre regulacion y ecosistema". Excluir paises sin regulacion eliminaria la varianza necesaria para responder la pregunta.  
**Impacto:** Permite comparaciones between-group (binding vs no_framework) que son centrales para la recomendacion politica.

---

## D-012: Incorporacion de confounders institucionales WGI (post-auditoria Tarea A)

**Fecha:** 2026-04
**Contexto:** Auditoria cientifica (Tarea A) detecto que `regulatory_intensity` sin controles institucionales captura "cultura regulatoria general" y no "regulacion AI-especifica" (Problema #6 de auditoria).
**Decision:** Incorporar dos nuevas variables WGI como confounders core:
- `regulatory_quality` (GOV_WGI_RQ.EST): calidad general de la regulacion del pais
- `rule_of_law` (GOV_WGI_RL.EST): estado de derecho

**Fuente:** World Bank Worldwide Governance Indicators (WGI), DataBank `db=3`, serie `GOV_WGI_*.EST` (nueva nomenclatura post-2024; la API v2 antigua con codigos `RQ.EST` / `RL.EST` devuelve 404).
**Ventana temporal:** [2019, 2023] — 2023 es la ultima publicacion WGI disponible a 2026-04 (delay de publicacion habitual).
**Cobertura resultante:** 85/86 paises (TWN excluido por D-004).
**Script:** `src/expand_wgi.py` descarga WGI para los 22 paises expansion faltantes en raw original.
**Integracion:** `src/build_source_masters.py::build_wb_master()` mergea `wdi_all_86.csv` (63 paises originales) + `wgi_expansion_22.csv` (22 paises nuevos).

**Evidencia empirica del confounding:**
- binding_regulation (N=27): regulatory_quality mean = +0.906
- strategy_only (N=34): regulatory_quality mean = +0.352
- no_framework (N=2): regulatory_quality mean = -0.913

Esta gradiente muestra que los paises con regulacion vinculante ya tenian alta calidad regulatoria general. Omitir este control sobreestima el efecto de la regulacion IA-especifica.

**Impacto en la muestra:** Nueva tier `complete_confounded` = 72/86, identico a `complete_principal` (los confounders no reducen la muestra, solo aumentan el rigor del control).

**Variables adicionales incluidas en la misma descarga:**
- `government_effectiveness`: ampliada de 63 → 85/86 (mejora la variable robustness existente)
- `control_of_corruption`: nueva (85/86), disponible para robustness adicional.

---

## D-013: Actualizacion de codificacion WGI en API (migracion GOV_WGI_*)

**Fecha:** 2026-04
**Problema detectado:** `src/expand_wdi.py` originalmente incluia `GE.EST` en INDICATORS pero no descargaba datos porque World Bank migro WGI a DataBank `db=3` con prefijo `GOV_WGI_*.EST`. Los 23 paises expansion nunca recibieron WGI por este motivo.
**Decision:** Crear `src/expand_wgi.py` separado que usa `wbgapi.data.fetch(... db=3)` con codigos correctos. No modificar `expand_wdi.py` mas alla de agregar los codigos antiguos para documentar (no se ejecutan exitosamente, se mantienen como referencia).
**Leccion operativa:** Para futuros indicadores WGI, usar SIEMPRE `db=3` y prefijo `GOV_WGI_`. La API v2 con formato `/country/XXX/indicator/RQ.EST` esta deprecada desde ~2024.

---

## D-014: Incorporacion de confounder legal-regulatorio has_gdpr_like_law (post-auditoria Tarea A, sub-tarea A.4)

**Fecha:** 2026-04
**Contexto:** Auditoria cientifica (Tarea A) detecto que sin controlar por preexistencia de marcos de proteccion de datos, `regulatory_intensity` captura parcialmente "tradicion regulatoria digital" (GDPR-like laws) en vez de "regulacion AI-especifica".

**Decision:** Incorporar dos nuevas variables como confounders legal-regulatorios core:
- `has_gdpr_like_law` (0/1): binary indicator de ley comprehensiva nacional de proteccion de datos
- `gdpr_similarity_level` (0-3 ordinal): nivel de alineacion con GDPR
  - 1 = sectoral/basica solamente
  - 2 = ley comprehensiva GDPR-like sin adequacy UE
  - 3 = miembro EU/EEA o decision de adequacy UE vigente

**Variables auxiliares agregadas:** `dp_law_year`, `has_dpa`, `eu_status`, `enforcement_active`, `dp_law_name`.

**Fuente:** Codificacion manual basada en DLA Piper *Data Protection Laws of the World 2025*, cross-check con UNCTAD Data Protection Tracker y EU Commission adequacy decisions list.
**Fecha de corte:** 2026-03.
**Cobertura:** 86/86 (exhaustiva).
**Script:** `src/build_source_masters.py::build_gdpr_master()` lee `data/raw/GDPR_coding/gdpr_like_coding.csv` y produce `data/interim/x2_gdpr_master.csv`.
**Metodologia completa:** Ver `info_data/METODOLOGIA_GDPR_CODING.md` con reglas de codificacion, casos limite y justificacion cientifica.

**Evidencia empirica del confounding (N=72 confounded sample):**

| regulatory_status_group | gdpr_similarity_level (mean) | N | EU members |
|---|---|---|---|
| binding_regulation | **2.889** | 27 | 22/27 |
| soft_framework | 2.222 | 9 | 0/9 |
| strategy_only | 2.147 | 34 | 0/34 |
| no_framework | 1.500 | 2 | 0/2 |

Gradiente monotonico: los paises con regulacion IA vinculante tienen casi todos nivel 3 (EU/EEA/adequacy). Sin este control, el "efecto de regulacion IA" se confunde con "estar en el ecosistema GDPR europeo".

**Impacto en la muestra:** `complete_confounded` se mantiene en 72/86 (variables GDPR tienen cobertura 86/86, no reducen muestra). Ampliacion del control sin perdida de N.

**Casos de codificacion notables documentados en METODOLOGIA_GDPR_CODING.md:**
- USA: level 1 (sin ley federal comprehensiva)
- CHL: level 2 (Ley 21.719 nueva, sin adequacy aun)
- BRA, CHN, IND: level 2 (comprehensive pero sin adequacy UE)
- 27 EU members + 2 EEA (ISL, NOR) + 9 adequacy (ARG, CAN, CHE, GBR, ISR, JPN, KOR, NZL, URY) = 38 paises nivel 3.

---

## D-015: Proxies de economia digital via WDI (post-auditoria Tarea A, sub-tarea A.5)

**Fecha:** 2026-04
**Contexto:** La auditoria cientifica (Tarea A) solicito incorporar un control por "tamano de la economia digital" para evitar que `ai_readiness_score` y `ai_investment_usd_bn_cumulative` reflejen simplemente la capacidad digital preexistente del pais en vez del efecto regulatorio-AI.

**Problema de fuente:** El UNCTAD *Digital Economy Report 2024* no publica "digital_economy_gdp_pct" a nivel pais para los 86 paises del estudio. UNCTAD reporta esta metrica solo a nivel global (~15% del PIB mundial) y regional. No existe dataset pais-ano reproducible de "economia digital como % del PIB" abierto y actualizado.

**Decision:** Adoptar dos proxies complementarios del World Bank WDI:
- `ict_service_exports_pct` (BX.GSR.CCIS.ZS): exportaciones de servicios ICT (% de exportaciones de servicios). Captura el tamano de la economia digital de servicios (software, telecom, computer services).
- `high_tech_exports_pct` (TX.VAL.TECH.MF.ZS): exportaciones de alta tecnologia (% de exportaciones manufactureras). Captura la dimension de manufactura tech-avanzada (aeroespacio, computers, farmaceutica, instrumentos cientificos).

**No-redundancia con controles existentes:**
- `internet_penetration` mide CONSUMO/acceso digital del hogar. Los nuevos proxies miden PRODUCCION/capacidad exportadora digital. Correlacion esperada pero no perfecta (p.ej. Irlanda tiene internet_penetration alto PERO high_tech_exports_pct muy alto tambien por hub de multinacionales; Chile tiene internet alto pero high_tech_exports moderado).
- No se solapan con `gdp_per_capita_ppp` (nivel agregado) ni con `rd_expenditure` (input a I+D).

**Script:** `src/expand_digital_economy.py` usa `wbgapi.data.fetch()` para descargar ambos indicadores (ventana 2019-2024) para 85 paises (TWN excluido por D-004). Output: `data/raw/World Bank WDI/digital_economy_86.csv` → integrado en `build_wb_master()`.

**Cobertura obtenida:**
- `ict_service_exports_pct`: 83/86
- `high_tech_exports_pct`: 83/86
- Paises sin cobertura: BGD, SRB, VNM (gaps historicos en estadisticas ICT trade)

**Clasificacion en hierarchy:** NO se incorpora a `complete_confounded` (72/86) para preservar la muestra principal. Se crea una tier NUEVA:
- `complete_digital` = `complete_confounded` + `ict_service_exports_pct` + `high_tech_exports_pct` → 69/86.

Se pierden 3 paises (BGD, SRB, VNM), todos del grupo `strategy_only`. La tier digital esta disponible para analisis de robustez del modelo principal, no para sustituirlo.

**Alternativa rechazada:** UNCTAD B2C E-commerce Index (2020) — descartada por: (a) no reproducible via API, (b) dataset estatico 2020 que no captura evolucion post-COVID, (c) cobertura pais-ano no armonizable con el resto del pipeline temporal.

**Justificacion cientifica:** La incorporacion de estos proxies reduce el riesgo de confundir "pais con ecosistema tecnologico-exportador fuerte" con "pais con regulacion IA efectiva", que es una amenaza identificada en la revision. Se documenta como robustness no-core porque el costo en N (-3 paises) no justifica forzar al modelo principal.

---

## D-016: Incorporacion de Freedom House como confounder politico-regimen (post-auditoria Tarea A, sub-tarea A.6)

**Fecha:** 2026-04
**Contexto:** La auditoria cientifica detecto la necesidad de controlar por tipo de regimen politico dado que democracias y autoritarismos regulan IA con motivaciones estructuralmente distintas: autoritarismos tipicamente usan regulacion IA como vehiculo de control informacional y vigilancia, mientras que democracias la orientan a derechos del usuario y transparencia. Sin este control, `regulatory_intensity` puede confundirse con "nivel democratico".

**Decision:** Incorporar dos variables de Freedom House *Freedom in the World 2025* (data ano 2024) como confounders politico-regimen de robustness:
- `fh_total_score` (0-100 continuous): score agregado Political Rights + Civil Liberties.
- `fh_democracy_level` (0-2 ordinal): derivado de status FH, NF→0, PF→1, F→2.

Variables auxiliares: `fh_status`, `fh_pr_score`, `fh_cl_score`, `fh_year`.

**Fuente:** Codificacion manual basada en FITW 2025 (publicado marzo 2025). Se recomienda validar scores exactos contra el Excel autoritativo "All Data, FIW 2013-2025.xlsx" antes de publicacion academica.

**Cobertura:** 86/86 (codificacion manual exhaustiva).

**Script:** `src/build_source_masters.py::build_fh_master()` lee `data/raw/FreedomHouse/freedom_in_the_world_2025.csv` y produce `data/interim/x2_fh_master.csv`.
**Metodologia completa:** `info_data/METODOLOGIA_FREEDOM_HOUSE.md`.

**Evidencia empirica del confounding (N=72 confounded sample):**

| regulatory_status_group | fh_mean | % Free | % Not Free | N |
|---|---|---|---|---|
| binding_regulation | **82.8** | 85.2% | 7.4% | 27 |
| soft_framework | 60.2 | 33.3% | 22.2% | 9 |
| strategy_only | 60.7 | 41.2% | 20.6% | 34 |
| no_framework | 28.0 | 0.0% | 50.0% | 2 |

Gradiente monotonico: paises con regulacion IA vinculante son 85% Free; paises sin marco son 50% Not Free. Sin control por regimen, el efecto de regulacion IA se confunde con "ser democracia consolidada".

**No-redundancia con WGI verificada empiricamente:**
- `fh_total_score` x `regulatory_quality`: r = 0.685
- `fh_total_score` x `rule_of_law`: r = 0.681
- `fh_total_score` x `gdpr_similarity_level`: r = 0.682

r ≈ 0.68 implica ~54% de varianza adicional no capturada por WGI. Casos como SGP (rule_of_law=+1.7, FH=48 PF) o CHN (rule_of_law=-0.2, FH=9 NF) confirman que FH mide una dimension ortogonal (libertades politicas/civiles) a la que mide WGI (gobernanza tecnica).

**Clasificacion en hierarchy:** NO se incorpora a `complete_confounded` (72/86) para preservar invariancia de la tier principal recomendada. Se crea tier NUEVA:
- `complete_regime` = `complete_confounded` + `fh_total_score` + `fh_democracy_level` → **72/86** (sin perdida de N porque FH cobertura 86/86).

**Uso analitico recomendado:**
1. Modelo principal sigue siendo `complete_confounded`.
2. Robustness: repetir modelo con `complete_regime` incluyendo `fh_democracy_level`.
3. Interaccion heterogenea: testear `regulatory_intensity × fh_democracy_level` para evaluar si el efecto de regulacion IA difiere por tipo de regimen (hipotesis de fondo de la investigacion).

**Decision de diseno rechazada y reconsiderada:** Se planteo inicialmente que FH podria ser redundante con rule_of_law. El analisis de correlacion (r=0.68) y casos emblematicos (SGP, CHN, HUN) demuestran lo contrario: FH captura una dimension distinta. La incorporacion es justificada.

---

## D-017: Incorporacion de legal_origin (La Porta 2008) como confounder de tradicion juridica (post-auditoria Tarea A, sub-tarea A.3-bis)

**Fecha:** 2026-04
**Contexto:** La auditoria cientifica (Problema #6) identifico la necesidad de controlar por *tradicion juridica heredada* como confounder del estilo regulatorio. Sin este control, `regulatory_intensity` captura no solo la propension actual a regular IA sino tambien la *propension historica/cultural a codificar exhaustivamente* que distingue a familias civil-law (French/German) de common-law (English). Este confounder actua sobre un eje temporal mas profundo (siglos, no decadas) que WGI o GDPR.

**Decision:** Incorporar dos variables derivadas de la clasificacion La Porta, Lopez-de-Silanes & Shleifer (2008) *"The Economic Consequences of Legal Origins"* (JEL 46(2)):
- `legal_origin` (categorica, 5 niveles): {English, French, German, Scandinavian, Socialist}.
- `is_common_law` (binaria): 1 si `legal_origin == "English"`, 0 en otro caso.

**Fuente:** Codificacion manual basada en La Porta 2008 Appendix + Djankov-La Porta 2003 para categoria Socialist. Casos ambiguos (SAU, JOR, IDN, PHL, TUR, MUS, CMR, CHN, VNM) desambiguados usando el criterio del codigo comercial / civil de origen (no status personal ni regimen politico actual), consistente con CBR Leximetric.

**Cobertura:** 86/86 (codificacion estable historicamente; no requiere updates temporales).

**Distribucion muestra completa:**
| Familia | N |
|---|---|
| French | 30 |
| English | 24 |
| Socialist | 19 |
| German | 8 |
| Scandinavian | 5 |

**Script:** `src/build_source_masters.py::build_legal_origin_master()` lee `data/raw/LegalOrigin/legal_origin_coding.csv` y produce `data/interim/x2_legal_origin_master.csv`.
**Metodologia completa:** `info_data/METODOLOGIA_LEGAL_ORIGIN.md`.

**Evidencia empirica del confounding (N=72 principal sample):**

Proporcion de `binding_regulation` por familia legal:

| Familia | N | % binding_regulation |
|---|---|---|
| English | 18 | **5.6%** |
| French | 26 | 30.8% |
| Socialist | 17 | 58.8% |
| German | 7 | **71.4%** |
| Scandinavian | 4 | **75.0%** |

**Gradiente de 13.3x entre English (5.6%) y Scandinavian (75%).** Este es el confounder con mayor efecto documentado de la auditoria Tarea A — supera a FH (~3x), WGI (~2x) y GDPR (~2.5x) en magnitud del gradiente.

**No-redundancia con controles existentes verificada empiricamente:**
- `is_common_law` x `rule_of_law`: r = 0.10
- `is_common_law` x `regulatory_quality`: r = 0.11
- `is_common_law` x `gdp_per_capita_ppp`: r = 0.06
- `is_common_law` x `regulatory_intensity`: **r = -0.22**

Correlaciones cercanas a cero con WGI confirman que `legal_origin` mide una dimension independiente (tradicion juridica) no capturada por calidad institucional actual. La correlacion negativa con `regulatory_intensity` es el hallazgo confirmatorio: paises common-law sistematicamente regulan IA con menor intensidad.

**Clasificacion en hierarchy:** Se crea tier NUEVA:
- `complete_legal_tradition` = `complete_confounded` + `legal_origin` + `is_common_law` → **72/86** (sin perdida de N porque cobertura 86/86).

**Uso analitico recomendado:**
1. Modelo principal: sigue siendo `complete_confounded` (no forzar legal_origin al modelo core para mantener parsimonia).
2. Robustness 1: OLS con `C(legal_origin)` dummies (categoria base: French). Si el coeficiente de `regulatory_intensity` persiste, el efecto es independiente de la tradicion juridica.
3. Robustness 2: OLS parsimonioso con `is_common_law` + interaccion `is_common_law x regulatory_intensity`. Testea si el efecto de la regulacion IA difiere entre common-law y civil-law (hipotesis sustantiva: mayor efecto marginal en civil-law por efecto de complementariedad con regulacion pre-existente).

**Decision de diseno rechazada y reconsiderada:** Inicialmente se omitio legal_origin del plan de Tarea A argumentando redundancia con WGI y region. El analisis empirico refuta ambas: correlacion con WGI ~0.10 (no redundante); region geografica no captura la dimension legal (paises latinoamericanos son todos French-origin, pero asiaticos son mixtos German/English/French/Socialist). La incorporacion se retomo como A.3-bis.

**Limitacion asumida:** La taxonomia es agregada (5 familias). Heterogeneidad intra-familia (ej: Francia vs Egipto ambos French) no se modela dada potencia estadistica limitada con N=72.

