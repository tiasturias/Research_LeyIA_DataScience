from fase3_pipeline.schemas import validate_core


def test_pandera_core_schemas_pass(panel, snapshot, dictionary, traceability):
    validate_core(panel, snapshot, dictionary, traceability)


def test_primary_keys_are_unique(panel, snapshot, dictionary, traceability):
    assert panel["cell_id"].is_unique
    assert snapshot.groupby(["iso3", "source_id", "variable_matriz"]).size().max() == 1
    assert dictionary["variable_matriz"].is_unique
    assert traceability["cell_id_wide"].is_unique


def test_dictionary_matches_wide_base_variables(wide, dictionary):
    id_cols = {
        "iso3", "country_name_canonical", "entity_type", "region", "income_group",
        "n_sources_present", "source_list", "n_variables_available", "pct_variables_available",
        "included_in_matrix", "included_in_dense_candidate", "inclusion_notes",
    }
    wide_vars = {
        c for c in wide.columns
        if c not in id_cols and not c.endswith("_year_used") and not c.endswith("_confidence")
    }
    dict_vars = set(dictionary["variable_matriz"])
    assert wide_vars == dict_vars


def test_traceability_maps_to_panel_and_all_non_null_wide_cells(panel, wide, traceability):
    panel_ids = set(panel["cell_id"])
    assert set(traceability["cell_id_panel"]).issubset(panel_ids)
    id_cols = {
        "iso3", "country_name_canonical", "entity_type", "region", "income_group",
        "n_sources_present", "source_list", "n_variables_available", "pct_variables_available",
        "included_in_matrix", "included_in_dense_candidate", "inclusion_notes",
    }
    value_cols = [c for c in wide.columns if c not in id_cols and not c.endswith("_year_used") and not c.endswith("_confidence")]
    expected = set()
    for _, row in wide[["iso3"] + value_cols].iterrows():
        for col in value_cols:
            if not row[[col]].isna().iloc[0]:
                expected.add(f"{row['iso3']}__{col}")
    assert expected == set(traceability["cell_id_wide"])


def test_traceability_has_source_fields(traceability):
    required = {
        "cell_id_snapshot", "cell_id_panel", "source_file", "source_sheet",
        "original_variable", "row_identifier", "extraction_rule",
    }
    assert required.issubset(traceability.columns)
    assert traceability[list(required)].notna().all().all()
