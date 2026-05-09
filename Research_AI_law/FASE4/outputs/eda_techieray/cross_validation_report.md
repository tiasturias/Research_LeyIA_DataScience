# Reporte de Validación Cruzada: IAPP vs Techieray

## Resumen de Muestra
- **Total países analizados (solapamiento):** 18
- Estos son los países que originalmente tenían datos de IAPP, contra los cuales cruzamos la rigurosa extracción de Techieray.

## Tasa de Concordancia (Concordance Rate)
- **Variable `Ley Vigente`:** 61.1% de concordancia.
- **Variable `Proyecto de Ley`:** 72.2% de concordancia.

## Análisis de Discrepancias en Ley Vigente
iso3 country_name_canonical  iapp_ley_ia_vigente  tr_ley_ia_vigente
 ARE   United Arab Emirates                  1.0                0.0
 CHN                  China                  1.0                0.0
 JPN                  Japan                  1.0                0.0
 KOR            South Korea                  1.0                0.0
 PER                   Peru                  1.0                0.0
 TWN                 Taiwan                  0.0                1.0
 USA          United States                  1.0                0.0

## Análisis de Discrepancias en Proyecto de Ley
iso3 country_name_canonical  iapp_proyecto_ley_ia  tr_proyecto_ley_ia
 AUS              Australia                   1.0                 0.0
 JPN                  Japan                   0.0                 1.0
 KOR            South Korea                   0.0                 1.0
 PER                   Peru                   0.0                 1.0
 TWN                 Taiwan                   1.0                 0.0
