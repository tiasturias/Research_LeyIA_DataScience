# Reglas de recodificación

## 4 buckets de `regulatory_regime_group`

| Régimen | Condiciones suficientes |
|---|---|
| `no_framework` | No hay estrategia, ley IA, ni leyes sectoriales relevantes vinculantes en vigor |
| `strategy_only` | Solo estrategia/política declarativa, sin base legal sectorial vinculante relevante ni autoridad designada |
| `soft_framework` | Cualquiera de: (a) estrategia + ≥1 ley sectorial vinculante con autoridad activa relevante para IA, (b) policy/framework con obligaciones concretas (AIAs, red lines, liability) aunque sin ley IA, (c) autoridad IA específica designada con mandato real, (d) pathway legislativo declarado con fecha |
| `binding_regulation` | Ley IA-específica vigente (Act of Parliament o equivalente) con autoridad IA y poderes sancionatorios |

## Reglas de decisión entre buckets adyacentes

**`no_framework` vs `strategy_only`:**
- ¿Hay al menos una estrategia IA oficial publicada, aunque sea preliminar?
  - No → `no_framework`.
  - Sí → `strategy_only` (mínimo).

**`strategy_only` vs `soft_framework`:**
- ¿Hay al menos una ley sectorial vinculante relevante (data protection, cybersecurity) en vigor con autoridad activa?
  - No → `strategy_only`.
  - Sí → `soft_framework`.
- ¿O hay obligaciones concretas (AIAs, red lines, liability, pathway legislativo con fecha)?
  - Sí → `soft_framework`.

**`soft_framework` vs `binding_regulation`:**
- ¿Hay ley IA-específica VIGENTE (no draft, no bill pending)?
  - No → `soft_framework`.
  - Sí → `binding_regulation`.

## Escalas continuas

### `regulatory_intensity` (0-10)

- **0-1:** casi nada o menciones periféricas.
- **2-3:** estrategia declarativa básica sin base legal sectorial.
- **4-5:** estrategia + 1-2 leyes sectoriales o framework voluntario robusto.
- **6-7:** ecosistema denso de frameworks + leyes sectoriales + autoridades activas.
- **8-9:** ley IA-específica vigente con enforcement.
- **10:** ley IA comprehensive con trayectoria de enforcement multi-año (UE post-AI-Act 2027+).

### `thematic_coverage` (0-15)

Contar cuántos de estos temas están cubiertos por los instrumentos del país:

1. AI ethics/principles
2. Data protection aplicable a IA
3. Cybersecurity aplicable a IA
4. Algorithmic transparency / explainability
5. Bias / fairness
6. Human oversight / accountability
7. High-risk classification (risk-based approach)
8. Prohibited practices (social scoring, mass surveillance)
9. Liability / redress
10. Generative AI specific
11. Copyright / IP para training data
12. Sector-specific: health
13. Sector-specific: finance
14. Sector-specific: public services
15. International cooperation / AI governance fora

### `enforcement_level`

- `none`: sin autoridades activas con poderes relevantes a IA.
- `low`: autoridades existen pero sin casos documentados o poderes limitados.
- `medium`: autoridades activas con poderes sancionatorios reales, casos aplicados a sistemas digitales/data.
- `high`: autoridades con IA-specific enforcement documentado (multas, prohibiciones, orders).

### `has_ai_law`

- **0:** no hay ley IA-específica vigente. Drafts, policies, frameworks no cuentan.
- **1:** hay ley IA-específica vigente (ej. EU AI Act para estados UE, Korea AI Basic Act, California SB 1047 si se promulga).

## Cuándo mantener `has_ai_law=0` aunque haya mucha densidad

**Singapur** es el caso testigo: intensity=6/7, coverage=12/13, ecosystem soft-law mundialmente líder → pero `has_ai_law=0` porque la política declarada es NO promulgar ley horizontal. El régimen es `soft_framework`, no `binding_regulation`.

## Checks de coherencia IAPP → régimen

La derivación de IAPP a `regulatory_regime_group` a veces es incoherente con sus propias métricas. Aplicar:

- Si `intensity ≥ 4` + hay leyes sectoriales vigentes → es `soft_framework`, no `strategy_only`.
- Si `intensity ≤ 2` + no hay nada vigente → `no_framework` o `strategy_only`, depende de si hay estrategia publicada.
- Si `has_ai_law = 1` → `binding_regulation` (salvo que la "ley" sea solo un draft sin promulgación).

## Ante duda

- Entre `strategy_only` y `soft_framework` → elegir `soft_framework` si (a) hay autoridad real con poderes o (b) hay pathway legislativo con fecha.
- Entre `soft_framework` y `binding_regulation` → mantener `soft_framework` a menos que haya ley IA-específica VIGENTE. **Drafts no cuentan.**
