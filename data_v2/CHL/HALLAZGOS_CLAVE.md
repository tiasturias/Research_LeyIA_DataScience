# Chile (CHL) — Perfil de Datos Consolidado

**Fecha:** 2026-04-28  
**Fuentes:** 10 estudios oficiales  
**Atributos extraídos:** 133  
**Cobertura:** 132/133 (99.2%)  
**Contexto político:** Boletín 16821-19 — Ley Marco de IA en tramitación

---

## 1. Identificación

| Atributo | Valor |
|----------|-------|
| ISO3 | CHL |
| País | Chile |
| Región | Latin America and the Caribbean |
| Grupo de ingreso | High Income (HI) |
| Población | 19,764,771 |
| PIB PPA per cápita | USD 36,181 |

---

## 2. Hallazgos Clave

### 2.1 El caso paradigmático: estrategia sin ley, con proyecto en carpeta

Chile es el caso focal del estudio porque encarna la decisión regulatoria que el gobierno está tomando ahora:

- **No tiene ley IA vinculante** (`iapp_has_ai_law=0`) pero tiene el **Boletín 16821-19** en tramitación parlamentaria
- IAPP clasifica como `strategy_led` (Política Nacional de IA 2021); OECD como `light_touch` — **discrepancia moderada**
- **Thematic coverage 8/15** — cubre transparencia, sesgo, datos, algunos temas sectoriales
- **Enforcement level: low** — sin autoridad IA específica (PDPC aún no opera)

**Implicancia:** Si Chile aprueba la Ley Marco IA, pasaría de `strategy_led` a `regulation_focused` o `comprehensive`, cambiando su posición en la distribución de `regulatory_intensity` de 4 a potencialmente 6-8. Este es el counterfactual que el estudio debe evaluar.

### 2.2 AI Readiness #50 — brecha compute crítica

