"""Q5: Uso poblacional."""

import pandas as pd
from ._common_design import ModelDesign, build_model_frame
from ._common_fractional import fit_fractional_logit_or_ols
from ._common_bootstrap import bootstrap_coefficients
from ._common_classification import fit_binary_median_sensitivity


def run_q5(fm: pd.DataFrame, config: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    questions_cfg = config.get("questions", {})
    q5_cfg = questions_cfg.get("Q5_population_usage", {})
    outcomes = q5_cfg.get("primary_outcomes", [])
    
    predictor_sets = config.get("predictor_sets", {})
    x1_core = predictor_sets.get("regulatory_core", ["n_binding", "n_non_binding"])
    x2_minimal = predictor_sets.get("controls_minimal", ["wb_gdp_per_capita_ppp_log", "wb_internet_penetration"])
    
    results = []
    scores = []
    
    for outcome in outcomes:
        if outcome not in fm.columns:
            continue
            
        for predictor in x1_core:
            # Primary Continuous/Fractional Model
            design = ModelDesign(
                question="Q5",
                outcome=outcome,
                predictors=[predictor],
                controls=x2_minimal,
                model_family="fractional_or_linear_by_scale",
                analysis_role="primary_continuous_or_fractional",
            )
            sub, meta = build_model_frame(fm, design)
            if meta["status"] != "ok":
                results.append(meta)
                continue
                
            fit_res = fit_fractional_logit_or_ols(sub, outcome, [predictor] + x2_minimal)
            
            def boot_func(sample):
                res = fit_fractional_logit_or_ols(sample, outcome, [predictor] + x2_minimal)
                return {r["term"]: r["estimate"] for r in res["rows"]}
                
            boot_res = bootstrap_coefficients(boot_func, sub, [predictor])
            boot_dict = boot_res.set_index("term").to_dict("index")
            
            for row in fit_res["rows"]:
                if row["term"] == predictor:
                    rec = {**meta, **row, "fit_status": fit_res["fit_status"]}
                    if predictor in boot_dict:
                        b = boot_dict[predictor]
                        rec["ci95_low"] = b["ci_low"]
                        rec["ci95_high"] = b["ci_high"]
                        rec["ci_method"] = b["ci_method"]
                        rec["bootstrap_success_rate"] = b["bootstrap_success_rate"]
                    
                    rec["primary_analysis"] = True
                    rec["external_validation_used"] = False
                    rec["independent_prediction"] = False
                    rec["causal_claim"] = False
                    results.append(rec)
            
            # Sensitivity Binary Median Model
            med = sub[outcome].median()
            y_bin = (sub[outcome] >= med).astype(int)
            bin_res = fit_binary_median_sensitivity(sub[[predictor] + x2_minimal].values, y_bin)
            bin_rec = {
                **meta,
                **bin_res,
                "analysis_role": "sensitivity_binary_median",
                "primary_analysis": False,
                "term": predictor,
            }
            results.append(bin_rec)
            
            # Descriptive In-Sample Scores
            for idx, r in sub.iterrows():
                scores.append({
                    "iso3": r["iso3"],
                    "question": "Q5",
                    "outcome": outcome,
                    "predictor": predictor,
                    "score_value": float(r[outcome]),
                    "score_scope": "in_sample_descriptive_positioning",
                    "independent_prediction": False,
                    "holdout_used": False,
                    "analysis_scope": "full_preregistered_sample_available_by_outcome"
                })

    df_scores = pd.DataFrame(scores)
    if not df_scores.empty and "country_name_canonical" in fm.columns:
        df_scores = df_scores.merge(fm[["iso3", "country_name_canonical"]], on="iso3", how="left")
        
    return pd.DataFrame(results), df_scores
