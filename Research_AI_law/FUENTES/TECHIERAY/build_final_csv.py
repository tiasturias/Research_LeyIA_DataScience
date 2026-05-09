import pandas as pd
import io
from pathlib import Path

BASE = Path("/home/pablo/Research_LeyIA_DataScience/Research_AI_law/FUENTES/TECHIERAY")

csv_text = """iso3,tr_ley_ia_vigente,tr_proyecto_ley_ia,tr_estrategia_nacional_ia,tr_tiene_guia_softlaw,tr_tiene_autoridad_dedicada,tr_categoria_obligatoriedad,tr_n_leyes_relacionadas,tr_n_autoridades,tr_sandbox_regulatorio,tr_marcos_voluntarios,tr_instituto_seguridad_ia,tr_herramientas_testing,tr_modelo_gobernanza,tr_adhiere_oecd,tr_adopto_unesco
ARG,0,1,1,1,1,non-binding,1,1,0,1,0,1,centralized,0,1
BRA,0,1,1,1,1,non-binding,1,1,0,1,0,1,centralized,0,1
CAN,0,0,1,1,1,non-binding,1,1,1,1,1,1,centralized,1,1
CHL,0,1,1,1,0,non-binding,1,1,1,1,0,1,none,1,1
COL,0,1,1,1,0,non-binding,1,1,1,1,0,1,none,1,1
CRI,0,1,0,0,0,non-binding,1,1,1,1,0,1,none,1,1
MEX,0,1,0,0,0,non-binding,1,1,1,1,0,1,none,1,1
PER,0,1,0,0,0,non-binding,1,1,0,1,0,1,none,0,1
URY,0,0,1,1,0,non-binding,1,1,0,1,0,1,none,0,1
USA,0,1,1,1,1,non-binding,1,1,1,1,1,1,centralized,1,1
AUS,0,0,1,1,1,non-binding,1,1,1,1,1,1,centralized,1,1
NZL,0,0,1,1,0,non-binding,1,1,1,1,0,1,none,1,1
CHN,0,1,1,1,1,binding,1,1,0,1,0,1,centralized,0,1
IND,0,1,1,1,1,non-binding,1,1,0,1,0,1,centralized,0,1
JPN,0,1,1,1,1,non-binding,1,1,1,1,0,1,centralized,1,1
KOR,0,1,1,1,1,mixed,1,1,1,1,0,1,centralized,1,1
SGP,0,0,1,1,0,non-binding,1,1,0,1,0,1,none,0,1
TWN,1,0,1,1,1,mixed,1,1,0,1,0,1,centralized,0,1
ISR,0,0,1,1,1,non-binding,1,1,1,1,0,1,centralized,1,1
ARE,0,0,1,1,1,non-binding,1,1,0,1,0,1,centralized,0,1
QAT,0,0,1,0,0,non-binding,1,1,0,1,0,1,none,0,1
AUT,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
BEL,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
BGR,0,1,1,1,1,binding,1,1,0,1,0,1,eu_delegated,0,1
HRV,0,1,1,1,1,binding,1,1,0,1,0,1,eu_delegated,0,1
CZE,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
DNK,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
EST,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
FIN,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
FRA,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
DEU,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
GRC,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
HUN,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
IRL,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
ITA,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
NLD,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
POL,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
ROU,0,1,1,1,1,binding,1,1,0,1,0,1,eu_delegated,0,1
ESP,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
SWE,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1
GBR,0,1,1,1,1,non-binding,1,1,1,1,1,1,centralized,1,1
CHE,0,1,1,1,0,non-binding,1,1,1,1,0,1,none,1,1
NOR,0,1,1,1,1,binding,1,1,1,1,0,1,eu_delegated,1,1"""

df_final = pd.read_csv(io.StringIO(csv_text))
df_final.to_csv(BASE / "tr_regulatory_metadata.csv", index=False)
print("✅ CSV final regenerado incluyendo Noruega (NOR) y los datos auditados.")