- **AI Readiness Index: 59.3** (ranking #50 global)
- Contraste dramático: **policy vision 100** pero **compute capacity 18.18** — la mayor brecha interna del ranking
- Policy commitment 87.5 (alto) vs AI sector maturity 24.68 (muy bajo)
- Gobierno digital delivery 96.53 (top 5 mundial) pero herramientas de IA en sector público significativamente menor

**Interpretación:** Chile tiene la voluntad política e institucional para gobernar IA, pero carece de la infraestructura de cómputo para desarrollar un ecosistema doméstico competitivo. Esta brecha Sugiere que la regulación sin inversión en infraestructura podría ser costo-efectiva limitada.

### 2.3 Adopción IA moderada — con fuga de talento

- **Adopción IA empresarial: 20.8%** (H2 2025) — lejos del top (SGP 60.9%, ARE 64%)
- Crecimiento de solo 1.2 pp en un semestre (19.6% → 20.8%)
- **Migración neta de talento IA: -0.19** por cada 10,000 miembros LinkedIn — **fuga de cerebros**
- Concentración de talento IA: 0.32% (vs SGP 1.64%, USA ~1.5%)
- Solo **17 startups IA financiadas** (2013-2024 acumulado) vs 239 en SGP
- **Inversión acumulada: USD 0.68 billion** — 10x menor que SGP en términos absolutos, y drásticamente menor per cápita

### 2.4 Innovación débil para HI — brecha input-output severa

- **GII Score: 33.07** (ranking #51) — último entre los High Income de la muestra
- Inputs 40.91 vs Outputs 24.34 — **brecha de 16.6 puntos**, la más grande entre países HI
- R&D apenas 0.36% del PIB (vs SGP 2.16%, OCDE promedio 2.7%)
- Patentes residentes: 402 (vs SGP 2,024)
- Knowledge creation: 16.73 (vs SGP 39.89)

**Diagnóstico:** Chile invierte poco en innovación y lo que invierte se traduce mal en outputs. Esta es una debilidad estructural que limita el ecosistema IA independientemente de la regulación.

### 2.5 Libertades políticas fuertes — democrat en contexto latino

- **Freedom House: Free (94/100)** — el más alto entre LATAM grandes
- Political Rights: 38/60, Civil Liberties: 56/40 (nota: 56+38=94)
- Voice & Accountability: **1.02** (positivo, raro en la región)
- Esto contrasta con SGP (PF, 48/100, voice & accountability -0.07)
- La fortaleza democrática de Chile podría facilitar una gobernanza IA más transparente y participativa

### 2.6 Ley de datos nueva pero enforcement pendiente

- **Law 21.719 (2024)** — nueva ley de protección de datos, texto alineado con GDPR
- Similaridad GDPR: nivel 2 (sustancial)
- **Enforcement activo: 0** — la APDP (Agencia de Protección de Datos) aún no está operativa
- Entrada en vigor: diciembre 2026
- Sin status EU (no es miembro, no tiene adecuación)

**Riesgo:** Chile tiene la ley pero no la autoridad funcional. Si la Ley Marco IA se aprueba antes de que la APDP esté operativa, habrá dos marcos regulatorios sin enforcement real.

### 2.7 Tradición civil law francesa

- **Legal origin: French** (código civil de Bello 1855)
- `is_common_law=0`
- Esto predicaría, según La Porta, una tendencia a regulación más prescriptiva y detallada — consistente con el enfoque de la Ley 16821-19

### 2.8 Discrepancia IAPP vs OECD

| Variable | IAPP | OECD | Impacto en análisis |
|----------|------|------|---------------------|
| `has_ai_law` | 0 | 1 | OECD cuenta la ley de neurorights como "AI law" |
| `regulatory_approach` | strategy_led | light_touch | Ambos concueran en que no es comprehensivo |
| `regulatory_intensity` | 4/10 | 7 (escala propia) | Escalas incomparables |
| `thematic_coverage` | 8/15 | 14 | OECD cuenta más temas incluyendo neurorights |
| `year_enacted` | NULL | 2020 | OECD señala ley de neurorights 2020 |

**Resolución:** La ley de neurorights (Ley 21.155) es una **ley sectorial de neurotecnología**, no una ley horizontal de IA. IAPP es más preciso. Pero OECD es válido si se incluye regulación sectorial no-IA como parte del ecosistema regulatorio.

---

## 3. Perfil Comparativo con SGP (benchmark regional)

| Dimensión | CHL | SGP | Diferencia |
|-----------|-----|-----|------------|
| AI Readiness | 59.3 (#50) | 76.42 (#7) | SGP +17.1 pts |
| Adopción IA | 20.8% | 60.9% | SGP +40.1 pp |
| Reg. Intensity (IAPP) | 4 | 6 | SGP +2 |
| GII Score | 33.07 (#51) | 59.94 (#5) | SGP +26.9 pts |
| GDP PPA per cápita | $36,181 | $150,689 | SGP +$114,508 |
| R&D % PIB | 0.36% | 2.16% | SGP +1.8 pp |
| Freedom House | F (94) | PF (48) | CHL +46 pts |
| Rule of Law (WGI) | 0.63 | 1.75 | SGP +1.12 |
| Inversión IA acum. | $0.68B | $7.27B | SGP +$6.59B |
| Startups IA | 17 | 239 | SGP +222 |
| Migración talento IA | -0.19 | +1.26 | SGP +1.45 |

**Lectura:** Singapur supera a Chile en todos los indicadores de ecosistema IA, pero Chile tiene ventaja democrática (F vs PF). La pregunta de investigación es: **¿la diferencia se explica por regulación, por estructura económica, o por ambos?**

---

## 4. Datos Faltantes (1/133)

| Atributo | Motivo |
|----------|--------|
| `iapp_year_enacted` | Chile no tiene ley IA específica vigente |

---

## 5. Tensión Central del Caso Chile

Chile enfrenta una decisión regulatoria con características únicas:

1. **Regulación sin infraestructura:** Policy vision 100/100 pero compute capacity 18/100. Aprobar la Ley Marco IA sin invertir en infraestructura de cómputo puede crear obligaciones sin los medios para cumplirlas.

2. **Fuga de talento:** Migración neta negativa (-0.19) sugiere que los profesionales IA capacitados en Chile emigran. La regulación podría agravar esto si impone costos sin generar oportunidades.

3. **Brecha input-output en innovación:** Con R&D al 0.36% del PIB (lejos del 2.7% OCDE), Chile no está generando suficiente conocimiento para alimentar un ecosistema IA competitivo, independientemente de la regulación.

4. **Democracia como ventaja contextual:** La alta libertad política (94/100) y voz y rendición de cuentas (1.02) podrían hacer que una regulación participativa y transparente tenga más legitimidad que en contextos autoritarios.

5. **Dos leyes sin enforcement:** Tanto la Ley de Protección de Datos (21.719, enforcement pendiente) como la potencial Ley Marco IA (16821-19, en tramitación) corren el riesgo de crear marcos sin dientes.

---

## 6. Fuentes y Trazabilidad

| Fuente | Año | Archivo |
|--------|-----|---------|
| IAPP | 2026-02 | `data/raw/IAPP/iapp_x1_core.csv` |
| Oxford Insights | 2025 | `data/raw/Oxford Insights/oxford_ai_readiness_snapshot_latest.csv` |
| Microsoft AIEI | H1+H2 2025 | `data/raw/Microsoft/microsoft_ai_diffusion_study.csv` |
| Stanford AI Index | 2025 | `data/raw/STANFORD AI INDEX 25/4. Economy/Data/` |
| WIPO GII | 2025 | `data/raw/WIPO Global Innovation Index/wipo_gii_snapshot_latest.csv` |
| World Bank WDI | 2023-2024 | `data/raw/World Bank WDI/wdi_core_controls.csv` |
| Freedom House | 2025 | `data/raw/FreedomHouse/freedom_in_the_world_2025.csv` |
| GDPR Coding | 2025 | `data/raw/GDPR_coding/gdpr_like_coding.csv` |
| Legal Origin | 2008 | `data/raw/LegalOrigin/legal_origin_coding.csv` |
| OECD AI | 2024 | `data/raw/OECD/oecd_x1_snapshot_2024.csv` |

---

*Perfil generado como parte del pipeline de extracción estandarizada del proyecto LeyIA DataScience.*  
*Caso focal: Boletín 16821-19 — Ley Marco de IA.*