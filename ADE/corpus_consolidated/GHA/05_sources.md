# GHA — Fuentes bibliográficas formales

**País:** Ghana (ISO3: GHA)
**Fecha de recopilación:** 2026-04-15
**Codificador:** Claude Opus 4.6 (asistido)

Este archivo consolida las fuentes documentales oficiales del corpus IA de Ghana en formato citable para el informe final del estudio. Cada entrada incluye la URL primaria utilizada para la descarga, el hash SHA-256 del archivo capturado y los metadatos de trazabilidad.

---

## Citas en formato académico (APA 7)

1. **Parliament of the Republic of Ghana.** (2012). *Data Protection Act, 2012 (Act 843)*. National Information Technology Agency (NITA). Recuperado el 15 de abril de 2026, de https://nita.gov.gh/wp-content/uploads/2017/12/Data-Protection-Act-2012-Act-843.pdf

2. **Parliament of the Republic of Ghana.** (2020, 29 de diciembre). *Cybersecurity Act, 2020 (Act 1038)*. Cyber Security Authority (CSA). Recuperado el 15 de abril de 2026, de https://www.csa.gov.gh/resources/cybersecurity_Act_2020(Act_1038).pdf

3. **Ministry of Communications and Digitalisation, Republic of Ghana.** (2022, octubre). *Republic of Ghana National Artificial Intelligence Strategy: 2023–2033*. Developed in collaboration with Smart Africa, GIZ FAIR Forward, and The Future Society. Recuperado el 15 de abril de 2026, de https://www.africadataprotection.org/Ghana-AI-Strat.pdf

4. **Ministry of Communications and Digitalisation, Republic of Ghana.** (2024, mayo). *Ghana Digital Economy Policy and Strategy*. Recuperado el 15 de abril de 2026, de https://moc.gov.gh/wp-content/uploads/2023/03/Ghana-Digital-Economy-Policy-Strategy.pdf

---

## Tabla de trazabilidad completa

| # | Documento | URL de descarga efectiva | Dominio | HTTP | Tamaño | SHA-256 |
|---|---|---|---|---|---|---|
| 1 | Data Protection Act 2012 (Act 843) | https://nita.gov.gh/wp-content/uploads/2017/12/Data-Protection-Act-2012-Act-843.pdf | nita.gov.gh | 200 | 364 KB | `7f12c273...358c` |
| 2 | Cybersecurity Act 2020 (Act 1038) | https://www.csa.gov.gh/resources/cybersecurity_Act_2020(Act_1038).pdf | csa.gov.gh | 200 | 545 KB | `e4c535fd...f9a1` |
| 3 | National AI Strategy 2023-2033 | https://www.africadataprotection.org/Ghana-AI-Strat.pdf | africadataprotection.org (mirror) | 200 | 6.0 MB | `39e99634...e929` |
| 4 | Digital Economy Policy and Strategy | https://moc.gov.gh/wp-content/uploads/2023/03/Ghana-Digital-Economy-Policy-Strategy.pdf | moc.gov.gh | 200 | 19 MB | `f11d7f29...be79` |

---

## Evidencia de oficialidad por documento

### 1. Data Protection Act, 2012 (Act 843)
- **Emisor:** Parliament of the Republic of Ghana (ley vinculante sectorial).
- **Dominio de hosting:** `nita.gov.gh` — National Information Technology Agency (agencia estatal).
- **Status:** En vigor desde 2012. Establece la **Data Protection Commission (DPC)** como autoridad regulatoria.
- **Relevancia IA:** Regula procesamiento automatizado de datos personales, aplicable directamente a sistemas IA que procesen datos de ciudadanos ghaneses. Referenciado en NAIS como pilar regulatorio base.

### 2. Cybersecurity Act, 2020 (Act 1038)
- **Emisor:** Parliament of the Republic of Ghana.
- **Aprobación:** Pasada por 7° Parlamento el 2020-11-06; asentida por Presidente Akufo-Addo el 2020-12-29.
- **Dominio de hosting:** `csa.gov.gh` — Cyber Security Authority (agencia estatal creada por esta misma ley).
- **Status:** En vigor. Establece la **Cyber Security Authority (CSA)**.
- **Relevancia IA:** Regula seguridad de sistemas digitales críticos, aplicable a infraestructura IA y sistemas automatizados de toma de decisiones. Referenciado como instrumento adyacente en la estrategia IA.

