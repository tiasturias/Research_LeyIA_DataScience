# Guía Metodológica

## Cómo Ejecutar tu Proyecto de

## Data Science Paso a Paso

## De la confusión a la claridad — Una guía práctica para principiantes

#### Proyecto: IMT3860 — Introducción a Data Science

#### Abril 2026

```
«¿Regular o no regular? Análisis comparativo del impacto de
marcos regulatorios de inteligencia artificial en el desarrollo
de ecosistemas de IA a nivel global.»
```
```
Generado por Perplexity Computer
```

### SECCIÓN 1 — Respira. Aquí está tu mapa

Antes de cualquier cosa: respira. Es completamente normal sentirse abrumado al inicio de un proyecto de data
science. Tienes datos por todas partes, métodos que no conoces, deadlines que se acercan y una pregunta de
investigación que parece gigante. Pero aquí va el secreto: todo proyecto de data science sigue un patrón
predecible.

Piensa en esto como armar un rompecabezas. No intentas encajar todas las piezas al mismo tiempo. Primero
miras la imagen completa en la caja (tu pregunta de investigación), luego separas las piezas por color (tus
datos), y finalmente vas armando sección por sección (tus análisis). No necesitas hacerlo todo a la vez.
Como dice el dicho: un elefante se come un bocado a la vez.

Las 9 fases de tu proyecto:

```
Fase 0: Organiza tu espacio de trabajo (repo, carpetas, dependencias)
Fase 1: Define tus variables ANTES de buscar datos
Fase 2: Recolecta datos fuente por fuente, en orden
Fase 3: Limpia e integra todo en un dataset maestro
Fase 4: Feature engineering (crear variables derivadas)
Fase 5: Análisis Exploratorio de Datos (EDA)
Fase 6: Modelamiento (OLS, K-Means, PCA, NLP)
Fase 7: Evalúa resultados y métricas
Fase 8: Conclusiones y recomendaciones
Fase 9: Comunicación (Notebook + Video)
```
```
Mensaje clave: En este momento, tu único trabajo es avanzar de la Fase 0 a la Fase 3. Todo lo demás puede
esperar. Cuando tengas tu dataset maestro listo, el 60% del trabajo estará hecho y lo que sigue fluirá mucho más
fácil.
```
### SECCIÓN 2 — FASE 0: Organiza tu espacio de trabajo

Antes de tocar un solo dato, necesitas un lugar ordenado donde trabajar. Imagina que vas a cocinar un plato
complejo: primero limpias la cocina, sacas los ingredientes y preparas los utensilios. Solo después empiezas a
cocinar. En data science es igual.

#### 1. Crea un repositorio en GitHub con esta estructura:


```
proyecto-ia-regulacion/
+-- data/
| +-- raw/ # datos crudos, NUNCA se modifican
| +-- interim/ # datos en proceso
| +-- processed/ # datos limpios finales
+-- notebooks/
| +-- 01_recoleccion.ipynb
| +-- 02_limpieza.ipynb
| +-- 03_eda.ipynb
| +-- 04_modelamiento.ipynb
| +-- 05_nlp.ipynb
+-- src/ # funciones reutilizables
+-- docs/ # propuesta, informes
+-- outputs/ # graficos, tablas exportadas
+-- README.md
+-- requirements.txt
```
#### 2. Crea un entorno virtual y 3. Instala dependencias:

```
python3 -m venv venv && source venv/bin/activate
pip install pandas numpy scikit-learn matplotlib seaborn plotly
pip install spacy gensim wbgapi requests openpyxl jupyter statsmodels
```
#### 4. ¿Por qué importa esta estructura?

Reproducibilidad: Cualquier persona puede clonar tu repo y ejecutar tu código. Seguridad: Los datos crudos
en data/raw/ nunca se tocan; si algo sale mal, siempre puedes volver al original. Orden mental: Sabes
exactamente dónde está cada cosa. Control de versiones: Git registra cada cambio.

```
Consejo: Haz tu primer git commit apenas crees la estructura, incluso antes de tener datos. Así tienes un punto
de partida limpio al que siempre puedes volver.
```

