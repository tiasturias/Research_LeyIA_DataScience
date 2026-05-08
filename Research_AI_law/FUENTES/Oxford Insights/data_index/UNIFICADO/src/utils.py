import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# UNIFICADO está DENTRO de data_index, subimos un nivel
DATA_INDEX = os.path.dirname(BASE_DIR)
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
SRC_DIR = os.path.join(BASE_DIR, "src")
VALIDATION_DIR = os.path.join(BASE_DIR, "validation")

SOURCE_FILES = {
    2019: "SHARED_-2019-Index-data-for-report.xlsx",
    2020: "2020-Government-AI-Readiness-Index-public-dataset.xlsx",
    2021: "2021-Government-AI-Readiness-Index-public-dataset.xlsx",
    2022: "2022-Government-AI-Readiness-Index-public-data.xlsx",
    2023: "2023-Government-AI-Readiness-Index-Public-Indicator-Data.xlsx",
    2024: "2024-GAIRI-data.xlsx",
    2025: "2025-Government-AI-Readiness-Index-data-1.xlsx",
}

EXPECTED_COUNTS = {2019: 194, 2020: 172, 2021: 160, 2022: 181, 2023: 193, 2024: 188, 2025: 195}

def source_path(year):
    return os.path.join(DATA_INDEX, SOURCE_FILES[year])

def output_path(name):
    return os.path.join(OUTPUT_DIR, name)

def read_sheet(year, sheet, **kwargs):
    path = source_path(year)
    return pd.read_excel(path, sheet_name=sheet, **kwargs)

def clean_country(name):
    if pd.isna(name):
        return name
    name = str(name).strip()
    name = name.replace("\n", "").replace("\r", "")
    return name

def validate_row_count(df, expected, label):
    actual = len(df)
    if actual == expected:
        print(f"  VALIDACION OK: {label} = {actual} filas")
    else:
        print(f"  VALIDACION ERROR: {label} esperaba {expected}, obtuvo {actual}")
    return actual == expected
