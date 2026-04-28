# FRA — Inventario de documentos y propuesta de recodificación

**País:** France (ISO3: FRA)
**Región:** EU
**EU AI Act:** Sí (directamente aplicable)
**Prioridad:** P1-TOP30 (#5 Microsoft AI Diffusion Report 2025)
**Fecha:** 2026-04-19
**Codificador:** Claude Opus 4.7 (asistido)
**Revisor humano:** Pendiente

---

## 1. Baseline IAPP

| Variable | Valor IAPP actual |
|---|---|
| `regulatory_regime` | `comprehensive` |
| `regulatory_intensity` | 10 |
| `thematic_coverage` | 14 |
| `has_ai_law` | 1 |

**Nota IAPP:** Francia está clasificada como `comprehensive` (has_ai_law=1) por el EU AI Act. Codificación correcta y consistente.

---

## 2. Diagnóstico del ecosistema regulatorio IA

### 2.1 Estructura regulatoria

**Capa 1 — Derecho UE directamente aplicable:**
- **EU AI Act** (Reg. 2024/1689) desde 1-08-2024.

**Capa 2 — Estrategia e implementación nacional:**
- **SNIA Phase 1** (2018): Plan Villani, €1.5B.
- **SNIA Phase 2** (2021): €2.22B adicionales, 4 hubs 3IA, foco talento y souveraineté.
- **Rapport Commission IA** (marzo 2024): 25 recomendaciones presidenciales. Base del realineamiento estratégico.
- **SNIA Phase 3** (febrero 2025): anunciada en el AI Action Summit; €109B de inversión total comprometidos; 4 prioridades (compute, écosystème, attractivité, IA pour l'action publique).
- **Rapport Cour des comptes** (noviembre 2025): evaluación oficial Phase 1+2.

**Capa 3 — Autoridad DP activa:**
- **CNIL** con Plan d'action IA desde mayo 2023; 7 recomendaciones (abril 2024); fiches pratiques intérêt légitime y scraping (abril-junio 2025).

**Capa 4 — Leyes sectoriales relevantes (no incluidas en corpus):**
- Loi SREN 2024-449 (DSA transpose + deepfakes).
- Loi Informatique et Libertés n° 78-17 (GDPR transpose).
- Code de la propriété intellectuelle (TDMR opt-out bajo Directive 2019/790).

### 2.2 Autoridades competentes

- **CNIL:** autoridad DP, coordinadora de facto IA + RGPD. Ejecutora de la vertiente RGPD del AI Act.
- **ARCOM** (audiovisual), **ACPR** (financiero), **DGCCRF** (consumo), **ARCEP** (telecom): autoridades sectoriales probables bajo el AI Act.
- **AI Office of France:** no creada aún (a diferencia de IRL). El Gobierno podría designar a la DGE (Direction Générale des Entreprises) o crear organismo nuevo.

### 2.3 Contexto estratégico

Francia es el segundo hub IA de la UE (tras Irlanda como sede europea de Big Tech). Ecosistema doméstico fuerte: Mistral AI, Hugging Face, Dust, Kyutai. €109B anunciados en AI Action Summit 2025 + campus Stargate FR. Posición Macron: "IA souveraine" + resistencia activa a cláusulas más restrictivas del AI Act durante el trílogo (GPAI foundation models). Enfoque pro-innovación dentro del marco UE.

---

## 3. Inventario de documentos

### Documento 1 — EU AI Act
| Campo | Valor |
|---|---|
| Archivo | `FRA_EUAIAct_Reg2024_1689.pdf` |
| Tipo | `binding_law_ai` |
| Status | `in_force` |
| Páginas | 144 |
| SHA-256 | `bba630444b3278e881066774002a1d7824308934f49ccfa203e65be43692f55e` |

Mismo documento que IRL/EUAIAct. Referencias y citas clave: ver `IRL/CANDIDATES.md §3 Doc 1`. Aplicación directa en Francia.

### Documento 2 — Commission IA "IA : notre ambition pour la France"
| Campo | Valor |
|---|---|
| Archivo | `FRA_CommissionIA_Ambition2024.pdf` |
| Emisor | Commission de l'IA (Aghion/Bouverot) — mandato presidencial |
| Tipo | `policy_strategy` |
| Fecha | 2024-03-13 |
| Status | `in_use` |
| Páginas | 130 |
| URL | https://www.info.gouv.fr/upload/media/content/0001/09/4d3cc456dd2f5b9d79ee75feea63b47f10d75158.pdf |
| SHA-256 | `866f86e8a02e817e76dae26ee1254548ed9c446a6aa066595e2ea62d67c8fc24` |

**Citas textuales relevantes:**

> "Notre ambition est de faire de la France un acteur majeur de la révolution technologique que représente l'IA. [...] Cette ambition passe par un investissement massif dans les talents, la recherche, le calcul, et par une régulation adaptée qui protège sans freiner." (Introduction)

> "Recommandation n° 1 — Créer les conditions d'une appropriation collective de l'IA et de ses enjeux pour définir collectivement les conditions dans lesquelles elle s'insère dans notre société et nos services publics." (Partie 3, Recommandations)

> "Recommandation n° 17 — Orienter résolument notre politique de concurrence et de régulation vers l'émergence d'acteurs européens de l'IA." (Partie 3)

> "Recommandation n° 22 — Agir d'urgence pour éviter le décrochage européen, en ajustant la mise en œuvre du règlement IA européen pour lever les incertitudes pesant sur les acteurs économiques." (Partie 3)

### Documento 3 — SNIA Phase 2 (2021)
| Campo | Valor |
|---|---|
| Archivo | `FRA_StrategieIA_Phase2_2021.pdf` |
| Emisor | MESRI |
| Tipo | `policy_strategy` |
| Fecha | 2021-11 |
| Status | `in_use` |
| Páginas | 28 |
| SHA-256 | `950ba9f465e2be07c0df8d8f73e2a4475be8eb3963386901d9ce024fd1d05e8b` |

**Citas textuales relevantes:**

> "La deuxième phase de la Stratégie Nationale pour l'IA mobilise 2,22 milliards d'euros sur la période 2021-2025 pour consolider l'écosystème français et renforcer notre souveraineté technologique."

> "Les 4 instituts 3IA (MIAI Grenoble, 3IA Côte d'Azur, ANITI Toulouse, PRAIRIE Paris) constituent les piliers de la recherche française en IA."

### Documento 4 — Cour des comptes — Rapport SNIA (2025)
| Campo | Valor |
|---|---|
| Archivo | `FRA_StrategieIA_CourComptes2025.pdf` |
| Emisor | Cour des comptes |
| Tipo | `policy_strategy` (évaluation) |
| Fecha | 2025-11 |
| Status | `in_use` |
| Páginas | 102 |
| SHA-256 | `c51aff35a92d94a0c34df278fe878f75cc2a9c8fbfba3eb5dc458b177b43bbea` |

**Citas textuales relevantes:**

> "La stratégie nationale pour l'intelligence artificielle : consolider les succès de la politique publique de l'IA, élargir son champ. Rapport public thématique. Novembre 2025." (Portada)

> "Les phases 1 et 2 de la SNIA ont contribué à structurer un écosystème français de l'IA, avec des succès notables en matière de recherche et de formation, mais des marges d'amélioration subsistent sur la diffusion de l'IA dans l'économie et l'administration." (Synthèse)

### Documento 5 — CNIL Synthèse fiches IA (2025)
| Campo | Valor |
|---|---|
| Archivo | `FRA_CNIL_FichesIA_Synthese2025.pdf` |
| Emisor | CNIL |
| Tipo | `guidelines` |
| Fecha | 2025-06 |
| Status | `in_force` |
| Páginas | 17 |
| SHA-256 | `f2c9fd01f34440111837aa3f73ad94c085da088f097e9d1ce9aefd1d044fce22` |

**Citas textuales relevantes:**

> "La CNIL a publié pour consultation publique deux fiches pratiques relatives au recours à l'intérêt légitime pour le développement de systèmes d'IA, notamment dans le cadre d'opérations de moissonnage de données (web scraping)." (Contexto)

> "La synthèse confirme la pertinence du cadre proposé tout en appelant à préciser les conditions de mise en œuvre du test de mise en balance et les mesures de mitigation applicables aux opérations de scraping à large échelle."

---

## 4. Propuesta de recodificación

### 4.1 Variables principales

| Variable | Valor IAPP | Propuesta estudio | Cambio |
|---|---|---|---|
| `has_ai_law` | 1 | **1** | Sin cambio |
| `regulatory_regime` | `comprehensive` | **`binding_regulation`** | Reclasificación taxonómica |
| `regulatory_intensity` | 10 | **10** | Sin cambio — confirmado |
| `thematic_coverage` | 14 | **14** | Sin cambio — confirmado |
| `enforcement_level` | — | **`high`** | Adición |
| `regulatory_regime_group` | — | **`binding_regulation`** | Adición |

### 4.2 Justificación

**`binding_regulation`:** Mismos criterios que IRL (AI Act directamente aplicable). Diferencial: CNIL con track record histórico de enforcement DP (multas a Google, Amazon, Microsoft — hasta €150M). Plan d'action IA operativo desde 2023 (pre-AI Act). Guidance maduro y aplicable.

**`enforcement_level: high`:**
- CNIL: autoridad DP con mayor intensidad de sanciones RGPD de la UE (junto a DPC irlandesa e italiana Garante).
- Sanciones AI Act hasta €35M o 7% facturación global.
- Historia de action publique fuerte (reconocimiento facial en escuelas, Clearview AI).

### 4.3 Variables adicionales

| Variable | Valor |
|---|---|
| `ai_law_name` | Regulation (EU) 2024/1689 (AI Act) |
| `ai_law_year` | 2024 |
| `ai_law_status` | in_force |
| `national_strategy` | 1 (Phase 1 2018 + Phase 2 2021 + Rapport Commission 2024 + Phase 3 2025) |
| `has_dedicated_ai_authority` | 0 (no AI Office nacional equivalente a IRL AI Office; coordinación via CNIL + DGE) |
| `gdpr_or_equivalent` | 1 (GDPR + Loi Informatique et Libertés) |

---

## 5. Comparación con IAPP

| Dimensión | IAPP | Este estudio |
|---|---|---|
| Régimen | `comprehensive` | `binding_regulation` |
| has_ai_law | 1 | 1 ✓ |
| intensity | 10/10 | 10/10 ✓ |
| coverage | 14/15 | 14/15 ✓ |
| Enforcement | no codif. | `high` |

**Veredicto:** La codificación IAPP es correcta. Reclasificación taxonómica, no corrección.

---

## 6. Limitaciones y notas

1. **SNIA Phase 3 sin documento programático consolidado.** Anunciada en AI Action Summit (feb 2025). Re-capturar cuando el Gobierno publique Phase 3 formal.
2. **GDPR / Loi IL / Loi SREN no incluidas.** Razones metodológicas documentadas en SOURCES.md §5.
3. **Rapport Villani 2018 no incluido.** Superseded por SNIA Phase 2 y por el rapport Cour des comptes 2025.
4. **CNIL fiches pratiques en HTML.** Se incluye la síntesis como PDF representativo. Re-capturar cuando haya consolidado.
5. **AI Office of France no creada.** A diferencia de IRL, Francia no ha legislado arquitectura nacional formal del AI Act todavía. Pendiente de observación.

---

## 7. Resumen ejecutivo

Francia presenta régimen IA `binding_regulation` vía aplicación directa del EU AI Act + ecosistema regulatorio interno maduro. Diferenciales respecto a Irlanda:
- Autoridad DP (CNIL) con más larga historia de enforcement activa que la DPC, aunque menor jurisdicción Big Tech.
- Arquitectura nacional AI Act aún sin legislación dedicada (IRL ya tiene General Scheme).
- Ecosistema IA doméstico más potente (Mistral, Hugging Face) con respaldo presidencial explícito.
- Estrategia estratificada en 3 fases (2018, 2021, 2025) con inversión acumulada de €109B anunciada.

Corpus: 5 documentos. 1 ley IA-específica vinculante + 3 estrategias nacionales (fases 2, 2024 Commission, eval Cour des comptes) + 1 guidance DP-IA (CNIL).
