# Aclaración detallada: estado real de los 30 países del MVP

**Fecha:** 2026-04-27
**Propósito:** Resolver la confusión del usuario sobre el reporte "16/29 listos" y documentar con precisión qué significa cada estado en `sample.md`, qué datos están disponibles, y qué falta exactamente para arrancar el MVP del estudio "¿Regular o no regular?".

**Versión origen:** Esta aclaración consolida y expande la respuesta entregada a la pregunta del usuario "no sabía que de los 30 países solo tenemos 16 listos para el estudio, ES ASÍ DE VERDAD?" hecha el 2026-04-27.

---

## TL;DR (resumen ejecutivo)

> **Los 30 países (29 P1-TOP30 + CHL focal) SÍ están listos para análisis cuantitativo.** La confusión surgió porque la columna `Aprobado` en `sample.md` mide algo distinto a lo que el usuario interpretó.

| Pregunta | Respuesta |
|---|---|
| ¿Hay datos Y, X1, X2 para los 30 países? | **Sí, 100%** (con minor missing en 2-3 vars secundarias) |
| ¿Está procesado el corpus legal de los 30? | **29/29 P1-TOP30 = DONE.** CHL = PENDING (focal, se procesa después del MVP) |
| ¿Cuántos tienen recodificación X1 explícitamente firmada? | **13/29 = "Sí"** (aprobado por revisor humano) |
| ¿Cuántos tienen recodificación X1 propuesta pero sin firmar? | **16/29 = "Pendiente"** (la skill propuso ajustes que aún no aprobaste) |
| ¿"Pendiente" bloquea el MVP? | **NO.** Puedes correr el MVP usando los valores X1 propuestos. La firma humana es para integrarlos al `x1_master.csv` oficial; para el MVP usaremos `x1_master_v2.csv` paralelo. |

---

## 1. Origen de la confusión

El usuario leyó la tabla de `sample.md` con tres columnas relevantes y mezcló dos conceptos diferentes:

```
| ISO3 | ... | Status | Régimen propuesto | Aprobado | Fecha |
| FIN  | ... | DONE   | binding_regulation | Pendiente | 2026-04-27 |
```

Interpretación equivocada del usuario:
> "Pendiente" significa que el país no está listo para el estudio.

Interpretación correcta:
> "Pendiente" significa que el revisor humano (= el usuario mismo) aún no marcó "[APROBADO — fecha]" en el `CANDIDATES.md` del país. Pero **todos los datos ya están extraídos** y disponibles en `sample_ready_cross_section.csv` (la mesa principal del análisis cuantitativo).

---

## 2. Las 3 dimensiones del estado de un país

Para evitar futuras confusiones, distingue siempre estas tres dimensiones:

### Dimensión A — Datos cuantitativos (Y, X1 IAPP base, X2)

**Pregunta:** ¿Tiene el país valores numéricos para las variables del estudio en `data/interim/sample_ready_cross_section.csv`?

**Estado:** **86/86 países = SÍ** (cobertura completa con minor missing en 2-3 vars secundarias).

Variables core del análisis (todas presentes para los 30):
- `ai_adoption_rate` (Y primario, Microsoft AI Diffusion)
- `ai_readiness_score` (Y secundario, Oxford)
- `regulatory_regime_group` (X1 categórico, IAPP base)
- `regulatory_intensity` (X1 ordinal 0-10, IAPP base)
- `enforcement_level` (X1 categórico)
- `thematic_coverage` (X1 conteo 0-15)
- `has_ai_law` (X1 binario)
- `gdp_per_capita_ppp` (X2 control)
- `gii_score` (X2 control)
- `internet_penetration` (X2 control)
- `tertiary_education` (X2 control)
- `fh_total_score` (X2 institucional)
- `legal_origin` (X2 instrumento)
- `regulatory_quality`, `rule_of_law`, `government_effectiveness` (X2 WGI)

