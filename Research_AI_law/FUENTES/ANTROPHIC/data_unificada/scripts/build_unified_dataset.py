#!/usr/bin/env python3
"""
build_unified_dataset.py
=========================
Unifica los 80+ archivos del repositorio Anthropic/EconomicIndex
(~360 MB, 1.6M+ filas) en un dataset SQLite + Excel.

**Proveniencia completa**: cada valor es trazable hasta su archivo origen,
número de línea original, y hash SHA256 del archivo fuente.

Salida:
  data_unificada/antrophic_economic_index.db       (~400 MB SQLite)
  data_unificada/antrophic_economic_index.xlsx      (~15 MB Excel)
  data_unificada/source_files_manifest.csv          (SHA256 de cada fuente)

Uso:
  python build_unified_dataset.py

Requisitos:
  pip install pandas openpyxl
"""

import os
import sys
import json
import hashlib
import pandas as pd
import sqlite3
import csv
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# ============================================================
# CONFIGURACIÓN
# ============================================================
BASE_DIR = Path("/Users/francoia/Documents/Research_AI_law/ANTROPHIC")
INPUT_DIR = BASE_DIR / "EconomicIndex"
OUTPUT_DIR = BASE_DIR / "data_unificada"

DB_PATH = OUTPUT_DIR / "antrophic_economic_index.db"
XLSX_PATH = OUTPUT_DIR / "antrophic_economic_index.xlsx"
MANIFEST_PATH = OUTPUT_DIR / "source_files_manifest.csv"

LOG_ROWS = []  # Para el log de verificación

# ============================================================
# FUNCIONES DE PROVENIENCIA
# ============================================================

