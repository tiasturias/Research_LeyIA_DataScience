# SWE — Hallazgo Diferencial

## 1. Tesis del hallazgo diferencial

**Suecia presenta el caso de "policy acceleration under binding regulation": el ciclo de política IA más ágil del corpus UE-27 — la AI Commission (creada en 2023) generó 75 propuestas en noviembre 2024, lo que derivó en la primera estrategia IA integral de Suecia en febrero 2026 (objetivo: top-10 global), todo en仅 14 meses — un proceso de política exhibe una velocidad y articulación notable que la distingue de sus pares AUT y BEL (con delays institucionales) y la alinea con NLD/ESP en términos de implementación robusta, aunque sin agencia IA dedicada.**

---

## 2. Evidencia cuantitativa — densidad del corpus

| Métrica | Valor | Cálculo |
|---|---|---|
| # documentos totales | 5 | count(manifest.csv) |
| # binding (law + sectoral) | 1 | EU AI Act |
| # soft/policy/strategy | 4 | AI Commission + Strategy + Action Plan + IMY |
| Páginas totales corpus | 322 | sum(pages) |
| Páginas binding / soft | 144 / 178 | 0.81:1 |
| Primer documento (fecha) | 2024 | IMY AI Strategy |
| Último documento (fecha) | 2026-02 | Sweden's AI Strategy + Action Plan |
| Años cubiertos | ~2 | (2026-02 - 2024) |
| Gap con fecha corpus | ~2 meses | 2026-04-21 - 2026-02 |
| # docs superseded | 0 | Ningún documento reemplazado |

---

## 3. Evidencia cuantitativa — timeline y proceso

| Fecha | Hito | Detalle |
|---|---|---|
| 2023 | AI Commission establecida | Órgano gubernamental ad hoc creado por el Gobierno de Suecia |
| 2024 | IMY AI Strategy | DPA sueco publica estrategia interna sobre IA + RGPD/AI Act |
| 2024-08 | Mandato Digg + IMY | Gobierno comisiona разработку riktlinjer (directrices) para IA generativa en administración pública |
| 2024-11-26 | AI Commission Roadmap / SOU 2025:12 | 75 propuestas presentadas al Gobierno. 136pp. |
| 2025-02 | AI Act deadline | Fecha límite para designación de autoridades competentes (Art. 70) |
| 2026-02 | Sweden's AI Strategy | Primera estrategia IA integral. Objetivo: top-10 global. 3 áreas: societal, sostenible, competitividad. |
| 2026-02 | Action Plan | Plan de acción con medidas concretas, plazos y responsables |
| 2026-04 | Estado del corpus | Implementación inicial del Action Plan en curso |

**Duración del ciclo de política:** ~14 meses (nov 2024 → feb 2026)
**Velocidad:** Proceso de política más rápido del corpus UE-27
**Emisor principal:** Government of Sweden / AI Commission / IMY

---

## 4. Datos que FORTALECEN la tesis

- **AI Commission con 75 propuestas formalizadas (SOU 2025:12)** — documento de 136pp con roadmap concreto. Citado: "Sweden is falling behind in AI development. This is alarming and requires the Government to take a number of urgent steps to avoid Sweden being left behind."

- **Sweden's AI Strategy (feb 2026): primera estrategia integral** —citado: "For the first time ever, Sweden has a holistic AI strategy. The strategy aims for Sweden to be among the world's top ten countries in the field of artificial intelligence."

- **Action Plan con asignaciones presupuestarias** — Vinnova (innovación), NAISS (compute), Digg+IMY (guidelines), Swedish Research Council (investigación). Medidas concretas con plazos y responsables.

- **Objetivo explícito top-10 global** — Ambición alta respaldada por propuesta €1.5B inversión adicional.

- **IMY (DPA) activo** — Estrategia interna IA (2024) con tres áreas prioritarias: salud, trabajo, niños. Historial riguroso de enforcement RGPD (tradición nórdica).

- **Proceso de política articulado** — AI Commission → 75 propuestas → Estrategia + Action Plan. Ciclo completo en 14 meses.

