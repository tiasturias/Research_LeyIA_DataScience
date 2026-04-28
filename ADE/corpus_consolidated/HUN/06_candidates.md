# HUN — Inventario de documentos y propuesta de recodificación

**País:** Hungary (ISO3: HUN)
**Región:** EU
**EU AI Act:** Sí (directamente aplicable)
**Prioridad:** P1-TOP30 (#18 Microsoft AI Diffusion Report 2025)
**Fecha:** 2026-04-19
**Codificador:** Claude Sonnet 4.6 (asistido)
**Revisor humano:** Pendiente

---

## 1. Baseline IAPP

| Variable | Valor IAPP actual |
|---|---|
| `regulatory_regime` | `comprehensive` |
| `regulatory_intensity` | 10 |
| `thematic_coverage` | 14 |
| `has_ai_law` | 1 |
| `enforcement` | `high` |

---

## 2. Diagnóstico del ecosistema regulatorio IA

### 2.1 Estructura regulatoria

**Capa 1 — UE directamente aplicable:** EU AI Act desde 01-08-2024.

**Capa 2 — Ley nacional de implementación (ÚNICA en corpus procesado):**
- **Act LXXV of 2025** (31-10-2025, vigor 01-12-2025): ley nacional que transpone el framework institucional del AI Act. Primera ley de implementación del AI Act promulgada y en vigor entre los países del corpus. Designa autoridades, crea el Consejo Húngaro de IA, establece poderes nacionales.

**Capa 3 — Estrategia nacional:**
- **AI Strategy 2020-2030** (sept. 2020, EN): primera estrategia nacional IA. 7 áreas. Aprobada por resolución gubernamental.
- **AI Strategy 2025-2030** (sept. 2025, HU): renovación con 6 pilares y 3 áreas prioritarias. Coordinada con Act LXXV.

### 2.2 Autoridades competentes (designadas por Act LXXV of 2025)

- **Ministro de Desarrollo Empresarial (Gazdaságfejlesztési Miniszter):** autoridad de vigilancia de mercado AI Act (art. 70 AI Act).
- **Autoridad Nacional de Acreditación (Nemzeti Akkreditációs Hatóság):** autoridad notificante (art. 28 AI Act).
- **Consejo Húngaro de IA (Magyar Mesterséges Intelligencia Tanács):** órgano consultivo creado por Act LXXV para asegurar implementación unificada.
- **NAIH (Nemzeti Adatvédelmi és Információszabadság Hatóság):** DPA independiente. Competencia en IA que trate datos personales.

### 2.3 Contexto estratégico

Hungría presenta el **ecosistema de implementación del AI Act más avanzado formalmente del corpus EU procesado** en términos de legislación nacional:
- Act LXXV of 2025: primera ley nacional de implementación del AI Act ya promulgada y en vigor (vs. IRL General Scheme pre-bill, ESP Anteproyecto pendiente, BEL/AUT sin ley).
- Dos estrategias IA sucesivas (2020 + 2025): continuidad política a lo largo de 5 años.
- Estructura institucional tripartita clara: vigilancia mercado (Ministro) + notificación (Acreditación) + asesoría (Consejo IA).
- Particularidad: Hungary ha completado la designación formal de autoridades AI Act que BEL/AUT incumplieron en el plazo.

---

## 3. Inventario de documentos

### Documento 1 — EU AI Act
| Campo | Valor |
|---|---|
| Archivo | `HUN_EUAIAct_Reg2024_1689.pdf` · Tipo: `binding_law_ai` · Páginas: 144 |
| SHA-256 | `bba630444b3278e881066774002a1d7824308934f49ccfa203e65be43692f55e` |

Ver IRL/CANDIDATES.md §3 Doc 1. Aplicación directa en HUN. Complementado por Act LXXV of 2025.

### Documento 2 — Act LXXV of 2025 (Magyar Közlöny 127/2025)
| Campo | Valor |
|---|---|
| Archivo | `HUN_ActLXXV_2025_MK.pdf` · Tipo: `binding_regulation` · Páginas: 218 |
| Fecha | 2025-10-31 · Status: `in_force` (vigor 01-12-2025) |
| SHA-256 | `a7f1d1a01fc9115d7a254c4ca2a6fd958752bc9e8d8e12ba874ff2458a476c25` |
| Idioma | HU (R5 — resúmenes EN en CMS Law, Digital Policy Alert) |

**Citas textuales relevantes (HU):**

> "1. § E törvény célja, hogy az Európai Unió mesterséges intelligenciáról szóló Rendelet [Reg. (EU) 2024/1689] magyarországi végrehajtásához szükséges intézményi és eljárási kereteket megállapítsa."

> "4. § (1) A mesterséges intelligencia rendszerek piacfelügyeleti hatósága a gazdaságfejlesztési miniszter (a továbbiakban: miniszter). (2) A bejelentő hatósága a Nemzeti Akkreditációs Hatóság."

> "7. § Létrejön a Magyar Mesterséges Intelligencia Tanács, mint az egységes végrehajtást biztosító konzultatív testület."

### Documento 3 — AI Strategy 2020-2030 (EN)
| Campo | Valor |
|---|---|
| Archivo | `HUN_AIStrategy_2020.pdf` · Tipo: `policy_strategy` · Páginas: 58 |
| Fecha | 2020-09 · Status: `in_use` (vigente hasta 2030; complementada por estrategia 2025) |
| SHA-256 | `dd69ff359db5df61bb2d5c1ecea9c310bba6a6c1db105b9e4cf1332bf4eba521` |

**Citas textuales relevantes:**

> "Hungary's National Artificial Intelligence Strategy 2020-2030 is a 10-year, whole-of-society policy framework that sets out national objectives for data governance, R&D, skills, infrastructure and sectoral deployment of AI."

> "The Strategy was completed in 2020 and the government approved implementation measures by resolution 1573/2020 (IX.9). The Strategy positions AI as a national development priority and provides an integrated set of measures covering data governance, research and innovation, infrastructure, education and ethical/regulatory frameworks."

### Documento 4 — AI Strategy 2025-2030 (HU)
| Campo | Valor |
|---|---|
| Archivo | `HUN_AIStrategy_2025.pdf` · Tipo: `policy_strategy` · Páginas: 119 |
| Fecha | 2025-09-03 · Status: `in_use` |
| SHA-256 | `e2f1056637b6888fad81071ed51037456e5d4da3d73c4c5e5b5002a3761f83c9` |
| Idioma | HU (R5) |

**Citas textuales relevantes (HU):**

> "Magyarország Mesterséges Intelligencia Stratégiája (2025-2030) hat pillérre épül: (1) kutatás-fejlesztés és innováció; (2) digitális infrastruktúra; (3) oktatás és készségfejlesztés; (4) digitális gazdaság; (5) közszféra digitalizációja; (6) etikai és szabályozási keret."

> "A stratégia három kiemelt területen határozza meg a prioritásokat: 'MI a Társadalomért' (közszolgáltatások, egészségügy, oktatás, fenntartható közlekedés); 'MI a Technológiáért' (K+F, nyílt forráskódú modellek, autonóm rendszerek); 'MI az Üzletért' (vállalati digitalizáció, gazdasági versenyképesség)."

---

## 4. Propuesta de recodificación

### 4.1 Variables principales

| Variable | Valor IAPP | Propuesta estudio | Cambio |
|---|---|---|---|
| `has_ai_law` | 1 | **1** | Sin cambio |
| `regulatory_regime` | `comprehensive` | **`binding_regulation`** | Reclasificación taxonómica |
| `regulatory_intensity` | 10 | **10** | Sin cambio |
| `thematic_coverage` | 14 | **14** | Sin cambio |
| `enforcement_level` | `high` (IAPP) | **`high`** | Confirmación |
| `regulatory_regime_group` | — | **`binding_regulation`** | Adición |

### 4.2 Justificación

**`binding_regulation`:** EU AI Act (directo) + **Act LXXV of 2025 (ley nacional de implementación en vigor desde dic. 2025)** — combinación más sólida del corpus EU procesado.

**`enforcement_level: high`** — confirmado vs. IAPP:
- Act LXXV of 2025 promulgada y en vigor: primera en EU entre los países del corpus.
- Autoridades formalmente designadas (Ministro Desarrollo Empresarial + Autoridad Acreditación).
- Consejo Húngaro de IA operativo.
- Dos estrategias IA sucesivas + renovación coordinada con legislación.
- NAIH (DPA) disponible para supervisión datos/IA.

**Nota de contexto:** El estado de derecho en Hungría (tensiones UE-Orbán) es un factor de riesgo de implementación efectiva, pero no modifica la codificación formal de `enforcement_level` basada en instrumentos jurídicos publicados.

### 4.3 Variables adicionales

| Variable | Valor |
|---|---|
| `ai_law_name` | Regulation (EU) 2024/1689 (AI Act) + Act LXXV of 2025 (implementación nacional) |
| `ai_law_year` | 2024 (UE) / 2025 (nacional) |
| `ai_law_status` | in_force |
| `national_strategy` | 1 (AI Strategy 2020-2030 + AI Strategy 2025-2030) |
| `has_dedicated_ai_authority` | 1 (Ministro Desarrollo Empresarial como MSA formal + Consejo IA) |
| `gdpr_or_equivalent` | 1 (GDPR + Infotv 2011) |

---

## 5. Comparación con IAPP

| Dimensión | IAPP | Este estudio |
|---|---|---|
| Régimen | `comprehensive` | `binding_regulation` |
| has_ai_law | 1 | 1 ✓ |
| intensity | 10/10 | 10/10 ✓ |
| coverage | 14/15 | 14/15 ✓ |
| enforcement | `high` | `high` ✓ |
| has_dedicated_ai_authority | — | 1 (Ministro MSA) |

**Veredicto:** Codificación IAPP correcta. Diferencial HUN: **única en el corpus con ley nacional de implementación AI Act ya promulgada y en vigor** (Act LXXV of 2025, desde dic. 2025). `has_dedicated_ai_authority=1` (Ministro como MSA formal). Dos estrategias sucesivas 2020+2025.

---

## 6. Limitaciones y notas

1. **Act LXXV Magyar Közlöny completo (218pp).** El número 127/2025 contiene múltiples leyes. Act LXXV es una de ellas. Fuente oficial correcta; no hay PDF separado de la ley en magyarkozlony.hu.
2. **Corpus HU con R5.** Act LXXV y AI Strategy 2025 en húngaro. AI Strategy 2020 en EN. Resúmenes EN disponibles para Act LXXV (CMS Law, Digital Policy Alert).
3. **Contexto político.** La implementación efectiva puede estar condicionada por la relación HUN-UE (Art. 7 TEU). No afecta codificación formal pero relevante para análisis.
4. **NAIH guidance AI no localizada.** DPA húngaro sin guidance AI específica como PDF al cierre del corpus.
5. **GDPR + Infotv (2011. évi CXII.) no incluidas.** Ver IRL/SOURCES.md §5.

---

## 7. Resumen ejecutivo

Hungría presenta **el régimen de implementación nacional del AI Act más avanzado formalmente** entre los países EU del corpus:
- Act LXXV of 2025 (vigor dic. 2025): **primera ley nacional de implementación AI Act promulgada** — antes que IRL (General Scheme, bill_pending) y ESP (Anteproyecto, bill_pending).
- Autoridades formalmente designadas: Ministro Desarrollo Empresarial (MSA) + Autoridad Acreditación (notificante) + Consejo IA (advisory).
- Dos estrategias IA (2020+2025) con continuidad política demostrada.
- `has_dedicated_ai_authority=1` gracias a Act LXXV.
- Contexto de alerta: relación tensa HUN-UE puede afectar implementación efectiva.

`enforcement_level: high` confirmado — IAPP correcto. `regulatory_regime: binding_regulation` (EU AI Act + ley nacional).

Corpus: 4 documentos. 1 ley UE vinculante + 1 ley nacional implementación AI Act + 2 estrategias (2020 EN + 2025 HU).
