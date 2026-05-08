# FINDINGS.md — Hallazgos diferenciales por país

Entregable por país que profundiza y **estresa con datos cuantitativos** el hallazgo diferencial que aparece en §Hallazgo diferencial de CANDIDATES.md. El objetivo es que la conclusión del codificador (régimen propuesto, upgrade/downgrade, tesis narrativa) quede **soportada y refutada** con métricas, no solo con narrativa.

Ubicación: `data/raw/legal_corpus/{ISO3}/FINDINGS.md`.

---

## Esquema fijo (6 secciones, en este orden)

### 1. Tesis del hallazgo diferencial

Un párrafo (3-5 oraciones). Qué hace único a este país en el corpus. Debe ser falsable — una afirmación que pueda ser refutada por evidencia posterior. Evitar trivialidades ("tiene ley de protección de datos") — solo tesis con contenido diferencial.

Ejemplo bueno: "AUS es el único país del corpus que consultó públicamente mandatory guardrails (sep 2024) y formalmente los abandonó 15 meses después (dic 2025)."
Ejemplo malo: "AUS tiene un framework voluntario." (no diferencial; lo tienen 10+ países)

### 2. Evidencia cuantitativa — densidad del corpus

Tabla con métricas calculadas:

| Métrica | Valor | Cálculo |
|---|---|---|
| # documentos totales | N | count(manifest.csv) |
| # binding (law + sectoral) | N | filter doc_type LIKE 'binding_%' |
| # soft/policy/strategy | N | resto |
| Páginas totales corpus | N | sum(pages) |
| Páginas binding / soft | A/B | ratio |
| Primer documento (fecha) | YYYY-MM-DD | min(publication_date) |
| Último documento (fecha) | YYYY-MM-DD | max(publication_date) |
| Años cubiertos | N | (max - min).years |
| Gap con fecha corpus | N meses | today - max |
| # docs superseded | N | filter status='superseded' |

### 3. Evidencia cuantitativa — timeline y proceso

- Hitos regulatorios con fecha absoluta (ej. "2024-09-05: publicación simultánea VAIS + Proposals Paper").
- Duración de consultas públicas (días entre apertura y cierre), si aplica.
- # rondas de consulta si el doc es iterativo.
- Ministerio / emisor principal (DISR, MIC, CNIL, etc.) + cambios de emisor a lo largo del período.
- Presupuesto público comprometido (si aparece en docs — ej. "AUD 124.1M en AI Action Plan 2021").

### 4. Datos que FORTALECEN la tesis

Lista de bullets. Cada bullet cita una fuente trazable (doc del corpus + page hint o sección). Ejemplos:

- Cita textual directa que soporta la tesis.
- Métrica numérica (N páginas dedicadas, N principios, N guardrails).
- Continuidad institucional (mismo ministerio, mismo framework, N años).
- Ausencia relevante (no hay ley IA-específica → refuerza tesis "soft framework").

### 5. Datos que REFUTAN la tesis (stress test honesto)

Lista de bullets. Qué evidencia podría hacer caer la tesis. Obligatorio incluir al menos 2 refutaciones potenciales. Si no hay ninguna, la tesis es trivial — reescribir.

- Bill pendiente que podría cambiar el régimen en N meses.
- Ley sectorial reciente que no se incluyó (justificar por qué no aplica).
- Anuncio ministerial posterior al cierre del corpus (flaggear como provisional).
- Contraste con peer group (si N países del mismo clúster tienen la misma característica, no es diferencial).

### 6. Comparación vs peer group

Tabla de comparación con 2-4 países del mismo clúster regulatorio (o del mismo régimen propuesto). Columnas: país, régimen, # docs, # binding, tesis diferencial (1 línea).

Ejemplo para AUS en clúster pro-innovation anglófono (GBR, NZL, CAN):

| País | Régimen | # docs | # binding | Nota distintiva |
|---|---|---|---|---|
| AUS | soft_framework | 7 | 1 | Retroceso explícito de mandatory guardrails (dic 2025) |
| GBR | soft_framework | 6 | 2 | Abandono AI Bill + AISI como institución |
| NZL | soft_framework | 5 | 1 | Strategy tardía (jul 2025) + Algorithm Charter gubernamental |
| CAN | TBD | ... | ... | ... |

### 7. Implicancias para el estudio

- Variable X1 directamente afectada (regulatory_regime_group, has_ai_law, enforcement_level, etc.).
- Hipótesis del estudio que este país ayuda a testear ("¿regular o no regular?" → AUS es cuasi-experimento).
- Sugerencia de uso analítico: "incluir como caso narrativo en §X del paper", "útil como control negativo para hipótesis Y".

### 8. Banderas de re-visita

Lista de eventos que, si ocurren, obligan a revisar este país:

- Australian AI Safety Institute operativo → revisar `has_dedicated_ai_authority` de 0 → 1.
- Schedule 1 Part 15 Privacy Amendment Act entra en vigor (2026-12-10) → revisar `enforcement_level`.
- Nuevo bill IA introducido en Parliament → revisar `has_ai_law`.

Indicar **horizonte de re-visita** (6m, 12m, 24m) y **trigger observable**.

---

## Reglas de escritura

- Todo dato numérico debe tener fuente: doc del corpus (con nombre de archivo) o manifest.csv.
- No inventar métricas. Si no se puede calcular (ej. páginas de docs no descargados), marcar como N/A + explicar por qué.
- Prohibido lenguaje evaluativo sin métrica ("muy ambicioso", "el más relevante") — reemplazar por la métrica ("69pp con 10 guardrails, vs promedio 25pp en peer group").
- Las tesis diferenciales deben ser falsables. "Único en X" requiere verificar al menos los 20 países del mismo clúster.
- Citar CANDIDATES.md y manifest.csv con links markdown.

---

## Índice agregado `docs/HALLAZGOS_DIFERENCIALES.md`

Un archivo a nivel de proyecto. **Yo (skill) lo mantengo** tras cada país. Estructura:

```markdown
# Hallazgos Diferenciales — Corpus Legal-IA

Índice de tesis diferenciales por país. Cada entrada linkea al FINDINGS.md del país.

## Por régimen

### binding_regulation
- [EU](../data/raw/legal_corpus/EU/FINDINGS.md) — tesis 1 línea
- ...

### soft_framework
- [AUS](../data/raw/legal_corpus/AUS/FINDINGS.md) — Retroceso explícito de mandatory guardrails (sep 2024 → dic 2025)
- [GBR](../data/raw/legal_corpus/GBR/FINDINGS.md) — ...
- ...

### strategy_only
- ...

### no_framework
- ...

## Por clúster analítico (pro-innovation, compliance-first, etc.)
...

## Última actualización: YYYY-MM-DD — N/86 países
```

Reglas del índice:
- Una línea por país. ≤120 caracteres.
- Sin prosa, solo link + tesis resumida.
- Agrupado por régimen propuesto (4 buckets).
- Actualizar contador y fecha en cada país procesado.