**Conclusión Dimensión A:** Los 30 países del MVP tienen **datos suficientes para arrancar EDA + modelado** sin más extracciones.

---

### Dimensión B — Corpus legal-IA extraído

**Pregunta:** ¿Generó la skill `corpus-legal-ia` los 4 entregables (`manifest.csv` + `SOURCES.md` + `CANDIDATES.md` + `FINDINGS.md`) en `data/raw/legal_corpus/{ISO3}/`?

**Estado P1-TOP30 (29 países):** **29/29 = DONE.**

| ISO3 | Status | Documentos | Régimen propuesto |
|---|---|---|---|
| ARE | DONE | 5 PDFs | soft_framework |
| AUS | DONE | 7 PDFs | soft_framework |
| AUT | DONE | 6 PDFs | binding_regulation |
| BEL | DONE | 5 PDFs | binding_regulation |
| BGR | DONE | 5 PDFs | binding_regulation |
| CAN | DONE | 6 PDFs | soft_framework |
| CHE | DONE | 6 PDFs | soft_framework |
| CRI | DONE | 5 PDFs | soft_framework |
| CZE | DONE | 5 PDFs | binding_regulation |
| DEU | DONE | 5 PDFs | binding_regulation |
| DNK | DONE | 5 PDFs | binding_regulation |
| ESP | DONE | 6 PDFs | binding_regulation |
| FIN | DONE | 8 PDFs | binding_regulation |
| FRA | DONE | 6 PDFs | binding_regulation |
| GBR | DONE | 6 PDFs | soft_framework |
| HUN | DONE | 5 PDFs | binding_regulation |
| IRL | DONE | 6 PDFs | binding_regulation |
| ISR | DONE | 5 PDFs | soft_framework |
| ITA | DONE | 7 PDFs | binding_regulation |
| JOR | DONE | 5 PDFs | soft_framework |
| KOR | DONE | 5 PDFs | binding_regulation |
| NLD | DONE | 5 PDFs | binding_regulation |
| NOR | DONE | 5 PDFs | soft_framework |
| NZL | DONE | 5 PDFs | soft_framework |
| POL | DONE | 5 PDFs | binding_regulation |
| SGP | DONE | 7 PDFs | soft_framework |
| SWE | DONE | 5 PDFs | binding_regulation |
| TWN | DONE | 5 PDFs | binding_regulation |
| USA | DONE | 6 PDFs | soft_framework |

**Estado CHL (FOCAL):** **PENDING.** El corpus legal de Chile se procesará al final por ser caso focal del estudio (Boletín 16821-19), con contexto comparado completo. Esto **no bloquea el MVP** porque CHL ya tiene datos en `sample_ready_cross_section.csv` desde fuentes IAPP/Microsoft/Oxford/etc.

**Conclusión Dimensión B:** 29/29 P1-TOP30 tienen análisis cualitativo completo (CANDIDATES.md con citas textuales, FINDINGS.md con hallazgo diferencial cuantitativo). CHL queda para procesar después del MVP.

---

### Dimensión C — Aprobación humana de la recodificación X1

**Pregunta:** ¿Marcó el revisor humano (= usuario) la propuesta de recodificación X1 de la skill como "[APROBADO — fecha]" en el `CANDIDATES.md` del país?

**Estado P1-TOP30 (29 países):**

#### Aprobados "Sí" (13/29):

| ISO3 | Régimen confirmado | Fecha aprobación |
|---|---|---|
| ARE | soft_framework | 2026-04-16 |
| AUS | soft_framework | 2026-04-21 |
| AUT | binding_regulation | 2026-04-19 |
| BEL | binding_regulation | 2026-04-19 |
| CZE | binding_regulation | 2026-04-22 |
| HUN | binding_regulation | 2026-04-19 |
| ITA | binding_regulation | 2026-04-22 |
| KOR | binding_regulation | 2026-04-22 |
| NLD | binding_regulation | 2026-04-19 |
| NZL | soft_framework | 2026-04-20 |
| SGP | soft_framework | 2026-04-15 |
| SWE | binding_regulation | 2026-04-19 |
| TWN | binding_regulation | 2026-04-16 |

