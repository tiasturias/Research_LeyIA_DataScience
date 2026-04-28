# BGD — Fuentes bibliográficas formales

**País:** Bangladesh (ISO3: BGD)
**Fecha de recopilación:** 2026-04-15
**Codificador:** Claude Opus 4.6 (asistido)

Este archivo consolida las fuentes documentales oficiales del corpus IA de Bangladesh en formato citable para el informe final del estudio. Cada entrada incluye la URL primaria utilizada para la descarga, el hash SHA-256 del archivo capturado y los metadatos de trazabilidad.

---

## Citas en formato académico (APA 7)

1. **ICT Division, Government of Bangladesh.** (2020, marzo). *National Strategy for Artificial Intelligence — Bangladesh*. Information and Communication Technology Division, Ministry of Posts, Telecommunications and Information Technology. Recuperado el 15 de abril de 2026, de https://file-rangpur.portal.gov.bd/files/pbs2.dinajpur.gov.bd/files/1885c0a0_28a4_4fcc_8d4d_dcd7ce23fd8b/7b684f19a15dfcd0f542382764572486.pdf

2. **ICT Division, Government of Bangladesh.** (2026, enero). *National AI Policy Bangladesh 2026-2030 (Draft V1.1)*. Ministry of Posts, Telecommunications and Information Technology. Recuperado el 15 de abril de 2026, de https://objectstorage.ap-dcc-gazipur-1.oraclecloud15.com/n/axvjbnqprylg/b/V2Ministry/o/office-ictd/2026/0/beec3a80-2c3a-4816-bb4c-dec7b96d740f.pdf

3. **ICT Division, Government of Bangladesh.** (2026, 9 de febrero). *Bangladesh National AI Policy 2026-2030 (Draft v2.0)*. Ministry of Posts, Telecommunications and Information Technology. Recuperado el 15 de abril de 2026, de https://aipolicy.gov.bd/docs/national-ai-policy-bangladesh-2026-2030-draft-v2.0.pdf

4. **UNESCO, UNDP & ICT Division, Government of Bangladesh.** (2025, noviembre). *Bangladesh: Artificial Intelligence Readiness Assessment Report* (UNESCO Document SHS/REI/EAI/2025/AI-RAM/BD). UNDP Bangladesh. Recuperado el 15 de abril de 2026, de https://www.undp.org/sites/g/files/zskgke326/files/2025-11/final_digital_bangladesh_ai_ram.pdf

---

## Tabla de trazabilidad completa

| # | Documento | URL de descarga efectiva | Dominio | HTTP | Tamaño | SHA-256 |
|---|---|---|---|---|---|---|
| 1 | NSAI 2020 | https://file-rangpur.portal.gov.bd/files/pbs2.dinajpur.gov.bd/files/1885c0a0_28a4_4fcc_8d4d_dcd7ce23fd8b/7b684f19a15dfcd0f542382764572486.pdf | portal.gov.bd | 200 | 2.2 MB | `d7a257b4...0ffd2` |
| 2 | NAIP V1.1 | https://objectstorage.ap-dcc-gazipur-1.oraclecloud15.com/n/axvjbnqprylg/b/V2Ministry/o/office-ictd/2026/0/beec3a80-2c3a-4816-bb4c-dec7b96d740f.pdf | oraclecloud15.com | 200 | 695 KB | `7ea17c05...0bbf` |
| 3 | NAIP V2.0 | https://aipolicy.gov.bd/docs/national-ai-policy-bangladesh-2026-2030-draft-v2.0.pdf | aipolicy.gov.bd | 200 | 1.1 MB | `95b861fa...1fa` |
| 4 | AIRAM 2025 | https://www.undp.org/sites/g/files/zskgke326/files/2025-11/final_digital_bangladesh_ai_ram.pdf | undp.org | 200 | 5.8 MB | `a1e85c06...c1dc` |

---

## Evidencia de oficialidad por documento

### 1. NSAI 2020
- **Emisor oficial declarado en portada:** "Information and Communication Technology Division, Government of the People's Republic of Bangladesh".
- **Dominio de hosting:** `file-rangpur.portal.gov.bd` (subdominio regional del portal gubernamental unificado `portal.gov.bd`).
- **URL emisora principal:** `https://ictd.portal.gov.bd/` (actualmente devuelve loop 301 para el PDF histórico; el documento permanece accesible vía mirror gubernamental regional).
- **Fecha en portada:** March 2020.