### SECCIÓN 3 — FASE 1: Define tus variables ANTES de buscar datos

Esta es la fase más importante del proyecto. Define exactamente qué datos necesitas antes de abrir un solo
navegador. Buscar datos sin saber qué variables necesitas es como ir al supermercado sin lista: compras de
todo, gastas más tiempo del necesario, y al llegar a casa te das cuenta de que olvidaste lo esencial.

Tu pregunta de investigación necesita tres tipos de variables: Dependientes (Y) = desarrollo del ecosistema de
IA; Independientes (X1) = regulación de IA; Control (X2) = factores socioeconómicos.

### VARIABLES DEPENDIENTES (Y) — Ecosistema de IA

```
Variable Descripción Fuente
ai_vibrancy_score Score compuesto de vitalidad del ecosistema de IA Stanford HAI
ai_investment_vc Inversión de capital de riesgo en IA (USD) Stanford HAI / OECD
ai_adoption_rate % de adopción de IA en la población Microsoft AI Diffusion
ai_patents Número de patentes de IA registradas Stanford HAI
ai_startups Número de startups de IA activas Stanford HAI
ai_readiness_score Government AI Readiness Index Oxford Insights
```
### VARIABLES INDEPENDIENTES (X1) — Regulación de IA

```
Variable Tipo Descripción Fuente
has_ai_law Dummy 0/1 ¿Tiene ley específica de IA? OECD / IAPP
regulatory_approach Categórica risk-based, sectoral, principles,
application-specific, none
```
```
OECD / IAPP
```
```
regulatory_intensity Ordinal 0-4 0=sin ley, 1=principios, 2=sectorial,
3=horizontal, 4=alto
```
```
Codificación manual
```
```
year_enacted Numérica Año de promulgación de la regulación OECD / IAPP / legislaturas
enforcement_level Ordinal Existencia de autoridad supervisora y
sanciones
```
```
Codificación manual
```
```
thematic_coverage Numérica Núm. de temas cubiertos (privacidad,
sesgo, etc.)
```
```
Codificación manual
```
### VARIABLES DE CONTROL (X2) — Factores socioeconómicos

```
Variable Descripción Fuente
gdp_per_capita_ppp PIB per cápita en paridad de poder adquisitivo World Bank WDI
rd_expenditure Gasto en I+D como % del PIB World Bank WDI
internet_penetration % de población con acceso a internet World Bank WDI
tertiary_education % de matrícula en educación terciaria World Bank WDI
gii_score Global Innovation Index score WIPO
government_effectiveness Indicador de efectividad gubernamental World Bank WGI
```

```
oecd_member Dummy 0/1 — Es miembro de la OECD OECD
region Categórica geográfica (Latam, Europe, Asia...) Clasificación manual
```
```
Mensaje clave: Con esta tabla en mano, ya sabes EXACTAMENTE qué datos buscar. No te pierdas en internet
buscando cosas al azar. Cada variable tiene nombre, descripción y fuente. Esa es tu lista de compras.
```
### SECCIÓN 4 — FASE 2: Recolección de datos, fuente por fuente

Ahora que tienes tu lista de variables, es hora de salir a buscar los datos. El orden importa: empieza por lo más
fácil y automatizable, y deja lo manual para el final. Así generas momentum — avanzas rápido al inicio y eso te
motiva para lo más tedioso.

### (1) PRIMERO: World Bank WDI — Variables de control

Qué buscar: gdp_per_capita_ppp, rd_expenditure, internet_penetration, tertiary_education. Cómo:
Automático con la librería wbgapi en Python. Guardar en: data/raw/worldbank_wdi.csv

```
import wbgapi as wb
import pandas as pd
```
```
indicators = {
'NY.GDP.PCAP.PP.CD': 'gdp_per_capita_ppp',
'GB.XPD.RSDV.GD.ZS': 'rd_expenditure',
'IT.NET.USER.ZS': 'internet_penetration',
'SE.TER.ENRR': 'tertiary_education'
}
```
```
df = wb.data.DataFrame(
list(indicators.keys()), economy='all', time=2023, labels=True)
df = df.rename(columns=indicators)
df.to_csv('data/raw/worldbank_wdi.csv')
print(f'Descargados {len(df)} paises')
```
### (2) SEGUNDO: Stanford HAI AI Vibrancy Tool — Variables dependientes

