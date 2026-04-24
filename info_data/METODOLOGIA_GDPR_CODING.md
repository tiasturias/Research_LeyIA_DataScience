# Metodologia de Codificacion: has_gdpr_like_law & gdpr_similarity_level

## Contexto y Justificacion Cientifica

**Fecha de creacion:** 2026-04
**Sub-tarea:** A.4 de la Tarea A (auditoria cientifica del estudio)
**Variables creadas:** `has_gdpr_like_law`, `gdpr_similarity_level`, y variables auxiliares (`dp_law_year`, `has_dpa`, `eu_status`, `enforcement_active`)

### Por que esta variable es necesaria

El estudio "¿Regular o no regular? Analisis comparativo del impacto de marcos regulatorios de IA" busca estimar el efecto causal de la regulacion IA-especifica sobre el desarrollo del ecosistema de IA.

Sin embargo, existe un **confounder crucial**: la **regulacion de proteccion de datos preexistente** (GDPR-like laws). Los paises que promulgan leyes AI-especificas **no parten de cero regulatorio**; muchos ya tenian un marco maduro de proteccion de datos personales (GDPR, LGPD, PIPL, etc.) que:

1. **Crea infraestructura institucional** (DPAs, procedimientos, jurisprudencia) que facilita legislar IA
2. **Educa a legisladores y reguladores** en conceptos como consentimiento, transparencia, derechos del titular
3. **Establece expectativas ciudadanas y de industria** sobre derechos digitales que luego se extienden a IA
4. **Correlaciona con variables outcome** (readiness, adopcion) de forma independiente a la regulacion IA

**Sin controlar este confounder, `regulatory_intensity` podria estar midiendo "tradicion regulatoria digital" en vez de "esfuerzo regulatorio IA-especifico"**, lo cual sesgaria la recomendacion politica a Chile (Ley Marco IA 16821-19).

### Evidencia empirica del confounding (sample N=72)

| regulatory_status_group | gdpr_similarity_level (mean) | N | EU members |
|---|---|---|---|
| binding_regulation | **2.889** | 27 | 22/27 |
| soft_framework | 2.222 | 9 | 0/9 |
| strategy_only | 2.147 | 34 | 0/34 |
| no_framework | 1.500 | 2 | 0/2 |

Los paises con regulacion IA vinculante tienen casi todos nivel 3 (EU/EEA/adequacy), mientras que los paises sin marco IA estan en niveles 1-2. Omitir este control sobreestima el efecto de la regulacion IA-especifica.

---

## Esquema de Variables

| Variable | Tipo | Rango | Descripcion |
|---|---|---|---|
| `has_gdpr_like_law` | binary | 0/1 | 1 si el pais tiene ley NACIONAL comprehensiva de proteccion de datos personales |
| `gdpr_similarity_level` | ordinal | 0-3 | Nivel de alineacion con estandar GDPR (ver reglas abajo) |
| `dp_law_year` | int | 1981-2024 | Ano de promulgacion / ultima enmienda mayor de la ley principal |
| `has_dpa` | binary | 0/1 | 1 si existe Autoridad de Proteccion de Datos operativa e independiente |
| `eu_status` | categorical | 4 niveles | `eu_member` / `eea_member` / `adequacy` / `none` |
| `enforcement_active` | binary | 0/1 | 1 si la ley ha sido activamente aplicada (multas / decisiones publicas) |
| `dp_law_name` | string | - | Nombre corto de la ley principal (campo descriptivo) |

### Reglas de codificacion para `gdpr_similarity_level`

| Nivel | Criterio | Ejemplos |
|---|---|---|
| **0** | No existe ley comprehensiva a nivel nacional Y no hay regimen sectorial significativo | (Ningun pais de la muestra) |
| **1** | Sin ley nacional comprehensiva (solo sectoriales: salud, telecom, finanzas) O con draft pendiente sin efectividad | USA (sectoral + state laws), PAK (draft bill), CMR (solo telecom) |
| **2** | Ley nacional comprehensiva estilo GDPR (principios de consentimiento, derechos de titular, DPA), PERO sin decision formal de adecuacion UE | BRA (LGPD), CHN (PIPL), IND (DPDP Act), CHL (Ley 21.719), SGP (PDPA), ZAF (POPIA) |
| **3** | Miembro UE O miembro EEA O decision de adecuacion UE vigente | FRA, DEU (EU); ISL, NOR (EEA); ARG, CAN, CHE, GBR, ISR, JPN, KOR, NZL, URY (adecuacy) |

**Justificacion del nivel 3 estricto:** Se requiere reconocimiento formal de equivalencia por la UE. Esto es cuantificable, replicable y academicamente defendible. Alternativas subjetivas (p.ej. "parece GDPR-like") introducen ruido de codificacion.

### Casos limite y decisiones

