# AUT — Hallazgo Diferencial

## 1. Tesis del hallazgo diferencial

**Austria presenta el caso de "high ambition, delayed execution" en el bucket binding_regulation: posee la estrategia IA nacional más madura de la UE-27 (AIM AT 2030 con 82% de sus 91 medidas implementadas a 2026) y un Umsetzungsplan 2024 con 47 medidas activas de 12 ministerios, pero incumplió el plazo obligatorio del 2 de agosto de 2025 para la designación formal de autoridades competentes bajo el AI Act — un gap de implementación que la distingue de sus pares NLD y ESP (que sí cumplieron) y la alinea con BEL (mismo incumplimiento).**

---

## 2. Evidencia cuantitativa — densidad del corpus

| Métrica | Valor | Cálculo |
|---|---|---|
| # documentos totales | 4 | count(manifest.csv) |
| # binding (law + sectoral) | 1 | EU AI Act |
| # soft/policy/strategy | 3 | AIM AT 2030 + Umsetzungsplan + DSB guidelines |
| Páginas totales corpus | 332 | sum(pages) |
| Páginas binding / soft | 144 / 188 | 0.77:1 |
| Primer documento (fecha) | 2021 | AIM AT 2030 |
| Último documento (fecha) | 2024-11 | Umsetzungsplan 2024 |
| Años cubiertos | ~3.5 | (2024-11 - 2021) |
| Gap con fecha corpus | ~17 meses | 2026-04-21 - 2024-11 |
| # docs superseded | 0 | Ningún documento reemplazado |

---

## 3. Evidencia cuantitativa — timeline y proceso

| Fecha | Hito | Detalle |
|---|---|---|
| 2021 | AIM AT 2030 | Estrategia IA nacional federal. 91 medidas en 7 áreas. Coordinación Federal Chancellery + BMK. |
| 2024-07-12 | EU AI Act entry into force | Regulation (EU) 2024/1689 entra en vigor. Aplicación directa en Austria. |
| 2024 | DSB guidance DSGVO/KI-VO | Datenschutzbehörde publica guía sobre paralelismo RGPD + AI Act para sector público. |
| 2024-11 | Umsetzungsplan 2024 | Plan de implementación actualizado. 47 medidas de 12 ministerios federales. |
| 2025-02 | AI Act deadline | Fecha límite para designación de autoridades competentes (Art. 70). |
| 2025-08-02 | Plazo incumplido | Austria NO completó designación formal de autoridades AI Act. |
| 2026-04 | Estado del corpus | AIM AT 2030: 82% medidas implementadas o en implementación. |

**Duración:** ~3.5 años de evolución regulatoria.
**Emisor principal:** Federal Chancellery / BMK / Digital Austria / DSB.
**RTR GmbH:** Designado como AI Service Office (punto de contacto), sin competencias formales de vigilancia.

---

## 4. Datos que FORTALECEN la tesis

- **AIM AT 2030 con 82% implementación** — 82% de las 91 medidas implementadas o en implementación a 2026. Tasa de ejecución más alta entre los países del corpus analizados. Documentado en SOURCES.md.

- **91 medidas en 7 áreas** — más comprehensiva que la mayoría de estrategias nacionales UE: economía y trabajo, cualificación, ética y regulación, investigación e innovación, infraestructura de datos, administración pública, educación.

- **Umsetzungsplan 2024 con 47 medidas de 12 ministerios** — coordinación horizontal interministerial extensa. Evidencia de gobierno activo y no meramente aspiracional.

- **DSB activo con guidance específica** — Datenschutzbehörde publicó guía DSGVO/KI-VO en 2024 tanto para sector público como privado. Engagement activo del DPA.

- **EU AI Act directamente aplicable** — binding regulation sin transposición nacional necesaria. Austria sujeto a la regulación más estricta del mundo sobre IA.

- **Sin agencia IA dedicada** — Austria no tiene una agencia específica como AISI (UK) o BSI (Alemania). RTR funciona como contact point sin competencias plenas.

---

## 5. Datos que REFUTAN la tesis (stress test honesto)