Qué buscar: ai_vibrancy_score, ai_investment_vc, ai_patents, ai_startups. Cómo: Ir a Stanford HAI AI Index —
Global AI Vibrancy Tool — seleccionar países — exportar CSV. Guardar en:
data/raw/stanford_hai_vibrancy.csv

### (3) TERCERO: OECD AI Policy Observatory — Variables regulatorias

Qué buscar: has_ai_law, regulatory_approach, year_enacted. Cómo: Ir a oecd.ai — Policy Areas — Countries
— revisar fichas por país. Formato: Extracción manual — crear tu propio CSV. Guardar en:
data/raw/oecd_ai_policy.csv

### (4) CUARTO: IAPP Global AI Legislation Tracker — Complemento regulatorio

Qué buscar: Validación cruzada de has_ai_law, regulatory_intensity, enforcement_level. Cómo: Ir a IAPP
Tracker — revisar tabla de legislaciones. Codificar manualmente las variables ordinales. Guardar en:
data/raw/iapp_regulatory.csv

### (5) QUINTO: Microsoft AI Diffusion + otros índices


Microsoft AI Diffusion Report: ai_adoption_rate — buscar el informe PDF más reciente. Tortoise Global AI
Index: score complementario. Oxford Insights: ai_readiness_score. WIPO GII: gii_score.

### (6) SEXTO (más adelante): Textos legales para NLP

Esto viene después de tener el análisis cuantitativo funcionando. Selecciona 15-20 países con textos legales
accesibles en inglés o español. Guarda los textos en data/raw/legal_texts/ como archivos .txt

```
Consejo: No intentes descargar todo en un día. Dedica 1-2 días a cada fuente. El World Bank y Stanford HAI son
rápidos; la codificación manual de OECD/IAPP toma más tiempo.
```

### SECCIÓN 5 — ¿Dónde guardar los datos? Google Sheets vs CSV vs SQL

Respuesta corta: para tu proyecto, usa CSV + Pandas + Git. Aquí va la comparación:

```
Criterio Google Sheets CSV / Parquet SQLite PostgreSQL
Facilidad de uso Muy alta Alta Media Baja
Tamaño de datos <100K filas Millones Millones Millones+
Colaboración Excelente Git Regular Complejo
Reproducibilidad Baja Alta Alta Alta
¿Ideal para este
proyecto? NO SÍ OPCIONAL NO
```
Tu dataset es pequeño (~68 filas × ~20-30 columnas). No necesitas una base de datos. CSV es el estándar en
data science: todos lo entienden, todos lo leen. Pandas carga CSV en una línea. Git te da control de versiones
gratis. Si quieres algo más eficiente, considera Parquet, pero para 68 filas, CSV es perfecto.

```
¿Y Google Sheets? No es recomendable como almacenamiento principal: no es reproducible (los cambios
manuales no quedan registrados), no se integra bien con pipelines de Python, y no tiene control de versiones real.
Puedes usarlo para explorar datos manualmente, pero tu fuente de verdad debe ser el CSV en tu repositorio.
```
### SECCIÓN 6 — FASE 3: Limpieza e integración — El trabajo sucio

La limpieza de datos no es glamorosa, pero es donde se ganan o se pierden los proyectos. Se estima que el
80% del tiempo de un proyecto de data science se va en recolectar y limpiar datos. Si seguiste las fases
anteriores, esto será más mecánico que creativo.

### Checklist de limpieza:

