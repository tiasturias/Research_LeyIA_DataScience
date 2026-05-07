"""Orquestador Fase 6: q4 → q1 → q3 → q2 → q5 → q6 → manifest."""

from __future__ import annotations
import json
import subprocess
from datetime import datetime, timezone

from ._common_data import F5_F8_MVP, sha256_file, validate_bundle_hash
from .q4_clustering import run_q4
from .q1_investment import run_q1
from .q3_innovation import run_q3
from .q2_adoption import run_q2
from .q5_population_usage import run_q5
from .q6_public_sector import run_q6

OUTPUTS = F5_F8_MVP / "FASE6" / "outputs"


def main():
    print("[Fase 6 v0.4] Iniciando build-all")
    print("[T1] Validando bundle Fase 5 v2.0 (12 archivos)...")
    validate_bundle_hash()

    print("[T2] Q4 clustering...")
    q4_result = run_q4(seed=42, k=4)
    print(f"  Q4 silhouettes: {q4_result}")

    print("[T3] Q1 inversión...")
    q1_result = run_q1(seed=42, n_boot=2000)
    print(f"  Q1: {q1_result}")

    print("[T4] Q3 innovación...")
    q3_result = run_q3(seed=42, n_boot=2000)
    print(f"  Q3: {q3_result}")

    print("[T5] Q2 adopción empresarial...")
    q2_result = run_q2(seed=42)
    print(f"  Q2: {q2_result}")

    print("[T6] Q5 uso población (NUEVO v0.2)...")
    q5_result = run_q5(seed=42, n_boot=2000)
    print(f"  Q5: {q5_result}")

    print("[T7] Q6 sector público (NUEVO v0.2)...")
    q6_result = run_q6(seed=42, n_boot=2000)
    print(f"  Q6: {q6_result}")

    print("[T8] Generando manifest...")
    write_manifest()

    print("[Fase 6 v0.4] build-all completado")


def write_manifest():
    try:
        git_sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=str(F5_F8_MVP.parent), stderr=subprocess.DEVNULL,
        ).decode().strip()
    except Exception:
        git_sha = "unknown"

    manifest = {
        "phase6_run_id": f"phase6_{git_sha[:8]}_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}",
        "version": "0.4",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "git_sha": git_sha,
        "seed": 42,
        "n_bootstrap": 2000,
        "fdr_method": "benjamini_hochberg",
        "fdr_alpha": 0.05,
        "n_subpreguntas": 6,
        "outputs": {},
        "decisions_log": [
            "F6-A: Q4 → Q1 → Q3 → Q2 → Q5 → Q6 → manifest",
            "F6-B: bootstrap-OLS principal, PSM exploratorio caliper 0.20",
            "F6-C: Q3 dual primary + auxiliary Stanford",
            "F6-D: 5×10 fold + bootstrap 2000 + LOOCV",
            "F6-E: separate Y models + consistency table + FDR",
            "F6-F: hyperparams fixed, no GridSearch",
            "F6-G: Q4 N=43 oficial Gower + N=18 complementario Jaccard",
            "F6-I: lenguaje 'asociación' por defecto",
            "F6-K: Q6 expandida con 6 vars Fase 5",
            "F6-L: PCA fuera de scope (Fase 4 cubre análisis exploratorio)",
            "F6-M: Q2/Q5/Q6 reuso Y",
        ],
    }
    for p in sorted(OUTPUTS.glob("*")):
        if p.is_file() and p.name != "fase6_manifest.json":
            manifest["outputs"][p.name] = {
                "sha256": sha256_file(p), "bytes": p.stat().st_size,
            }
    with open(OUTPUTS / "fase6_manifest.json", "w") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
