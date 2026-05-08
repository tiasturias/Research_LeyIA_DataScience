import pandas as pd
from pathlib import Path

FASE5_OUTPUTS = Path("FASE5/outputs")


def test_variable_count_contract():
    if not (FASE5_OUTPUTS / "mvp_variables_catalog.csv").exists():
        return
    vars_catalog = pd.read_csv(FASE5_OUTPUTS / "mvp_variables_catalog.csv")
    if "is_observed_core" in vars_catalog.columns:
        observed = vars_catalog[vars_catalog["is_observed_core"] == True]
    else:
        observed = vars_catalog
    assert len(observed) == 46