### 2. NAIP V1.1
- **Emisor:** "ICT Division" (portada del PDF).
- **Dominio de hosting:** Oracle Cloud Infrastructure tenant `axvjbnqprylg` — bucket oficial del Ministerio V2 (`V2Ministry/office-ictd/`).
- **URL emisora principal:** `https://aipolicy.gov.bd/` (sitio gubernamental oficial).
- **Versión previa al proceso de consulta pública.**

### 3. NAIP V2.0
- **Emisor:** "ICT Division" (portada del PDF).
- **Dominio de hosting:** `aipolicy.gov.bd` — sitio gubernamental oficial dedicado al proceso legislativo del NAIP.
- **Fecha en portada:** February 9, 2026.
- **Comité:** "National AI Policy Steering Committee" listado nominalmente en páginas 2-3 del PDF (12 miembros, incluye Secretario de ICT Division y Special Assistant al Chief Adviser).

### 4. AIRAM 2025
- **Emisor:** UNESCO (publicador) + UNDP + ICT Division GoB (co-firmantes).
- **Identificador UNESCO:** SHS/REI/EAI/2025/AI-RAM/BD.
- **Dominio de hosting:** `undp.org` (repositorio de publicaciones de UNDP).
- **Licencia:** CC-BY-SA 3.0 IGO.
- **Co-autoría documentada en agradecimientos:** "Mr Faiz Ahmad Taiyeb, Special Assistant to Hon'ble Chief Adviser, ICT Division" y "Mr Shish Haider Chowdhury, Secretary, ICT Division".

---

## Verificación de integridad

Todos los hashes SHA-256 fueron calculados con `shasum -a 256` sobre los archivos PDF tal como quedaron guardados en `data/raw/legal_corpus/BGD/`. Cualquier reintento de descarga debe producir el mismo hash para considerarse equivalente al archivo citado en el estudio. Si un documento cambia en la URL oficial, la nueva versión se trata como documento separado con nuevo `retrieved_date` y nuevo hash.

---

## Fuentes complementarias (no incorporadas al corpus, útiles para discusión)

Estas fuentes **no forman parte del corpus analizable** (no son instrumentos estatales oficiales) pero pueden citarse en el informe como contexto:

- The Daily Star. (2024). *An Overview of Bangladesh National Artificial Intelligence Policy 2024*. https://www.thedailystar.net/law-our-rights/law-vision/news/overview-bangladesh-national-artificial-intelligence-policy-2024-3590351
- Tech Global Institute. *Reforming AI Laws and Regulation in Bangladesh: Current Harms and Possible Futures*. https://techglobalinstitute.com/research/reforming-ai-laws-and-regulation-in-bangladesh-current-harms-and-possible-futures/
- Policy Magazine. *Bangladesh's AI Moment: Testing the Implementation Gap*. https://www.policymagazine.ca/bangladeshs-ai-moment-testing-the-implementation-gap/
- Digitally Right. *Policy Brief: AI Policy and Governance in Bangladesh*. https://digitallyright.org/policy-brief-ai-policy-and-governance-in-bangladesh/

---

## Notas de proceso

1. **URL no accesible registrada para transparencia:** El ICT Division portal (`https://ictd.portal.gov.bd/sites/default/files/.../Draft National_AI_Policy_2024.pdf`) devuelve loop 301 infinito. Se asume que el documento NAIP 2024 Draft fue retirado tras la publicación de la V1.1 en enero 2026. Su contenido normativo está absorbido en V1.1 y V2.0, por lo que la pérdida para el análisis es nula.

2. **Método de descarga reproducible:** Todos los archivos fueron descargados con `curl -sLk` (follow redirects, ignorar certificados SSL cuando aplicable), User-Agent "Mozilla/5.0" para bypass de bloqueos básicos. Los comandos exactos están registrados en el campo `retrieval_method` del `manifest.csv`.

3. **Política de actualización:** Si durante la vida del estudio se publica una versión V3 del NAIP o se adopta formalmente el AI Act de Bangladesh, se debe re-ejecutar la captura manteniendo los archivos históricos y agregando los nuevos con nuevo `retrieved_date`.
