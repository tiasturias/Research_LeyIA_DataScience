# Metodologia — Legal Origin (Tradicion Juridica) como Confounder Institucional

**Fecha:** 2026-04 (Tarea A sub-tarea A.3-bis)
**Fuente:** La Porta, Lopez-de-Silanes & Shleifer (2008). "The Economic Consequences of Legal Origins." *Journal of Economic Literature* 46(2), 285-332.
**Archivo raw:** `data/raw/LegalOrigin/legal_origin_coding.csv` (86 paises)
**Master:** `data/interim/x2_legal_origin_master.csv`

---

## 1. Justificacion

La tradicion juridica heredada (familia legal) es un predictor robusto y empiricamente validado de:

1. **Estilo regulatorio:** Paises civilistas (French/German) tienden a codificar exhaustivamente; common-law (English) prefiere regulacion por principios y jurisprudencia.
2. **Cultura de enforcement:** La intensidad de fiscalizacion regulatoria estatal difiere sistematicamente entre familias.
3. **Propension a legislar nuevas tecnologias:** La evidencia historica (finanzas, competencia, proteccion al consumidor, proteccion de datos) muestra que civil-law countries regulan mas rapidamente y con mayor formalidad.

**Sin controlar por legal_origin**, el coeficiente de `regulatory_intensity` en el modelo principal podria capturar "la propension ex ante a emitir regulacion formal" en vez del efecto causal de la regulacion IA sobre el ecosistema. Esto replica exactamente el mismo problema que WGI y GDPR-like law abordaron (confounder del estilo institucional pre-existente), pero desde un eje temporal mas profundo (siglos, no decadas).

**Fundamento teorico:** La Porta et al. (2008) documentan que la familia legal heredada explica ~20-40% de la variacion transpais en formalismo procedimental, intervencion estatal, y rigidez regulatoria, persistente sobre controles socioeconomicos.

---

## 2. Taxonomia: Las Cinco Familias Legales (La Porta 2008)

| Familia | Origen historico | Caracteristica regulatoria | N en muestra |
|---|---|---|---|
| **English** | Common law ingles, derecho jurisprudencial | Regulacion por principios, menor formalismo, mercados financieros profundos | 24 |
| **French** | Codigo Napoleonico (1804) | Civilismo intervencionista, regulacion codificada exhaustiva | 30 |
| **German** | BGB aleman (1900), ABGB austriaco | Civilismo con enfasis academico, regulacion tecnica sofisticada | 8 |
| **Scandinavian** | Tradicion juridica nordica | Civilismo pragmatico, regulacion minima pero efectiva | 5 |
| **Socialist** | Sistema sovietico + transicion | Centralismo heredado, en transicion a civil-law continental | 19 |
| **Total** | | | **86** |

---

## 3. Codificacion de los 86 Paises

### English (24)
ARE, AUS, BGD, BHR, BLZ, BRB, CAN, CYP, GBR, GHA, IND, IRL, ISR, KEN, LKA, MLT, MYS, NGA, NZL, PAK, SGP, UGA, USA, ZAF

### French (30)
ARG, BEL, BRA, CHL, CMR, COL, CRI, ECU, EGY, ESP, FRA, GRC, IDN, ITA, JOR, LBN, LUX, MAR, MEX, MUS, NLD, PAN, PER, PHL, PRT, SAU, SYC, TUN, TUR, URY

### German (8)
AUT, CHE, CHN, DEU, JPN, KOR, THA, TWN

### Scandinavian (5)
DNK, FIN, ISL, NOR, SWE

### Socialist (19)
ARM, BGR, BLR, CZE, EST, HRV, HUN, KAZ, LTU, LVA, MNG, POL, ROU, RUS, SRB, SVK, SVN, UKR, VNM

---

## 4. Casos Ambiguos y Criterios de Desambiguacion

La Porta et al. (2008) define la familia legal segun el **codigo comercial / civil de origen** (no segun el derecho de estatus personal ni el sistema politico actual). Aplicamos esta regla estrictamente:

