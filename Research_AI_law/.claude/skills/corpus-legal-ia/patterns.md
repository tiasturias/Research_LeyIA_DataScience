# Patrones aprendidos de los 4 pilotos

## 9.1 Bangladesh (BGD) — "policy draft denso"

**Régimen final:** `soft_framework`.

**Ruta:** Sin ley IA. Strategy 2020 + Policy Draft V2.0 2026 con obligaciones concretas (AIAs mandatorios, strict liability, red lines) + pathway a AI Act 2028 declarado con fecha + AIRAM UNESCO/UNDP co-firmado 2025.

**Lección:** un policy draft post-consulta pública con obligaciones concretas y autoridad designada vale como `soft_framework` aunque no sea vinculante todavía. El pathway legislativo declarado con FECHA es el criterio clave.

## 9.2 Ghana (GHA) — "leyes sectoriales + estrategia lanzada"

**Régimen final:** `soft_framework`.

**Ruta:** Sin ley IA. Dos leyes sectoriales vinculantes robustas (Data Protection Act 2012 + Cybersecurity Act 2020) con autoridades activas (DPC, CSA) + NAIS 2023-2033 lanzada por Presidente en 2026-04 + DEPS 2024.

**Lección:** la presencia de leyes sectoriales vinculantes DESDE HACE AÑOS con autoridades establecidas justifica `soft_framework` incluso si la estrategia IA es reciente.

## 9.3 Singapur (SGP) — "corrección de IAPP + densidad soft-law máxima"

**Régimen final:** `soft_framework` (corrección de `strategy_only` incoherente).

**Ruta:** 7 documentos — PDPA 2012+2020 + CSL 2018 (vinculantes) + MAS FEAT 2018 + MGF 2020 + MGF GenAI 2024 + MGF Agentic 2026 + NAIS 2.0 2023.

**Lección:** `has_ai_law=0` NO implica `strategy_only`. Siempre releer la derivación IAPP de `regulatory_regime_group` contra la evidencia primaria. Si `intensity ≥ 4` y hay leyes sectoriales vigentes → es `soft_framework`.

## 9.4 Mongolia (MNG) — "IAPP supplementary desactualizado"

**Régimen final:** `soft_framework` (upgrade desde `light_touch` / `no_framework` ambiguo).

**Ruta:** Paquete de 4 leyes digitales dic-2021 en vigor desde may-2022 (PDPL + CSL + otras 2) + AILA UNDP+MDDIC 2025 + draft National Strategy presentado a State Great Khural 2025.

**Lección:** los países con `source = IAPP_supplementary_research` son los más probables de estar desactualizados. La codificación `light_touch, intensity=1, coverage=1` es sospechosa por defecto — verificar agresivamente si hay leyes sectoriales vinculantes que IAPP no capturó.

## Reglas heurísticas derivadas

1. **Si el país tiene GDPR-like + CSL-like desde hace ≥2 años** → mínimo `soft_framework`, sin importar lo que diga IAPP.
2. **Si el país tiene draft strategy post-consulta pública con obligaciones concretas** → revisar si califica para `soft_framework`.
3. **Si IAPP dice `light_touch` + `intensity=1` + `coverage=1`** → casi siempre está desactualizado. Buscar agresivamente.
4. **Si IAPP dice `strategy_led` + `intensity≥5`** pero deriva a `strategy_only` → probablemente `soft_framework` correcto.
5. **Ante duda entre `strategy_only` y `soft_framework`** → elegir `soft_framework` si (a) hay autoridad real con poderes o (b) hay pathway legislativo con fecha.
6. **Ante duda entre `soft_framework` y `binding_regulation`** → mantener `soft_framework` a menos que haya ley IA-específica VIGENTE. Drafts no cuentan.

## Errores comunes a evitar

1. **No asumir régimen sin leer citas.** Incluso países "obvios" como Singapur tenían errores de derivación en IAPP.
2. **No confundir co-emisión con counterpart.** Lee production team / acknowledgements.
3. **No usar URLs de think tanks como si fueran oficiales.** Wilson Center, Brookings, etc. NO son instrumentos estatales.
4. **No descargar PDFs sin validar con `file`.** Muchos WAFs sirven HTML de error con status 200.
5. **No dejar HTTP 403 sin intentar headers completos.** AGC Singapore, UNDP, algunos portales gov exigen Referer + UA Chrome.
6. **No inventar fechas.** Si no conoces la fecha exacta, deja el año y documenta en notas.
7. **No proponer `binding_regulation` para drafts.** Solo leyes vigentes.
8. **No olvidar R1.** URL verificable obligatoria. No excepciones.
9. **No saltarte la lectura de plantillas.** Cada CANDIDATES.md subsecuente mejora al previo.
10. **No empezar descarga antes de confirmación del usuario** en sesión nueva.
11. **ERROR CZE: No limitarse a 1-2 documentos.** Al procesar un país, buscar agresivamente TODOS los documentos IA relacionados (leyes + estrategia + presentaciones + comunicados + proyectos de ley + reportes sectoriales). No detenerse hasta tener mínimo 3-4 documentos verificables. El usuario no debe pedir 2 veces.
