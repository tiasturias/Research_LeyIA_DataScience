"""Q3: Asociación innovación ~ regulación + controles."""

import pandas as pd
from ._common_design import ModelDesign, build_model_frame
from ._common_regression import fit_ols_adjusted, repeated_kfold_regression_diagnostic
from ._common_bootstrap import bootstrap_coefficients


def run_q3(fm: pd.DataFrame, config: dict) -> pd.DataFrame:
    questions_cfg = config.get("questions", {})
    q3_cfg = questions_cfg.get("Q3_innovation", {})
    outcomes = q3_cfg.get("primary_outcomes", [])
    
    predictor_sets = config.get("predictor_sets", {})
    x1_core = predictor_sets.get("regulatory_core", ["n_binding", "n_non_binding"])
    x2_minimal = predictor_sets.get("controls_minimal", ["wb_gdp_per_capita_ppp_log", "wb_internet_penetration"])
    
    results = []
    
    for outcome in outcomes:
        if outcome not in fm.columns:
            continue
            
        for predictor in x1_core:
            design = ModelDesign(
                question="Q3",
                outcome=outcome,
                predictors=[predictor],
                controls=x2_minimal,
                model_family="linear_or_log_linear_by_distribution",
                analysis_role="primary",
            )
            sub, meta = build_model_frame(fm, design)
            if meta["status"] != "ok":
                results.append(meta)
                continue
                
            fit_res = fit_ols_adjusted(sub, outcome, [predictor] + x2_minimal)
            
            def boot_func(sample):
                res = fit_ols_adjusted(sample, outcome, [predictor] + x2_minimal)
                return {r["term"]: r["estimate"] for r in res["rows"]}
                
            boot_res = bootstrap_coefficients(boot_func, sub, [predictor])
            boot_dict = boot_res.set_index("term").to_dict("index")
            
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
                    
                    rec["external_validation_used"] = False
                    rec["independent_prediction"] = False
                    rec["causal_claim"] = False
                    results.append(rec)

    return pd.DataFrame(results)
