import hashlib
import json


def test_manifest_hashes_outputs(output_dir):
    manifest = json.loads((output_dir / "manifest.json").read_text())
    required = {
        "manifest.json", "fase3_fuentes_usadas.csv", "fase3_tablas_seleccionadas.csv",
        "fase3_geo_crosswalk_manual.csv", "fase3_universo_geografico.csv",
        "fase3_diccionario_variables.csv", "fase3_variables_excluidas.csv",
        "fase3_reglas_temporales.csv", "fase3_decisiones_metodologicas.csv",
        "fase3_issue_resolution_log.csv", "fase3_human_review_log.csv",
        "matriz_larga_panel.csv", "matriz_larga_snapshot.csv", "matriz_madre_wide.csv",
        "matriz_madre_trazabilidad.csv", "fase3_reporte_calidad_matriz.csv",
        "Matriz_Madre_Fase3.xlsx", "README_MATRIZ_MADRE.md",
    }
    assert required.issubset(set(manifest["outputs"]))
    for name, meta in manifest["outputs"].items():
        if name == "manifest.json":
            assert meta["self_hash_policy"]
            continue
        digest = hashlib.sha256((output_dir / name).read_bytes()).hexdigest()
        assert digest == meta["sha256"], f"hash mismatch for {name}"


def test_manifest_does_not_use_example_workbook_as_source(output_dir):
    manifest = json.loads((output_dir / "manifest.json").read_text())
    assert not any("Matriz_EJEMPLO" in key for key in manifest["source_files"])


def test_manifest_version_and_configs(output_dir):
    manifest = json.loads((output_dir / "manifest.json").read_text())
    # accept any 1.x version (1.0 base, 1.1+ for in-place quality fixes)
    assert manifest["version"].startswith("1."), f"unexpected version {manifest['version']}"
    config_dir = output_dir.parent / "config" / "fase3"
    for name in ["geo_crosswalk.yaml", "temporal_rules.yaml", "variable_dictionary.yaml", "decisions.yaml"]:
        assert (config_dir / name).exists()
