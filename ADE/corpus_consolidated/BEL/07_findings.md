# BEL — Hallazgo Diferencial

## 1. Tesis del hallazgo diferencial

**Bélgica presenta el caso de "institutional gap under binding regulation": sujeito ao EU AI Act diretamente (como AUT, NLD, ESP, IRL) mas com implementación nacional mais rezagada que seus pares EU-27: sem agência IA nacional dedicada, incumplimiento del prazo obligatorio de designación de autoridades (02-08-2025), y BIPT designado como MSA solo via coalition agreement político (sin instrumento legal formal publicado), en un contexto de estructura federal compleja (3 regiones + nivel federal) que distribuye competencias y dificulta implementación uniforme.**

---

## 2. Evidencia cuantitativa — densidad del corpus

| Métrica | Valor | Cálculo |
|---|---|---|
| # documentos totales | 5 | count(manifest.csv) |
| # binding (law + sectoral) | 1 | EU AI Act |
| # soft/policy/strategy | 4 | AI4Belgium + Convergence Plan + 2 APD guidelines |
| Páginas totales corpus | 248 | sum(pages) |
| Páginas binding / soft | 144 / 104 | 1.38:1 |
| Primer documento (fecha) | 2019-03 | AI 4 Belgium |
| Último documento (fecha) | 2024-09 | APD AI/GDPR brochure |
| Años cubiertos | 5.5 | (2024-09 - 2019-03) |
| Gap con fecha corpus | ~7 meses | 2026-04-21 - 2024-09 |
| # docs superseded | 0 | Ningún documento reemplazado |

---

## 3. Evidencia cuantitativa — timeline y proceso

| Fecha | Hito | Detalle |
|---|---|---|
| 2019-03 | AI 4 Belgium Report | Primer documento estratégico IA. Coalición público-privada FPS BOSA. 7 objetivos. |
| 2022-10-28 | National Convergence Plan | Aprobado Consejo de Ministros. 9 pilares, ~70 ejes de acción. Coordinación FPS BOSA. |
| 2024-07-12 | EU AI Act entry into force | Regulation (EU) 2024/1689 entra en vigor. Aplicación directa en Bélgica. |
| 2024-09-19 | APD — AI Systems + GDPR | Brochure APD/GBA sobre paralelismo RGPD ↔ AI Act. 21pp. |
| 2024 | APD — Impact of AI on Privacy | Dossier temático APD sobre impacto IA en privacidad. 16pp. |
| 2025-01-31 | Government Declaration | BIPT/IBPT designado como Market Surveillance Authority. Coalition agreement 2025-2029 (De Wever). |
| 2025-02-08 | AI Act deadline | Fecha límite para designación de autoridades competentes (Art. 70). |
| 2025-08-02 | Plazo incumplido | Bélgica NO completó designación formal de autoridades AI Act. |

**Duración:** 5.5 años de evolución regulatoria.
**Emisor principal:** FPS BOSA / APD/GBA / BIPT.
**Complejidad estructural:** Nivel federal + Flandes + Valonia + Bruselas.

---

## 4. Datos que FORTALECEN la tesis

- **EU AI Act directamente aplicable** — binding regulation sin transposición. Bélgica sujeto a la regulación más estricta globally.

- **AI4Belgium (2019) + National Convergence Plan (2022)** — dos documentos estratégicos consolidados. Arquitectura de políticas coherente. Convergence Plan aprobado en Consejo de Ministros con 9 pilares y ~70 ejes de acción.

- **APD/GBA activa con guidance dual** — DPA belga publicó dos documentos (2024) sobre intersección RGPD/AI Act: brochure AI/GDPR (21pp, sept. 2024) + dossier temático privacidad (16pp). Evidencia de engagement institucional activo.

- **BIPT designado como MSA** — Government Declaration 31-01-2025 identifica BIPT como Market Surveillance Authority. Aunque sin instrumento formal, hay designación política declarada.

- **Estructura federal con 3 regiones** — Flandes, Valonia y Bruselas tienen competencias digitales propias. La estructura federal, aunque compleja, también implica que hay múltiples niveles de implementación (no solo federal).

---

## 5. Datos que REFUTAN la tesis (stress test honesto)

