"""Update manifest.json with new SHA-256 hashes after the country names fix.

Bumps version 1.0 -> 1.1, sets created_at, adds changelog entry.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        while chunk := fh.read(65536):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    manifest_path = OUT_DIR / "manifest.json"
    with open(manifest_path) as fh:
        manifest = json.load(fh)

    new_hashes = {}
    for name in manifest.get("outputs", {}):
        path = OUT_DIR / name
        if name == "manifest.json":
            # preserve self-hash policy entry
            new_hashes[name] = {"self_hash_policy": "excluded_to_avoid_recursion"}
            continue
        if path.exists():
            new_hashes[name] = {
                "sha256": sha256_of(path),
                "bytes": path.stat().st_size,
            }
            print(f"  hashed {name}")
        else:
            print(f"  MISSING {name}")

    manifest["version"] = "1.1"
    manifest["outputs"] = new_hashes
    manifest["created_at"] = datetime.now(timezone.utc).isoformat()

    changelog = manifest.setdefault("changelog", [])
    changelog.append({
        "date": datetime.now(timezone.utc).isoformat(),
        "version": "1.1",
        "change": "country_name_canonical fix",
        "description": (
            "Fixed bug where 86/199 wide rows had country_name_canonical equal "
            "to ISO3 (e.g. ARG instead of Argentina). Root cause: geo.py used "
            "split(' | ')[0] on country_name_best_effort which returned the "
            "ISO3 code, not the human name. Fix re-derives names from "
            "cobertura_pais_fuente.csv + manual overrides for 35 edge cases."
        ),
        "affected_outputs": [
            "matriz_madre_wide.csv",
            "matriz_larga_panel.csv",
            "matriz_larga_snapshot.csv",
            "matriz_madre_trazabilidad.csv",
            "fase3_universo_geografico.csv",
            "fase3_entidades_excluidas_geografia.csv",
            "fase3_geo_crosswalk_manual.csv",
            "Matriz_Madre_Fase3.xlsx",
        ],
        "rows_fixed_summary": {
            "wide": 86,
            "universe": 99,
            "panel_rows_with_unresolved_iso3": 10103,
            "snapshot_rows_with_unresolved_iso3": 2003,
        },
    })

    with open(manifest_path, "w") as fh:
        json.dump(manifest, fh, indent=2)
    print(f"\nManifest updated to v1.1: {manifest_path}")


if __name__ == "__main__":
    main()