| Pais | Decision | Razonamiento |
|---|---|---|
| **USA** | Nivel 1 (no 2) | DPF framework es bilateral sectorial, no hay ley federal comprehensiva. Estados (CCPA etc.) no califican para nivel 2 nacional. |
| **CHL** | Nivel 2 (no 3) | Nueva Ley 21.719 (Dec 2024, efectiva 2026) es GDPR-aligned textualmente, pero sin adecuacy formal. Se espera que obtenga adecuacy post-2026. |
| **BRA** | Nivel 2 (no 3) | LGPD es textualmente muy GDPR-like, pero UE aun no ha concedido adecuacy (discusion en curso 2025-2026). |
| **CHN** | Nivel 2 | PIPL 2021 es comprehensivo y activamente aplicado (CAC), pero divergente en filosofia (data sovereignty, localizacion). Sin adecuacy UE ni expectativa de obtenerla. |
| **CMR** | Nivel 1 (no 0) | Tiene Ley 2010/012 sobre comunicaciones electronicas con provisiones de privacidad sectorial. No califica como "0 total". |
| **PAK** | Nivel 1 | PECA 2016 es sectorial (ciberseguridad), no proteccion de datos. Proyecto PDPB desde 2018 aun no promulgado. |
| **UKR** | Nivel 2 | Ley 2297-VI (2010) es comprehensiva pero pre-GDPR. Reforma hacia alineacion UE pendiente por candidatura UE. |
| **TUR** | Nivel 2 | KVKK 2016 es GDPR-inspired pero con divergencias significativas (adequacy rechazada). |
| **RUS** | Nivel 2 | Ley 152-FZ es comprehensiva pero con requisitos de localizacion divergentes. No hay perspectiva de adecuacy. |
| **MEX** | Nivel 2 | LFPDPPP es comprehensiva, pero INAI bajo reforma/eliminacion politica (2024-2025). |

---

## Fuentes Consultadas

### Fuente primaria
**DLA Piper** — *Data Protection Laws of the World 2025* (<https://www.dlapiperdataprotection.com>)
- Estandar de facto en comparative privacy law
- Cubre 160+ jurisdicciones
- Actualizado anualmente por abogados locales
- Incluye nivel de severidad regulatoria (Heavy / Moderate / Limited / No specific)

### Fuentes secundarias (cross-check)
1. **UNCTAD** — *Data Protection and Privacy Legislation Worldwide* (<https://unctad.org/page/data-protection-and-privacy-legislation-worldwide>)
2. **Comision Europea** — *Adequacy decisions* (<https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en>)
3. **IAPP** — Global Privacy Directory
4. **Fuentes nacionales** — paginas oficiales de DPAs para confirmar operatividad

### Fecha de corte
**Marzo 2026** (leyes promulgadas / decisiones de adecuacy hasta esa fecha).

---

## Limitaciones y Usos Recomendados

### Limitaciones
1. **Estatica:** No captura cambios en aplicacion (enforcement) que podrian ocurrir despues de marzo 2026.
2. **Ordinal, no cardinal:** `gdpr_similarity_level` es ordinal; las diferencias entre niveles no son comparables aritmeticamente (level 2 no es "2 veces" level 1).
3. **Codificacion manual:** Aunque basada en fuentes academicas establecidas, sujeta a juicio en casos limite (documentados arriba).
4. **Enforcement_active binario es burdo:** Un pais con 1 multa historica y otro con cientos de multas al ano estan ambos en 1. Para analisis fino, considerar indicadores alternativos.

### Usos recomendados
1. **Control/confounder** en modelo confounded (ya integrado en `complete_confounded`).
2. **Analisis de heterogeneidad:** interactuar con `regulatory_intensity` para testear si el efecto de la regulacion IA varia segun preexistencia de GDPR-like law.
3. **Robustez:** reportar modelos con y sin este control para mostrar sensibilidad.
4. **Descriptivo:** usar cross-tab con `regulatory_status_group` para caracterizar la muestra.

### Usos NO recomendados
1. Tratarla como outcome (es preexistente a regulacion IA).
2. Usarla como instrumento sin verificar exclusion restriction.
3. Comparar paises con level 3 como "idénticos" regulatoriamente — hay variacion dentro del nivel (p.ej. FRA vs ESP vs MLT).

---

## Integracion en el Pipeline

### Archivos creados/modificados
- **Nuevo:** `data/raw/GDPR_coding/gdpr_like_coding.csv` — dataset fuente (86 filas)
- **Nuevo:** `data/interim/x2_gdpr_master.csv` — master output (86 filas)
- **Modificado:** `src/build_source_masters.py` — agregada `build_gdpr_master()`
- **Modificado:** `src/build_sample_ready.py` — agregado `X2_CONFOUNDERS_GDPR` y merge
- **Nuevo:** `info_data/METODOLOGIA_GDPR_CODING.md` — este documento

### Como reproducir
```bash
cd "Research_LeyIA_DataScience"
source .venv/bin/activate
python src/build_source_masters.py   # produce x2_gdpr_master.csv
python src/build_sample_ready.py     # integra a sample_ready_cross_section.csv
```

### Como actualizar (futuro)
Si se requiere actualizar la codificacion:
1. Editar `data/raw/GDPR_coding/gdpr_like_coding.csv` directamente
2. Documentar el cambio agregando fila en seccion "Historial" abajo
3. Re-ejecutar pipeline
4. Actualizar fecha de corte en este documento

---

## Contribucion al Estudio

Este control permite al estudio responder una pregunta mas rigurosa:

> **"Controlando por preexistencia de marco de proteccion de datos, ¿la regulacion IA-especifica tiene efecto marginal significativo sobre el desarrollo del ecosistema?"**

Para Chile (caso de aplicacion directa):
- Chile tiene nivel 2 (Ley 21.719 nueva) — similar a Brasil, Sudafrica, Singapur
- Chile NO esta en nivel 3 (sin adequacy EU aun)
- Al modelar Chile, el "contrafactual" no es solo "¿que pasaria sin regulacion IA?" sino "¿que pasaria sin regulacion IA dado que ya tiene marco de proteccion de datos maduro?"

Esta distincion es **critica** para la recomendacion politica de la Ley Marco IA 16821-19: evita atribuir a la regulacion IA efectos que en realidad vienen del marco de proteccion de datos preexistente.

---

## Historial de Actualizaciones

| Fecha | Cambio |
|---|---|
| 2026-04-14 | Creacion inicial. 86 paises codificados. Fecha de corte: 2026-03. |
