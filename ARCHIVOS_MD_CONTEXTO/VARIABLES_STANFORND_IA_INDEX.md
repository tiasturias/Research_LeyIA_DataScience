# Variables Stanford AI Index 2025

## Proposito

Este documento resume, en una version operativa, que variables del estudio pueden extraerse desde la fuente Stanford AI Index 2025 ya descargada en `data/raw/STANFORD AI INDEX 25/`.

Su objetivo es servir como referencia rapida para:
- saber que variables de la metodologia si estan en Stanford;
- identificar el archivo exacto a usar;
- distinguir entre variables centrales, proxies y variables no disponibles;
- preparar la extraccion hacia tablas intermedias antes de limpieza.

## Fuente

- Fuente base: Stanford AI Index 2025
- Ubicacion local: `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25`
- Manifest de descarga: `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25/download_manifest.csv`

## Conclusion Ejecutiva

Stanford AI Index 2025 aporta principalmente variables dependientes del ecosistema de IA, es decir variables `Y`.

No aporta de forma directa las variables regulatorias `X1` definidas en la metodologia, ni las variables de control `X2` como PIB per capita, I+D, penetracion de internet o efectividad gubernamental.

Tampoco se identifico en esta descarga una variable explicita `ai_vibrancy_score`. Si esa variable exacta se quiere usar, habra que obtenerla desde otro export especifico del Stanford Global AI Vibrancy Tool.

## Cobertura Real De Paises

**Aclaracion importante**: si en algun resumen de auditoria Stanford aparece con `paises (raw) = -` o `paises (estudio) = -`, eso **no** significa ausencia de datos. Significa que Stanford no entra al proyecto como un solo panel tabular consolidado, sino como varios archivos `figure-level` con coberturas distintas por variable y, en algunos casos, con mezcla de paises, territorios y filas agregadas por anio.

Conteo consolidado verificado sobre los **7 archivos Stanford efectivamente usados o priorizados** en el proyecto:

| metrica | valor | nota |
|---|---|---|
| Archivos Stanford auditados | 7 | job postings, skill, talent, startups 2024, startups 2013-24, patents, investment |
| Labels geograficos unicos en raw (union) | 96 | incluye paises y algunos territorios/economias no pertenecientes a la muestra |
| ISO3 mapeables tras normalizacion | 88 | despues de armonizar nombres como `Taiwan`, `Slovak Republic`, `Czech Republic`, `Turkey` |
| Paises de la muestra del estudio cubiertos por Stanford | 86 de 86 | interseccion completa con la muestra actual del estudio |

Cobertura verificada por archivo principal:

| variable Stanford | archivo | paises raw aprox. | paises estudio cubiertos |
|---|---|---:|---:|
| `ai_job_postings` | `fig_4.2.1.csv` | 11 | 10 |
| `ai_skill` | `fig_4.2.15.csv` | 48 | 47 |
| `ai_talent` | `fig_4.2.17.csv` | 48 | 47 |
| `ai_startups` (snapshot 2024) | `fig_4.3.12.csv` | 62 | 54 |
| `ai_startups_cumul` | `fig_4.3.13.csv` | 91 | 80 |
| `ai_patents` | `fig_1.2.4.csv` | 55 | 52 |
| `ai_investment` | `fig_4.3.10.csv` | 2 | 2 |

Interpretacion correcta:
- Stanford **si aporta datos** y de hecho aporta una base Y muy relevante para el estudio.
- Lo que no aporta es una sola tabla fuente con un `n_paises` unico y estable como World Bank, Oxford o IAPP.
- Por eso, en resumentes muy comprimidos, poner `-` en la columna de paises para Stanford puede inducir a error. La lectura correcta deberia ser: `cobertura variable-especifica; no resumible en un unico n sin consolidacion previa`.

## Variables Operativas Recomendadas

