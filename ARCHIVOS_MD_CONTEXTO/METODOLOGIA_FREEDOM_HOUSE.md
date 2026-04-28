# Metodologia de Codificacion Freedom House (Tarea A sub-tarea A.6)

## Contexto

La auditoria cientifica (Tarea A) detecto la necesidad de controlar por **tipo de
regimen politico / libertades civiles** como confounder de la regulacion IA.
Democracias y autoritarismos regulan IA con motivaciones radicalmente distintas:

- **Autoritarismos**: control de informacion, vigilancia masiva, censura, proteccion
  del regimen. Regulacion IA puede ser vehiculo de consolidacion autoritaria
  (p.ej. CHN con reglas de "algoritmos recomendadores", RUS con ley de IA estatal).
- **Democracias**: derechos del usuario, transparencia, rendicion de cuentas,
  prevencion de discriminacion algoritmica (p.ej. EU AI Act, Colorado AI Act).

Sin controlar por este factor, el efecto medido de `regulatory_intensity` sobre
`ai_readiness_score` puede confundirse con el efecto del tipo de regimen.

## Justificacion adicional por redundancia parcial con WGI

En la discusion previa a la codificacion se planteo que Freedom House podria ser
redundante con `rule_of_law`. La evidencia empirica muestra correlacion moderada
pero NO alta:

- `fh_total_score` x `regulatory_quality`: r = 0.685
- `fh_total_score` x `rule_of_law`:         r = 0.681
- `fh_total_score` x `gdpr_similarity_level`: r = 0.682

r ≈ 0.68 implica que FH captura ~54% de varianza NO explicada por WGI. Casos
emblematicos que ejemplifican la no-redundancia:

- **SGP** (Singapur): `rule_of_law` = +1.7 (muy alto), `fh_total_score` = 48 (PF).
  Estado de derecho economico solido, pero libertades politicas restringidas.
- **CHN**: `rule_of_law` = -0.2 (medio), `fh_total_score` = 9 (NF). Autoritario
  con rule_of_law nominal.
- **HUN**: `rule_of_law` = +0.4, `fh_total_score` = 65 (PF). Regresion democratica
  sin colapso institucional.

Estos casos confirman que FH agrega una dimension (libertades politicas/civiles)
ortogonal a la dimension de gobernanza tecnica que mide WGI.

## Evidencia empirica del confounding (N=72 confounded sample)

| regulatory_status_group | N  | fh_mean | % Free | % Not Free |
|---|---|---|---|---|
| binding_regulation       | 27 | 82.8    | 85.2   | 7.4  |
| strategy_only            | 34 | 60.7    | 41.2   | 20.6 |
| soft_framework           |  9 | 60.2    | 33.3   | 22.2 |
| no_framework             |  2 | 28.0    | 0.0    | 50.0 |

Gradiente monotonico clarisimo: paises con regulacion IA vinculante son 85%
Free (promedio 82.8), mientras paises sin marco tienen 50% Not Free (promedio 28).
Sin control por regimen politico, el "efecto de binding_regulation" se confunde
con el "efecto de ser democracia liberal consolidada".

## Fuente y fecha de corte

**Fuente primaria:** Freedom House *Freedom in the World 2025* (publicado marzo
2025, cubre eventos del ano 2024).

**Criterios FH (metodologia publica):**
- Political Rights (PR): 0-40 puntos, 10 preguntas agrupadas en 3 categorias
  (proceso electoral, pluralismo politico, funcionamiento del gobierno).
- Civil Liberties (CL): 0-60 puntos, 15 preguntas agrupadas en 4 categorias
  (libertad expresion/creencia, asociacion/organizacion, estado de derecho,
  autonomia individual).
- Total = PR + CL (rango teorico -4 a 100; score negativo en PR posible por
  "Additional discretionary question" en casos extremos, p.ej. CHN).
- Status:
  - F (Free): total 70-100
  - PF (Partly Free): total 35-69
  - NF (Not Free): total 0-34

**Fuente secundaria de validacion:** Freedom House "All Data, FIW 2013-2025.xlsx"
descargable en freedomhouse.org. Para publicacion final se recomienda
cross-check con este archivo autoritativo.

## Codificacion manual de los 86 paises

Se creo el archivo `data/raw/FreedomHouse/freedom_in_the_world_2025.csv` con
las siguientes columnas:

| Columna | Tipo | Descripcion |
|---|---|---|
| iso3 | str | Codigo ISO-3 |
| country_name | str | Nombre pais en FH |
| fh_status | F / PF / NF | Estatus FITW 2025 |
| fh_total_score | int 0-100 | Score agregado PR+CL |
| fh_pr_score | int | Subscore Political Rights |
| fh_cl_score | int | Subscore Civil Liberties |
| fh_year | int | Ano publicacion FH (2025) |
| notes | str | Comentarios por pais |

La variable derivada `fh_democracy_level` (0-2 ordinal) se construye en
`build_fh_master()`: NF→0, PF→1, F→2.

## Distribucion en la muestra (86 paises)

| Estatus | N | % |
|---|---|---|
| F (Free)        | 51 | 59.3 |
| PF (Partly Free)| 21 | 24.4 |
| NF (Not Free)   | 14 | 16.3 |

Rango de scores: 8 (BLR, SAU) a 100 (FIN, NOR, SWE). Media: 69.4.

## Casos de codificacion notables

- **CHN**: PR = -2 (negativo), CL = 11, Total = 9. Negative PR per metodologia FH
  ("Additional discretionary question"). Status NF.
- **PAK**: downgrade a NF en FITW 2025 tras elecciones 2024 cuestionadas y
  encarcelamiento de Imran Khan. Previamente PF (~35 puntos), ahora 27 NF.
- **HUN**: PF desde 2019, unico miembro UE classified PF. Continua en 65.
- **IND**: PF desde 2021, continua en 66 en 2025.
- **UKR**: PF en condiciones de guerra, 48 total. FH valida su democracia bajo
  condiciones excepcionales.
- **SGP**: PF historicamente (48), no F a pesar de prosperidad economica.
- **BGD**: transicion 2024 post-Hasina, codificado PF (40) reflejando periodo
  de transicion.
- **POL**: upgrade dentro de F tras elecciones 2023 (Tusk), 81 puntos.

## Limitaciones y avisos de validacion

1. **Verificacion final**: las puntuaciones exactas se basan en el conocimiento
   de FITW 2025 en el momento de la codificacion. Para publicacion academica se
   recomienda re-validar contra el Excel oficial "All Data, FIW 2013-2025.xlsx"
   de Freedom House. Errores de 1-3 puntos en scores individuales no afectan
   el status categorico ni la estructura del modelo.

2. **Uso canonico**: `fh_democracy_level` (ordinal 0-2) es robusto y recomendado
   como variable principal. `fh_total_score` (continuous 0-100) permite analisis
   mas fino pero incorpora el ruido de estimacion de los puntos exactos.

3. **Ano de referencia**: FITW 2025 cubre EL ANO 2024. Para analisis de
   series temporales, los scores anteriores deben venir del Excel oficial.

4. **Cyprus**: FH codifica solo "Cyprus" (areas bajo gobierno central, excluye
   territorio ocupado). Score refleja Republica de Chipre.

5. **Correlacion con otros controles**: ver seccion "Justificacion adicional"
   arriba. No hay colinearidad peligrosa (r < 0.70 con WGI y GDPR), pero al
   incluir FH + rule_of_law simultaneamente en una regresion se debe verificar
   VIF para ajuste de multicolinealidad.

## Clasificacion en la hierarchy del estudio

FH se incorpora como **robustness confounder**, NO core. Esto es consistente
con la decision A.5 (digital economy): variables que amplian el control pero
no se fuerzan al modelo principal si no cambian el N.

- `complete_principal`: **72/86** (sin cambio)
- `complete_confounded` (WGI + GDPR-like): **72/86** (sin cambio, tier recomendada)
- `complete_regime` (+ FH score + FH democracy level): **72/86** ← NUEVA
  - No reduce N porque FH cobertura 86/86
  - Para analisis de robustez al incluir regimen politico

**Uso recomendado:**
1. Modelo principal: `complete_confounded` (WGI + GDPR-like), N=72.
2. Modelo robusto regime: `complete_regime` (+ FH), N=72, verificar si
   el efecto de `regulatory_intensity` se mantiene al controlar por
   `fh_democracy_level`.
3. Interaccion heterogenea: testear si el efecto de regulacion IA varia por
   tipo de regimen (`regulatory_intensity` × `fh_democracy_level`).
