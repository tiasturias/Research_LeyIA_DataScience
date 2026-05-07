from __future__ import annotations

import hashlib
import json

from _common.paths import FASE5_OUTPUTS, MVP_ROOT


def _sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def test_phase3_phase4_input_hashes_still_match_manifest(phase5_results):
    manifest = json.loads((FASE5_OUTPUTS / "fase5_manifest.json").read_text(encoding="utf-8"))

    assert manifest["rules"]["phase3_phase4_immutable"] is True
    assert manifest["inputs_hashed"]
    for rel_path, metadata in manifest["inputs_hashed"].items():
        path = MVP_ROOT.parent / rel_path
        assert path.exists(), rel_path
        assert _sha256_file(path) == metadata["sha256"], rel_path
