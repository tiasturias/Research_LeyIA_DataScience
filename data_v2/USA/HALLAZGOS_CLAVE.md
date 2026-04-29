# United States (USA) — Perfil de Datos Consolidado

**Fecha:** 2026-04-28  
**Atributos extraídos:** 189  
**Cobertura:** 189/189 (100%)

---

## 1. Identificación

| Atributo | Valor |
|----------|-------|
| ISO3 | USA |
| País | United States |
| Región | North America |
| Grupo de ingreso | HI |
| Población | 340,110,988 |
| PIB PPA per cápita | USD 85,810 |

---

## 2. Hallazgos Clave

### 2.1 El outlier: líder mundial sin ley federal

USA es el caso más influyente en cualquier modelo del estudio:

- **Sin ley IA federal** (`iapp_has_ai_law=0`), pero **intensidad regulatoria 6/10** y **cobertura temática 13/15** — la más alta entre países sin ley horizontal
- IAPP clasifica como `strategy_led`; OECD como `regulation_focused` — **discrepancia significativa** que refleja la fragmentación regulatoria
- **27 leyes IA aprobadas 2016-2024** (Stanford) — pero ninguna es una ley federal comprehensiva; son ejecutivos presidenciales, leyes estatales y regulaciones sectoriales
- El Executive Order 14110 (oct 2023) es el instrumento federal más relevante, pero no tiene fuerza de ley permanente

### 2.2 AI Readiness #1 mundial — dominancia en todos los pilares

- **AI Readiness Index: 88.36** — #1 global, 12 puntos sobre el #2 (FRA: 80.81)
- Dominancia consistente: policy vision 100, e-government delivery 97.84, safety 100, compute 90.92
- Pero **resilience relativamente baja (78.28)** comparada con otros pilares — vulnerabilidad sistémica

### 2.3 Ecosistema IA: tamaño desproporcionado

- **Inversión acumulada 2013-2024: USD 470.9 billion** — ~60-65% del total mundial
- **Inversión 2024: USD 109 billion** — más que todo el resto del mundo combinado
- **6,956 startups IA financiadas** (2013-2024 acumulado), **1,073 nuevas en 2024 solo**
- **Patentes IA: 5.2 por 100,000 habitantes** — líder global
- **558 modelos notables de ML** (2003-2024 acumulado) — más que el resto del mundo combinado
- Concentración de talento: 0.78% — alto pero no el más alto (SGP 1.64%)
- Migración neta positiva: +1.07 por cada 10,000 LinkedIn

### 2.4 Adopción empresarial moderada-alta

- **Adopción IA H2 2025: 28.3%** — ranking ~10 global
- Crecimiento de 2.1 pp en un semestre (26.3% → 28.3%)
- Menor que SGP (60.9%) y ARE (64%) pero sobre base mucho más grande

### 2.5 GII #3 — innovación consolidada