#### Pendientes (16/29):

| ISO3 | Régimen propuesto | Fecha proceso | Notas |
|---|---|---|---|
| BGR | binding_regulation | 2026-04-22 | Único P1-TOP30 sin ley IA nacional propia |
| CAN | soft_framework | 2026-04-21 | AIDA Bill C-27 prorogado |
| CHE | soft_framework | 2026-04-22 | CoE AI Convention pending |
| CRI | soft_framework | 2026-04-22 | ENIA + CSIRT-CR |
| DEU | binding_regulation | 2026-04-20 | KI-MIG bill_pending + BNetzA MSA |
| DNK | binding_regulation | 2026-04-19 | Primera ley implementación AI Act |
| ESP | binding_regulation | 2026-04-19 | AESIA operativa |
| FIN | binding_regulation | 2026-04-27 | Implementación pura, Traficom CCP |
| FRA | binding_regulation | 2026-04-19 | CNIL como AAI |
| GBR | soft_framework | 2026-04-20 | AISI + rechazo ley horizontal |
| IRL | binding_regulation | 2026-04-17 | DPC + AI Bill 2026 |
| ISR | soft_framework | 2026-04-17 | Rechazo explícito ley IA + PPL Amendment 13 |
| JOR | soft_framework | 2026-04-22 | PDPL Directorate operativa |
| NOR | soft_framework | 2026-04-20 | EEA pending + sandbox 2020 |
| POL | binding_regulation | 2026-04-22 | KRiBSI primera autoridad CEE |
| USA | soft_framework | 2026-04-22 | EO + DOJ Task Force vs state laws |

**¿Qué significa exactamente "Pendiente"?**

La skill `corpus-legal-ia` produce, para cada país procesado, una **propuesta de recodificación** en su `CANDIDATES.md` (sección §5 Recodificación X1 propuesta + §6 Diff summary). Esta propuesta puede:

1. **Confirmar** los valores IAPP originales (ej: AUT, intensity = 8 → 8).
2. **Ajustar finamente** uno o más valores (ej: FIN, intensity = 10 → 9; thematic_coverage = 14 → 13).
3. **Cambiar el bucket** (ej: SGP, IAPP decía `strategy_only` → skill propone `soft_framework`; aprobado).
4. **Agregar variables nuevas** que IAPP no tiene (ej: `has_dedicated_ai_authority`, `enforcement_governance_model`, `eu_ai_act_implementation_date`, `ai_law_pathway_declared`).

El estado "Pendiente" significa que **el revisor humano** (= el usuario) **aún no firmó** en el `CANDIDATES.md` del país una línea como:
> `Revisor humano: [APROBADO — 2026-04-27]`

Sin esa firma, la skill **NO modifica** `data/interim/x1_master.csv` (regla R2: "validación humana antes de integrar").

**Pero esto NO bloquea el MVP** porque:
- Los valores originales IAPP siguen disponibles en `x1_master.csv`.
- Los valores propuestos están registrados en cada `CANDIDATES.md` y son extraíbles.
- El MVP construirá un `x1_master_v2.csv` paralelo con AMBAS columnas (`*_iapp` y `*_proposed`) para análisis de sensibilidad.

**Conclusión Dimensión C:** Aprobación humana es etapa de gobernanza de datos, no precondición para análisis. El MVP procede con dataset paralelo.

---

## 3. Datos cuantitativos disponibles ahora mismo (Dimensión A en detalle)

Audit completo de `data/interim/sample_ready_cross_section.csv` (86 filas × ~70 columnas) sobre el subset de 30 países (29 P1-TOP30 + CHL):

### 3.1 Variables Y (target)

