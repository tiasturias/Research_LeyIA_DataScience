"""Command line entrypoint for Fase 3."""

from __future__ import annotations

import argparse

import pandas as pd

from src.fase3_pipeline.build import build_all
from src.fase3_pipeline.schemas import validate_core
from src.fase3.api import load_dictionary, load_panel, load_snapshot, load_wide


def main() -> None:
    parser = argparse.ArgumentParser(description="Fase 3 Matriz Madre pipeline")
    parser.add_argument("command", choices=["build-all", "validate"])
    args = parser.parse_args()
    if args.command == "build-all":
        outputs = build_all(validate=True)
        for name, df in outputs.items():
            print(f"{name}: {df.shape}")
    elif args.command == "validate":
        panel = load_panel()
        snapshot = load_snapshot()
        dictionary = load_dictionary()
        trace = pd.read_csv(load_wide.__globals__["OUTPUT_DIR"] / "matriz_madre_trazabilidad.csv")
        validate_core(panel, snapshot, dictionary, trace)
        print("Fase 3 validation passed")


if __name__ == "__main__":
    main()
