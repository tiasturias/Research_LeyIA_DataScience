# Muestra autoritativa del estudio (86 países)

Fuente: `data/interim/sample_ready_cross_section.csv` — la muestra final del estudio "¿Regular o no regular?".

## Tabla maestra de estado

Leyenda status:
- `DONE` — Carpeta `data/raw/legal_corpus/{ISO3}/` con CANDIDATES.md aprobado o pendiente aprobación.
- `PENDING` — Aún no procesado.
- `OUTSIDE` — Procesado pero fuera de la muestra de 86 (referencia externa solamente).

Leyenda prioridad:
- `P1-TOP30` — Top 30 Microsoft AI Diffusion Report 2025 (prioridad máxima).
- `P2-IAPP-LOW` — Países IAPP baja confianza / "Additional research".
- `P3-SAMPLE` — Resto de la muestra.
- `FOCAL` — Chile: caso focal del estudio (procesar después de cubrir Top 30).

| # | ISO3 | País | Región | EU AI Act | Prioridad | Status | Régimen propuesto | Aprobado | Fecha |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ARE | United Arab Emirates | MENA | No | P1-TOP30 | DONE | soft_framework | Sí | 2026-04-16 |
| 2 | ARG | Argentina | LATAM | No | P3-SAMPLE | PENDING | — | — | — |
|  3 | ARM | Armenia | Europe-Other | No | P2-IAPP-LOW | DONE | strategy_only | Pendiente | 2026-04-23 |
| 4 | AUS | Australia | Oceania | No | P1-TOP30 | DONE | soft_framework | Sí | 2026-04-21 |
| 5 | AUT | Austria | EU | Sí | P1-TOP30 | DONE | binding_regulation | Sí | 2026-04-19 |
| 6 | BEL | Belgium | EU | Sí | P1-TOP30 | DONE | binding_regulation | Sí | 2026-04-19 |
| 7 | BGD | Bangladesh | South Asia | No | P2-IAPP-LOW | DONE | soft_framework | Sí | 2026-04-15 |
| 8 | BGR | Bulgaria | EU | Sí | P1-TOP30 | DONE | binding_regulation | Pendiente | 2026-04-22 |
|  9 | BHR | Bahrain | MENA | No | P2-IAPP-LOW | DONE | soft_framework | Pendiente | 2026-04-23 |
| 10 | BLR | Belarus | Europe-Other | No | P2-IAPP-LOW | DONE | soft_framework | Pendiente | 2026-04-27 |
| 11 | BLZ | Belize | LATAM | No | P2-IAPP-LOW | PENDING | — | — | — |
| 12 | BRA | Brazil | LATAM | No | P3-SAMPLE | PENDING | — | — | — |
| 13 | BRB | Barbados | LATAM | No | P2-IAPP-LOW | PENDING | — | — | — |
| 14 | CAN | Canada | North America | No | P1-TOP30 | DONE | soft_framework | Pendiente | 2026-04-21 |
| 15 | CHE | Switzerland | Europe-Other | No | P1-TOP30 | DONE | soft_framework | Pendiente | 2026-04-22 |
| 16 | CHL | Chile | LATAM | No | FOCAL | PENDING | — | — | — |
| 17 | CHN | China | East Asia | No | P3-SAMPLE | PENDING | — | — | — |
| 18 | CMR | Cameroon | Sub-Saharan Africa | No | P2-IAPP-LOW | DONE | strategy_only | Pendiente | 2026-04-23 |
| 19 | COL | Colombia | LATAM | No | P3-SAMPLE | PENDING | — | — | — |
| 20 | CRI | Costa Rica | LATAM | No | P1-TOP30 | DONE | soft_framework | Pendiente | 2026-04-22 |
| 21 | CYP | Cyprus | EU | Sí | P3-SAMPLE | PENDING | — | — | — |
| 22 | CZE | Czechia | EU | Sí | P1-TOP30 | DONE | binding_regulation | Sí | 2026-04-22 |
| 23 | DEU | Germany | EU | Sí | P1-TOP30 | DONE | binding_regulation | Pendiente | 2026-04-20 |
| 24 | DNK | Denmark | EU | Sí | P1-TOP30 | DONE | binding_regulation | Pendiente | 2026-04-19 |
| 25 | ECU | Ecuador | LATAM | No | P2-IAPP-LOW | PENDING | — | — | — |
| 26 | EGY | Egypt | MENA | No | P3-SAMPLE | PENDING | — | — | — |
| 27 | ESP | Spain | EU | Sí | P1-TOP30 | DONE | binding_regulation | Pendiente | 2026-04-19 |
| 28 | EST | Estonia | EU | Sí | P3-SAMPLE | PENDING | — | — | — |
| 29 | FIN | Finland | EU | Sí | P1-TOP30 | DONE | binding_regulation | Pendiente | 2026-04-27 |
| 30 | FRA | France | EU | Sí | P1-TOP30 | DONE | binding_regulation | Pendiente | 2026-04-19 |
| 31 | GBR | United Kingdom | Europe-Other | No | P1-TOP30 | DONE | soft_framework | Pendiente | 2026-04-20 |
| 32 | GHA | Ghana | Sub-Saharan Africa | No | P2-IAPP-LOW | DONE | soft_framework | Sí | 2026-04-15 |
| 33 | GRC | Greece | EU | Sí | P3-SAMPLE | PENDING | — | — | — |
| 34 | HRV | Croatia | EU | Sí | P3-SAMPLE | PENDING | — | — | — |
| 35 | HUN | Hungary | EU | Sí | P1-TOP30 | DONE | binding_regulation | Sí | 2026-04-19 |
| 36 | IDN | Indonesia | Southeast Asia | No | P3-SAMPLE | PENDING | — | — | — |
| 37 | IND | India | South Asia | No | P3-SAMPLE | DONE | soft_framework | Sí | 2026-04-27 |
| 38 | IRL | Ireland | EU | Sí | P1-TOP30 | DONE | binding_regulation | Pendiente | 2026-04-17 |
| 39 | ISL | Iceland | Europe-Other | No | P2-IAPP-LOW | PENDING | — | — | — |
| 40 | ISR | Israel | MENA | No | P1-TOP30 | DONE | soft_framework | Pendiente | 2026-04-17 |
| 41 | ITA | Italy | EU | Sí | P1-TOP30 | DONE | binding_regulation | Sí | 2026-04-22 |
| 42 | JOR | Jordan | MENA | No | P1-TOP30 | DONE | soft_framework | Pendiente | 2026-04-22 |
| 43 | JPN | Japan | East Asia | No | P3-SAMPLE | DONE | binding_regulation | Pendiente | 2026-04-27 |
| 44 | KAZ | Kazakhstan | Central Asia | No | P2-IAPP-LOW | DONE | binding_regulation | Pendiente | 2026-04-23 |
| 45 | KEN | Kenya | Sub-Saharan Africa | No | P3-SAMPLE | PENDING | — | — | — |
| 46 | KOR | South Korea | East Asia | No | P1-TOP30 | DONE | binding_regulation | Sí | 2026-04-22 |
| 47 | LBN | Lebanon | MENA | No | P2-IAPP-LOW | DONE | strategy_only | Pendiente | 2026-04-23 |
| 48 | LKA | Sri Lanka | South Asia | No | P2-IAPP-LOW | PENDING | — | — | — |
| 49 | LTU | Lithuania | EU | Sí | P3-SAMPLE | PENDING | — | — | — |
| 50 | LUX | Luxembourg | EU | Sí | P3-SAMPLE | PENDING | — | — | — |
| 51 | LVA | Latvia | EU | Sí | P3-SAMPLE | PENDING | — | — | — |
| 52 | MAR | Morocco | MENA | No | P2-IAPP-LOW | PENDING | — | — | — |
| 53 | MEX | Mexico | LATAM | No | P2-IAPP-LOW | PENDING | — | — | — |
| 54 | MLT | Malta | EU | Sí | P3-SAMPLE | PENDING | — | — | — |
| 55 | MNG | Mongolia | East Asia | No | P2-IAPP-LOW | DONE | soft_framework | Sí | 2026-04-15 |
| 56 | MUS | Mauritius | Sub-Saharan Africa | No | P3-SAMPLE | PENDING | — | — | — |
| 57 | MYS | Malaysia | Southeast Asia | No | P2-IAPP-LOW | PENDING | — | — | — |
| 58 | NGA | Nigeria | Sub-Saharan Africa | No | P3-SAMPLE | PENDING | — | — | — |
| 59 | NLD | Netherlands | EU | Sí | P1-TOP30 | DONE | binding_regulation | Sí | 2026-04-19 |
| 60 | NOR | Norway | Europe-Other | No | P1-TOP30 | DONE | soft_framework | Pendiente | 2026-04-20 |
| 61 | NZL | New Zealand | Oceania | No | P1-TOP30 | DONE | soft_framework | Sí | 2026-04-20 |
| 62 | PAK | Pakistan | South Asia | No | P2-IAPP-LOW | PENDING | — | — | — |
| 63 | PAN | Panama | LATAM | No | P2-IAPP-LOW | PENDING | — | — | — |
| 64 | PER | Peru | LATAM | No | P3-SAMPLE | PENDING | — | — | — |
| 65 | PHL | Philippines | Southeast Asia | No | P2-IAPP-LOW | PENDING | — | — | — |
| 66 | POL | Poland | EU | Sí | P1-TOP30 | DONE | binding_regulation | Pendiente | 2026-04-22 |
| 67 | PRT | Portugal | EU | Sí | P3-SAMPLE | PENDING | — | — | — |
| 68 | ROU | Romania | EU | Sí | P3-SAMPLE | PENDING | — | — | — |
| 69 | RUS | Russia | Europe-Other | No | P2-IAPP-LOW | PENDING | — | — | — |
| 70 | SAU | Saudi Arabia | MENA | No | P3-SAMPLE | PENDING | — | — | — |
| 71 | SGP | Singapore | Southeast Asia | No | P1-TOP30 | DONE | soft_framework | Sí | 2026-04-15 |
| 72 | SRB | Serbia | Europe-Other | No | P2-IAPP-LOW | PENDING | — | — | — |
| 73 | SVK | Slovakia | EU | Sí | P3-SAMPLE | PENDING | — | — | — |
| 74 | SVN | Slovenia | EU | Sí | P3-SAMPLE | PENDING | — | — | — |
| 75 | SWE | Sweden | EU | Sí | P1-TOP30 | DONE | binding_regulation | Sí | 2026-04-19 |
| 76 | SYC | Seychelles | Sub-Saharan Africa | No | P2-IAPP-LOW | PENDING | — | — | — |
| 77 | THA | Thailand | Southeast Asia | No | P2-IAPP-LOW | PENDING | — | — | — |
| 78 | TUN | Tunisia | MENA | No | P2-IAPP-LOW | PENDING | — | — | — |
| 79 | TUR | Turkey | Europe-Other | No | P3-SAMPLE | PENDING | — | — | — |
| 80 | TWN | Taiwan | East Asia | No | P1-TOP30 | DONE | binding_regulation | Sí | 2026-04-16 |
| 81 | UGA | Uganda | Sub-Saharan Africa | No | P2-IAPP-LOW | PENDING | — | — | — |
| 82 | UKR | Ukraine | Europe-Other | No | P2-IAPP-LOW | PENDING | — | — | — |
| 83 | URY | Uruguay | LATAM | No | P2-IAPP-LOW | PENDING | — | — | — |
| 84 | USA | United States | North America | No | P1-TOP30 | DONE | soft_framework | Pendiente | 2026-04-22 |
| 85 | VNM | Vietnam | Southeast Asia | No | P3-SAMPLE | PENDING | — | — | — |
| 86 | ZAF | South Africa | Sub-Saharan Africa | No | P3-SAMPLE | PENDING | — | — | — |

