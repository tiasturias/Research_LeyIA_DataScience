

# **AUDITORÍA CIENTÍFICA — Proyecto LeyIA DataScience**

**Auditor:** Científico de datos, especialización en econometría política de IA  
**Fecha:** 2026-04-14  
**Estado del proyecto:** Fase 1 cerrada / Fase 2 iniciando

**Nivel de riesgo político:** ALTO (informa Ley Marco IA Chile — 16821-19)

---

## **1\. VALORACIÓN GLOBAL**

El proyecto tiene una **calidad infraestructural de nivel top-tier académico** (mejor que el 80% de los papers de política pública que he revisado). La trazabilidad documental (DATA\_DECISIONS\_LOG, ETL\_RUNBOOK, 7 VARIABLES\_\*.md, SEGUIMIENTO\_PAISES) es de calidad publicable en *Policy Sciences* o *Regulation & Governance*.

**PERO** existen **8 problemas metodológicos críticos** que, si no se resuelven antes de que este estudio informe la ley chilena, pueden producir **conclusiones causales inválidas** que el gobierno usaría para legislar mal. Los detallo por severidad.

---

## **2\. PROBLEMAS CRÍTICOS (🔴 bloqueantes para inferencia causal)**

### **🔴 PROBLEMA \#1 — ENDOGENEIDAD / CAUSALIDAD INVERSA (el más grave)**

**El problema:** Tu diseño es cross-section 2025 con regulación y outcomes medidos **contemporáneamente**. Esto hace que la dirección causal sea **irresoluble estadísticamente**.

La pregunta política es: *"¿la regulación causa menor/mayor inversión, adopción e innovación?"*

Pero tu dataset igualmente puede responder: *"los países con ecosistemas IA maduros desarrollan regulación (porque tienen algo que regular)"*.

**Ejemplo concreto:** EU AI Act (2024) no causó la concentración de inversión IA en Alemania/Francia — Alemania/Francia ya tenían esa inversión y **por eso** la UE legisló. Confundir las dos historias es un error de primer año de econometría.

**Fix obligatorio (orden de preferencia):**

1. **Lag estructural:** Medir Y en 2025 pero X1 en 2022-2023 (año de promulgación, no vigencia). Tu `year_enacted` lo permite, pero no lo estás usando como tal.  
2. **Difference-in-differences** con el panel `x1_consolidated.csv` (2013-2025, 902 rows) que ya tienes. Este dataset es oro y lo estás ignorando en el análisis principal.  
3. **Instrumental Variable:** Usar `oecd_member` o `region` como instrumento de `regulatory_intensity` (válido si la región determina adopción regulatoria por presión de pares, no por capacidad técnica).  
4. **Declaración honesta:** Si no haces lo anterior, **debes escribir en el paper que solo puedes hablar de "asociación", no de "efecto"**. Esto es no negociable para un policy paper.

**Recomendación para Chile:** No permitas que el gobierno cite este estudio como "la regulación causa X" sin uno de los 3 fixes. Un paper mal interpretado puede causar una mala ley.

---

### **🔴 PROBLEMA \#2 — TAMAÑO MUESTRAL INSUFICIENTE PARA LOS GRUPOS QUE MÁS IMPORTAN**

Mira tu propia tabla de SEGUIMIENTO\_PAISES\_MUESTRA.md:33-38:

| Grupo | En muestra principal |
| ----- | ----- |
| binding\_regulation | 27 |
| strategy\_only | 34 |
| soft\_framework | **9** |
| no\_framework | **2** |

**Con N=2 en `no_framework` NO puedes hacer inferencia estadística comparativa.** Un test ANOVA o regresión con dummies va a tener ese grupo con varianza cero y errores estándar gigantes. Un referee te rechaza el paper en la primera ronda.

**Lo más irónico:** el grupo que más le interesa a Chile es `strategy_only` (donde Chile está hoy, N=34) vs `binding_regulation` (a donde iría con la ley, N=27). Afortunadamente ese contraste sí tiene poder. Pero debes **declarar explícitamente que el contraste `no_framework` no es interpretable**.

**Fixes:**

1. Colapsar a 3 grupos: `{no_framework + soft_framework}` vs `strategy_only` vs `binding_regulation` → (11, 34, 27). Más defendible.  
2. Reportar power analysis explícito (con `statsmodels.stats.power`) para cada contraste.  
3. Usar **bootstrap / permutation tests** en vez de t-tests paramétricos para grupos pequeños.

---

