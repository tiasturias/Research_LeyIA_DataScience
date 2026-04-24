**Propuesta de Proyecto**

IMT3860 — Introducción a Data Science | Abril 2026

# **1\. Título del Proyecto**

***¿Regular o no regular? Análisis comparativo del impacto de marcos regulatorios de inteligencia artificial en el desarrollo de ecosistemas de IA a nivel global.***

# **2\. Contexto y Motivación**

## **2.1 Contexto legislativo chileno**

Chile se encuentra en un momento decisivo respecto a la regulación de la inteligencia artificial. La Cámara de Diputados ha aprobado el proyecto de «Ley Marco de Inteligencia Artificial» (Boletín 16821-19), que actualmente se encuentra en la Comisión de Ciencia, Tecnología e Innovación del Senado para su tramitación. Esta decisión legislativa tendrá consecuencias directas sobre la capacidad de Chile para atraer inversión, fomentar la adopción de IA en el sector público y privado, y posicionarse competitivamente en América Latina.

## **2.2 El dilema regulatorio**

Existe un debate global entre dos visiones contrapuestas: por un lado, la regulación como mecanismo de protección ciudadana frente a riesgos de la IA (sesgo, privacidad, transparencia); por otro, la regulación como potencial barrera para la innovación, la inversión y la adopción tecnológica. La Unión Europea ha optado por un enfoque basado en riesgos con el EU AI Act (2024), Estados Unidos ha preferido un enfoque sectorial y de mercado, y China ha implementado regulaciones específicas por aplicación. Cada enfoque tiene implicancias distintas en los indicadores de desarrollo del ecosistema de IA.

## **2.3 Motivación**

Este proyecto nace de la necesidad concreta de informar una decisión legislativa real: como equipo, buscamos generar evidencia empírica que permita evaluar si Chile necesita una legislación específica de IA y, de ser así, qué tipo de enfoque regulatorio se asocia con mejores resultados en el desarrollo del ecosistema de IA, controlando por factores socioeconómicos e institucionales. La investigación se apoya en el creciente cuerpo de índices y datos comparativos internacionales disponibles, como el Stanford HAI AI Index, el Global AI Index de Tortoise Media, el Government AI Readiness Index de Oxford Insights y los datos del Observatorio de Políticas de IA de la OCDE.

**¿Chile necesita una legislación específica de IA?y, de ser así, ¿qué tipo de enfoque regulatorio se asocia con mejores resultados en el desarrollo del ecosistema de IA?**

**Fuentes de datos:**

- [ ] Stanford HAI AI Index

- [ ] Global AI Index de Tortoise Media

- [ ] Government AI Readiness Index de Oxford Insights

- [ ] Observatorio de Políticas de IA de la OCDE

## **2.4 Audiencia objetivo**

El análisis está dirigido a tres audiencias:

* Legisladores y asesores de la Comisión de Ciencia del Senado, como insumo para la discusión del proyecto de Ley Marco de IA.  
* Tomadores de decisión en el Ministerio de Ciencia, Tecnología, Conocimiento e Innovación, quienes podrían utilizar los hallazgos para el diseño de políticas públicas.  
* La comunidad académica y de datos abiertos interesada en análisis comparativos de regulación tecnológica.

# **3\. Objetivos**

## **3.1 Pregunta principal**

**Pregunta:** *¿Existe una asociación estadísticamente significativa entre las características de la regulación de inteligencia artificial de un país y el desarrollo de su ecosistema de IA, después de controlar por factores socioeconómicos e institucionales?*

## **3.2 Sub-preguntas**

* **Inversión:** ¿Los países con marcos regulatorios más restrictivos muestran menores niveles de inversión privada en IA (capital de riesgo, centros de datos)?  
* **Adopción:** ¿Qué tipo de enfoque regulatorio (basado en riesgos, sectorial, principios, sin regulación específica) se asocia con mayores tasas de adopción de IA en empresas y sector público?  
* **Innovación:** ¿Existe relación entre la presencia y tipo de regulación de IA y los indicadores de innovación (patentes, publicaciones, startups)?  
* **Contenido regulatorio:** ¿Qué temas y enfoques dominan en los textos legales de IA a nivel global, y cómo se agrupan temáticamente los países según el contenido de su regulación?

## **3.3 Accionables esperados**

Los resultados del proyecto permitirán:

* Generar una recomendación basada en datos sobre si Chile debe aprobar, modificar o rechazar el proyecto de Ley Marco de IA actualmente en trámite.  
* Identificar los elementos regulatorios específicos que se asocian con mejores resultados de ecosistema, para informar el diseño de una eventual legislación.  
* Crear un dataset estructurado y replicable de regulación de IA comparada que pueda ser útil para futuras investigaciones.

# **4\. Datos**

## **4.1 Fuentes de datos principales**

El proyecto integrará datos de múltiples fuentes públicas, organizados en tres categorías:

**A. Variables dependientes: Indicadores de ecosistema de IA**

| Fuente | Cobertura | Indicadores clave | Formato / Acceso |
| :---- | :---- | :---- | :---- |
| Stanford HAI AI Index(Global AI Vibrancy Tool) | 36–66 países,series desde 2017 | Inversión, innovación, talento, infraestructura | Descargable, abierto |
| Global AI Index(Tortoise Media) | 83 países,122 indicadores | Implementación, inversión, estrategia gubernamental | Web, metodología pública |
| Gov. AI Readiness Index(Oxford Insights) | 195 países,69 indicadores | Capacidad gubernamental, adopción pública, infraestructura | PDF \+ web |
| Our World in Data / CSET | Cobertura global | Inversión privada en IA por país | CSV descargable |

**B. Variables independientes: Caracterización regulatoria**

