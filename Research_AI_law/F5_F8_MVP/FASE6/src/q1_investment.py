"""Q1: Asociación inversión ~ regulación + controles."""

import pandas as pd
from ._common_design import ModelDesign, build_model_frame
from ._common_regression import fit_ols_adjusted, repeated_kfold_regression_diagnostic
from ._common_bootstrap import bootstrap_coefficients


def run_q1(fm: pd.DataFrame, config: dict) -> pd.DataFrame:
    questions_cfg = config.get("questions", {})
    q1_cfg = questions_cfg.get("Q1_investment", {})
    outcomes = q1_cfg.get("primary_outcomes", [])
    
    # We use predictor sets from config
    predictor_sets = config.get("predictor_sets", {})
    x1_core = predictor_sets.get("regulatory_core", ["n_binding", "n_non_binding"])
    x2_minimal = predictor_sets.get("controls_minimal", ["wb_gdp_per_capita_ppp_log", "wb_internet_penetration"])
    
    results = []
    
    for outcome in outcomes:
        if outcome not in fm.columns:
            continue
            
        for predictor in x1_core:
            design = ModelDesign(
                question="Q1",
                outcome=outcome,
                predictors=[predictor],
                controls=x2_minimal,
                model_family="linear_regression_parsimonious",
                analysis_role="primary",
            )
            sub, meta = build_model_frame(fm, design)
            if meta["status"] != "ok":
                results.append(meta)
                continue
                
            # OLS Adjusted
            fit_res = fit_ols_adjusted(sub, outcome, [predictor] + x2_minimal)
            
            # Bootstrap for uncertainty
            def boot_func(sample):
                res = fit_ols_adjusted(sample, outcome, [predictor] + x2_minimal)
                return {r["term"]: r["estimate"] for r in res["rows"]}
                
            boot_res = bootstrap_coefficients(boot_func, sub, [predictor])
            boot_dict = boot_res.set_index("term").to_dict("index")
            
            # Diagnostics
            diag = repeated_kfold_regression_diagnostic(
                sub[[predictor] + x2_minimal].values, 
                sub[outcome].values
            )
            
            for row in fit_res["rows"]:
                if row["term"] == predictor:
                    rec = {**meta, **row, **diag}
                    if predictor in boot_dict:
                        b = boot_dict[predictor]
                        rec["ci95_low"] = b["ci_low"]
                        rec["ci95_high"] = b["ci_high"]
                        rec["ci_method"] = b["ci_method"]
                        rec["bootstrap_success_rate"] = b["bootstrap_success_rate"]
                    else:
                        rec["ci_method"] = "not_computed"
                    
                    rec["external_validation_used"] = False
                    rec["independent_prediction"] = False
                    rec["causal_claim"] = False
                    results.append(rec)

    return pd.DataFrame(results)