1. Estandarizar nombres de países: Usa códigos ISO 3166-1 alpha-3 (CHL, USA, DEU...). Cada fuente
nombra los países diferente. Un solo estándar evita errores al unir tablas.
2. Verificar cobertura: Revisa que los 68 países tengan datos en todas las fuentes. Crea una matriz: países
x variables.
3. Manejar valores faltantes (NaN): Si <10% faltantes: imputa con la media regional. Si >10%: considera
excluir el país o la variable. Documenta cada decisión.
4. Normalizar escalas: Para variables que van a K-Means, aplica min-max o z-score. K-Means es sensible a
la escala.
5. Crear el dataset maestro: Unifica todo en un solo CSV: cada fila = 1 país, cada columna = 1 variable.
Guarda en data/processed/dataset_master.csv
6. Validar el resultado: Ejecuta df.info(), df.describe(), df.isnull().sum(). Verifica tipos de datos.


# Ejemplo: merge de datasets por código ISO
import pandas as pd
wb = pd.read_csv('data/raw/worldbank_wdi.csv')
hai = pd.read_csv('data/raw/stanford_hai_vibrancy.csv')
reg = pd.read_csv('data/raw/regulatory_variables.csv')
master = wb.merge(hai, on='iso3', how='outer')
master = master.merge(reg, on='iso3', how='outer')
print(f'Paises: {len(master)}, Variables: {len(master.columns)}')
master.to_csv('data/processed/dataset_master.csv', index=False)


### SECCIÓN 7 — FASES 4-9: Vista rápida del resto del camino

No te preocupes por estas fases todavía. Concéntrate en las Fases 0-3 primero. Este es solo un mapa para
que sepas qué viene después.

### Fase 4: Feature Engineering

Crear variables derivadas como regulatory_intensity (ordinal), dummies para regulatory_approach, y
logaritmos de variables financieras. La mayor parte ya la definiste en la tabla de variables.

### Fase 5: Análisis Exploratorio (EDA)

Estadísticas descriptivas, distribuciones con histogramas, matriz de correlación con heatmap, y scatterplots
de tus variables clave. El EDA te dice si tus datos tienen sentido antes de modelar.

### Fase 6: Modelamiento

Capa cuantitativa: Regresión OLS para medir la asociación entre regulación y ecosistema de IA. K-Means para
agrupar países en clusters. PCA para reducir dimensionalidad. Capa NLP: TF-IDF para vectorizar textos legales.
LDA para descubrir temas latentes.

### Fase 7: Métricas

R² y R² ajustado para OLS. Silhouette score para K-Means. Coherencia de temas para LDA. Pruebas de
supuestos: normalidad de residuos, homocedasticidad, multicolinealidad (VIF).

### Fase 8: Conclusiones

¿La regulación impacta al ecosistema de IA? ¿Cómo? ¿Qué recomiendas para Chile? Las conclusiones deben
responder directamente tu pregunta de investigación.

### Fase 9: Comunicación

Jupyter Notebook limpio y narrativo (entrega: 10 de mayo). Video de presentación (entrega: 14 de mayo). Tu
audiencia son legisladores — mantén las conclusiones simples.

```
Recuerda: No necesitas dominar todo desde el día uno. Cada fase se apoya en la anterior. Si haces bien las Fases
0-3, las Fases 4-9 serán mucho más llevaderas. Confía en el proceso.
```
### SECCIÓN 8 — Tu checklist de las próximas 4 semanas

Aquí tienes un plan concreto, día a día. No tienes que pensar en qué hacer — solo sigue la lista. El progreso es
motivación.

### SEMANA 1 (16-23 abril): Recolección de datos

```
[ ] Día 1-2: Crear repo GitHub + estructura de carpetas + instalar dependencias
[ ] Día 2-3: Descargar datos World Bank con wbgapi (variables de control)
[ ] Día 3-4: Descargar Stanford HAI AI Vibrancy Tool (variables dependientes)
[ ] Día 4-5: Revisar OECD + IAPP y codificar variables regulatorias manualmente
[ ] Día 5-6: Completar con Microsoft AI Diffusion, Oxford Insights y otros índices
```

```
[ ] Día 7: Integrar todo en un CSV maestro preliminar
```
### SEMANA 2 (23-30 abril): Limpieza + EDA

