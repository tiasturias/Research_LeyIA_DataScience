# IRL — Hallazgo Diferencial

## 1. Tesis del hallazgo diferencial

**Irlanda presenta el régimen de binding regulation más consolidado del corpus por su combinación única de EU AI Act directamente aplicable + DPC (Data Protection Commission) como autoridad GDPR con jurisdicción sobre las mayores Big Tech del mundo (Meta, Google, Apple, TikTok, Microsoft) y bill nacional avanzado (AI Bill 2026, General Scheme de febrero 2026) que creará la AI Office of Ireland y designará 15 autoridades sectoriales — posicionando a Irlanda como la jurisdicción donde se cruzan la regulación IA supranacional más estricta con la supervisión de datos más intensa de Europa.**

---

## 2. Evidencia cuantitativa — densidad del corpus

| Métrica | Valor | Cálculo |
|---|---|---|
| # documentos totales | 4 | count(manifest.csv) |
| # binding (law + sectoral) | 1 | EU AI Act |
| # soft/policy/strategy | 3 | 2 estrategias + bill_pending |
| Páginas totales corpus | 429 | sum(pages) |
| Páginas binding / soft | 144 / 285 | 0.51:1 |
| Primer documento (fecha) | 2021-07 | National AI Strategy 2021 |
| Último documento (fecha) | 2026-02 | AI Bill 2026 General Scheme |
| Años cubiertos | 4.5 | (2026-02 - 2021-07) |
| Gap con fecha corpus | ~2 meses | 2026-04-21 - 2026-02 |
| # docs superseded | 0 | Ningún documento reemplazado |

---

## 3. Evidencia cuantitativa — timeline y proceso

| Fecha | Hito | Detalle |
|---|---|---|
| 2021-07 | National AI Strategy 2021 | Estrategia IA nacional base. "AI – Here for Good." |
| 2024-07-12 | EU AI Act publication | OJ L 2024/1689. Entrada en vigor 01-08-2024. |
| 2024-10 | National AI Strategy Refresh 2024 | Actualización post-AI Act. Posiciona a IRL como hub IA europeo. |
| 2026-02 | AI Bill 2026 General Scheme | Anteproyecto nacional. Crea AI Office, 15 autoridades sectoriales. Operativo previsto 01-08-2026. |

**Duración:** 4.5 años de evolución regulatoria.
**Emisor principal:** Department of Enterprise, Trade and Employment / DPC.
**Diferencial:** Hub Big Tech + DPC con jurisdicción GDPR principal UE.

---

## 4. Datos que FORTALECEN la tesis

- **EU AI Act directamente aplicable desde agosto 2024** — Regulation (EU) 2024/1689. Prohibiciones absolutas (Art. 5), obligaciones proveedores/deployers, sanciones hasta €35M o 7% facturación global (Art. 99).

- **DPC como autoridad principal de Big Tech** — Data Protection Commission tiene jurisdicción GDPR sobre Meta (multa €1.2B, 2023), WhatsApp (€225M, 2021), y todas las Big Tech con sede europea en Irlanda. Designada como Market Surveillance Authority en AI Bill 2026.

- **AI Bill 2026 General Scheme (180pp)** — Anteproyecto publicado feb 2026. Crea AI Office of Ireland (Oifig Intleachta Shaorga na hÉireann), designa 15 autoridades competentes sectoriales, establece sanciones nacionales adicionales (€500K).

- **National AI Strategy Refresh 2024 explícitamente pro-hub** — Citado: "Ireland's ambition is to be the best place in Europe to develop and deploy AI."

- **AI Office operativa prevista agosto 2026** — Simultánea con aplicación plena del EU AI Act.

- **Historial de enforcement GDPR de 8 cifras** — DPC tiene track record de enforcement más intenso que cualquier otra DPA europea.

---

## 5. Datos que REFUTAN la tesis (stress test honesto)

- **AI Bill no es ley promulgada** — General Scheme (anteproyecto) ≠ ley. Puede modificarse o retrasarse. *Refutador primario.* La AI Office no está operativa aún.

- **AI Act aplicable a todos los EEMM** — El EU AI Act no es diferencial de IRL per se. Todos los países EU del corpus tienen el mismo AI Act. La diferencia está en la institucionalidad (DPC + bill).

- **DPC no es autoridad IA específica** — La DPC es DPA/GDPR, no agencia IA dedicada. El AI Office será el coordinador IA, no aún creado.

- **Multas IA Act no impuestas aún** — Ningún caso de enforcement bajo AI Act publicado al cierre del corpus. Efectividad por verificar.

- **NLD tiene AP con DCA dedicado** — Países Bajos también tiene DPA fuerte con historial de enforcement. La tesis se distingue por DPC + bill avanzado.

---

## 6. Comparación vs peer group

| País | Régimen | # docs | # binding | Tesis diferencial |
|---|---|---|---|---|
| FRA | binding_regulation | 5 | 1 | AI Act + CNIL activa + ley national en desarrollo |
| ESP | binding_regulation | 5 | 1 | AI Act + AESIA activa + sandbox IA |
| **IRL** | **binding_regulation** | **4** | **1** | **AI Act + DPC jurisdicción Big Tech + AI Bill 2026 creando AI Office** |
| AUT | binding_regulation | 4 | 1 | AI Act + estrategia madura pero incumplimiento plazo |
| NLD | binding_regulation | 5 | 1 | AI Act + DCA dedicado + Algoritmeregister |

**Análisis:** IRL comparte el bucket binding_regulation con FRA, ESP, AUT, NLD. Se distingue por:
- DPC con jurisdicción Big Tech más intensa de la UE
- AI Bill 2026 General Scheme más avanzado que leyes nacionales de otros EEMM
- Objetivo explícito de hub IA europeo
- 4 documentos, 1 ley binding = menor # docs pero mayor profundidad institucional

**Contraste:** IRL ≈ NLD (ambos con DPA fuerte + enforcement) pero IRL con jurisdicción Big Tech más directa.

---

## 7. Implicancias para el estudio

| Variable X1 | Efecto potencial |
|---|---|
| `has_ai_law` | 1 (EU AI Act directamente aplicable) |
| `regulatory_intensity` | 10/10 (confirmado — máximo) |
| `thematic_coverage` | 14/15 (confirmado) |
| `enforcement_level` | `high` (confirmado — DPC + AI Bill) |
| `regulatory_regime_group` | `binding_regulation` (confirmado) |
| `has_dedicated_ai_authority` | 0 (AI Office operativa agosto 2026) |

**Hipótesis testeable:**
- ¿Países con DPA con jurisdicción Big Tech (IRL, NLD) tienen mejor enforcement que países sin ella?
- ¿La concentración de Big Tech en IRL afecta outcomes de adopción/inversión?

**Caso narrativo útil para:**
- §Discusión como "caso de binding regulation con jurisdicción Big Tech"
- Control para tesis "EU AI Act igual para todos"
- Comparación con NLD (DPA), AUT (estrategia), ESP (AESIA)

---

## 8. Banderas de re-visita

| Evento | Horizonte | Trigger observable |
|---|---|---|
| AI Bill 2026 aprobado por Dáil | 1-3m | oireachtas.ie publicación |
| AI Office operativa | 3-6m | enterprise.gov.ie |
| DPC enforcement casos AI Act | 6-12m | DPC decisiones publicadas |
| Aplicación plena EU AI Act | 3m | 01-08-2026 |
| AI Growth Zones Ireland | 6-12m | Anuncio DETE |

---

## Links

- [CANDIDATES.md](CANDIDATES.md)
- [SOURCES.md](SOURCES.md)
- [manifest.csv](manifest.csv)