---

## 5. Datos que REFUTAN la tesis (stress test honesto)

- **Sin agencia IA dedicada** — Suecia no tiene una agencia específica como AESIA (España). IMY + Digg distribuyen competencias. *Refutador primario.*

- **Estrategia muy reciente (feb 2026)** — Publicada solo 2 meses antes del cierre del corpus. Efectividad por verificar. *Refutador secundario.* La estrategia es ambicioso pero no probada.

- **Digg riktlinjer IA generativa pendiente** — Mandato recibido ago 2024, publicación final pendiente. Guía para sector público no disponible aún.

- **AUT y BEL también incumplieron plazo** — La tesis de "agilidad" se refiere solo al proceso de política nacional post-2024, no al cumplimiento del deadline AI Act.

- **NLD y ESP tienen institucionalidad más establecida** — Países Bajos con AP + RvIG, España con AESIA + sandbox. SWE está en proceso de construcción institucional.

---

## 6. Comparación vs peer group

| País | Régimen | # docs | # binding | Tesis diferencial |
|---|---|---|---|---|
| NLD | binding_regulation | 5 | 1 | AI Act + supervisión establecida + GenAI Vision 2024 |
| ESP | binding_regulation | 5 | 1 | AI Act + AESIA activa + sandbox IA (RD 817/2023) |
| **SWE** | **binding_regulation** | **5** | **1** | **Ciclo de política más ágil UE (14 meses: Commission → estrategia integral)** |
| AUT | binding_regulation | 4 | 1 | Estrategia madura (82% impl.) pero incumplimiento plazo AI Act |
| BEL | binding_regulation | 5 | 1 | Sin agencia dedicada + estructura federal compleja |

**Análisis:** SWE comparte bucket binding_regulation con NLD, ESP, AUT, BEL. Se distingue por:
- Ciclo de política más rápido (14 meses)
- Estrategia más reciente (feb 2026) vs AUT/BEL (estrategias más antiguas)
- Sin agencia dedicada (como AUT/BEL)
- Enforcement level high confirmado (como NLD/ESP)

**Contraste:** SWE ≈ NLD/ESP en velocidad de implementación, pero sin agencia dedicada como AUT/BEL.

---

## 7. Implicancias para el estudio

| Variable X1 | Efecto potencial |
|---|---|
| `has_ai_law` | 1 (EU AI Act directamente aplicable) |
| `regulatory_intensity` | 10/10 (sin cambio vs IAPP) |
| `thematic_coverage` | 14/15 (sin cambio) |
| `enforcement_level` | `high` (confirmado — IAPP correcto) |
| `regulatory_regime_group` | `binding_regulation` (confirmado) |
| `has_dedicated_ai_authority` | 0 (IMY + Digg, no agencia dedicada) |

**Hipótesis testeable:**
- ¿Países con ciclos de política más rápidos (SWE) tienen mejores outcomes que países con delays (AUT, BEL)?
- ¿La ausencia de agencia IA dedicada tiene efecto negative sobre implementación?

**Caso narrativo útil para:**
- §Discusión como "caso de policy acceleration under binding regulation"
- Control para tesis "EU AI Act igual para todos" — velocidad de implementación nacional varía
- Comparación con AUT/BEL (mismo bucket, diferente velocidad)

---

## 8. Banderas de re-visita

| Evento | Horizonte | Trigger observable |
|---|---|---|
| Publicación Digg riktlinjer IA generativa | 3-6m | digg.se nuevo documento |
| Efectividad Action Plan | 6-12m | Evaluación interim del Gobierno |
| Designación formal autoridades AI Act | 3-6m | Publicación en svenskforfattningssamling.se |
| NAISS compute infrastructure operativo | 12-18m | Anuncio Vinnova o Gobierno |
| Ranking IA global 2026 | 12m | Stanford AI Index / Microsoft Diffusion 2026 |

---

## Links

- [CANDIDATES.md](CANDIDATES.md)
- [SOURCES.md](SOURCES.md)
- [manifest.csv](manifest.csv)