| variable_estudio | tipo_metodologico | estado_en_stanford | variable_operativa_sugerida | archivo_principal | rutas_alternativas | observacion_metodologica |
|---|---|---|---|---|---|---|
| ai_investment_vc | Y | Disponible como proxy fuerte | ai_investment_total_country_year | `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25/4. Economy/Data/fig_4.3.10.csv` | `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25/4. Economy/Data/fig_4.3.8.csv`; `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25/4. Economy/Data/fig_4.3.9.csv` | Es la mejor aproximacion disponible desde Stanford para inversion en IA. Validar si la metrica corresponde exactamente a VC o a inversion privada total. |
| ai_patents | Y | Disponible parcialmente | ai_patents_per_100k_2023 | `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25/1. Research and Development/Data/fig_1.2.4.csv` | `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25/1. Research and Development/Data/fig_1.2.3.csv`; `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25/1. Research and Development/Data/fig_1.2.2.csv` | La mejor version comparable es per capita. No se identifico un conteo absoluto pais-anual general limpio para todos los paises. |
| ai_startups | Y | Disponible como proxy fuerte | ai_newly_funded_companies_2024 | `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25/4. Economy/Data/fig_4.3.12.csv` | `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25/4. Economy/Data/fig_4.3.13.csv`; `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25/4. Economy/Data/fig_4.3.14.csv` | No mide startups activas literalmente, pero si empresas de IA recien financiadas. Es una proxy razonable para dinamismo emprendedor. |
| ai_vibrancy_score | Y | No disponible de forma explicita | null | null | null | No aparece un archivo o columna con vibrancy score explicito en esta descarga. |
| ai_adoption_rate | Y | No disponible | null | null | null | Debe obtenerse desde Microsoft AI Diffusion u otra fuente definida en la metodologia. |
| ai_readiness_score | Y | No disponible | null | null | null | Debe obtenerse desde Oxford Insights. |
| has_ai_law | X1 | No disponible de forma valida | null | null | `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25/6. Policy and Governance/Data/fig_6.2.1.csv` | Stanford contiene actividad legislativa, pero no permite inferir con rigor si existe ley especifica de IA. |
| regulatory_approach | X1 | No disponible | null | null | null | Debe venir de OECD / IAPP y codificacion manual. |
| regulatory_intensity | X1 | No disponible | null | null | null | Debe construirse manualmente. |
| year_enacted | X1 | No disponible | null | null | null | Debe obtenerse desde OECD / IAPP / legislaturas. |
| enforcement_level | X1 | No disponible | null | null | null | Debe construirse manualmente. |
| thematic_coverage | X1 | No disponible | null | null | null | Debe construirse manualmente. |
| gdp_per_capita_ppp | X2 | No disponible | null | null | null | Debe obtenerse desde World Bank WDI. |
| rd_expenditure | X2 | No disponible | null | null | null | Debe obtenerse desde World Bank WDI. |
| internet_penetration | X2 | No disponible | null | null | null | Debe obtenerse desde World Bank WDI. |
| tertiary_education | X2 | No disponible | null | null | null | Debe obtenerse desde World Bank WDI. |
| gii_score | X2 | No disponible | null | null | null | Debe obtenerse desde WIPO. |
| government_effectiveness | X2 | No disponible | null | null | null | Debe obtenerse desde World Bank WGI. |
| oecd_member | X2 | No disponible | null | null | null | Debe construirse aparte. |
| region | X2 | No disponible | null | null | null | Debe construirse aparte. |

## Variables Stanford Adicionales Que Podrian Servir

Estas variables no estan en la tabla principal de la metodologia, pero pueden servir para EDA, robustez o enriquecimiento del dataset:

| variable_adicional | archivo | uso_posible |
|---|---|---|
| ai_talent_concentration | `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25/4. Economy/Data/fig_4.2.17.csv` | Proxy de concentracion de talento IA por pais |
| ai_skill_penetration | `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25/4. Economy/Data/fig_4.2.15.csv` | Proxy de penetracion de habilidades IA |
| ai_job_postings_share | `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25/4. Economy/Data/fig_4.2.1.csv` | Proxy de demanda laboral asociada a IA |
| notable_ml_models | `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/STANFORD AI INDEX 25/1. Research and Development/Data/fig_1.3.1.csv` | Proxy de capacidad de frontera |

## Recomendacion Operativa Para Este Estudio

Si hubiera que construir hoy un primer bloque `Y` solo con Stanford, la prioridad recomendada es:

1. `ai_investment_total_country_year` desde `fig_4.3.10.csv`
2. `ai_patents_per_100k_2023` desde `fig_1.2.4.csv`
3. `ai_newly_funded_companies_2024` desde `fig_4.3.12.csv`
4. `ai_newly_funded_companies_2013_24` desde `fig_4.3.13.csv`

## Regla De Uso

- Usar `data/raw/` solo como fuente original.
- No modificar estos archivos.
- Cuando se extraigan variables concretas desde Stanford, guardar el resultado en `data/interim/` con nombres descriptivos.
- Si se estandarizan paises o se renombran columnas, documentarlo en `notebooks/01_recoleccion.ipynb` y luego en `02_limpieza.ipynb`.