- **GII Score: 61.69** (#3 mundial, detrás de Suiza y Suecia)
- Inputs 67.20, Outputs 57.56 — brecha de 9.6 puntos (mucho menor que CHL o SGP)
- R&D 3.59% del PIB — el más alto de la muestra
- Eficiencia: convierte inversión en outputs mejor que la mayoría

### 2.6 Privacidad: mosaico sin ley federal

- **Sin ley de protección de datos federal** (`gdpr_has_gdpr_like_law=0`, similarity=1)
- Sectorial: HIPAA, COPPA, GLBA, FCRA + 19+ leyes estatales (CCPA/VCDPA)
- **Sin DPA federal** — enforcement fragmentado por estado y sector
- **Enforcement activo** por FTC y state AGs
- EU-US Data Privacy Framework (DPF) vigente pero vulnerable a revocación

### 2.7 Freedom House: Free pero con divisiones

- **Freedom House: Free (83/100)**
- Political Rights: 33/60 (bajo para una democracia plena — refleja polarización)
- Civil Liberties: 50/40 (nota: max es 60, no 40 — ajustar en metadata)
- Voice & Accountability: **1.02** (positivo)

### 2.8 Common law: la tradición que define el enfoque

- **Legal origin: English common law** (`is_common_law=1`)
- Tradición que favorece regulación sectorial, incremental y basada en precedentes — no comprehensiva
- Consistente con la ausencia de ley federal horizontal

### 2.9 Discrepancia IAPP vs OECD: el caso más extremo

| Variable | IAPP | OECD | Explicación |
|----------|------|------|-------------|
| `has_ai_law` | 0 | 1 | IAPP: no ley federal. OECD: cuenta EO 14110 + leyes estatales |
| `regulatory_approach` | strategy_led | regulation_focused | IAPP: predominan frameworks voluntarios. OECD: 20 regulaciones sectoriales |
| `regulatory_intensity` | 6 | 30 | Escalas incomparables; OECD cuenta cada iniciativa |
| `thematic_coverage` | 13 | 2 | IAPP: temas cubiertos por EO/frameworks. OECD: sectores con regulación específica |
| `year_enacted` | NULL | 1999 | OECD señala primera regulación relevante (probablemente sectorial) |
| `enforcement_level` | medium | high | IAPP: FTC enforcement. OECD: múltiples agencias activas |

---

## 3. Perfil Comparativo: USA vs SGP vs CHL

| Dimensión | USA | SGP | CHL |
|-----------|-----|-----|-----|
| AI Readiness | 88.36 (#1) | 76.42 (#7) | 59.30 (#50) |
| Adopción IA | 28.3% | 60.9% | 20.8% |
| Reg. Intensity (IAPP) | 6 | 6 | 4 |
| has_ai_law | 0 | 0 | 0 |
| GII Score | 61.69 (#3) | 59.94 (#5) | 33.07 (#51) |
| GDP PPA per cápita | $85,810 | $150,689 | $36,181 |
| R&D % PIB | 3.59% | 2.16% | 0.36% |
| Inversión IA acum. | $470.9B | $7.27B | $0.68B |
| Startups IA | 6,956 | 239 | 17 |
| Freedom House | F (83) | PF (48) | F (94) |
| Rule of Law | 1.33 | 1.75 | 0.63 |
| Regulatory Quality | 1.39 | 2.31 | 0.93 |
| Common law | Sí | Sí | No |
| Migración talento IA | +1.07 | +1.26 | -0.19 |

**Lectura:** USA domina en ecosistema pero tiene regulación fragmentada. SGP tiene menor ecosistema pero regulación más cohesiva. CHL tiene debilidad estructural en ambos frentes.

---

## 4. Implicancia para el Estudio

USA es el outlier más influyente en cualquier modelo:

1. **Obligatorio reportar con y sin USA** — si USA se incluye, domina todos los coeficientes
2. **`has_ai_law=0` es engañoso** — USA tiene 27 leyes relacionadas con IA, solo no tiene una ley federal horizontal
3. **La clasificación `strategy_led` subestima** — el enforcement real por FTC/DOJ es alto, y las regulaciones estatales (CCPA, Colorado AI Act) son vinculantes
4. **El ecosistema IA de USA es un confounder masivo** — la correlación entre inversión y outcomes no es causalidad regulatoria
5. **El caso USA soporta la hipótesis de que no se necesita ley federal para tener ecosistema dominante** — pero esto es específico a common law con calidad regulatoria alta

---

## 5. Datos Faltantes

Ninguno (189/189 = 100%).

---

## 6. Fuentes y Trazabilidad

| Fuente | Año | Archivo |
|--------|-----|---------|
| IAPP | 2026-02 | `data/raw/IAPP/iapp_x1_core.csv` |
| Oxford Insights | 2025 | `data/raw/Oxford Insights/oxford_ai_readiness_snapshot_latest.csv` |
| Microsoft AIEI | H1+H2 2025 | `data/raw/Microsoft/microsoft_ai_diffusion_study.csv` |
| Stanford AI Index | 2025 | `data/raw/STANFORD AI INDEX 25/` |
| WIPO GII | 2025 | `data/raw/WIPO Global Innovation Index/` |
| World Bank WDI | 2023-2024 | `data/raw/World Bank WDI/` |
| Freedom House | 2025 | `data/raw/FreedomHouse/` |
| GDPR Coding | 2025 | `data/raw/GDPR_coding/` |
| Legal Origin | 2008 | `data/raw/LegalOrigin/` |
| OECD AI | 2024 | `data/raw/OECD/oecd_x1_snapshot_2024.csv` |

---

*Perfil generado como parte del pipeline de extracción estandarizada del proyecto LeyIA DataScience.*