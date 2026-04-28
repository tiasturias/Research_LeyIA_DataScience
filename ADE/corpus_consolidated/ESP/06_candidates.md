# ESP — Inventario de documentos y propuesta de recodificación

**País:** España (ISO3: ESP)
**Región:** EU
**EU AI Act:** Sí (directamente aplicable)
**Prioridad:** P1-TOP30 (#6 Microsoft AI Diffusion Report 2025)
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

---

## 2. Diagnóstico del ecosistema regulatorio IA

### 2.1 Estructura regulatoria

**Capa 1 — UE directamente aplicable:** EU AI Act desde 01-08-2024.

**Capa 2 — Normativa nacional vinculante complementaria:**
- **RD 729/2023** (agosto 2023): crea AESIA — **primera agencia IA nacional de la UE**.
- **RD 817/2023** (noviembre 2023): primer **AI regulatory sandbox de la UE**. Vigente hasta 36 meses o aplicación plena AI Act.
- **Anteproyecto Ley IA 2025** (marzo 2025, bill_pending): transpone obligaciones nacionales, designa autoridades, fija sanciones.

**Capa 3 — Estrategia e implementación:**
- **ENIA 2020** → **Estrategia IA 2024** (mayo 2024). €2.100M (€1.500M PRTR + €600M previos). 3 ejes / 8 palancas.

**Capa 4 — Ejes no incluidos:** LOPDGDD 3/2018 (GDPR transpose), AEPD guidance IA (múltiples guías), Instrucción 2/2026 CGPJ (IA jurisdiccional).

### 2.2 Autoridades competentes

- **AESIA** (A Coruña, desde 2023): autoridad nacional coordinadora IA. Primera en UE.
- **AEPD** (Madrid): autoridad DP, vigilancia mercado en IA con datos personales. Histórico activo (multas a Google, Facebook).
- **CGPJ, JEC, BdE, CNMV, CNMC, DGSFP**: autoridades sectoriales designadas en Anteproyecto Ley IA 2025.

### 2.3 Contexto estratégico

España es el EEMM con **mayor nivel de institucionalización nacional del AI Act** de la UE:
- Única con agencia nacional dedicada operativa (AESIA, desde 2023).
- Primera con sandbox AI funcional (2023).
- Entre las primeras con anteproyecto de ley nacional (marzo 2025; IRL publicó General Scheme en feb 2026).

Ecosistema IA doméstico menor que Francia o Alemania pero con apuesta pública fuerte (PRTR / Fondos Next Generation).

---

## 3. Inventario de documentos

### Documento 1 — EU AI Act
| Campo | Valor |
|---|---|
| Archivo | `ESP_EUAIAct_Reg2024_1689.pdf` · Tipo: `binding_law_ai` · Páginas: 144 |
| SHA-256 | `bba630444b3278e881066774002a1d7824308934f49ccfa203e65be43692f55e` |

Ver IRL/CANDIDATES.md §3 Doc 1 para citas clave. Aplicación directa en España.

### Documento 2 — RD 729/2023 (Estatuto AESIA)
| Campo | Valor |
|---|---|
| Archivo | `ESP_RD729_2023_AESIAEstatuto.pdf` · Tipo: `binding_regulation` · Páginas: 30 |
| Fecha | 22-08-2023 (BOE 02-09-2023) · Status: `in_force` |
| SHA-256 | `3d95ee2a634d5c29b84470a1ca54ba0a05b2bc2b8dbd29b6e000ce2f7e2c1763` |

**Citas textuales relevantes:**

> "Artículo 4. Fines. La Agencia tiene como fines la minimización de los riesgos significativos sobre la seguridad y salud de las personas, así como sobre sus derechos fundamentales, que puedan derivarse del uso de sistemas de inteligencia artificial, así como el desarrollo de una inteligencia artificial inclusiva, sostenible y centrada en la ciudadanía."

> "Disposición final primera. Sede. La Agencia Española de Supervisión de Inteligencia Artificial tendrá su sede institucional en la ciudad de A Coruña."

### Documento 3 — RD 817/2023 (Sandbox IA)
| Campo | Valor |
|---|---|
| Archivo | `ESP_RD817_2023_SandboxIA.pdf` · Tipo: `binding_regulation` · Páginas: 31 |
| Fecha | 08-11-2023 (BOE 09-11-2023) · Status: `in_force` |
| SHA-256 | `aa9cfe8f19dc6a1bc84f16425081fbf27193473e58fdd76aac78a3f9dcb7c340` |

**Citas textuales relevantes:**

> "Artículo 1. Objeto. Este real decreto tiene por objeto establecer un entorno controlado de pruebas para el ensayo del cumplimiento de la propuesta de Reglamento del Parlamento Europeo y del Consejo por el que se establecen normas armonizadas en materia de inteligencia artificial."

> "Artículo 2. Ámbito. Sistemas de inteligencia artificial de alto riesgo identificados según los Anexos II y III de la propuesta de Reglamento IA, sistemas de propósito general y modelos fundacionales."

> "Disposición final cuarta. Vigencia. El presente real decreto tendrá una vigencia máxima de treinta y seis meses desde su entrada en vigor o, en su caso, hasta que sea aplicable en el Reino de España el Reglamento europeo de inteligencia artificial, si dicha aplicación se produjese antes del mencionado plazo."

### Documento 4 — Estrategia IA 2024
| Campo | Valor |
|---|---|
| Archivo | `ESP_EstrategiaIA_2024.pdf` · Tipo: `policy_strategy` · Páginas: 68 |
| Fecha | 14-05-2024 · Status: `in_use` |
| SHA-256 | `aa10a2ff077628f3a0f9d5f46a994f5b092975889ea9bb62072d137dc520e603` |

**Citas textuales relevantes:**

> "La Estrategia de Inteligencia Artificial 2024 se articula en torno a 3 ejes vertebradores: (1) impulso de la IA como motor de competitividad y bienestar, (2) desarrollo de un ecosistema IA de excelencia y (3) adopción de una IA transparente, responsable y humanista."

> "El presupuesto de esta Estrategia asciende a 1.500 millones de euros procedentes del Plan de Recuperación, Transformación y Resiliencia, que se suman a los 600 millones ya movilizados."

### Documento 5 — Anteproyecto Ley IA 2025 ("Buen uso y gobernanza")
| Campo | Valor |
|---|---|
| Archivo | `ESP_Anteproyecto_LeyIA2025.pdf` · Tipo: `bill_pending` · Páginas: 35 |
| Fecha | 11-03-2025 · Status: `bill_pending` |
| SHA-256 | `a3ebaec8a04d2ffc855ab148af36d62d36673a92ee387cc6fa576ff37eec33df` |

**Citas textuales relevantes:**

> "Artículo 1. Objeto. Esta ley tiene por objeto complementar, en el ámbito del Reino de España, el desarrollo y aplicación del Reglamento (UE) 2024/1689."

> "Artículo 17. Autoridades de vigilancia de mercado. 1. La Agencia Española de Supervisión de Inteligencia Artificial actuará como autoridad de vigilancia de mercado con carácter general. 2. La Agencia Española de Protección de Datos, en lo relativo a los sistemas de IA que impliquen el tratamiento de datos personales [...]. 3. El Consejo General del Poder Judicial [...] 4. La Junta Electoral Central [...]."

> "Artículo 28. Régimen sancionador. Las infracciones muy graves podrán ser sancionadas con multa de entre 7.500.000 y 35.000.000 de euros, o entre el 2% y el 7% del volumen de negocio total anual mundial del ejercicio anterior, si esta cifra fuese superior."

---

## 4. Propuesta de recodificación

### 4.1 Variables principales

| Variable | Valor IAPP | Propuesta estudio | Cambio |
|---|---|---|---|
| `has_ai_law` | 1 | **1** | Sin cambio |
| `regulatory_regime` | `comprehensive` | **`binding_regulation`** | Reclasificación taxonómica |
| `regulatory_intensity` | 10 | **10** | Sin cambio |
| `thematic_coverage` | 14 | **14** | Sin cambio |
| `enforcement_level` | — | **`high`** | Adición |
| `regulatory_regime_group` | — | **`binding_regulation`** | Adición |

### 4.2 Justificación

**`binding_regulation`:** Igual que IRL/FRA (AI Act aplicable directo) pero con el diferencial institucional más fuerte de la UE: AESIA operativa desde 2023 + sandbox AI nacional + anteproyecto específico.

**`enforcement_level: high`:**
- AESIA operativa con competencias asignadas vía RD 729/2023.
- AEPD con track record RGPD activo.
- Anteproyecto fija sanciones hasta €35M o 7% facturación (equivalentes al techo AI Act).
- CGPJ y JEC como autoridades sectoriales con poderes plenos.

### 4.3 Variables adicionales

| Variable | Valor |
|---|---|
| `ai_law_name` | Regulation (EU) 2024/1689 (AI Act) + Anteproyecto Ley IA (pendiente) |
| `ai_law_year` | 2024 |
| `ai_law_status` | in_force (UE) + bill_pending (nacional) |
| `national_strategy` | 1 (ENIA 2020 + Estrategia IA 2024) |
| `has_dedicated_ai_authority` | **1** (AESIA operativa desde 2023) |
| `gdpr_or_equivalent` | 1 (GDPR + LOPDGDD) |

---

## 5. Comparación con IAPP

| Dimensión | IAPP | Este estudio |
|---|---|---|
| Régimen | `comprehensive` | `binding_regulation` |
| has_ai_law | 1 | 1 ✓ |
| intensity | 10/10 | 10/10 ✓ |
| coverage | 14/15 | 14/15 ✓ |
| has_dedicated_ai_authority | — | 1 |
| Enforcement | no codif. | `high` |

**Veredicto:** Codificación IAPP correcta. Diferencial respecto a otros EEMM: España es el único país de la UE con `has_dedicated_ai_authority=1` operativa (AESIA), variable adicional del estudio.

---

## 6. Limitaciones y notas

1. **Anteproyecto vs Ley aprobada.** El Anteproyecto está en tramitación. Re-capturar cuando sea promulgado como Ley y publicado en BOE.
2. **Sandbox vigencia limitada.** 36 meses o hasta aplicación del AI Act. En 2026 puede quedar absorbido por el sandbox obligatorio del art. 57 AI Act.
3. **GDPR / LOPDGDD / guidance AEPD no incluidas.** Documentadas en SOURCES.md §5.
4. **ENIA 2020 no incluida.** Superseded por Estrategia 2024; archivo histórico.
5. **Instrucción CGPJ 2/2026.** Aplicable solo al Poder Judicial, no horizontal. No incluida.

---

## 7. Resumen ejecutivo

España presenta el **régimen de implementación nacional más desarrollado del AI Act en la UE**:
- Única con agencia IA nacional operativa (AESIA, A Coruña, desde 2023).
- Pionera en AI regulatory sandbox (RD 817/2023, precedente del art. 57 AI Act).
- Anteproyecto de ley nacional específico en tramitación (marzo 2025), adelanta a IRL (General Scheme feb 2026) y a la mayoría de EEMM.
- Régimen sancionador nacional complementario que replica topes AI Act (€35M / 7%).
- Ecosistema IA doméstico menor que FR/DE pero con respaldo presupuestario PRTR (€2.100M).

Corpus: 5 documentos. 1 ley IA-específica UE vinculante + 2 RRDD nacionales vinculantes (AESIA + sandbox) + 1 estrategia + 1 anteproyecto.