| Pais | Criterio aplicado | Resultado |
|---|---|---|
| **CHN** | Codigo Civil chino recibido via Japon (tradicion alemana post-Meiji) | German |
| **VNM** | Sistema socialista contemporaneo con influencia civil-law francesa | Socialist |
| **SAU** | Codigo comercial derivado del Mejelle otomano (tradicion francesa); status personal bajo Sharia | French |
| **JOR** | Codigo civil egipcio Sanhuri (tradicion francesa); jurisdiccion comercial con influencia common-law britanica | French |
| **PHL** | Codigo civil espanol colonial (base francesa); fuerte influencia common-law de la era americana | French |
| **IDN** | Codigo civil holandes (tradicion francesa reformulada) | French |
| **ZAF** | Base Roman-Dutch mixta + common-law britanico; La Porta clasifica como English | English |
| **LKA** | Base Roman-Dutch + common-law britanico; codigo comercial English | English |
| **TUR** | Reforma 1926 recibe codigo suizo (familia francesa); Mejelle previa; La Porta: French | French |
| **MUS** | Bijural French/English; La Porta: French (codigo civil Napoleonico) | French |
| **CMR** | Bijural French/English (regiones anglofonas); La Porta: French | French |

**Criterio residual:** Para casos donde la clasificacion La Porta 2008 no es explicita, usamos el criterio CBR Leximetric (Cambridge Centre for Business Research): familia del **codigo comercial de origen**, no del codigo civil derivado.

---

## 5. Variables Derivadas

| Variable | Tipo | Definicion |
|---|---|---|
| `legal_origin` | categorical (5) | {English, French, German, Scandinavian, Socialist} |
| `is_common_law` | binary (0/1) | 1 si `legal_origin == "English"`, 0 en otro caso |

**Nota metodologica:** Para analisis OLS en `04_modelado`, se recomienda usar `legal_origin` como variable dummy con `French` como categoria base (grupo mas grande en la muestra). Alternativamente, `is_common_law` como indicador binario unico cuando el interes es el contraste common-law vs civil-law (mas parsimonioso y con potencia estadistica superior para N=72).

---

## 6. Validacion Empirica (N=72, muestra PRINCIPAL)

### 6.1 No redundancia con controles existentes

| Variable | Correlacion con `is_common_law` |
|---|---|
| `rule_of_law` | +0.10 |
| `regulatory_quality` | +0.11 |
| `gdp_per_capita_ppp` | +0.06 |
| `regulatory_intensity` | **-0.22** |

La correlacion con WGI es despreciable (r=0.10-0.11), confirmando que `legal_origin` captura una dimension **independiente** de la calidad institucional. La correlacion negativa con `regulatory_intensity` (-0.22) es el hallazgo esperado: paises common-law regulan IA con menor intensidad que civil-law.

### 6.2 Gradiente regulatorio por familia legal

Proporcion de paises con `regulatory_status_group = binding_regulation`:

| Familia | N | Binding | % Binding |
|---|---|---|---|
| English | 18 | 1 | **5.6%** |
| French | 26 | 8 | 30.8% |
| Socialist | 17 | 10 | 58.8% |
| German | 7 | 5 | **71.4%** |
| Scandinavian | 4 | 3 | **75.0%** |

**Gradiente de 13.3x entre English (5.6%) y Scandinavian (75%).** Este es el confounder mas potente de Tarea A — supera en magnitud a FH (gradiente ~3x), WGI (~2x), y GDPR-like (~2.5x).

### 6.3 AI readiness por familia legal

Media de `ai_readiness_score` (Oxford Insights):

| Familia | Media | N |
|---|---|---|
| Scandinavian | 72.34 | 4 |
| German | 71.72 | 7 |
| English | 62.82 | 18 |
| French | 58.27 | 26 |
| Socialist | 55.70 | 17 |

El diferencial se correlaciona con el nivel de desarrollo, pero el **control por PIB per capita no elimina el efecto de familia legal** en modelos OLS preliminares — confirmando valor como confounder independiente.

---

## 7. Integracion al Pipeline ETL

### Archivo raw
`data/raw/LegalOrigin/legal_origin_coding.csv`
**Columnas:** iso3, country_name, legal_origin, is_common_law, source_notes

### Funcion de build
`src/build_source_masters.py::build_legal_origin_master()`
**Output:** `data/interim/x2_legal_origin_master.csv` (86 filas)

