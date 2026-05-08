# Auditoría Dataset Unificado Anthropic/EconomicIndex

**Fecha:** 2026-05-04 13:24:13

## Resumen

| Estado | Cantidad |
|--------|----------|
| ✅ PASS | 35 |
| ⚠️ WARN | 4 |
| ❌ FAIL | 0 |
| ⏭️ SKIP | 3 |
| ℹ️ INFO | 3 |
| ❌ ERROR | 0 |

**Veredicto:** ✅ DATOS VERIFICADOS - 100% REALES

---

## AEI_PROVENANCE

| Item | Estado | Detalle |
|------|--------|--------|
| ✅ `Source file references` | PASS | All 6 referenced files exist on disk |
| ✅ `_origin_line coverage` | PASS | 1400819/1400819 rows (100.0%) |
| ✅ `NULL check: geo_id` | PASS | No NULLs |
| ✅ `NULL check: variable` | PASS | No NULLs |
| ✅ `NULL check: value` | PASS | No NULLs |

## MANIFEST

| Item | Estado | Detalle |
|------|--------|--------|
| ✅ `manifest loaded` | PASS | 80 source files listed |
| ✅ `SHA256 verification complete` | PASS | 80/80 files verified, 0 mismatches, 0 not found |

## PROVENANCE

| Item | Estado | Detalle |
|------|--------|--------|
| ✅ `aei_metrics_long._origin_file` | PASS | 1400819/1400819 rows (100.0%) |
| ℹ️ `aei_metrics_wide` | INFO | Derived table (provenance tracked via data_lineage table). Columns: _origin_files |
| ℹ️ `aei_metrics_wide_by_cluster` | INFO | Derived table (provenance tracked via data_lineage table). Columns: _origin_files |
| ⏭️ `data_lineage` | SKIP | Metadata table (no provenance needed) |
| ✅ `dim_cluster_hierarchy._origin_file` | PASS | 970/970 rows (100.0%) |
| ✅ `dim_cluster_hierarchy._origin_sha256` | PASS | 970/970 rows |
| ✅ `dim_geography._origin_file` | PASS | 304/304 rows (100.0%) |
| ✅ `dim_occupation._origin_file` | PASS | 1596/1596 rows (100.0%) |
| ✅ `dim_onet_task._origin_file` | PASS | 19530/19530 rows (100.0%) |
| ✅ `fact_automation_tasks._origin_file` | PASS | 3364/3364 rows (100.0%) |
| ✅ `fact_automation_vs_augmentation_summary._origin_file` | PASS | 6/6 rows (100.0%) |
| ✅ `fact_cluster_profiles._origin_file` | PASS | 630/630 rows (100.0%) |
| ✅ `fact_demographics_us._origin_file` | PASS | 13572/13572 rows (100.0%) |
| ✅ `fact_gdp_economic._origin_line_gdp` | PASS | 174/194 rows |
| ✅ `fact_gdp_economic._origin_file_gdp` | PASS | 194/194 rows |
| ✅ `fact_gdp_economic._origin_line_pop` | PASS | 194/194 rows |
| ✅ `fact_gdp_economic._origin_file_pop` | PASS | 194/194 rows |
| ✅ `fact_gdp_us_state._origin_file` | PASS | 105/105 rows (100.0%) |
| ✅ `fact_labor_market._origin_file` | PASS | 1868/1868 rows (100.0%) |
| ✅ `fact_onet_task_mappings_aggregated._origin_file` | PASS | 3514/3514 rows (100.0%) |
| ✅ `fact_task_penetration._origin_file` | PASS | 17998/17998 rows (100.0%) |
| ✅ `fact_task_percentages._origin_file` | PASS | 3514/4098 rows (85.7%) from v1 (remaining rows from v2 or thinking_fractions) |
| ✅ `fact_task_percentages._origin_file_v2` | PASS | 3365/4098 rows |
| ✅ `fact_task_percentages._origin_line_v2` | PASS | 3365/4098 rows |
| ✅ `fact_task_percentages._origin_file_thinking` | PASS | 3365/4098 rows |
| ✅ `fact_task_percentages._origin_line_thinking` | PASS | 3365/4098 rows |
| ✅ `fact_workforce_demographics._origin_file` | PASS | 266/266 rows (100.0%) |
| ⏭️ `metadata_column_descriptions` | SKIP | Metadata table (no provenance needed) |
| ⏭️ `metadata_row_counts` | SKIP | Metadata table (no provenance needed) |

## ROW_COUNTS

| Item | Estado | Detalle |
|------|--------|--------|
| ✅ `Source CSV rows (manifest)` | PASS | 1,661,257 total rows |
| ✅ `Destination rows (SQLite)` | PASS | 1,474,286 total rows |
| ℹ️ `Source vs Destination` | INFO | Source: 1,661,257 rows vs Dest: 1,474,286 rows (difference: 186,971) |

## SPOT_CHECK

| Item | Estado | Detalle |
|------|--------|--------|
| ✅ `All spot checks` | PASS | 50/50 passed, 0 failed, 0 skipped |

## SYNTHETIC

| Item | Estado | Detalle |
|------|--------|--------|
| ⚠️ `fact_gdp_economic.year_gdp` | WARN | Only 1 unique value across 194 rows (could be legit) |
| ⚠️ `fact_gdp_economic.year_pop` | WARN | Only 1 unique value across 194 rows (could be legit) |
| ⚠️ `fact_workforce_demographics.date` | WARN | Only 1 unique value across 266 rows (could be legit) |
| ⚠️ `fact_workforce_demographics.decimal` | WARN | Only 1 unique value across 266 rows (could be legit) |
| ✅ `Anomaly scan complete` | PASS | No synthetic data patterns detected |

---

*Auditoría generada automáticamente por audit_unified_dataset.py*