```
[ ] Día 1-2: Limpieza — estandarizar ISO codes, manejar NaN, detectar outliers
[ ] Día 3-4: EDA cuantitativo — estadísticas descriptivas, correlaciones, heatmaps
[ ] Día 5-6: Primeros modelos exploratorios — OLS preliminar, K-Means con 3-5 clusters
[ ] Día 7: Documentar hallazgos iniciales en notebook 03_eda.ipynb
```
### SEMANA 3 (30 abril - 7 mayo): Modelamiento + NLP

```
[ ] Día 1-2: OLS final — verificar supuestos, iterar con diferentes especificaciones
[ ] Día 3-4: K-Means + PCA — optimizar número de clusters, interpretar componentes
[ ] Día 5-6: NLP — recolectar textos legales, TF-IDF, LDA topic modeling
[ ] Día 7: Integrar resultados cuantitativos y textuales
```
### SEMANA 4 (7-14 mayo): Resultados + Notebook + Video

```
[ ] Día 1-2: Redactar conclusiones y recomendaciones para Chile
[ ] Día 3-4: Limpiar y narrar el Jupyter Notebook final — debe contar una historia
[ ] Día 5 (10 mayo): ENTREGAR Jupyter Notebook
[ ] Día 6-7: Preparar y grabar video de presentación
[ ] Día 8 (14 mayo): ENTREGAR video de presentación
```
```
Consejo práctico: Imprime esta página y pégala en tu pared, o conviértela en un checklist digital (Notion, Todoist,
o incluso un Issue en GitHub). Tachar tareas completadas es sorprendentemente satisfactorio.
```

### SECCIÓN 9 — Errores comunes de un junior (y cómo evitarlos)

Todos cometemos errores al principio. Aquí van los más frecuentes en proyectos de data science
universitarios. Si los conoces de antemano, puedes esquivarlos.

1. Error: Buscar datos sin saber qué variables necesitas
Solución: Define tu tabla de variables PRIMERO (Sección 3). Es tu lista de compras.
2. Error: Guardar todo en Google Sheets
Solución: Google Sheets no es reproducible. Usa CSV + Git como fuente de verdad.
3. Error: Modificar los datos originales
Solución: NUNCA toques data/raw/. Trabaja sobre copias en data/interim/ o data/processed/.
4. Error: No documentar las transformaciones
Solución: Cada cambio debe quedar registrado en un notebook con explicación. Tu "yo del futuro" te lo
agradecerá.
5. Error: Intentar hacer todo perfecto de una vez
Solución: Haz una versión "fea pero funcional" primero. Un OLS con 5 variables que corre es mejor que un modelo
perfecto que nunca terminas.
6. Error: Perderse buscando más fuentes de datos
Solución: Las fuentes ya están definidas. No necesitas más. Resiste la tentación.
7. Error: No verificar supuestos de los modelos
Solución: OLS requiere normalidad de residuos, homocedasticidad y no multicolinealidad. K-Means asume
clusters esféricos.
8. Error: Olvidar quién es tu audiencia
Solución: Tu audiencia son legisladores, no estadísticos. Un gráfico claro vale más que una tabla de coeficientes.
9. Error: No hacer backups frecuentes
Solución: git commit temprano y seguido. Si pasaste más de 30 minutos sin guardar, ya te atrasaste.
10. Error: Comparar todo con todo sin hipótesis
Solución: No corras 50 regresiones a ver qué sale significativo. Eso es p-hacking. Enfócate en tu pregunta central.

Y recuerda: el mejor proyecto no es el más complejo, sino el que responde su pregunta de
investigación de forma clara y reproducible. Tú puedes con esto. Un paso a la vez.


Fuentes principales de datos para el proyecto:

1. Stanford HAI AI Index — https://hai.stanford.edu/ai-index
2. OECD AI Policy Observatory — https://oecd.ai
3. IAPP Global AI Legislation Tracker — https://iapp.org/resources/article/global-ai-legislation-tracker
4. World Bank WDI — https://wdi.worldbank.org
5. Oxford Insights AI Readiness — https://oxfordinsights.com/ai-readiness/ai-readiness-index/