### Integracion en sample_ready
`src/build_sample_ready.py`
- Nueva categoria: `X2_LEGAL_ORIGIN = ["legal_origin", "is_common_law"]`
- Nuevo tier: `complete_legal_tradition` = confounded_vars + X2_LEGAL_ORIGIN
- Cobertura: **72/86** (igual que confounded, sin reduccion de N)
- Tier en coverage_matrix: `X2_legal_origin`

### Requiere re-ejecucion
1. `python src/build_source_masters.py` (+ `build_legal_origin_master`)
2. `python src/build_sample_ready.py` (integra merge + tier)

---

## 8. Uso Recomendado en Modelamiento (Fase 4)

### Modelo principal (N=72)
OLS: `Y ~ X1 + X2_core` — **NO incluir legal_origin en este nivel** (mantiene parsimonia).

### Modelo confounded (N=72, recomendado post-auditoria)
OLS: `Y ~ X1 + X2_core + regulatory_quality + rule_of_law + gdpr_similarity_level`

### Modelo robustez — legal-tradition (N=72)
OLS: `Y ~ X1 + X2_core + WGI + GDPR + C(legal_origin)` con dummies
**Interpretacion:** Si el coeficiente de `regulatory_intensity` persiste tras controlar por legal_origin, hay evidencia de que el efecto de la regulacion IA es **independiente** de la tradicion juridica heredada.

### Modelo robustez — common-law binario (N=72)
OLS: `Y ~ X1 + X2_core + WGI + GDPR + is_common_law + is_common_law * regulatory_intensity`
**Interpretacion:** El termino de interaccion testea si el efecto de la intensidad regulatoria **difiere** entre common-law y civil-law. Hipotesis sustantiva plausible: la regulacion IA tiene mayor impacto negativo en ecosistemas civil-law (donde se complementa con regulacion pre-existente) que en common-law.

---

## 9. Limitaciones

1. **Tipologia agregada:** Las cinco familias ocultan heterogeneidad intra-familia (ej: Francia vs. Egipto son ambos French, pero su cultura regulatoria difiere). Justificado por potencia estadistica (N=72 no permite subdivisiones finas).
2. **Sistemas mixtos:** MUS, CMR, SYC, PHL, SAU tienen clasificacion ambigua; usamos el criterio del codigo comercial por consistencia con La Porta 2008.
3. **Temporal:** La clasificacion es estable desde 2008; no capta reformas recientes (ej: reforma del codigo civil chino 2020 podria argumentarse como drift desde German). Efecto esperado: marginal.
4. **No hay variable continua:** `legal_origin` es categorica; `is_common_law` simplifica a binario. El "grado" de formalismo regulatorio podria aproximarse mejor con el indice CBR Leximetric (no disponible para todos los 86 paises).

---

## 10. Referencias

1. **La Porta, R., Lopez-de-Silanes, F., & Shleifer, A. (2008).** The Economic Consequences of Legal Origins. *Journal of Economic Literature*, 46(2), 285-332.
2. **La Porta, R., Lopez-de-Silanes, F., Shleifer, A., & Vishny, R. (1998).** Law and Finance. *Journal of Political Economy*, 106(6), 1113-1155. — classificacion original de 4 familias.
3. **Djankov, S., La Porta, R., Lopez-de-Silanes, F., & Shleifer, A. (2003).** Courts. *Quarterly Journal of Economics*, 118(2), 453-517. — expansion de la taxonomia con Socialist.
4. **Armour, J., Deakin, S., Lele, P., & Siems, M. (2009).** How Do Legal Rules Evolve? Evidence from a Cross-Country Comparison of Shareholder, Creditor, and Worker Protection. *American Journal of Comparative Law*, 57(3), 579-630. — dataset CBR Leximetric para casos ambiguos.
5. **World Bank Doing Business** (descontinuado 2021) — uso historico de la taxonomia La Porta para clasificacion de 190 paises.

---

## 11. Historial

| Fecha | Accion |
|---|---|
| 2026-04-15 | Creacion inicial. Codificacion manual de 86 paises basada en La Porta 2008 y cross-check con CBR Leximetric para casos ambiguos. N=72 (complete_legal_tradition), sin reduccion de muestra vs confounded. |