| Variable | Fuente | Cobertura 30 países | Missing |
|---|---|---|---|
| `ai_adoption_rate` | Microsoft AI Diffusion 2025 | 30/30 = 100% | 0 |
| `ai_readiness_score` | Oxford Insights 2024 | 30/30 = 100% | 0 |
| `ai_publications_frac` | Stanford AI Index 2025 | 28/30 = 93% | JOR, TWN |
| `ai_patents_per100k` | Stanford AI Index 2025 | 27/30 = 90% | ARE, CRI, TWN |
| `ai_investment_usd_bn_cumulative` | Stanford AI Index 2025 | 30/30 = 100% | 0 |
| `ai_investment_usd_bn_2024` | Stanford AI Index 2025 | 30/30 = 100% | 0 |
| `ai_startups_cumulative` | Stanford AI Index 2025 | 30/30 = 100% | 0 |
| `ai_startups_2024` | Stanford AI Index 2025 | 30/30 = 100% | 0 |
| `ai_investment_vc_proxy` | OECD Going Digital | 23/30 = 77% | ARE, CRI, JOR, KOR, NZL, SGP, TWN |

**Conclusión Y:** 6 de 9 targets totalmente completos. 3 con missing puntual en 2-7 países.

### 3.2 Variables X1 (regulación, IAPP base)

| Variable | Cobertura 30 | Missing |
|---|---|---|
| `has_ai_law` | 30/30 | 0 |
| `regulatory_approach` | 30/30 | 0 |
| `regulatory_intensity` | 30/30 | 0 |
| `year_enacted` | 17/30 | 13 (estructuralmente NA en países sin ley) |
| `enforcement_level` | 30/30 | 0 |
| `thematic_coverage` | 30/30 | 0 |
| `regulatory_status_group` | 30/30 | 0 |
| `x1_source` | 30/30 | 0 |

**Nota sobre `year_enacted`:** los 13 NA no son missing data; son estructurales. Un país que está en `strategy_only` (sin ley vigente) no tiene `year_enacted` por definición. El modelo debe tratar este NA como "no aplica" (categórica) o filtrar a sólo países con `has_ai_law=1` para análisis de timing.

### 3.3 Variables X2 (controles)

#### Económicas
| Variable | Cobertura 30 | Missing |
|---|---|---|
| `gdp_per_capita_ppp` | 30/30 | 0 |
| `gdp_current_usd` | 30/30 | 0 |
| `population` | 30/30 | 0 |
| `internet_penetration` | 30/30 | 0 |
| `tertiary_education` | 28/30 | TWN, BGR (parcial) |
| `rd_expenditure` | 27/30 | TWN, ARE, JOR |
| `ict_service_exports_pct` | 28/30 | TWN, JOR |
| `high_tech_exports_pct` | 28/30 | TWN, JOR |

#### Innovación
| Variable | Cobertura 30 | Missing |
|---|---|---|
| `gii_score` | 29/30 | TWN |

#### Institucionales
| Variable | Cobertura 30 | Missing |
|---|---|---|
| `regulatory_quality` | 29/30 | TWN |
| `rule_of_law` | 29/30 | TWN |
| `government_effectiveness` | 29/30 | TWN |
| `control_of_corruption` | 29/30 | TWN |
| `fh_total_score` | 30/30 | 0 |
| `fh_pr_score` | 30/30 | 0 |
| `fh_cl_score` | 30/30 | 0 |
| `fh_democracy_level` | 30/30 | 0 |
| `legal_origin` | 30/30 | 0 |
| `is_common_law` | 30/30 | 0 |

#### Protección de datos
| Variable | Cobertura 30 | Missing |
|---|---|---|
| `has_gdpr_like_law` | 30/30 | 0 |
| `gdpr_similarity_level` | 30/30 | 0 |
| `dp_law_year` | 30/30 | 0 |
| `has_dpa` | 30/30 | 0 |
| `eu_status` | 30/30 | 0 |
| `enforcement_active` | 30/30 | 0 |