- **Incumplimiento del plazo AI Act (02-08-2025)** — Austria no designó formalmente autoridades competentes. Mismo problema que BEL. *Refutador primario.* Sin embargo, el EU AI Act sigue siendo directamente aplicable aunque las autoridades no estén formalmente designadas.

- **RTR sin competencias plenas** — AI Service Office funciona como punto de contacto pero no tiene autoridad de vigilancia de mercado formalizada. *Refutador secundario.*

- **Alemania (DEU) tiene BSI y estructura más robusta** — comparación con vecino DEU (agencia dedicada, estrategia más antigua) podría mostrar que AUT está por debajo en institucionalidad.

- **NLD y ESP cumplieron el plazo** — España y Países Bajos designaron autoridades formales a tiempo. AUT quedó rezagado en ejecución institucional.

- **Sin ley IA nacional adicional** — Austria no tiene ley IA nacional propia; depende enteramente del EU AI Act. Esto es consistente con el bucket binding_regulation pero limita el "diferencial" a nivel nacional.

---

## 6. Comparación vs peer group

| País | Régimen | # docs | # binding | Tesis diferencial |
|---|---|---|---|---|
| NLD | binding_regulation | 5 | 1 | AI Act + estrategia madura + supervisión bien establecida (AP + RvIG) |
| ESP | binding_regulation | 5 | 1 | AI Act + AEPD activa + sandbox IA (RD 817/2023) |
| **AUT** | **binding_regulation** | **4** | **1** | **Estrategia más madura UE-27 (82% impl.) pero incumplimiento plazo AI Act** |
| BEL | binding_regulation | 5 | 1 | AI Act + estrategia + DPA activo; mismo incumplimiento de plazo que AUT |
| DEU | binding_regulation | 8 | 4 | BSI + estrategia + KIMIG en desarrollo; institucionalidad más robusta |

**Análisis:** AUT comparte el bucket binding_regulation con NLD, ESP, BEL, DEU. Se distingue por:
- Mayor madurez estratégica (82%) que BEL (estrategia menos desarrollada)
- Mismo incumplimiento de plazo que BEL
- Sin agencia IA dedicada (vs DEU con BSI, NLD con AP, ESP con AEPD)
- Menor # docs que DEU (4 vs 8)

---

## 7. Implicancias para el estudio

| Variable X1 | Efecto potencial |
|---|---|
| `has_ai_law` | 1 (EU AI Act directamente aplicable) |
| `regulatory_intensity` | 10/10 (sin cambio vs IAPP) |
| `thematic_coverage` | 14/15 (sin cambio) |
| `enforcement_level` | `medium-high` (matización: alta implementación estratégica pero incumplimiento de plazo institucional) |
| `regulatory_regime_group` | `binding_regulation` (confirmado) |

**Hipótesis testeable:**
- ¿Países con alta implementación estratégica pero delays institucionales (AUT, BEL) tienen outcomes distintos a países con institucionalidad robusta desde el inicio (NLD, ESP)?
- ¿El incumplimiento del plazo de designación de autoridades tiene efecto sobre la percepción de enforcement?

**Caso narrativo útil para:**
- §Discusión como "caso de high ambition, delayed execution" en binding_regulation
- Control para tesis "EU AI Act igual para todos" — implementación nacional varía
- Comparación con BEL (mismo problema) y NLD/ESP (ejecución exemplar)

---

## 8. Banderas de re-visita

| Evento | Horizonte | Trigger observable |
|---|---|---|
| Designación formal autoridades AI Act | 3-6m | Publicación en bgbl.gv.at o comunicado DSB/RTR |
| Actualización AIM AT 2030 | 6-12m | digitalaustria.gv.at nuevo documento |
| Nuevo guidance DSB sobre AI Act | 6m | dsb.gv.at publicación |
| Sanciones AI Act aplicadas | 12-24m | Decisiones DSB o RTR publicadas |
| Cambio de estrategia o plan | 12m | Nuevo documento en digitalaustria.gv.at |

---

## Links

- [CANDIDATES.md](CANDIDATES.md)
- [SOURCES.md](SOURCES.md)
- [manifest.csv](manifest.csv)