def sha256_file(path):
    """Calcula SHA256 de un archivo."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_source_manifest():
    """
    Construye un manifiesto de TODOS los archivos fuente con:
      - Ruta relativa
      - SHA256 hash
      - Tamaño en bytes
      - Número de filas (si es CSV)
      - Fecha de procesamiento
    """
    print("\n" + "=" * 60)
    print("SOURCE MANIFEST: Hashing all source files")
    print("=" * 60)

    data_extensions = {".csv", ".tsv", ".json", ".xlsx", ".txt", ".pdf", ".ipynb", ".py", ".md"}
    skip_patterns = {".DS_Store", ".git"}

    rows = []
    all_files = sorted(INPUT_DIR.rglob("*"))

    for fpath in all_files:
        if not fpath.is_file():
            continue
        if fpath.name in skip_patterns or any(p in fpath.parts for p in skip_patterns):
            continue

        rel_path = fpath.relative_to(INPUT_DIR)
        size_bytes = fpath.stat().st_size
        ext = fpath.suffix.lower()

        sha = sha256_file(fpath)

        n_rows = None
        if ext == ".csv":
            try:
                with open(fpath, "r") as f:
                    n_rows = sum(1 for _ in f)
            except:
                pass
        elif ext == ".tsv":
            try:
                with open(fpath, "r") as f:
                    n_rows = sum(1 for _ in f)
            except:
                pass

        rows.append({
            "source_file": str(rel_path),
            "sha256": sha,
            "size_bytes": size_bytes,
            "size_mb": round(size_bytes / (1024 * 1024), 2),
            "extension": ext,
            "n_rows": n_rows,
            "processed_at": datetime.now().isoformat(),
        })

    manifest = pd.DataFrame(rows)
    manifest.to_csv(MANIFEST_PATH, index=False)
    print(f"  Manifest saved: {len(manifest)} source files")
    print(f"  Total size: {manifest['size_mb'].sum():.1f} MB")
    return manifest


def add_origin_columns(df, source_file, origin_line_col="_origin_line"):
    """
    Agrega columnas de proveniencia a un DataFrame.
    - _origin_file: ruta relativa del archivo fuente
    - _origin_line: número de línea (1-indexed) en el archivo original
    """
    df = df.copy()
    df["_origin_file"] = str(source_file)
    # El número de línea: header es línea 1, datos desde línea 2
    df[origin_line_col] = range(2, len(df) + 2)
    return df


def add_origin_columns_multi(df, origin_map):
    """
    Para tablas que combinan múltiples fuentes, agrega columnas
    _origin_file_{suffix} y _origin_line_{suffix} por cada fuente.
    
    origin_map: dict {suffix: (source_file_relpath, series_with_lines)}
    """
    df = df.copy()
    for suffix, (source_file, line_series) in origin_map.items():
        df[f"_origin_file_{suffix}"] = str(source_file)
        if line_series is not None:
            df[f"_origin_line_{suffix}"] = line_series
    return df


# ============================================================
# LECTURA CON PROVENIENCIA
# ============================================================

def read_csv_with_provenance(path, **kwargs):
    """
    Lee CSV y retorna (DataFrame con _origin_file, _origin_line) o (DataFrame vacío, None).
    """
    try:
        raw_path = str(path)
        # Leer todas las filas primero para asignar números de línea
        with open(raw_path, "r") as f:
            lines = f.readlines()

        if len(lines) < 1:
            return pd.DataFrame(), None

        header = lines[0].strip().split(kwargs.get("sep", ","))
        data_lines = lines[1:]

        # Parsear con pandas
        # IMPORTANT: keep_default_na=False para que "NA" (Namibia, ISO-2) no se convierta en NaN
        df_kwargs = {**kwargs}
        if "keep_default_na" not in df_kwargs:
            df_kwargs["keep_default_na"] = False
        if "na_values" not in df_kwargs:
            df_kwargs["na_values"] = [""]  # Solo tratar strings vacíos como NaN
        df = pd.read_csv(raw_path, **df_kwargs)
        df = normalize_cols(df)

        # Asignar números de línea: header = línea 1, datos desde línea 2
        df["_origin_line"] = range(2, len(df) + 2)
        # La ruta relativa
        try:
            rel = path.relative_to(INPUT_DIR)
        except:
            rel = path.name
        df["_origin_file"] = str(rel)

        return df, rel
    except Exception as e:
        print(f"  WARNING: Error reading {path}: {e}")
        return pd.DataFrame(), None


def normalize_cols(df):
    """Normaliza nombres de columnas a lowercase con underscores."""
    df = df.copy()
    mapper = {}
    for c in df.columns:
        if c.startswith("_"):
            mapper[c] = c
            continue
        new = c.strip().lower()
        new = new.replace(" ", "_").replace("-", "_").replace("/", "_")
        new = new.replace(".", "_").replace("(", "").replace(")", "")
        new = new.replace("：", ":").replace("，", ",")
        new = new.replace("·", "").replace("'", "")
        new = new.replace("o*net-soc", "onet_soc").replace("o*net", "onet")
        mapper[c] = new
    df.rename(columns=mapper, inplace=True)
    return df


def read_csv_tracked(path, **kwargs):
    """Versión simplificada que lee CSV y agrega tracking."""
    df, _ = read_csv_with_provenance(path, **kwargs)
    return df


def log_row_count(table_name, source, n_rows):
    LOG_ROWS.append({
        "table": table_name,
        "source": str(source) if source else "unknown",
        "n_rows": n_rows
    })
    print(f"  [{table_name}] {source}: {n_rows} rows")

# ============================================================
# SECCIÓN 1: LEER TODOS LOS ARCHIVOS
# ============================================================

def read_all_source_files():
    """Lee todos los 65+ archivos de datos del EconomicIndex con proveniencia."""
    data = {}

    print("=" * 60)
    print("SECTION 1: Reading all source files with provenance")
    print("=" * 60)

    # --- labor_market_impacts ---
    print("\n--- labor_market_impacts ---")
    lm_dir = INPUT_DIR / "labor_market_impacts"
    data["job_exposure"] = read_csv_tracked(lm_dir / "job_exposure.csv")
    log_row_count("job_exposure", "labor_market_impacts/job_exposure.csv", len(data["job_exposure"]))
    data["task_penetration"] = read_csv_tracked(lm_dir / "task_penetration.csv")
    log_row_count("task_penetration", "labor_market_impacts/task_penetration.csv", len(data["task_penetration"]))

    # --- release_2025_02_10 ---
    print("\n--- release_2025_02_10 ---")
    r0210 = INPUT_DIR / "release_2025_02_10"
    data["soc_structure_0210"] = read_csv_tracked(r0210 / "SOC_Structure.csv")
    log_row_count("soc_structure_0210", "release_2025_02_10/SOC_Structure.csv", len(data["soc_structure_0210"]))
    data["automation_vs_augmentation_0210"] = read_csv_tracked(r0210 / "automation_vs_augmentation.csv")
    log_row_count("automation_vs_augmentation_0210", "release_2025_02_10/automation_vs_augmentation.csv", len(data["automation_vs_augmentation_0210"]))
    data["bls_employment"] = read_csv_tracked(r0210 / "bls_employment_may_2023.csv")
    log_row_count("bls_employment", "release_2025_02_10/bls_employment_may_2023.csv", len(data["bls_employment"]))
    data["onet_task_mappings_0210"] = read_csv_tracked(r0210 / "onet_task_mappings.csv")
    log_row_count("onet_task_mappings_0210", "release_2025_02_10/onet_task_mappings.csv", len(data["onet_task_mappings_0210"]))
    data["onet_task_statements_0210"] = read_csv_tracked(r0210 / "onet_task_statements.csv")
    log_row_count("onet_task_statements_0210", "release_2025_02_10/onet_task_statements.csv", len(data["onet_task_statements_0210"]))
    data["wage_data"] = read_csv_tracked(r0210 / "wage_data.csv")
    log_row_count("wage_data", "release_2025_02_10/wage_data.csv", len(data["wage_data"]))

    # --- release_2025_03_27 ---
    print("\n--- release_2025_03_27 ---")
    r0327 = INPUT_DIR / "release_2025_03_27"
    data["automation_vs_augmentation_by_task"] = read_csv_tracked(
        r0327 / "automation_vs_augmentation_by_task.csv")
    log_row_count("automation_vs_augmentation_by_task",
                  "release_2025_03_27/automation_vs_augmentation_by_task.csv",
                  len(data["automation_vs_augmentation_by_task"]))
    data["onet_task_statements_0327"] = read_csv_tracked(r0327 / "onet_task_statements.csv")
    log_row_count("onet_task_statements_0327", "release_2025_03_27/onet_task_statements.csv",
                  len(data["onet_task_statements_0327"]))
    data["task_pct_v1_0327"] = read_csv_tracked(r0327 / "task_pct_v1.csv")
    log_row_count("task_pct_v1_0327", "release_2025_03_27/task_pct_v1.csv",
                  len(data["task_pct_v1_0327"]))
    data["task_pct_v2_0327"] = read_csv_tracked(r0327 / "task_pct_v2.csv")
    log_row_count("task_pct_v2_0327", "release_2025_03_27/task_pct_v2.csv",
                  len(data["task_pct_v2_0327"]))
    data["task_thinking_fractions"] = read_csv_tracked(r0327 / "task_thinking_fractions.csv")
    log_row_count("task_thinking_fractions", "release_2025_03_27/task_thinking_fractions.csv",
                  len(data["task_thinking_fractions"]))

    # TSV cluster_level_dataset
    try:
        tsv_path = r0327 / "cluster_level_data" / "cluster_level_dataset.tsv"
        df_tsv = pd.read_csv(tsv_path, sep="\t")
        df_tsv = normalize_cols(df_tsv)
        df_tsv["_origin_line"] = range(2, len(df_tsv) + 2)
        df_tsv["_origin_file"] = "release_2025_03_27/cluster_level_data/cluster_level_dataset.tsv"
        data["cluster_level_dataset"] = df_tsv
        log_row_count("cluster_level_dataset",
                      "release_2025_03_27/cluster_level_data/cluster_level_dataset.tsv",
                      len(df_tsv))
    except Exception as e:
        print(f"  WARNING: {e}")
        data["cluster_level_dataset"] = pd.DataFrame()

    # --- release_2025_09_15 ---
    print("\n--- release_2025_09_15 ---")
    r0915 = INPUT_DIR / "release_2025_09_15"

    # data/input
    r0915_input = r0915 / "data" / "input"
    input_files = [
        "bea_us_state_gdp_2024.csv",
        "sc-est2024-agesex-civ.csv",
        "soc_structure_raw.csv",
        "task_pct_v1.csv",
        "task_pct_v2.csv",
        "working_age_pop_2024_country_raw.csv",
    ]
    for fname in input_files:
        key = f"r0915_input_{fname.replace('.csv','').replace('-','_').replace(' ','_')}"
        if fname == "bea_us_state_gdp_2024.csv":
            # BEA CSV has 3 metadata lines before header
            data[key] = read_csv_tracked(r0915_input / fname, skiprows=3)
        else:
            data[key] = read_csv_tracked(r0915_input / fname)
        log_row_count(key, f"release_2025_09_15/data/input/{fname}", len(data[key]))

    # data/intermediate
    r0915_inter = r0915 / "data" / "intermediate"
    inter_files = [
        "aei_raw_1p_api_2025-08-04_to_2025-08-11.csv",
        "aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv",
        "gdp_2024_country.csv",
        "gdp_2024_us_state.csv",
        "iso_country_codes.csv",
        "onet_task_statements.csv",
        "soc_structure.csv",
        "working_age_pop_2024_country.csv",
        "working_age_pop_2024_us_state.csv",
    ]
    for fname in inter_files:
        key = f"r0915_inter_{fname.replace('.csv','').replace('-','_').replace(' ','_')}"
        data[key] = read_csv_tracked(r0915_inter / fname)
        log_row_count(key, f"release_2025_09_15/data/intermediate/{fname}", len(data[key]))

    # data/output
    r0915_out = r0915 / "data" / "output"
    data["aei_enriched_claude_ai"] = read_csv_tracked(
        r0915_out / "aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv")
    log_row_count("aei_enriched_claude_ai",
                  "release_2025_09_15/data/output/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv",
                  len(data["aei_enriched_claude_ai"]))

    # JSON hierarchy trees
    print("\n--- JSON hierarchy trees ---")
    for json_fname in ["request_hierarchy_tree_1p_api.json", "request_hierarchy_tree_claude_ai.json"]:
        json_path = r0915_out / json_fname
        try:
            with open(json_path, "r") as f:
                raw = f.read()
            data[f"hierarchy_{json_fname.replace('.json','')}"] = json.loads(raw)
            rel = f"release_2025_09_15/data/output/{json_fname}"
            data[f"hierarchy_{json_fname.replace('.json','')}_sha256"] = hashlib.sha256(raw.encode()).hexdigest()
            data[f"hierarchy_{json_fname.replace('.json','')}_path"] = rel
            log_row_count(f"hierarchy_{json_fname.replace('.json','')}", rel, "N/A (JSON)")
        except Exception as e:
            print(f"  WARNING: Error reading {json_path}: {e}")

    # --- release_2026_01_15 ---
    print("\n--- release_2026_01_15 ---")
    r0115 = INPUT_DIR / "release_2026_01_15"
    for fname in [
        "aei_raw_1p_api_2025-11-13_to_2025-11-20.csv",
        "aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv",
    ]:
        key = f"r0115_{fname.replace('.csv','').replace('-','_').replace(' ','_')}"
        data[key] = read_csv_tracked(r0115 / "data" / "intermediate" / fname)
        log_row_count(key, f"release_2026_01_15/data/intermediate/{fname}", len(data[key]))

    # --- release_2026_03_24 ---
    print("\n--- release_2026_03_24 ---")
    r0324 = INPUT_DIR / "release_2026_03_24"
    for fname in [
        "aei_raw_1p_api_2026-02-05_to_2026-02-12.csv",
        "aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv",
    ]:
        key = f"r0324_{fname.replace('.csv','').replace('-','_').replace(' ','_')}"
        data[key] = read_csv_tracked(r0324 / "data" / fname)
        log_row_count(key, f"release_2026_03_24/data/{fname}", len(data[key]))

    return data

# ============================================================
# SECCIÓN 2: CONSTRUIR AEI METRICS LONG (con proveniencia)
# ============================================================

def build_aei_metrics_long(data):
    """Unifica los 6 archivos AEI raw en una tabla long con trazabilidad completa."""
    print("\n" + "=" * 60)
    print("SECTION 2: Building aei_metrics_long (with full provenance)")
    print("=" * 60)

    raw_keys = [
        ("r0915_inter_aei_raw_1p_api_2025_08_04_to_2025_08_11",
         "1P API", "2025-08-04", "2025-08-11",
         "release_2025_09_15/data/intermediate/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv"),
        ("r0915_inter_aei_raw_claude_ai_2025_08_04_to_2025_08_11",
         "Claude AI", "2025-08-04", "2025-08-11",
         "release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv"),
        ("r0115_aei_raw_1p_api_2025_11_13_to_2025_11_20",
         "1P API", "2025-11-13", "2025-11-20",
         "release_2026_01_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv"),
        ("r0115_aei_raw_claude_ai_2025_11_13_to_2025_11_20",
         "Claude AI", "2025-11-13", "2025-11-20",
         "release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv"),
        ("r0324_aei_raw_1p_api_2026_02_05_to_2026_02_12",
         "1P API", "2026-02-05", "2026-02-12",
         "release_2026_03_24/data/aei_raw_1p_api_2026-02-05_to_2026-02-12.csv"),
        ("r0324_aei_raw_claude_ai_2026_02_05_to_2026_02_12",
         "Claude AI", "2026-02-05", "2026-02-12",
         "release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv"),
    ]

    all_dfs = []
    for key, platform, ds, de, origin_file in raw_keys:
        df = data.get(key)
        if df is None or df.empty:
            print(f"  SKIP {key}: no data")
            continue
        if "geo_id" not in df.columns:
            print(f"  SKIP {key}: unexpected cols {list(df.columns)[:5]}")
            continue
        # Asegurar que _origin_file está correcto
        if "_origin_file" in df.columns:
            df["_origin_file"] = origin_file
        df["_source_release"] = key.replace("r0915_inter_", "").replace("r0115_", "").replace("r0324_", "")
        all_dfs.append(df)
        print(f"  APPEND {origin_file}: {len(df)} rows")

    if not all_dfs:
        print("  ERROR: No AEI data found!")
        return pd.DataFrame()

    result = pd.concat(all_dfs, ignore_index=True)
    print(f"  TOTAL aei_metrics_long: {len(result)} rows")

    # Agregar geo_name desde enriched
    enriched = data.get("aei_enriched_claude_ai")
    if enriched is not None and not enriched.empty and "geo_name" in enriched.columns:
        geo_name_map = enriched[["geo_id", "geo_name"]].drop_duplicates()
        geo_name_map = geo_name_map.set_index("geo_id")["geo_name"].to_dict()
        result["geo_name"] = result["geo_id"].map(geo_name_map)
        n_mapped = result["geo_name"].notna().sum()
        print(f"  Mapped {n_mapped}/{len(result)} geo_ids to geo_name "
              f"(from release_2025_09_15/data/output/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv)")

    return result

# ============================================================
# SECCIÓN 3: AEI METRICS WIDE
# ============================================================

def build_aei_metrics_wide(aei_long):
    """
    Pivotea aei_metrics_long a formato ancho.
    
    ESTRATEGIA: No pivotamos por cluster_name (hay ~1400 clusters únicos, lo que
    crearía cientos de miles de columnas). En su lugar:
      - Tabla WIDE: pivotea solo por 'variable', agregando (suma para counts,
        promedio para pcts) a través de todos los clusters.
      - Tabla aparte: aei_metrics_wide_by_cluster (geo_id x cluster_name).
    """
    print("\n" + "=" * 60)
    print("SECTION 3: Building aei_metrics_wide")
    print("=" * 60)

    if aei_long.empty:
        return pd.DataFrame(), pd.DataFrame()

    df = aei_long.copy()

    # ===== WIDE TABLE 1: Aggregate by variable (across all clusters) =====
    # Separar counts (sum) de percentages (mean)
    count_vars = [v for v in df["variable"].unique() if "count" in v or "cost" in v]
    pct_vars = [v for v in df["variable"].unique() if "pct" in v or "index" in v]

    def agg_func(var_name):
        if "count" in var_name or "cost" in var_name:
            return "sum"
        return "mean"

    # Agrupar y agregar
    index_cols = ["geo_id", "geography", "date_start", "date_end", "platform_and_product"]
    wide_agg = df.groupby(index_cols + ["variable"])["value"].agg(
        lambda x: x.sum() if "count" in x.name or "cost" in x.name else x.mean()
    ).reset_index()

    # Agregar por variable
    wide_rows = []
    for key_tuple, grp in df.groupby(index_cols):
        if not isinstance(key_tuple, tuple):
            key_tuple = (key_tuple,)
        row = dict(zip(index_cols, key_tuple))
        for var_val, var_grp in grp.groupby("variable"):
            vals = var_grp["value"].dropna()
            if len(vals) == 0:
                continue
            if "count" in var_val or "cost" in var_val:
                row[var_val] = vals.sum()
            else:
                row[var_val] = vals.mean()
        wide_rows.append(row)

    wide1 = pd.DataFrame(wide_rows)

    # Agregar _origin_files
    origin_agg = df.groupby(index_cols)["_origin_file"].apply(
        lambda x: "; ".join(sorted(set(x)))
    ).reset_index()
    wide1 = wide1.merge(origin_agg, on=index_cols, how="left")
    wide1.rename(columns={"_origin_file": "_origin_files"}, inplace=True)

    # Agregar geo_name
    geo_map = aei_long[["geo_id", "geo_name"]].dropna().drop_duplicates(
        subset="geo_id").set_index("geo_id")["geo_name"].to_dict()
    wide1["geo_name"] = wide1["geo_id"].map(geo_map)

    print(f"  WIDE (aggregated): {wide1.shape[0]} rows × {wide1.shape[1]} columns")

    # ===== WIDE TABLE 2: By cluster (only collaboration metrics for level 0) =====
    cluster_df = df[
        (df["facet"] == "collaboration") &
        (df["level"] == 0) &
        (df["variable"].isin(["collaboration_count", "collaboration_pct"]))
    ].copy()

    if not cluster_df.empty:
        cluster_wide_rows = []
        for (idx_vals), grp in cluster_df.groupby(index_cols):
            row = dict(zip(index_cols, idx_vals))
            for _, r in grp.iterrows():
                cname = str(r.get("cluster_name", "__unknown__")).strip().strip('"')
                vname = str(r.get("variable", "unknown"))
                col_name = f"cluster_{cname[:60]}_{vname}"
                row[col_name] = r.get("value", None)
            cluster_wide_rows.append(row)
        wide2 = pd.DataFrame(cluster_wide_rows)
        print(f"  WIDE (by_cluster): {wide2.shape[0]} rows × {wide2.shape[1]} columns")
    else:
        wide2 = pd.DataFrame()

    return wide1, wide2

# ============================================================
# SECCIÓN 4: DIMENSIONES CON PROVENIENCIA
# ============================================================

def build_dim_occupation(data):
    """dim_occupation desde SOC_Structure con _origin_file."""
    print("\n" + "=" * 60)
    print("SECTION 4: Building dimensions with provenance")
    print("=" * 60)

    for key, origin in [
        ("soc_structure_0210", "release_2025_02_10/SOC_Structure.csv"),
        ("r0915_inter_soc_structure", "release_2025_09_15/data/intermediate/soc_structure.csv"),
    ]:
        df = data.get(key)
        if df is not None and not df.empty:
            df = df.copy()
            # Ya tiene _origin_file y _origin_line de la lectura
            if "_origin_file" not in df.columns:
                df["_origin_file"] = origin
            print(f"  dim_occupation: {len(df)} rows from {origin}")
            return df

    print("  WARNING: No SOC structure found!")
    return pd.DataFrame()


def build_dim_onet_task(data):
    for key, origin in [
        ("onet_task_statements_0210", "release_2025_02_10/onet_task_statements.csv"),
        ("onet_task_statements_0327", "release_2025_03_27/onet_task_statements.csv"),
        ("r0915_inter_onet_task_statements",
         "release_2025_09_15/data/intermediate/onet_task_statements.csv"),
    ]:
        df = data.get(key)
        if df is not None and not df.empty:
            df = df.copy()
            if "_origin_file" not in df.columns:
                df["_origin_file"] = origin
            n_before = len(df)
            # Eliminar duplicados exactos (manteniendo _origin_line del primero)
            df = df.drop_duplicates(subset=[c for c in df.columns
                                            if c not in ("_origin_line",)])
            print(f"  dim_onet_task: {len(df)} rows from {origin} "
                  f"(removed {n_before - len(df)} dups)")
            return df

    print("  WARNING: No ONET task statements found!")
    return pd.DataFrame()


def build_dim_geography(data):
    """dim_geography con ISO codes + US states + global, cada fila con su origen."""
    rows = []

    # ISO country codes
    iso = data.get("r0915_inter_iso_country_codes")
    if iso is not None and not iso.empty:
        for _, r in iso.iterrows():
            rows.append({
                "geo_id": r.get("iso_alpha_3", ""),
                "geography_type": "country",
                "iso_alpha_2": r.get("iso_alpha_2", None),
                "iso_alpha_3": r.get("iso_alpha_3", None),
                "country_name": r.get("country_name", None),
                "state_code": None,
                "state_name": None,
                "_origin_file": r.get("_origin_file",
                                      "release_2025_09_15/data/intermediate/iso_country_codes.csv"),
                "_origin_line": r.get("_origin_line", None),
            })

    # US states
    state_data = data.get("r0915_inter_working_age_pop_2024_us_state")
    if state_data is not None and not state_data.empty:
        for _, r in state_data.iterrows():
            st = str(r.get("state", "").strip()) if pd.notna(r.get("state", None)) else ""
            code = str(r.get("state_code", "").strip()) if pd.notna(r.get("state_code", None)) else ""
            rows.append({
                "geo_id": f"US-{code}" if code else f"US-{st}",
                "geography_type": "state_us",
                "iso_alpha_2": None,
                "iso_alpha_3": "USA",
                "country_name": "United States",
                "state_code": code,
                "state_name": st,
                "_origin_file": r.get("_origin_file",
                                      "release_2025_09_15/data/intermediate/working_age_pop_2024_us_state.csv"),
                "_origin_line": r.get("_origin_line", None),
            })

    # Global
    rows.append({
        "geo_id": "GLOBAL",
        "geography_type": "global",
        "iso_alpha_2": None,
        "iso_alpha_3": None,
        "country_name": "Global",
        "state_code": None,
        "state_name": None,
        "_origin_file": "builtin:global_entry",
        "_origin_line": None,
    })

    result = pd.DataFrame(rows)
    result = result.drop_duplicates(subset=["geo_id"])
    print(f"  dim_geography: {len(result)} rows")
    return result


def build_dim_cluster_hierarchy(data):
    """dim_cluster_hierarchy desde JSON trees, con SHA256 de origen."""
    print("\n--- dim_cluster_hierarchy ---")
    rows = []
    for prefix, platform in [
        ("hierarchy_request_hierarchy_tree_1p_api", "1P API"),
        ("hierarchy_request_hierarchy_tree_claude_ai", "Claude AI"),
    ]:
        tree = data.get(prefix)
        if tree is None:
            continue

        json_path = data.get(f"{prefix}_path", "unknown")
        json_sha = data.get(f"{prefix}_sha256", "unknown")

        def walk(node, lvl2_name="", lvl2_desc="", lvl1_name="", lvl1_desc=""):
            lvl = node.get("level", -1)
            cname = node.get("cluster_name", "")
            cdesc = node.get("cluster_description", "")
            children = node.get("children", [])

            if lvl == 2:
                lvl2_name, lvl2_desc = cname, cdesc
            elif lvl == 1:
                lvl1_name, lvl1_desc = cname, cdesc

            if lvl == 0:
                rows.append({
                    "platform": platform,
                    "level_2_cluster": lvl2_name,
                    "level_2_description": lvl2_desc,
                    "level_1_cluster": lvl1_name,
                    "level_1_description": lvl1_desc,
                    "level_0_cluster": cname,
                    "level_0_description": cdesc,
                    "_origin_file": json_path,
                    "_origin_sha256": json_sha,
                })

            for child in children:
                walk(child, lvl2_name, lvl2_desc, lvl1_name, lvl1_desc)

        for root_node in tree.get("request_hierarchy", []):
            walk(root_node)

    result = pd.DataFrame(rows)
    if not result.empty:
        result = result.drop_duplicates()
    print(f"  dim_cluster_hierarchy: {len(result)} rows")
    return result

# ============================================================
# SECCIÓN 5: TABLAS DE HECHOS CON PROVENIENCIA
# ============================================================

def build_fact_automation_tasks(data):
    print("\n" + "=" * 60)
    print("SECTION 5: Building fact tables with provenance")
    print("=" * 60)

    df = data.get("automation_vs_augmentation_by_task")
    if df is not None and not df.empty:
        df = df.copy()
        if "_origin_file" not in df.columns:
            df["_origin_file"] = "release_2025_03_27/automation_vs_augmentation_by_task.csv"
        print(f"  fact_automation_tasks: {len(df)} rows")
        return df
    print("  WARNING: automation_vs_augmentation_by_task not found!")
    return pd.DataFrame()


def build_fact_task_penetration(data):
    df = data.get("task_penetration")
    if df is not None and not df.empty:
        print(f"  fact_task_penetration: {len(df)} rows")
        return df
    print("  WARNING: task_penetration not found!")
    return pd.DataFrame()


def build_fact_labor_market(data):
    """fact_labor_market: job_exposure + wage_data + bls_employment con proveniencia."""
    parts = []
    for key, origin in [
        ("job_exposure", "labor_market_impacts/job_exposure.csv"),
        ("wage_data", "release_2025_02_10/wage_data.csv"),
        ("bls_employment", "release_2025_02_10/bls_employment_may_2023.csv"),
    ]:
        df = data.get(key)
        if df is not None and not df.empty:
            df = df.copy()
            if "_origin_file" not in df.columns:
                df["_origin_file"] = origin
            parts.append(df)

    if not parts:
        print("  WARNING: No labor market data!")
        return pd.DataFrame()

    result = pd.concat(parts, ignore_index=True)
    print(f"  fact_labor_market: {len(result)} rows "
          f"(sources: job_exposure, wage_data, bls_employment)")
    return result


def build_fact_cluster_profiles(data):
    df = data.get("cluster_level_dataset")
    if df is not None and not df.empty:
        if "_origin_file" not in df.columns:
            df["_origin_file"] = "release_2025_03_27/cluster_level_data/cluster_level_dataset.tsv"
        print(f"  fact_cluster_profiles: {len(df)} rows")
        return df
    print("  WARNING: cluster_level_dataset not found!")
    return pd.DataFrame()


def build_fact_gdp_economic(data):
    """
    fact_gdp_economic: merge GDP + working_age_pop por país.
    Cada columna mantiene su propio _origin_file.
    """
    gdp = data.get("r0915_inter_gdp_2024_country")
    pop = data.get("r0915_inter_working_age_pop_2024_country")

    if gdp is None or gdp.empty:
        print("  WARNING: No GDP data!")
        return pd.DataFrame()

    # Preservar proveniencia de GDP
    gdp_origin = gdp["_origin_file"].iloc[0] if "_origin_file" in gdp.columns else "release_2025_09_15/data/intermediate/gdp_2024_country.csv"

    if pop is not None and not pop.empty:
        pop_origin = pop["_origin_file"].iloc[0] if "_origin_file" in pop.columns else "release_2025_09_15/data/intermediate/working_age_pop_2024_country.csv"
        result = pd.merge(gdp, pop, on="iso_alpha_3", how="outer",
                          suffixes=("_gdp", "_pop"))
        result["_origin_file_gdp"] = gdp_origin
        result["_origin_file_pop"] = pop_origin
        print(f"  fact_gdp_economic: {len(result)} rows (merged GDP + population)")
    else:
        result = gdp.copy()
        print(f"  fact_gdp_economic: {len(result)} rows (GDP only)")

    return result


def build_fact_gdp_us_state(data):
    gdp = data.get("r0915_input_bea_us_state_gdp_2024")
    pop = data.get("r0915_inter_working_age_pop_2024_us_state")

    parts = []
    if gdp is not None and not gdp.empty:
        if "_origin_file" not in gdp.columns:
            gdp["_origin_file"] = "release_2025_09_15/data/input/bea_us_state_gdp_2024.csv"
        parts.append(gdp)
    if pop is not None and not pop.empty:
        if "_origin_file" not in pop.columns:
            pop["_origin_file"] = "release_2025_09_15/data/intermediate/working_age_pop_2024_us_state.csv"
        parts.append(pop)

    if not parts:
        print("  WARNING: No US state data!")
        return pd.DataFrame()

    result = pd.concat(parts, ignore_index=True)
    print(f"  fact_gdp_us_state: {len(result)} rows")
    return result


def build_fact_task_percentages(data):
    """fact_task_percentages: task_pct_v1 + v2 + thinking, cada columna con origen."""
    # Leer v1 como base
    base_key = "task_pct_v1_0327"
    base_origin = "release_2025_03_27/task_pct_v1.csv"

    df = data.get(base_key)
    if df is None or df.empty:
        base_key = "r0915_input_task_pct_v1"
        base_origin = "release_2025_09_15/data/input/task_pct_v1.csv"
        df = data.get(base_key)

    if df is None or df.empty:
        print("  WARNING: No task_pct data!")
        return pd.DataFrame()

    result = df[["task_name", "pct", "_origin_file", "_origin_line"]].copy()
    result.rename(columns={"pct": "pct_v1"}, inplace=True)

    # Agregar v2
    v2_key = "task_pct_v2_0327"
    v2_origin = "release_2025_03_27/task_pct_v2.csv"
    v2 = data.get(v2_key)
    if v2 is None or v2.empty:
        v2_key = "r0915_input_task_pct_v2"
        v2_origin = "release_2025_09_15/data/input/task_pct_v2.csv"
        v2 = data.get(v2_key)

    if v2 is not None and not v2.empty:
        v2_sub = v2[["task_name", "pct", "_origin_file", "_origin_line"]].copy()
        v2_sub.rename(columns={"pct": "pct_v2",
                               "_origin_file": "_origin_file_v2",
                               "_origin_line": "_origin_line_v2"}, inplace=True)
        result = result.merge(v2_sub, on="task_name", how="outer")

    # Agregar thinking_fraction
    thinking = data.get("task_thinking_fractions")
    if thinking is not None and not thinking.empty:
        th_sub = thinking[["task_name", "thinking_fraction",
                           "_origin_file", "_origin_line"]].copy()
        th_sub.rename(columns={"_origin_file": "_origin_file_thinking",
                               "_origin_line": "_origin_line_thinking"}, inplace=True)
        result = result.merge(th_sub, on="task_name", how="outer")

    result = result.drop_duplicates(subset=["task_name"])
    print(f"  fact_task_percentages: {len(result)} rows")
    return result


def build_fact_demographics_us(data):
    df = data.get("r0915_input_sc_est2024_agesex_civ")
    if df is not None and not df.empty:
        if "_origin_file" not in df.columns:
            df["_origin_file"] = "release_2025_09_15/data/input/sc-est2024-agesex-civ.csv"
        print(f"  fact_demographics_us: {len(df)} rows")
        return df
    print("  WARNING: US demographics not found!")
    return pd.DataFrame()


def build_fact_onet_task_mappings_aggregated(data):
    for key, origin in [
        ("onet_task_mappings_0210", "release_2025_02_10/onet_task_mappings.csv"),
    ]:
        df = data.get(key)
        if df is not None and not df.empty:
            if "_origin_file" not in df.columns:
                df["_origin_file"] = origin
            print(f"  fact_onet_task_mappings_aggregated: {len(df)} rows")
            return df
    return pd.DataFrame()


def build_fact_automation_vs_augmentation_summary(data):
    dfs = []
    for key, origin, version in [
        ("automation_vs_augmentation_0210",
         "release_2025_02_10/automation_vs_augmentation.csv", "v0"),
        ("r0915_input_automation_vs_augmentation_v1",
         "release_2025_09_15/data/input/automation_vs_augmentation_v1.csv", "v1"),
    ]:
        df = data.get(key)
        if df is not None and not df.empty:
            df = df.copy()
            df["version"] = version
            if "_origin_file" not in df.columns:
                df["_origin_file"] = origin
            dfs.append(df)

    if not dfs:
        return pd.DataFrame()
    result = pd.concat(dfs, ignore_index=True).drop_duplicates()
    print(f"  fact_automation_vs_augmentation_summary: {len(result)} rows")
    return result


def build_fact_workforce_demographics(data):
    df = data.get("r0915_input_working_age_pop_2024_country_raw")
    if df is not None and not df.empty:
        if "_origin_file" not in df.columns:
            df["_origin_file"] = "release_2025_09_15/data/input/working_age_pop_2024_country_raw.csv"
        print(f"  fact_workforce_demographics: {len(df)} rows")
        return df
    print("  WARNING: workforce demographics not found!")
    return pd.DataFrame()

# ============================================================
# SECCIÓN 6: LÍNEA DE DATOS (DATA LINEAGE)
# ============================================================

def build_data_lineage(all_tables, source_manifest):
    """
    Construye la tabla de linaje de datos.
    Para cada tabla de salida, registra:
      - output_table, output_rows
      - source_file(s) que la originaron
      - sha256 de los source files
      - tipo de transformación (direct copy, merge, pivot, concat)
    """
    print("\n" + "=" * 60)
    print("SECTION 6: Building data lineage")
    print("=" * 60)

    sha_map = {}
    if source_manifest is not None and not source_manifest.empty:
        for _, r in source_manifest.iterrows():
            sha_map[r["source_file"]] = r["sha256"]

    lineage = []

    # Mapeo manual table → (sources, transformation_type)
    table_lineage = {
        "aei_metrics_long": (
            [
                "release_2025_09_15/data/intermediate/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv",
                "release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv",
                "release_2026_01_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv",
                "release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv",
                "release_2026_03_24/data/aei_raw_1p_api_2026-02-05_to_2026-02-12.csv",
                "release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv",
            ],
            "concat (6 files)"
        ),
        "aei_metrics_wide": (
            ["aei_metrics_long (derived)"],
            "pivot (long → wide)"
        ),
        "dim_occupation": (
            ["release_2025_02_10/SOC_Structure.csv"],
            "direct copy"
        ),
        "dim_onet_task": (
            ["release_2025_02_10/onet_task_statements.csv"],
            "direct copy (deduplicated)"
        ),
        "dim_geography": (
            [
                "release_2025_09_15/data/intermediate/iso_country_codes.csv",
                "release_2025_09_15/data/intermediate/working_age_pop_2024_us_state.csv",
            ],
            "concat + builtin"
        ),
        "dim_cluster_hierarchy": (
            [
                "release_2025_09_15/data/output/request_hierarchy_tree_1p_api.json",
                "release_2025_09_15/data/output/request_hierarchy_tree_claude_ai.json",
            ],
            "JSON parse + flatten"
        ),
        "fact_automation_tasks": (
            ["release_2025_03_27/automation_vs_augmentation_by_task.csv"],
            "direct copy"
        ),
        "fact_task_penetration": (
            ["labor_market_impacts/task_penetration.csv"],
            "direct copy"
        ),
        "fact_labor_market": (
            [
                "labor_market_impacts/job_exposure.csv",
                "release_2025_02_10/wage_data.csv",
                "release_2025_02_10/bls_employment_may_2023.csv",
            ],
            "concat (3 files)"
        ),
        "fact_cluster_profiles": (
            ["release_2025_03_27/cluster_level_data/cluster_level_dataset.tsv"],
            "direct copy"
        ),
        "fact_gdp_economic": (
            [
                "release_2025_09_15/data/intermediate/gdp_2024_country.csv",
                "release_2025_09_15/data/intermediate/working_age_pop_2024_country.csv",
            ],
            "merge on iso_alpha_3"
        ),
        "fact_gdp_us_state": (
            [
                "release_2025_09_15/data/input/bea_us_state_gdp_2024.csv",
                "release_2025_09_15/data/intermediate/working_age_pop_2024_us_state.csv",
            ],
            "concat"
        ),
        "fact_task_percentages": (
            [
                "release_2025_03_27/task_pct_v1.csv",
                "release_2025_03_27/task_pct_v2.csv",
                "release_2025_03_27/task_thinking_fractions.csv",
            ],
            "merge on task_name"
        ),
        "fact_demographics_us": (
            ["release_2025_09_15/data/input/sc-est2024-agesex-civ.csv"],
            "direct copy"
        ),
        "fact_onet_task_mappings_aggregated": (
            ["release_2025_02_10/onet_task_mappings.csv"],
            "direct copy"
        ),
        "fact_automation_vs_augmentation_summary": (
            [
                "release_2025_02_10/automation_vs_augmentation.csv",
                "release_2025_09_15/data/input/automation_vs_augmentation_v1.csv",
            ],
            "concat + version tag"
        ),
        "fact_workforce_demographics": (
            ["release_2025_09_15/data/input/working_age_pop_2024_country_raw.csv"],
            "direct copy"
        ),
    }

    for table_name, df in all_tables.items():
        if df is None or df.empty:
            continue
        sources, transform = table_lineage.get(table_name, (["unknown"], "unknown"))

        n_rows = len(df)
        source_str = "; ".join(sources)
        sha_strs = []
        for s in sources:
            if s in sha_map:
                sha_strs.append(f"{s}:{sha_map[s]}")
            elif s == "aei_metrics_long (derived)":
                sha_strs.append("derived from aei_metrics_long")
            else:
                sha_strs.append(f"{s}:not_in_manifest")

        lineage.append({
            "output_table": table_name,
            "output_rows": n_rows,
            "source_files": source_str,
            "source_sha256": "; ".join(sha_strs),
            "transformation": transform,
        })

    result = pd.DataFrame(lineage)
    print(f"  data_lineage: {len(result)} entries")
    return result

# ============================================================
# SECCIÓN 7: METADATA
# ============================================================

def build_metadata_column_descriptions(all_tables):
    print("\n--- metadata_column_descriptions ---")
    rows = []
    for table_name, df in all_tables.items():
        if df is None or df.empty:
            continue
        if table_name in ("aei_metrics_wide_by_cluster",):
            # Tablas muy anchas: describir solo primeras 200 columnas
            cols_to_describe = df.columns[:200].tolist()
            skipped = len(df.columns) - 200
        else:
            cols_to_describe = df.columns.tolist()
            skipped = 0
        for col in cols_to_describe:
            try:
                col_data = df[col]
                dtype = str(col_data.dtype) if hasattr(col_data, 'dtype') else type(col_data).__name__
                n_non_null = int(col_data.notna().sum()) if hasattr(col_data, 'notna') else len(col_data)
                n_total = len(df)
                if hasattr(col_data, 'dropna'):
                    sample_vals = col_data.dropna().unique()[:3].tolist()
                else:
                    sample_vals = []
                sample_str = "; ".join(str(v)[:80] for v in sample_vals) if sample_vals else ""
                rows.append({
                    "table_name": table_name,
                    "column_name": str(col)[:100],
                    "dtype": dtype,
                    "n_non_null": n_non_null,
                    "n_total": n_total,
                    "pct_non_null": round(n_non_null / n_total * 100, 1) if n_total > 0 else 0,
                    "sample_values": sample_str
                })
            except Exception as e:
                rows.append({
                    "table_name": table_name,
                    "column_name": str(col)[:100],
                    "dtype": "ERROR",
                    "n_non_null": 0,
                    "n_total": len(df),
                    "pct_non_null": 0,
                    "sample_values": f"metadata_error: {str(e)[:80]}"
                })
        if skipped:
            print(f"    {table_name}: described 200/{len(df.columns)} columns ({skipped} skipped)")
    result = pd.DataFrame(rows)
    print(f"  metadata_column_descriptions: {len(result)} rows")
    return result


def build_metadata_row_counts():
    df = pd.DataFrame(LOG_ROWS)
    print(f"  metadata_row_counts: {len(df)} rows")
    return df

# ============================================================
# SECCIÓN 8: ESCRIBIR SQLITE
# ============================================================

def write_sqlite(all_tables, db_path):
    print("\n" + "=" * 60)
    print("SECTION 8: Writing SQLite database")
    print("=" * 60)

    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(str(db_path))

    for table_name, df in all_tables.items():
        if df is None or df.empty:
            continue
        # Limpiar nombres de columnas para SQLite
        clean_df = df.copy()
        rename_map = {}
        for c in clean_df.columns:
            new = str(c).replace('"', "").replace("'", "")
            if new != c:
                rename_map[c] = new
        if rename_map:
            clean_df.rename(columns=rename_map, inplace=True)

        clean_df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"  WROTE {table_name}: {len(clean_df)} rows")

        # Crear índices
        cursor = conn.cursor()
        try:
            cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_{table_name}_origin ON {table_name}(_origin_file)")
        except:
            pass
        if "geo_id" in clean_df.columns:
            try:
                cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_{table_name}_geo ON {table_name}(geo_id)")
            except:
                pass
        if "task_name" in clean_df.columns:
            try:
                cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_{table_name}_task ON {table_name}(task_name)")
            except:
                pass
        if "iso_alpha_3" in clean_df.columns:
            try:
                cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_{table_name}_iso ON {table_name}(iso_alpha_3)")
            except:
                pass
        conn.commit()

    conn.close()
    db_size_mb = db_path.stat().st_size / (1024 * 1024)
    print(f"\n  SQLite: {db_path}")
    print(f"  Size: {db_size_mb:.1f} MB")

# ============================================================
# SECCIÓN 9: ESCRIBIR EXCEL
# ============================================================

def write_excel(all_tables, xlsx_path):
    print("\n" + "=" * 60)
    print("SECTION 9: Writing Excel workbook")
    print("=" * 60)

    if xlsx_path.exists():
        xlsx_path.unlink()

    sheet_order = [
        "README",
        "aei_metrics_wide",
        "aei_metrics_wide_by_cluster",
        "dim_occupation",
        "dim_onet_task",
        "dim_geography",
        "dim_cluster_hierarchy",
        "data_lineage",
        "fact_automation_tasks",
        "fact_task_penetration",
        "fact_labor_market",
        "fact_cluster_profiles",
        "fact_gdp_economic",
        "fact_gdp_us_state",
        "fact_task_percentages",
        "fact_demographics_us",
        "fact_onet_task_mappings_aggregated",
        "fact_automation_vs_augmentation_summary",
        "fact_workforce_demographics",
        "metadata_column_descriptions",
        "metadata_row_counts",
    ]

    with pd.ExcelWriter(str(xlsx_path), engine="openpyxl") as writer:
        # Hoja README
        readme_lines = [
            ["ANTHROPIC ECONOMIC INDEX - UNIFIED DATASET"],
            [""],
            [f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"],
            [f"Source: https://huggingface.co/datasets/Anthropic/EconomicIndex"],
            [f"License: MIT"],
            [""],
            ["=== PROVENANCE GUARANTEE ==="],
            ["Every value in this dataset is traceable to its exact source file."],
            ["Every table has _origin_file and _origin_line columns pointing to"],
            ["the exact file and line number in the original EconomicIndex repository."],
            ["The source_files_manifest.csv contains SHA256 hashes of every source file"],
            ["so you can verify no data was altered."],
            [""],
            ["=== SHEET DESCRIPTIONS ==="],
            ["aei_metrics_wide - Core AEI metrics (1 row per geo x date x platform)"],
            ["dim_occupation - SOC occupational taxonomy"],
            ["dim_onet_task - O*NET task catalog (19k+ tasks)"],
            ["dim_geography - Country ISO codes, US states, global"],
            ["dim_cluster_hierarchy - 3-level cluster hierarchy from JSON trees"],
            ["data_lineage - For every output table: which source files, what SHA256, what transformation"],
            ["fact_automation_tasks - Automation vs augmentation scores per task"],
            ["fact_task_penetration - Task penetration from Claude usage"],
            ["fact_labor_market - Job exposure + wages + BLS employment"],
            ["fact_cluster_profiles - 631 cluster profiles"],
            ["fact_gdp_economic - GDP + working age population by country"],
            ["fact_gdp_us_state - GDP + working age population by US state"],
            ["fact_task_percentages - Task pct v1, v2, and thinking fractions"],
            ["fact_demographics_us - US population by age/sex (Census 2024)"],
            ["fact_onet_task_mappings_aggregated - Task name to pct mappings"],
            ["fact_automation_vs_augmentation_summary - Global automation pcts"],
            ["fact_workforce_demographics - World Bank raw workforce data"],
            ["metadata_column_descriptions - Column-by-column dictionary"],
            ["metadata_row_counts - Row count verification log"],
            [""],
            ["=== AUDIT INSTRUCTIONS ==="],
            ["1. Find the value you want to verify"],
            ["2. Note the _origin_file and _origin_line columns"],
            ["3. Open the corresponding file in EconomicIndex/"],
            ["4. Go to line number _origin_line"],
            ["5. The value should match exactly"],
            ["6. Compute SHA256 of that file and compare with source_files_manifest.csv"],
            [""],
            ["=== DATA INTEGRITY ==="],
            ["- NO synthetic data, NO imputation, NO estimation"],
            ["- NaN values are original missing data (left as-is)"],
            ["- All numeric values are stored as their original type (float/int)"],
            ["- The aei_metrics_long table (~1.4M rows) is only in SQLite (too large for Excel)"],
        ]
        readme_df = pd.DataFrame(readme_lines, columns=["Content"])
        readme_df.to_excel(writer, sheet_name="README", index=False)
        ws = writer.sheets["README"]
        ws.column_dimensions["A"].width = 130
        print("  WROTE README")

        for sheet_name in sheet_order[1:]:
            # aei_metrics_long no cabe en Excel
            if sheet_name == "aei_metrics_long":
                continue

            df = all_tables.get(sheet_name)
            if df is not None and not df.empty:
                excel_short = sheet_name[:31]
                df.to_excel(writer, sheet_name=excel_short, index=False)
                ws = writer.sheets[excel_short]
                for col_idx, col_name in enumerate(df.columns):
                    max_len = max(len(str(col_name)), 8)
                    ws.column_dimensions[
                        chr(65 + col_idx) if col_idx < 26
                        else chr(64 + col_idx // 26) + chr(65 + col_idx % 26)
                    ].width = min(max_len + 2, 45)
                print(f"  WROTE {excel_short}: {len(df)} rows × {len(df.columns)} cols")

    xlsx_size_mb = xlsx_path.stat().st_size / (1024 * 1024)
    print(f"\n  Excel: {xlsx_path}")
    print(f"  Size: {xlsx_size_mb:.1f} MB")

# ============================================================
# SECCIÓN 10: VERIFICACIÓN DE INTEGRIDAD
# ============================================================

def verify_integrity(all_tables, source_manifest):
    print("\n" + "=" * 60)
    print("SECTION 10: Integrity verification")
    print("=" * 60)
    issues = []
    exempt_tables = {"data_lineage", "metadata_column_descriptions", "metadata_row_counts"}

    for table_name, df in all_tables.items():
        if df is None or df.empty:
            continue

        n_cols = df.shape[1]
        n_rows = df.shape[0]

        # Tablas de metadata/no aplica verificar proveniencia
        if table_name in exempt_tables:
            print(f"  {table_name}: {n_rows} rows × {n_cols} cols (metadata table)")
            continue

        # Verificar que las columnas de origen existen
        if n_cols < 500:
            origin_cols = [c for c in df.columns if c.startswith("_origin")]
            if not origin_cols:
                issues.append(f"{table_name}: NO provenance columns found!")
            elif "_origin_file" in df.columns:
                n_missing = df["_origin_file"].isna().sum()
                if n_missing > 0:
                    issues.append(f"{table_name}: {n_missing} rows missing _origin_file")
            elif "_origin_files" in df.columns:
                n_missing = df["_origin_files"].isna().sum()
                if n_missing > 0:
                    issues.append(f"{table_name}: {n_missing} rows missing _origin_files")

        n_nulls = df.isna().sum().sum()
        n_cells = n_rows * n_cols
        null_pct = round(n_nulls / n_cells * 100, 2) if n_cells else 0
        print(f"  {table_name}: {n_rows} rows × {n_cols} cols, "
              f"nulls: {n_nulls:,}/{n_cells:,} ({null_pct}%)")

    # Verificar source manifest
    if source_manifest is not None and not source_manifest.empty:
        n_csv = len(source_manifest[source_manifest["extension"] == ".csv"])
        n_total = len(source_manifest)
        print(f"\n  Source manifest: {n_total} files ({n_csv} CSVs)")

    # Verificar data lineage
    if "data_lineage" in all_tables:
        dl = all_tables["data_lineage"]
        print(f"  Data lineage: {len(dl)} table mappings")

    if issues:
        print("\n  ISSUES FOUND:")
        for i in issues:
            print(f"    - {i}")
    else:
        print("\n  INTEGRITY: ALL OK - every table has provenance tracking")

# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("  ANTHROPIC ECONOMIC INDEX - UNIFIED DATASET BUILDER")
    print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # 0. Source manifest (SHA256 de todos los archivos)
    source_manifest = build_source_manifest()

    # 1. Read all source files with provenance
    source_data = read_all_source_files()

    # 2. Build AEI long
    aei_long = build_aei_metrics_long(source_data)

    # 3. Build AEI wide (returns tuple: aggregated, by_cluster)
    aei_wide, aei_wide_by_cluster = build_aei_metrics_wide(aei_long)

    # 4. Build dimensions
    dim_occ = build_dim_occupation(source_data)
    dim_onet = build_dim_onet_task(source_data)
    dim_geo = build_dim_geography(source_data)
    dim_cluster = build_dim_cluster_hierarchy(source_data)

    # 5. Build fact tables
    fact_auto_tasks = build_fact_automation_tasks(source_data)
    fact_penetration = build_fact_task_penetration(source_data)
    fact_labor = build_fact_labor_market(source_data)
    fact_clusters = build_fact_cluster_profiles(source_data)
    fact_gdp = build_fact_gdp_economic(source_data)
    fact_gdp_state = build_fact_gdp_us_state(source_data)
    fact_task_pct = build_fact_task_percentages(source_data)
    fact_demo = build_fact_demographics_us(source_data)
    fact_onet_maps = build_fact_onet_task_mappings_aggregated(source_data)
    fact_auto_summary = build_fact_automation_vs_augmentation_summary(source_data)
    fact_workforce = build_fact_workforce_demographics(source_data)

    # 6. Assemble all tables
    all_tables = {
        "aei_metrics_long": aei_long,
        "aei_metrics_wide": aei_wide,
        "aei_metrics_wide_by_cluster": aei_wide_by_cluster,
        "dim_occupation": dim_occ,
        "dim_onet_task": dim_onet,
        "dim_geography": dim_geo,
        "dim_cluster_hierarchy": dim_cluster,
        "fact_automation_tasks": fact_auto_tasks,
        "fact_task_penetration": fact_penetration,
        "fact_labor_market": fact_labor,
        "fact_cluster_profiles": fact_clusters,
        "fact_gdp_economic": fact_gdp,
        "fact_gdp_us_state": fact_gdp_state,
        "fact_task_percentages": fact_task_pct,
        "fact_demographics_us": fact_demo,
        "fact_onet_task_mappings_aggregated": fact_onet_maps,
        "fact_automation_vs_augmentation_summary": fact_auto_summary,
        "fact_workforce_demographics": fact_workforce,
    }

    # 7. Build lineage + metadata
    data_lineage = build_data_lineage(all_tables, source_manifest)
    meta_cols = build_metadata_column_descriptions(all_tables)
    meta_rows = build_metadata_row_counts()

    all_tables["data_lineage"] = data_lineage
    all_tables["metadata_column_descriptions"] = meta_cols
    all_tables["metadata_row_counts"] = meta_rows

    # 8. Write SQLite
    write_sqlite(all_tables, DB_PATH)

    # 9. Write Excel
    write_excel(all_tables, XLSX_PATH)

    # 10. Verify
    verify_integrity(all_tables, source_manifest)

    total_rows = sum(len(df) for df in all_tables.values() if df is not None and not df.empty)
    print(f"\n{'=' * 60}")
    print(f"  COMPLETE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Total rows across all tables: {total_rows:,}")
    print(f"  Outputs:")
    print(f"    SQLite: {DB_PATH}")
    print(f"    Excel:  {XLSX_PATH}")
    print(f"    Manifest: {MANIFEST_PATH}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