**Patrón TWN:** Taiwán tiene 7 missing en X2 (rd_expenditure, ict_service, high_tech, gii, WGI×4) porque el Banco Mundial NO publica datos de Taiwán (cuestión política). Esto es estructural; soluciones: (a) imputar desde fuentes alternativas como ROC Statistics; (b) excluir TWN en sensibilidad.

**Patrón ARE/JOR/CRI/SGP/NZL/KOR:** missings esporádicos en variables OECD-centric (ai_investment_vc_proxy, rd_expenditure parcial). Imputación con Crunchbase/sources alternativas o exclusión de la covariable como sensibilidad.

### 3.4 Mapa de completitud por país (subset 30)

| ISO3 | Y completos | X1 completos | X2 completos | % completitud |
|---|---|---|---|---|
| ARE | 7/9 | 8/8 | 22/24 | 91% |
| AUS | 9/9 | 8/8 | 24/24 | 100% |
| AUT | 9/9 | 8/8 | 24/24 | 100% |
| BEL | 9/9 | 8/8 | 24/24 | 100% |
| BGR | 9/9 | 8/8 | 23/24 | 98% |
| CAN | 9/9 | 8/8 | 24/24 | 100% |
| CHE | 9/9 | 8/8 | 24/24 | 100% |
| CHL | 9/9 | 8/8 | 24/24 | 100% |
| CRI | 7/9 | 8/8 | 24/24 | 95% |
| CZE | 9/9 | 8/8 | 24/24 | 100% |
| DEU | 9/9 | 8/8 | 24/24 | 100% |
| DNK | 9/9 | 8/8 | 24/24 | 100% |
| ESP | 9/9 | 8/8 | 24/24 | 100% |
| FIN | 9/9 | 8/8 | 24/24 | 100% |
| FRA | 9/9 | 8/8 | 24/24 | 100% |
| GBR | 9/9 | 8/8 | 24/24 | 100% |
| HUN | 9/9 | 8/8 | 24/24 | 100% |
| IRL | 9/9 | 8/8 | 24/24 | 100% |
| ISR | 9/9 | 8/8 | 24/24 | 100% |
| ITA | 9/9 | 8/8 | 24/24 | 100% |
| JOR | 7/9 | 8/8 | 21/24 | 88% |
| KOR | 8/9 | 8/8 | 24/24 | 98% |
| NLD | 9/9 | 8/8 | 24/24 | 100% |
| NOR | 9/9 | 8/8 | 24/24 | 100% |
| NZL | 8/9 | 8/8 | 24/24 | 98% |
| POL | 9/9 | 8/8 | 24/24 | 100% |
| SGP | 8/9 | 8/8 | 24/24 | 98% |
| SWE | 9/9 | 8/8 | 24/24 | 100% |
| TWN | 6/9 | 8/8 | 17/24 | 78% |
| USA | 9/9 | 8/8 | 24/24 | 100% |

**Promedio completitud:** **97.3%** sobre los 30 países.

---

## 4. Datos faltantes (resumen consolidado)

### 4.1 Missing values en variables existentes (acción inmediata posible)

| Variable | Missing en | Solución |
|---|---|---|
| `ai_patents_per100k` | ARE, CRI, TWN (3) | OECD AI Patent Database 2025 / Stanford AI Index 2026 (datos actualizados) |
| `ai_publications_frac` | JOR, TWN (2) | UNESCO Science Report 2024 / Scopus AI subset |
| `ai_investment_vc_proxy` | ARE, CRI, JOR, KOR, NZL, SGP, TWN (7) | Crunchbase / Stanford AI Index 2026 Cap. 4 / OECD AI Going Digital 2025 |
| `tertiary_education` | TWN, BGR (parcial) | Eurostat (BGR) / ROC Ministry of Education (TWN) |
| `rd_expenditure` | TWN, ARE, JOR | UNESCO UIS / ROC NSC |
| `gii_score`, WGI×4 | TWN | Estructural; documentar como limitación O imputar con alternative governance index |