## Países fuera de muestra (procesados como referencia)

| ISO3 | País | Status | Régimen | Nota |
|---|---|---|---|---|
| QAT | Qatar | DONE | soft_framework | Top 30 Microsoft pero fuera de muestra de 86. Útil como benchmark regional Golfo. No integrar a x1_master_v2.csv. |

## Contadores

- **Total muestra:** 86
- **Completados (en muestra):** 38 / 86
- **Pendientes:** 48 / 86
- **Fuera de muestra procesados:** 1 (QAT)

## Orden de ejecución por prioridad

1. **P1-TOP30** (29 en muestra, 29 done, 0 pending): ARE✅, SGP✅, TWN✅, ISR✅, IRL✅, FRA✅, ESP✅, NLD✅, BEL✅, SWE✅, AUT✅, HUN✅, DNK✅, DEU✅, NOR✅, NZL✅, GBR✅, AUS✅, CAN✅, CHE✅, POL✅, CZE✅, KOR✅, ITA✅, BGR✅, CRI✅, JOR✅, USA✅, FIN✅.
2. **P2-IAPP-LOW** (20 en muestra, 4 done, 16 pending): ARM✅, BGD✅, BHR✅, BLR✅, CMR✅, GHA✅, KAZ✅, LBN✅, MNG✅, ISL, LKA, MAR, MEX, MYS, PAK, PAN, PHL, RUS, SRB, SYC, THA, TUN, UGA, UKR, URY, ECU.
3. **P3-SAMPLE** (31 en muestra, 2 done): ARG, BRA, CHN, COL, CYP, EGY, EST, GRC, HRV, IDN, IND✅, JPN✅, KEN, LTU, LUX, LVA, MLT, MUS, NGA, PER, PRT, ROU, SAU, SVK, SVN, TUR, VNM, ZAF.
4. **FOCAL** (1): CHL — procesar después del Top 30 para tener contexto comparado.

## Regla "continúa"

Si el usuario dice "continúa" sin especificar país, tomar el siguiente PENDING de P1-TOP30 en el orden listado arriba. Si P1 está completo, pasar a P2-IAPP-LOW. Si P2 está completo, pasar a P3-SAMPLE. FOCAL (CHL) solo cuando el usuario lo indique expresamente.
