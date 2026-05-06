"""Regenerate Matriz_Madre_Fase3.xlsx from the (already fixed) CSVs.

The previous run timed out during Excel regeneration leaving a corrupted file.
This script rebuilds it cleanly from outputs/*.csv.
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
EXCEL = OUT_DIR / "Matriz_Madre_Fase3.xlsx"

SHEETS = [
    ("README", None),
    ("Matriz Madre", "matriz_madre_wide.csv"),
    ("Matriz Larga Panel", "matriz_larga_panel.csv"),
    ("Matriz Larga Snapshot", "matriz_larga_snapshot.csv"),
    ("Diccionario Variables", "fase3_diccionario_variables.csv"),
    ("Fuentes Usadas", "fase3_fuentes_usadas.csv"),
    ("Reglas Temporales", "fase3_reglas_temporales.csv"),
    ("Crosswalk Geografico", "fase3_geo_crosswalk_manual.csv"),
    ("Trazabilidad", "matriz_madre_trazabilidad.csv"),
    ("Issues Resueltos", "fase3_issue_resolution_log.csv"),
    ("Decision Log", "fase3_decisiones_metodologicas.csv"),
]


def main() -> None:
    print(f"Regenerating {EXCEL.name}...")
    if EXCEL.exists():
        EXCEL.unlink()

    with pd.ExcelWriter(EXCEL, engine="openpyxl") as writer:
        for sheet, csv_name in SHEETS:
            if csv_name is None:
                # README sheet
                readme_path = OUT_DIR / "README_MATRIZ_MADRE.md"
                if readme_path.exists():
                    text = readme_path.read_text(encoding="utf-8")
                    pd.DataFrame({"README": text.split("\n")}).to_excel(
                        writer, sheet_name="README", index=False
                    )
                    print(f"  README written")
                continue
            csv_path = OUT_DIR / csv_name
            if not csv_path.exists():
                print(f"  SKIP {sheet}: missing {csv_name}")
                continue
            df = pd.read_csv(csv_path)
            df.to_excel(writer, sheet_name=sheet[:31], index=False)
            print(f"  {sheet}: {len(df):,} rows x {len(df.columns)} cols")

        # Chile_Snapshot
        wide = pd.read_csv(OUT_DIR / "matriz_madre_wide.csv")
        chile = wide[wide["iso3"] == "CHL"]
        if not chile.empty:
            chile_long = chile.T.reset_index()
            chile_long.columns = ["variable", "value"]
            chile_long.to_excel(writer, sheet_name="Chile_Snapshot", index=False)
            print(f"  Chile_Snapshot: {len(chile_long)} rows")

        # Chile_vs_Peers
        peers = ["CHL", "ARG", "BRA", "MEX", "COL", "PER", "URY", "ESP"]
        peers_df = wide[wide["iso3"].isin(peers)]
        if not peers_df.empty:
            peers_df.to_excel(writer, sheet_name="Chile_vs_Peers", index=False)
            print(f"  Chile_vs_Peers: {len(peers_df)} rows")

    size = EXCEL.stat().st_size
    print(f"\nDone. {EXCEL} ({size:,} bytes)")


if __name__ == "__main__":
    main()