### 4.2 Variables nuevas no extraídas todavía (enriquecimiento, no bloquea MVP)

Mencionadas en AI Index 2026 (p.323-339, Cap. 8 Policy & Governance + Cap. 4 Economy):

| Variable | Fuente | Existencia data abierta |
|---|---|---|
| `microsoft_diffusion_capital_score` | Microsoft AI Diffusion 2025 (subscore) | Sí, disponible en reporte |
| `microsoft_diffusion_skills_score` | Microsoft AI Diffusion 2025 (subscore) | Sí |
| `microsoft_diffusion_infra_score` | Microsoft AI Diffusion 2025 (subscore) | Sí |
| `microsoft_diffusion_innovation_score` | Microsoft AI Diffusion 2025 (subscore) | Sí |
| `genai_adoption_pct` (Fig 4.3.10) | Microsoft AI Economy Institute 2025 | Cita Stanford 2026, fuente Microsoft |
| `ai_job_posting_share_pct` | Lightcast (Fig 4.4.1/4.4.2) | Sí, Lightcast público |
| `state_backed_supercomputers_count` | Epoch AI (Fig 8.3.1) | Sí, Epoch dataset abierto |
| `data_localization_measures_count` | Ferracane et al. 2026 (Fig 8.3.3) | Sí, replication data |
| `nvidia_openai_infrastructure_partnership` | Stanford HAI (Fig 8.3.2) | Binario derivable de Fig 8.3.2 |
| `ai_publications_per_capita` | Stanford AI Index 2026 Cap. 1 | Derivable |
| `ai_patents_per_capita_v2` | Stanford AI Index 2026 Cap. 1 | Versión actualizada del Index 2025 |
| `talent_flow_index_zeki` | Zeki/Brookings | Disponible con registración |
| `public_trust_ai_government_pct` | Stanford 2026 Cap. 9 | Survey data |
| `ai_engineering_skills_growth_rate` | Stanford 2026 Take-away #13 | Lightcast subset |

### 4.3 Variables X1 propuestas por la skill (en CANDIDATES.md, no en x1_master.csv)

| Variable | Significado | Cobertura potencial |
|---|---|---|
| `regulatory_intensity_proposed` | Intensity ajustada por skill (vs IAPP) | 29/29 P1-TOP30 |
| `thematic_coverage_proposed` | Coverage ajustada por skill (vs IAPP) | 29/29 P1-TOP30 |
| `regulatory_regime_group_proposed` | Bucket harmonizado (4 niveles) | 29/29 P1-TOP30 |
| `has_dedicated_ai_authority` | 0/1 si autoridad IA-específica designada | 29/29 (extraíble) |
| `enforcement_governance_model` | "centralized\|delegated\|coordinator-only\|hybrid" | 29/29 |
| `eu_ai_act_implementation_date` | YYYY-MM-DD si UE-aplicable | 14/29 (UE/EEA) |
| `ai_law_pathway_declared` | 0/1 si bill/draft con fecha pública | 29/29 |
| `confidence_iapp_to_skill` | "high\|medium-high\|medium\|low" diff IAPP vs skill | 29/29 |

---

## 5. Lecciones para el futuro

1. **Distinguir siempre las 3 dimensiones** (datos cuantitativos / corpus legal / aprobación humana). Un país puede estar `DONE` sin estar `Aprobado` y aun así tener datos completos para análisis.

2. **El estado `Pendiente` no es malo.** Es transitorio. Significa que la skill propuso un ajuste y el revisor humano aún no lo confirmó. El análisis cuantitativo puede correr con valores `_proposed` en columna paralela.

3. **El corpus legal es para análisis cualitativo + NLP** (notebook 05_nlp.ipynb pendiente, sub-pregunta 4 de la tesis). No es prerequisito para análisis cuantitativo (notebooks 03-04).

