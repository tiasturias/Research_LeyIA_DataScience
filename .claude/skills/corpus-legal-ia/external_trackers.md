# Trackers externos — workflow híbrido de discovery

Recursos de terceros usados como **pista de discovery previa**, no como fuente primaria. Todo documento descubierto aquí debe descargarse del dominio oficial del emisor estatal y cumplir R1-R5.

---

## 1. Techieray — Global AI Regulation Tracker

**Autor:** Raymond Sun (abogado tech, Australia). Curado manualmente.

**URLs:**
- Mapa interactivo: https://www.techieray.com/GlobalAIRegulationTracker
- Substack (metodología + updates): https://techieray.substack.com/
- Cliente Python MIT: https://github.com/aegis-blue-ai/ai-reg-tracker
- Paquete PyPI: https://pypi.org/project/ai-reg-tracker/

**Cobertura:** 195+ jurisdicciones, 8 categorías:
1. Latest Macro Developments
2. Sector Developments
3. Bilateral & Multilateral Engagements
4. Official Materials & Public Communications
5. Acts, Bills & Reforms
6. Guidelines, Frameworks & Standards
7. Executive & Regulatory Instruments
8. (categoría residual según país)

**Qué entrega:** metadata + `href` a la fuente oficial. **NO entrega PDFs.** El documento sigue viviendo en el dominio del emisor (regjeringen.no, bundestag.de, etc.).

**NO entrega:** taxonomía de régimen (binding/voluntary/strategy). Sus categorías son temáticas, no tipológicas → no reemplaza `recoding.md`.

**Licencia/acceso:**
- Sitio web y mapa: **gratis**, navegable en browser.
- Substack: **gratis** con email.
- API Python: **paga** ($25-$200/mes). Commercial use prohibido. Redistribución de data prohibida.
- Repo GitHub: código MIT, pero la data vive detrás de API key.

## 2. Workflow híbrido gratuito (adoptado abril 2026)

**Regla:** antes de ejecutar las búsquedas web de las 6 capas para cualquier país pendiente, hacer cross-check manual en techieray.

### Pasos

1. **Abrir** `https://www.techieray.com/GlobalAIRegulationTracker` en el browser.
2. **Seleccionar** el país en el mapa o filtro.
3. **Leer las 8 categorías** (~3-5 min). Anotar en scratchpad:
   - Títulos de documentos no vistos en búsqueda inicial.
   - Fechas de publicación.
   - Emisores estatales (ministerios, agencias).
   - Bills en tramitación con número/fecha de proyecto.
4. **Ejecutar las 6 capas normales** de [pipeline.md](pipeline.md), **usando los títulos anotados como queries dirigidas** adicionales.
5. **Descargar** del dominio oficial siguiendo [download.md](download.md). Nunca copiar texto/JSON de techieray.
6. **En CANDIDATES.md §Notas de proceso**, añadir línea: *"Cross-check techieray ejecutado dd-mm-aaaa. Descubrimientos incrementales: [lista] / ninguno."*

### Qué NO hacer

- Copiar descripción o metadata de techieray al corpus (viola licencia).
- Citar techieray como fuente primaria en `source_url_primary` (R1 exige dominio del emisor).
- Incluir techieray en `SOURCES.md`. Si el cross-check aporta, se menciona solo en `CANDIDATES.md §Notas de proceso`.
- Tratar la ausencia en techieray como evidencia de ausencia del documento — Raymond Sun no es exhaustivo al 100%.

### Cuándo escalar a API paga ($25 Mini)

Solo si se justifica un script programático que compare los 86 `manifest.csv` contra el índice techieray y emita un diff global. Uso táctico ≤1 mes, cancelar al terminar. Aun con API, los PDFs se descargan manualmente del dominio oficial.

## 3. Otros trackers útiles (referencia, gratis)

- **OECD AI Policy Observatory** — https://oecd.ai/en/dashboards/countries — perfiles país. No co-emisor (excluido del corpus por Capa 5) pero útil para cross-check.
- **IAPP Global AI Law and Policy Tracker** — fuente primaria del x1_core. Ya integrado.
- **Stanford AI Index — Policy section** — https://aiindex.stanford.edu — benchmark comparado.
- **Future of Life Institute — AI Policy** — https://futureoflife.org/ai-policy/ — tracking bills.
- **Library of Congress — Regulation of AI in Selected Jurisdictions** — https://www.loc.gov/item/2023555920/ — textos comparados.