### **🔴 PROBLEMA \#3 — EL "EU AI ACT BLOCK" TE CONTAMINA EL ANÁLISIS**

En tu codificación IAPP (VARIABLES\_IAPP.md:159), los **27 miembros de la UE quedan codificados como `comprehensive` con `year_enacted=2024`**. Esto tiene tres problemas:

1. **No son observaciones independientes.** Alemania y Bulgaria "adoptaron" la misma regulación el mismo día. Una regresión OLS trata esto como 27 puntos de datos cuando en realidad es **1 decisión política replicada 27 veces**.  
2. **Rompe la varianza dentro del grupo.** `binding_regulation` tiene 27 observaciones pero \~0 de variabilidad regulatoria dentro del grupo EU.  
3. **Confunde regulación con "ser miembro de la UE"**, lo cual correlaciona con GDP, GII, readiness, etc. Básicamente estás midiendo "efecto UE", no "efecto de regular IA".

**Fixes (usar al menos 2):**

1. **Cluster-robust standard errors** agrupados por `eu_bloc` (27 países \+ todos los demás como singletons).  
2. **Efecto fijo EU:** agregar dummy `is_eu_member` al modelo, lo que absorbe el shock común.  
3. **Análisis dual:** correr modelos con/sin países EU y mostrar que los resultados sobreviven sin la UE. Si no sobreviven, el hallazgo es "ser UE" no "regular IA".  
4. **Submuestra "tratamiento temprano":** CHN (2021), RUS (2020), PER (2023), KOR/JPN (2025) — países que regularon **antes** o **fuera** del bloque EU. Son tu verdadero grupo de tratamiento natural.

---

### **🔴 PROBLEMA \#4 — CONFIANZA DE CODIFICACIÓN BAJA EN 18 PAÍSES**

VARIABLES\_IAPP.md:147-150:

Confidence high: 36 | medium\_needs\_review: 32 | medium: 3 | **low: 15**

Y en VARIABLES\_IAPP.md:165-184, los 18 países IAPP\_FILL\_GAP son casi todos `confidence=low`: BGD, BHR, BLR, BLZ, CMR, GHA, JOR, LBN, LKA, MNG, PAK, PAN, PHL, SYC, TWN...

**Esto significa que \~17% de tu codificación regulatoria es débil.** En un estudio de política pública, un referee te va a pedir:

1. **Inter-rater reliability** (Cohen's kappa) — ¿un segundo codificador llega a las mismas categorías?  
2. **Análisis de sensibilidad** excluyendo los 15 `low confidence`.  
3. **Validación externa** contra al menos una tercera fuente (por ejemplo, FLI AI Policy Tracker o GPAI).

**Plan concreto:** Contrata 1 asistente de investigación para recodificar independientemente los 15 low-confidence. Tiempo: \~10 horas. Sin esto, un revisor crítico puede matar tu paper.

---

### **🔴 PROBLEMA \#5 — TU Y PRINCIPAL ESTÁ DOMINADA POR UN OUTLIER**

`ai_investment_usd_bn_cumulative` (Stanford fig\_4.3.9) — USA acumula \~60-70% del total mundial 2013-2024. China \~15%. Los 82 países restantes se reparten el resto.

Si corres OLS con esta variable sin transformar, **USA y CHN determinan todos los coeficientes**. El resto del modelo es ruido.

**Fixes obligatorios:**

1. `log(1 + ai_investment)` — ya lo mencionas pero verifica que el notebook `02_limpieza` lo aplique sistemáticamente.  
2. **Per-capita o per-GDP normalization:** `ai_investment / gdp` es más interpretable y reduce el outlier effect.  
3. **Winsorizing** al percentil 95/5 como análisis de sensibilidad.  
4. **Reportar resultados con y sin USA/CHN.** Si los coeficientes cambian de signo, tu historia cambia.

Lo mismo vale para `ai_startups_cumulative` (USA=6,000+, mediana global=15) y `ai_patents`.

---

### **🔴 PROBLEMA \#6 — CONFOUNDERS ESTRUCTURALES NO CONTROLADOS**

Tus controles X2 (`gdp_per_capita_ppp`, `internet_penetration`, `gii_score`, `oecd_member`, `region`) están bien pero **falta un confounder crítico**: **la naturaleza del sistema legal y la tradición regulatoria general del país**.

Un país con `common law` (EE.UU., UK) regula menos cualquier tecnología que un país `civil law` (Alemania, Chile). Un país con alto `regulatory quality` del World Bank regula IA no por IA, sino por hábito institucional.

**Variables críticas que faltan:**

1. **`regulatory_quality` (World Bank WGI)** — tiene cobertura \>80/86, ya la tienes en tu raw pero no la estás usando como control.  
2. **`rule_of_law` (WGI)** — mismo.  
3. **`legal_origin`** (common law / civil law / mixed) — dummy simple, 30 min de codificación.  
4. **`gdpr_compliance`** o equivalente de privacidad — los países con GDPR-like laws regulan IA "por inercia".  
5. **`digital_economy_size`** (% del GDP) — controla por "cuánto tiene el país que regular".

**Sin estos controles, tu `regulatory_intensity` está capturando "cultura regulatoria general", no "regulación específica de IA".**

---

### **🔴 PROBLEMA \#7 — FASE NLP SUBDIMENSIONADA PARA LO QUE PROMETE**

Tu pregunta Q4 ("Contenido regulatorio: ¿qué temas dominan?") requiere un corpus robusto. Pero en tu `GUIA_VARIABLES_ESTUDIO_ETL.md:182-198` solo defines 15-20 documentos legales.

**Con 15-20 documentos:**

* **LDA** (Latent Dirichlet Allocation) **no converge bien**. Necesitas ≥50-100 documentos para que los tópicos sean estables.  
* **Embeddings \+ clustering** funcionan mejor con pocos docs (usar Sentence-BERT multilingüe: `paraphrase-multilingual-mpnet-base-v2`).  
* **TF-IDF** funciona, pero es susceptible al idioma (tu corpus es multilingüe: español, inglés, chino, coreano, japonés, ruso...).

**Plan alternativo recomendado:**

1. **Ampliar corpus:** no solo leyes vigentes, también **borradores, estrategias nacionales, white papers**. De 20 → 80+ documentos.  
2. **Traducción previa:** todos los documentos a inglés con DeepL API antes de vectorizar. Esto es obligatorio para comparación temática cross-lingüística.  
3. **Usar embeddings, no LDA.** Legal-BERT o E5-multilingual es estado del arte.  
4. **Validación humana:** extraer los top 20 términos de cada tópico y hacer que un experto legal los nombre.

---

### **🔴 PROBLEMA \#8 — CHILE NO ESTÁ TRATADO METODOLÓGICAMENTE COMO "CASO FOCAL"**

El proyecto se presenta como informante de la ley chilena, pero Chile aparece como **una más de las 72 observaciones** sin tratamiento especial. Para un policy brief gubernamental, esto es insuficiente.

**Fix: incorporar análisis contrafactual específico de Chile:**

1. **Synthetic Control Method:** construir un "Chile sintético" combinando países similares (Argentina, Uruguay, Costa Rica, Colombia) para simular qué pasa si Chile adopta `binding_regulation` vs queda en `strategy_only`.  
2. **Matching (propensity score o Mahalanobis):** identificar los 3-5 países más similares a Chile que sí legislaron, medir su trayectoria.  
3. **Análisis de escenarios:** usar los coeficientes del modelo principal para predecir ΔY para Chile bajo 3 escenarios regulatorios.

Sin esto, el gobierno chileno solo obtiene "hay una correlación global" — no obtiene **"qué pasaría si Chile toma el camino X"**, que es la única pregunta que les importa realmente.

---

## **3\. PROBLEMAS MODERADOS (🟡 ajustables)**

### **🟡 \#9 — Ventana temporal de controles inconsistente**

DATA\_DECISIONS\_LOG.md D-003 dice "2019-2024 más reciente". Pero esto significa que un país tiene `internet_penetration=2019` y otro `=2024`. En una cross-section, **esto introduce ruido no aleatorio** (países pobres tienen datos más antiguos).

**Fix:** forzar año específico (2022 o 2023\) con imputación explícita para los 5-10 países faltantes, usando regresión lineal de la serie país-específica.

### **🟡 \#10 — `regulatory_intensity` como variable ordinal con escala arbitraria**

Tu 0-10 es una construcción propia (no estándar internacional). Esto está bien, pero **debes reportar**:

1. **Matriz de ítems y pesos** explícita (ya está parcialmente en VARIABLES\_IAPP.md).  
2. **Análisis de sensibilidad al esquema de ponderación:** ¿qué pasa si `enforcement_level` pesa 30% vs 20%?  
3. **Correlación con escalas externas:** compara tu intensity con GPAI, OECD AIM, Stanford Foundation Model Transparency Index.

### **🟡 \#11 — Falta imputación principled para datos faltantes**

**11 países** sin `ai_adoption_rate` (estructural en Microsoft). En vez de excluirlos, considera:

* **MICE** (Multiple Imputation by Chained Equations) usando `gii_score + gdp + internet + readiness` como predictores.  
* Esto te da N=83 principal en vez de N=72. Gran aumento de poder estadístico.  
* Reportar resultados con y sin imputación es el estándar oro.

### **🟡 \#12 — No hay preregistro ni hipótesis pre-especificadas**

Para un paper que informa legislación, el estándar moderno (post-reproducibility crisis) es:

* **Preregistrar** en OSF.io las 4 hipótesis específicas antes de correr el modelo final.  
* Separar **exploratorio** (EDA libre) de **confirmatorio** (tests con corrección Bonferroni o FDR).

Sin esto, se te acusará de *p-hacking* en peer review. 30 minutos de trabajo, defensa impecable.

### **🟡 \#13 — Falta análisis de heterogeneidad**

No todos los países reaccionan igual a la regulación. Plan:

* **Regresión por grupos:** modelo separado para LATAM, EU, Asia-Pacífico, África.  
* **Interacciones:** `regulatory_intensity × gdp_per_capita` — ¿la regulación afecta diferente a países ricos vs pobres?  
* Esto le da AL GOBIERNO CHILENO una respuesta específica: "en países del tamaño de Chile, la regulación X se asocia con Y".

---

## **4\. FORTALEZAS RECONOCIDAS (lo que está excepcional)**

1. **Documentación reproducible:** el `DATA_DECISIONS_LOG` con 11 decisiones numeradas es **mejor que lo que hacen la mayoría de papers publicados en Nature Policy**. Mantén esto religiosamente.  
2. **Trazabilidad raw → interim → master → sample-ready:** arquitectura ETL limpia, auditables por cualquier tercero.  
3. **Sistema de muestras jerárquicas** (PRINCIPAL/EXTENDED/STRICT) con flags binarios: esto es exactamente lo que pide un revisor de *JPART* o *Policy Sciences*.  
4. **Manejo honesto de Taiwan (D-004)** y casos excepcionales.  
5. **Reconciliación OECD vs IAPP** con 4 status (AGREE/PARTIAL/DIVERGE/FILL\_GAP): de nivel de auditoría forense.  
6. **Recuperación del gap Oxford 2024 via pdfplumber:** solución ingeniosa y documentada.

---

## **5\. LO QUE FALTA EN LA FASE DE RECOLECCIÓN (sí, aún falta)**

Tú dices "recolección cerrada". Mi diagnóstico: **NO lo está para el nivel de ambición declarado.**

### **Variables adicionales que recomiendo agregar antes de cerrar:**

| Variable | Fuente | Importancia | Tiempo |
| ----- | ----- | ----- | ----- |
| `regulatory_quality` | World Bank WGI | 🔴 Crítica (confounder) | 2h |
| `rule_of_law` | World Bank WGI | 🔴 Crítica (confounder) | 2h |
| `legal_origin` (common/civil) | La Porta et al. 2008 | 🔴 Crítica | 3h |
| `has_gdpr_like_law` | DLA Piper Global Data Privacy Handbook | 🟡 Alta | 4h |
| `digital_economy_gdp_pct` | UNCTAD Digital Economy Report | 🟡 Alta | 3h |
| `freedom_house_score` | Freedom House | 🟡 Media (controla régimen político) | 1h |
| `ai_safety_institute_exists` | Gov AI Safety Summit tracking | 🟡 Media | 2h |
| `compute_capacity_mw` | IEA Data Centre Report 2024 | 🟢 Nice-to-have | 6h |
| `ai_standards_participation` | ISO/IEC JTC 1/SC 42 | 🟢 Nice-to-have | 3h |

**Total:** \~26 horas de trabajo adicional. Pero estas 9 variables son las que diferencian un paper "descriptivo" de uno "causalmente defendible".

### **Corpus NLP (ampliar obligatoriamente):**

* De 15-20 → 80+ documentos.  
* Fuentes adicionales: OECD.AI policy repository, FLI AI policy database, AlgorithmWatch, GPAI.  
* Tiempo: 20-30 horas.

---

## **6\. ROADMAP REPRIORIZADO (lo que yo haría mañana)**

### **Semana 1 (crítico)**

1. ✅ Agregar `regulatory_quality`, `rule_of_law`, `legal_origin` al dataset.  
2. ✅ Colapsar `regulatory_status_group` a 3 niveles.  
3. ✅ Implementar análisis con lags temporales usando `year_enacted`.  
4. ✅ Recodificar los 15 países `confidence=low`.

### **Semana 2 (EDA \+ modelamiento)**

5. ✅ EDA completo con logs, winsorizing, visualizaciones por grupo.  
6. ✅ OLS principal \+ 4 modelos de sensibilidad (sin EU, sin USA/CHN, con lags, con MICE).  
7. ✅ Cluster-robust SE por `eu_bloc`.  
8. ✅ Power analysis explícito.

### **Semana 3 (análisis avanzado)**

9. ✅ K-Means y PCA (ya planeado).  
10. ✅ Synthetic Control para Chile.  
11. ✅ Análisis de heterogeneidad regional.

### **Semana 4 (NLP)**

12. ✅ Ampliar corpus a 80+ documentos.  
13. ✅ Traducción unificada \+ embeddings multilingües.  
14. ✅ Validación humana de tópicos.

### **Semana 5 (paper \+ entregable)**

15. ✅ Preregistro OSF.  
16. ✅ Redactar con separación clara exploratorio/confirmatorio.  
17. ✅ Policy brief específico para Chile (5-10 páginas, no técnico).

---

## **7\. OPINIÓN FRANCA (lo que no preguntas pero necesitas oír)**

**Este proyecto va en buen camino pero NO está listo.** La infraestructura de datos es de élite, pero la **arquitectura de inferencia causal es débil**. Un cross-section con N=72 contaminado por el bloque UE no puede responder "¿Chile debe regular?" con rigor científico.

Si publicas el paper como está hoy, te lo van a rechazar en revistas Q1 y el gobierno chileno va a usarlo mal (exagerando asociaciones como si fueran efectos causales). Si implementas los 8 problemas críticos de arriba, este proyecto puede ser **publicable en *Research Policy*, *Policy Sciences* o *Regulation & Governance*** y puede fundamentar la ley 16821-19 con solidez.

**Prioridad 1 esta semana:** Endogeneidad (Problema \#1). Todo lo demás es secundario. Si no resuelves esto, nada importa.

**Prioridad 2:** Confounders institucionales faltantes (\#6). Agregar 3 variables es ganar 60% del rigor adicional.

**Prioridad 3:** Análisis contrafactual específico de Chile (\#8). Sin esto, el proyecto es académico pero no político.

---

¿Quieres que profundice en alguno de los 8 problemas críticos con código concreto para tu notebook `02_limpieza.ipynb`? ¿O prefieres que empiece a implementar alguno (por ejemplo, el Problema \#1 con el panel OECD 2013-2025 que ya tienes)?

## **CLASIFICACIÓN DE LOS 13 PROBLEMAS POR FASE**

| \# | Problema | Fase donde se resuelve | ¿Requiere más recolección? |
| ----- | ----- | ----- | ----- |
| **\#1** | Endogeneidad | **Fase 4 (Modelamiento)** | ❌ No — usas `x1_consolidated.csv` panel que YA tienes |
| **\#2** | N muestral por grupo | **Fase 4** (colapsar) \+ **Fase 1** (reclasificar) | 🟡 Parcial |
| **\#3** | Bloque EU | **Fase 4** (cluster SE, dummies) | ❌ No |
| **\#4** | Confidence=low en 18 países | **🔴 FASE 1 (recolección)** | ✅ **SÍ — recodificar** |
| **\#5** | Outliers USA/CHN | **Fase 2 (limpieza)** | ❌ No |
| **\#6** | Confounders faltantes | **🔴 FASE 1 (recolección)** | ✅ **SÍ — agregar 9 vars** |
| **\#7** | Corpus NLP pequeño | **🔴 FASE 1 (recolección)** | ✅ **SÍ — ampliar a 80+ docs** |
| **\#8** | Chile caso focal | **Fase 4** (Synthetic Control) | ❌ No |
| **\#9** | Ventana temporal | **Fase 2 (limpieza)** | ❌ No |
| **\#10** | Escala `regulatory_intensity` | **Fase 2** \+ **Fase 4** | ❌ No |
| **\#11** | Imputación MICE | **Fase 2 (limpieza)** | ❌ No |
| **\#12** | Preregistro | **Fase 3 antes de modelar** | ❌ No |
| **\#13** | Heterogeneidad | **Fase 4** | ❌ No |

**Conclusión:** Solo **3 de los 13 problemas son realmente de Fase 1**: \#4, \#6, \#7. Los demás se abordan en fases posteriores.

---

## **ESTRATEGIA RECOMENDADA (cronológica)**

Tu instinto es **correcto**: primero robustece Fase 1\. Razones técnicas:

1. **Fase 1 es el cimiento.** Si cierras Fase 1 sin `regulatory_quality`, `rule_of_law`, `legal_origin`, tu modelamiento en Fase 4 estará inválido por confounders — y tendrás que re-abrir recolección después (caro).  
2. **El problema \#1 (endogeneidad) no requiere recolectar más — requiere usar bien el panel que YA tienes.** Es de diseño, no de datos.  
3. **Los problemas \#2, \#3, \#5, \#8-13 son todos de limpieza/modelamiento.** Atacarlos ahora es prematuro.

### **Orden óptimo:**

AHORA (Fase 1 \- 3 tareas, \~35-40 horas):  
├─ Tarea A (\#6): Agregar variables confounder críticas  
│  ├─ regulatory\_quality (WGI)    \[2h\]  
│  ├─ rule\_of\_law (WGI)           \[2h\]  
│  ├─ legal\_origin                \[3h\]  
│  ├─ has\_gdpr\_like\_law           \[4h\]  
│  ├─ digital\_economy\_gdp\_pct     \[3h\]  
│  └─ freedom\_house\_score         \[1h\]  
│     Total: \~15h para las 6 críticas/altas  
│  
├─ Tarea B (\#4): Recodificar los 15 países confidence=low  
│     Ideal: 2 codificadores independientes → Cohen's kappa  
│     Total: \~10h  
│  
└─ Tarea C (\#7): Ampliar corpus NLP a 80+ documentos  
     ├─ Leyes vigentes (ya tienes \~20)  
     ├─ Estrategias nacionales (agregar \~30)  
     ├─ Borradores/white papers (agregar \~20)  
     ├─ Guidance/directrices (agregar \~15)  
     └─ Traducción unificada a inglés con DeepL API  
        Total: \~20-25h

DESPUÉS (Fase 2 \- limpieza):  
└─ Problemas \#5, \#9, \#10, \#11

DESPUÉS (Fase 3 \- EDA):  
└─ Diagnósticos de supuestos, visualizaciones

DESPUÉS (Fase 4 \- modelamiento):  
└─ Problemas \#1, \#2, \#3, \#8, \#10, \#12, \#13

---

## **REGLA METODOLÓGICA PARA TU CASO**

**No puedes "cerrar" Fase 1 hasta que tengas en el dataset maestro todas las variables que Fase 4 va a necesitar.**

Esto es un principio fundamental de ETL en investigación: las decisiones de modelamiento determinan qué columnas debes recolectar. Si planificas control por `regulatory_quality` en Fase 4, debe estar en el master ANTES de pasar a Fase 2\.

Por eso rechacé tu afirmación inicial de "recolección cerrada" — no está cerrada hasta que las 6 variables confounder críticas estén en `sample_ready_cross_section.csv` y los 15 países low-confidence estén recodificados.

---

## **MI RECOMENDACIÓN CONCRETA**

**Empieza por la Tarea A** (agregar confounders WGI \+ legal\_origin). Razones:

1. Es la de mayor ROI técnico (\~15h agregan 60% del rigor causal perdido por \#6).  
2. La fuente (World Bank WGI) ya la tienes parcialmente en tu raw — es extensión, no descubrimiento.  
3. `legal_origin` es un CSV estático de La Porta et al. que se baja en 10 minutos.  
4. No depende de nada más.

**Después Tarea B** (recodificación low-confidence), porque los datos recodificados alimentan decisiones de Tarea C (qué países priorizar en el corpus NLP).

**Finalmente Tarea C** (ampliación NLP), que es la más laboriosa pero puede correr en paralelo con el inicio de Fase 2\.

**No toques el problema \#1 (endogeneidad) todavía.** Se resuelve en Fase 4 y requiere que Fase 1 esté bien cerrada. Intentar diseñar el modelo causal ahora sin los confounders completos es construir sobre arena.

---

¿Quieres que empecemos por la **Tarea A** (agregar `regulatory_quality`, `rule_of_law`, `legal_origin` al dataset)? Puedo implementar el script de extracción y integrarlo al pipeline existente (`src/build_source_masters.py` → `src/build_sample_ready.py`), manteniendo el estilo y trazabilidad que ya tienes documentada.