### 3. National AI Strategy 2023-2033
- **Portada del PDF (palabras literales):** "Republic of Ghana National Artificial Intelligence Strategy: 2023-2033 ... Developed by the Ministry of Communications and Digitalisation with Smart Africa, GIZ FAIR Forward, and The Future Society (TFS). October 2022."
- **Emisor declarado:** Ministry of Communications and Digitalisation (MoCD), Republic of Ghana.
- **Co-desarrollado con:** Smart Africa (organismo intergubernamental africano), GIZ FAIR Forward (cooperación alemana), The Future Society (think tank).
- **Acknowledgements internos (p.8):** "Through the Data Protection Commission, the Ministry of Communications and Digitalisation collaborated with Smart Africa, GIZ FAIR Forward, and The Future Society (TFS) to develop the Ghana National Artificial Intelligence Strategy."
- **Status actual:** Aprobada por Cabinet; formalmente lanzada por el Presidente John Dramani Mahama el 24 de abril de 2026.
- **Dominio de hosting:** `africadataprotection.org` (mirror estable; el PDF NO está publicado directamente en `moc.gov.gh`; el ministerio sí anunció la estrategia en su portal pero no aloja el PDF descargable — verificado en `https://moc.gov.gh/downloads/`).
- **Limitación documentada:** aunque el hosting es en un mirror no gubernamental, la autoría gubernamental está evidenciada en la portada y acknowledgements internos del documento. Es la única URL pública accesible al momento de recopilación.

### 4. Digital Economy Policy and Strategy
- **Emisor declarado:** Ministry of Communications and Digitalisation (MoCD), Republic of Ghana.
- **Contiene:** "Foreword from the President" y "Statement by the Minister" (firma gubernamental explícita).
- **Status:** Aprobada por Cabinet el 14 de mayo de 2024.
- **Dominio de hosting:** `moc.gov.gh` (dominio oficial del Ministerio).
- **Observación:** existe también una variante en `nita.gov.gh` (3.1 MB, escaneada sin texto extraíble) que fue descartada por inferior calidad técnica. El PDF de `moc.gov.gh` (19 MB, con texto extraíble) es la versión primaria.

---

## Verificación de integridad

SHA-256 calculados con `shasum -a 256` al momento de descarga. Cualquier re-captura debe producir el mismo hash para equivalencia.

---

## Fuentes complementarias (no incorporadas al corpus)

- **UNESCO Readiness Assessment Measurement (RAM) Ghana** — lanzado 2024-09-30 por MoCD + Data Protection Commission + UNESCO. Reporte final validado en noviembre 2025 pero aún sin publicación PDF pública al 2026-04-15. Útil como contexto pero no descargable.
- **Ghana AI Practitioners' Guide** (GIZ, Heritors Labs, 2025-09). Publicado por GIZ (cooperación alemana) — no es instrumento estatal, por lo que queda excluido del corpus analizable.
- **Emerging Technologies Bill** (anunciado 2026) — aún no presentado ante Parlamento al 2026-04-15. Sin PDF disponible.
- Digital Policy Alert. *DPA Digital Digest: Ghana [2025 Edition]*. https://digitalpolicyalert.org/digest/dpa-digital-digest-ghana
- Wilson Center. *Regulating Artificial Intelligence in Africa: Strategies and Insights from Kenya, Ghana, and the African Union*. https://www.wilsoncenter.org/blog-post/regulating-artificial-intelligence-africa-strategies-and-insights-kenya-ghana-and-african

---

## Notas de proceso

1. **Leyes vinculantes sectoriales priorizadas:** Ghana NO tiene una ley IA-específica al 2026-04-15, pero tiene dos leyes sectoriales vinculantes directamente aplicables al ciclo de vida de sistemas IA: Data Protection Act 2012 (procesamiento de datos) y Cybersecurity Act 2020 (seguridad de sistemas digitales). Ambas establecen autoridades regulatorias activas (DPC, CSA).

2. **URL primaria del NAIS en dominio gubernamental:** NO disponible al momento de captura. El MoCD anunció y promocionó la estrategia en su portal pero no aloja el PDF. La URL mirror (`africadataprotection.org`) es la única accesible; la autoría gubernamental está evidenciada en la portada e internos del documento.

3. **URL primaria del DEPS:** disponible directamente en `moc.gov.gh` (dominio oficial del Ministerio).

4. **Política de re-captura:** si el MoCD publica el NAIS en `moc.gov.gh` después de la ceremonia de lanzamiento del 24 abril 2026, re-capturar desde la URL gubernamental y actualizar `source_url_primary` (manteniendo el hash histórico como trazabilidad). Igualmente, si el Emerging Technologies Bill es presentado al Parlamento, incorporarlo como nuevo documento.