| Fuente | Cobertura | Contenido | Formato / Acceso |
| :---- | :---- | :---- | :---- |
| OECD AI Policy Observatory | 900+ políticas,70+ países | Estrategias, leyes, instrumentos | API (JSON), sin clave |
| IAPP Global AI Law Tracker | Cobertura global | Legislación de IA por jurisdicción | Web scraping |
| Textos legales(EUR-Lex, legislaturas) | 15–20 países(subconjunto) | Texto completo de leyes de IA | PDF/HTML, extracción |

**C. Variables de control: Factores socioeconómicos e institucionales**

| Fuente | Cobertura | Variables |
| :---- | :---- | :---- |
| World Bank WDI | 200+ países | PIB per cápita (PPP), gasto en I+D, penetración de internet, años de escolaridad, índice de capital humano |
| Global Innovation Index(WIPO) | 130+ países | Índice de innovación general, calidad de universidades, infraestructura tecnológica |

## **4.2 Estrategia de recolección de datos**

La recolección se organizará en dos capas:

* **Capa cuantitativa (50+ países):** Se construirá un dataset tabular integrando los índices existentes (Stanford HAI, Global AI Index, Oxford Insights) con variables de control del World Bank WDI. La caracterización regulatoria para esta capa será categórica, basada en los trackers de la OCDE e IAPP: presencia/ausencia de ley específica de IA, tipo de enfoque (basado en riesgos, sectorial, principios, horizontal) y año de promulgación. Esta codificación se realizará manualmente para garantizar consistencia.  
* **Capa de análisis textual (15–20 países):** Para un subconjunto de países con textos legales accesibles en inglés o español, se recopilarán los textos completos de las leyes de IA para aplicar técnicas de NLP. Se priorizarán las jurisdicciones que representen los principales arquetipos regulatorios: UE, EE.UU. (federal \+ estados clave), China, Reino Unido, Canadá, Brasil, Chile, Singapur, Corea del Sur, Japón, India, EAU, entre otros.

## **4.3 Volumen estimado**

* Dataset principal: \~50–80 filas (países) × \~40–60 columnas (indicadores \+ controles \+ variables regulatorias).  
* Corpus textual: 15–20 documentos legales, estimado de 500–2.000 páginas totales.  
* Formato de trabajo: CSV/Parquet para datos tabulares, archivos .txt para corpus legal.

# **5\. Diseño Tentativo**

## **5.1 Análisis exploratorio de datos (EDA)**

* Estadísticas descriptivas de las variables clave por grupos regulatorios (con/sin ley, tipo de enfoque).  
* Visualizaciones: mapas coropleth de indicadores de IA por país, gráficos de dispersión entre intensidad regulatoria e indicadores de ecosistema, heatmaps de correlación.  
* Análisis de valores faltantes y estrategia de imputación o exclusión.

## **5.2 Análisis de texto (NLP)**

* **Preprocesamiento:** Tokenización, eliminación de stopwords, lematización de textos legales usando spaCy.  
* **TF-IDF:** Vectorización de documentos legales para identificar términos diferenciadores entre jurisdicciones.  
* **Topic Modeling (LDA):** Extracción de temas latentes en los textos legales (ej: riesgo, transparencia, innovación, sanciones, datos personales) para caracterizar el enfoque de cada país.  
* **Similaridad entre documentos:** Cálculo de distancias coseno entre representaciones TF-IDF para identificar clusters de países con regulaciones similares.

## **5.3 Modelamiento estadístico**

* **Regresión múltiple (OLS):** Modelo principal que relaciona indicadores de ecosistema de IA (variable dependiente) con variables regulatorias (independientes) y controles socioeconómicos. Se evaluarán supuestos de normalidad, homocedasticidad y multicolinealidad.  
* **Clustering (K-Means):** Agrupación no supervisada de países según su perfil regulatorio y de ecosistema, para identificar arquetipos (ej: «reguladores fuertes con alto ecosistema» vs. «sin regulación con bajo ecosistema»).  
* **Análisis de componentes principales (PCA):** Reducción de dimensionalidad para visualizar la relación entre múltiples indicadores y facilitar la interpretación.

## **5.4 Herramientas**

* Python 3.x, Pandas, NumPy para manipulación de datos.  
* scikit-learn para modelos de regresión, clustering y PCA.  
* spaCy, gensim para procesamiento de lenguaje natural y topic modeling.  
* Matplotlib, Seaborn, Plotly para visualización.  
* World Bank API (wbgapi) para descarga programática de datos.  
* Jupyter Notebook como entorno de desarrollo y presentación.

## **5.5 Cronograma tentativo**

| Semana | Actividades | Entregable |
| :---- | :---- | :---- |
| Sem 1(16–23 abr) | Recolección de datos: descarga de índices, WDI, codificación regulatoria manual, recolección de textos legales | Datasets crudos integrados |
| Sem 2(23–30 abr) | Integración de datasets, limpieza, EDA inicial, preprocesamiento NLP | EDA \+ corpus limpio |
| Sem 3(30 abr – 7 may) | Modelamiento: regresión, clustering, topic modeling. Visualizaciones principales | Modelos \+ visualizaciones |
| Sem 4(7–14 may) | Resultados finales, narrativa, Jupyter Notebook completo, grabación del video de presentación | Notebook \+ video (8 min) |

**Nota:**

*  Esta propuesta es un punto de partida. Se espera que las preguntas, métodos y alcance evolucionen a medida que avance el proyecto y se conozca mejor la disponibilidad real de los datos. El enfoque principal es pragmático: generar evidencia útil para una decisión legislativa concreta, utilizando las herramientas y métodos de un curso introductorio de ciencia de datos.  
* Estudiarlo en detalle.  
*  Involucrate en la comisión donde está radicado el tema. Trata de ir adelantado a lo que ocurra.

