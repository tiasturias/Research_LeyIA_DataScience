from pathlib import Path
import pandas as pd
import yaml

OUTPUTS = Path("FASE5/outputs")


def test_phase6_column_groups_exclude_non_estimable():
    if not (OUTPUTS / "mvp_transform_params.csv").exists():
        return
    t = pd.read_csv(OUTPUTS / "mvp_transform_params.csv")
    groups = yaml.safe_load((OUTPUTS / "phase6_ready" / "phase6_column_groups.yaml").read_text())

    non_estimable = set(
        t.loc[t["used_in_primary_modeling"].eq(False), "variable_derived"].dropna()
    )
    primary_groups = [
        "X1_regulatory", "X2_control", "Y_Q1_investment", "Y_Q2_adoption",
        "Y_Q3_innovation", "Y_Q5_population_usage", "Y_Q6_public_sector",
        "primary_model_features",
    ]
    for group in primary_groups:
        used = set(groups.get(group, []))
        assert not used.intersection(non_estimable), f"Non-estimable features in group {group}"
