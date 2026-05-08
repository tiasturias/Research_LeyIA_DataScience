# Estructura exacta de entregables

Los 4 archivos van en `data/raw/legal_corpus/{ISO3}/`: `manifest.csv`, `SOURCES.md`, `CANDIDATES.md`, `FINDINGS.md`. Lee los 4 pilotos antes de empezar un país nuevo — las plantillas mejoran con cada iteración. Usa siempre la más reciente.

El esquema de FINDINGS.md está en [findings.md](findings.md) (archivo separado por tamaño).

Plantillas de referencia (ordenadas de más reciente a más antigua):
- [data/raw/legal_corpus/MNG/CANDIDATES.md](../../../data/raw/legal_corpus/MNG/CANDIDATES.md) — 3 docs, estrategia no publicada.
- [data/raw/legal_corpus/SGP/CANDIDATES.md](../../../data/raw/legal_corpus/SGP/CANDIDATES.md) — 7 docs, corrección IAPP.
- [data/raw/legal_corpus/GHA/CANDIDATES.md](../../../data/raw/legal_corpus/GHA/CANDIDATES.md) — 4 docs, leyes sectoriales + estrategia.
- [data/raw/legal_corpus/BGD/CANDIDATES.md](../../../data/raw/legal_corpus/BGD/CANDIDATES.md) — validado por usuario.

---

## 1. `manifest.csv`

Cabecera exacta (18 columnas):

```
iso3,filename,document_title,doc_type,issuer,publication_date,status,language,source_url_primary,source_url_mirror,source_domain,retrieved_date,retrieval_http_status,retrieval_method,sha256,size_bytes,pages,notes
```

**Convenciones:**
- `doc_type`: `binding_law_sectoral | binding_law_ai | strategy | policy_strategy | policy_draft | soft_framework | soft_framework_sectoral | readiness_assessment | guidelines | bill_pending`.
- `status`: `in_force | in_use | draft_under_review | draft_public_consultation | historical_with_effect | official_joint_publication | bill_pending | approved_cabinet_{FECHA}`.
- `publication_date`: `YYYY-MM-DD` | `YYYY-MM` | `YYYY`.
- `retrieved_date`: fecha del sistema al descargar.
- `retrieval_method`: string con comando usado (ej. `"curl -sLk -A Chrome/120 -H Referer:sso.agc.gov.sg"`).
- `pages`: vacío si no verificable fácilmente.
- `notes`: español, ≤3 oraciones, por qué este documento se eligió + status.

---

## 2. `SOURCES.md`

Secciones exactas, en este orden:

1. **Cabecera** — país, ISO3, fecha de recopilación, codificador.
2. **Citas en formato académico (APA 7)** — una por documento, orden cronológico.
3. **Tabla de trazabilidad completa** — columnas: `#`, `Documento`, `URL de descarga efectiva`, `Dominio`, `HTTP`, `Tamaño`, `SHA-256` (primeros 8 chars + últimos 4).
4. **Evidencia de oficialidad por documento** — un bloque por documento: emisor declarado, aprobación/fecha, dominio de hosting, status, relevancia IA.
5. **Verificación de integridad** — párrafo corto sobre SHA-256 y reproducibilidad.
6. **Fuentes complementarias (no incorporadas al corpus)** — documentos identificados que no cumplen criterios (think tanks, académicos, borradores no publicados). Registrarlos en transparencia.
7. **Notas de proceso** — decisiones editoriales, URLs no accesibles, mirrors usados, políticas de actualización.

---

## 3. `CANDIDATES.md`

Secciones exactas, en este orden:

1. **Cabecera** — país, fecha, codificador, `Revisor humano: [PENDIENTE]`, confidence IAPP actual → propuesta, links a SOURCES.md y manifest.csv.

2. **Codificación actual (IAPP / OECD base)** — tabla con `has_ai_law`, `regulatory_approach`, `regulatory_intensity`, `enforcement_level`, `thematic_coverage`, `regulatory_regime_group`, `ai_year_enacted`, `ai_framework_note`. Consultar `data/raw/IAPP/iapp_x1_core.csv`.

3. **Diagnóstico preliminar** — 1 párrafo: por qué la codificación actual es/no es correcta.

4. **Inventario de instrumentos estatales IA** — tabla con una fila por documento (incluidos no descargables, con la razón).

5. **Candidatos uno por uno** — para cada documento descargado:
   - Metadatos (título, emisor, fecha, URL, SHA-256, idioma).
   - Rol en corpus IA.
   - Citas textuales clave (3-5 relevantes para justificar recodificación). Marcadas con `>` Markdown.

6. **Recodificación X1 propuesta** — tabla: `Variable | Actual (IAPP) | Propuesta | Justificación (con cita)`.

7. **Diff summary** — bloque de código con cambios:
   ```
   has_ai_law:              0 -> 0
   regulatory_intensity:    2 -> 4          (+2)
   ...
   regulatory_regime_group: strategy_only -> soft_framework  (UPGRADE ✅)
   confidence:              low -> medium-high
   ```

8. **Fundamento del upgrade/downgrade de régimen** — criterios cumplidos; por qué SÍ / por qué NO el bucket adyacente.

9. **Comparación con pilotos ya procesados** (si aplica) — tabla mostrando el país nuevo vs BGD/GHA/SGP/MNG para contextualizar.

10. **Checklist de validación humana** — por candidato, 6-7 ítems con `[ ]`.

11. **Decisión del revisor** — bloque con `[ ] APROBAR / [ ] RECHAZAR / [ ] PEDIR OTRA FUENTE` por candidato + por diff + por régimen.

12. **Notas del codificador** — limitaciones, diferencias frente a IAPP, siguientes pasos sugeridos.

---

## Checklist final antes de entregar

- [ ] Todos los PDFs validados con `file` como "PDF document".
- [ ] SHA-256 calculado para todos.
- [ ] `manifest.csv` tiene 18 columnas y una fila por PDF.
- [ ] `SOURCES.md` tiene citas APA 7 para todos los docs.
- [ ] `CANDIDATES.md` tiene inventario completo (incluidos no descargables).
- [ ] `FINDINGS.md` generado según esquema de [findings.md](findings.md) — 8 secciones, métricas calculadas desde manifest.csv, ≥2 refutaciones, peer-group.
- [ ] `docs/HALLAZGOS_DIFERENCIALES.md` actualizado con la tesis del país bajo su bucket de régimen, contador N/86 incrementado.
- [ ] Recodificación propuesta con diff summary claro.
- [ ] Checklist de validación humana presente.
- [ ] Todos los links internos funcionan (nombres exactos).
- [ ] Comparación con pilotos previos si el régimen no es trivial.
- [ ] Tono del resumen final: terse, español, sin emojis, 2-4 frases + tesis diferencial (1 línea) + pregunta de continuación.