- **Incumplimiento del plazo AI Act (02-08-2025)** — Bélgica no designó formalmente autoridades competentes. *Refutador primario.* Sin embargo, el AI Act sigue siendo directamente aplicable aunque las autoridades no estén formalmente designadas.

- **Sin agencia IA dedicada** — Bélgica no tiene una agencia específica como AESIA (España) o AISI (UK) o BSI (Alemania). BIPT es un regulador sectorial (telecomunicaciones) reconvertido, no una agencia IA.

- **Estructura federal compleja** — Flandes tiene Vlaams AI Plan, Valonia tiene estrategias propias. El corpus cubre solo nivel federal; la picture completa podría mostrar mayor densidad.

- **NLD y ESP cumplieron el plazo** — España y Países Bajos designaron autoridades formales a tiempo. Bélgica quedó rezagado en ejecución institucional.

- **AUT tiene el mismo problema** — Austria también incumplió el plazo de designación (02-08-2025). La tesis de "rezago" aplica a ambos. *Validación: BEL y AUT son paralelos en el bucket binding_regulation con delays de implementación.*

---

## 6. Comparación vs peer group

| País | Régimen | # docs | # binding | Tesis diferencial |
|---|---|---|---|---|
| NLD | binding_regulation | 5 | 1 | AI Act + supervisión establecida (AP + RvIG) + GenAI Vision 2024 |
| ESP | binding_regulation | 5 | 1 | AI Act + AESIA activa + sandbox IA (RD 817/2023) |
| **BEL** | **binding_regulation** | **5** | **1** | **Sin agencia dedicada, incumplimiento plazo AI Act, estructura federal compleja** |
| AUT | binding_regulation | 4 | 1 | Estrategia más madura UE-27 (82%) pero mismo incumplimiento plazo AI Act |
| DEU | binding_regulation | 8 | 4 | BSI + institucionalidad robusta + KIMIG en desarrollo |

**Análisis:** BEL comparte bucket binding_regulation con AUT, NLD, ESP, DEU. Se distingue por:
- Sin agencia IA dedicada (vs DEU/NLD/ESP)
- Mismo incumplimiento de plazo que AUT
- APD activa con guidance RGPD/AI (diferencial positivo)
- Estructura federal compleja (vs NLD/ESP centralizados)

**Cuasi-paralelo:** BEL ≈ AUT — ambos incumplieron plazo, sin agencia dedicada, pero BEL tiene APD más activa.

---

## 7. Implicancias para el estudio

| Variable X1 | Efecto potencial |
|---|---|
| `has_ai_law` | 1 (EU AI Act directamente aplicable) |
| `regulatory_intensity` | 10/10 (sin cambio vs IAPP) |
| `thematic_coverage` | 14/15 (sin cambio) |
| `enforcement_level` | `medium` (matización: ley vinculante con machinery incompleta) |
| `regulatory_regime_group` | `binding_regulation` (confirmado) |
| `has_dedicated_ai_authority` | 0 (BIPT designado MSA pero no agencia IA dedicada) |

**Hipótesis testeable:**
- ¿Países con binding regulation pero delays institucionales (BEL, AUT) tienen outcomes distintos a países con implementación robusta desde el inicio (NLD, ESP)?
- ¿La ausencia de agencia IA dedicada tiene efecto independente sobre adopción/inversión?

**Caso narrativo útil para:**
- §Discusión como "caso de institutional gap bajo binding regulation"
- Control para tesis "EU AI Act igual para todos" — BEL ≠ NLD ≠ ESP en implementación nacional
- Comparación con AUT (mismo problema, estrategias más maduras)

---

## 8. Banderas de re-visita

| Evento | Horizonte | Trigger observable |
|---|---|---|
| Instrumento legal formalizando BIPT como MSA | 3-6m | Publicación en moniteur.be o bgset.be |
| Nuevo guidance APD sobre AI Act | 6m | autoriteprotectiondonnees.be publicación |
| Flandes AI Plan actualización | 6-12m | vlaanderen.be nuevo documento |
| Sanciones AI Act aplicadas | 12-24m | Decisiones BIPT o APD publicadas |
| Agence IA dedicada publicada | 12-24m | Moniteur.be nuevo documento |

---

## Links

- [CANDIDATES.md](CANDIDATES.md)
- [SOURCES.md](SOURCES.md)
- [manifest.csv](manifest.csv)