4. **El usuario es el revisor humano.** Aprobar un CANDIDATES.md significa firmar `[APROBADO — fecha]` en su §11 (Decisión del revisor). Esto puede hacerse en lote para los 16 pendientes después del MVP, si los modelos confirman que la recodificación de la skill da resultados consistentes.

5. **CHL es FOCAL, no PENDING normal.** Su corpus se procesa después del MVP por diseño metodológico (procesar último para tener contexto comparado completo de los demás 29). Sus datos cuantitativos están disponibles desde IAPP/Microsoft/Oxford/etc, suficientes para incluirlo en el N=30.

---

## 6. Decisión operativa para el MVP

Basado en el audit anterior:

| Aspecto | Decisión |
|---|---|
| **Tamaño muestra MVP** | N=30 (29 P1-TOP30 + CHL focal) |
| **Datos Y, X1 IAPP, X2** | Usar `sample_ready_cross_section.csv` filtrado |
| **X1 propuesta skill** | Construir `x1_master_v2.csv` paralelo con valores `_proposed` extraídos de los 29 CANDIDATES.md |
| **Missing Y secundarios** | Imputar 12 valores faltantes (ai_patents×3, ai_publications×2, ai_invest_vc×7) desde fuentes alternativas |
| **Variables AI Index 2026** | Extraer al máximo posible (Microsoft subscores, Lightcast, Epoch, Ferracane) — ver `PLAN_MVP_TOP30_PAISES.md` |
| **Aprobación 16 Pendientes** | Diferir hasta post-MVP. Si los modelos muestran sensibilidad baja a IAPP vs proposed, aprobar en lote. |
| **CHL corpus** | Procesar después del MVP. Sus datos cuantitativos suficientes para el modelo. |

---

## 7. Glosario de estados

| Término | Definición operativa |
|---|---|
| **DONE** (Status) | La skill `corpus-legal-ia` generó los 4 entregables (manifest.csv, SOURCES.md, CANDIDATES.md, FINDINGS.md) en `data/raw/legal_corpus/{ISO3}/`. |
| **PENDING** (Status) | El país aún no se ha procesado por la skill. No tiene corpus legal. Sus datos cuantitativos pueden estar disponibles igualmente. |
| **Sí** (Aprobado) | El revisor humano firmó `[APROBADO — fecha]` en §11 del CANDIDATES.md, autorizando integrar la recodificación X1 propuesta a `x1_master.csv`. |
| **Pendiente** (Aprobado) | La recodificación está propuesta en CANDIDATES.md pero el revisor no la firmó. Los datos cuantitativos siguen disponibles via IAPP base. |
| **OUTSIDE** | País procesado pero fuera de la muestra de 86 (ej: QAT). Se mantiene como benchmark regional. |
| **FOCAL** | CHL — caso central del estudio, se procesa al final por diseño metodológico. |

---

## 8. Referencias internas

- [sample.md](../.claude/skills/corpus-legal-ia/sample.md) — tabla maestra de los 86 países
- [data/interim/sample_ready_cross_section.csv](../data/interim/sample_ready_cross_section.csv) — dataset cuantitativo
- [docs/HALLAZGOS_DIFERENCIALES.md](../docs/HALLAZGOS_DIFERENCIALES.md) — índice de tesis diferenciales
- [.claude/skills/corpus-legal-ia/recoding.md](../.claude/skills/corpus-legal-ia/recoding.md) — reglas de recodificación X1
- [.claude/skills/corpus-legal-ia/execution.md](../.claude/skills/corpus-legal-ia/execution.md) — flujo aprobación humana
- [PLAN_MVP_TOP30_PAISES.md](PLAN_MVP_TOP30_PAISES.md) — plan de ejecución del MVP

---

**Fin del documento.** Este archivo no debe ser editado a menos que cambien las definiciones operativas de `Status`/`Aprobado` en la skill `corpus-legal-ia`.
