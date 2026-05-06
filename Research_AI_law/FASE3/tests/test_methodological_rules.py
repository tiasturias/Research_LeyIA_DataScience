import pandas as pd


def test_wide_contains_only_country_entities(wide):
    assert set(wide["entity_type"].unique()) == {"country_iso3"}
    forbidden = {
        "EU", "EUU", "WLD", "WORLD", "AFE", "AFW", "EAR", "IDB", "LDC",
        "ANT", "ATA", "ATF", "BVT", "CCK", "CXR", "HMD", "IOT", "NFK", "SCG",
    }
    assert not wide["iso3"].isin(forbidden).any()
    assert wide["n_variables_available"].gt(0).all()


def test_microsoft_crosswalk_clean(output_dir):
    cw = pd.read_csv(output_dir / "fase3_geo_crosswalk_manual.csv")
    assert cw["action"].isin(["approved_by_human", "corrected_by_human"]).all()
    assert cw["confidence_score"].min() >= 90
    assert cw["review_status"].str.contains("approved", case=False, na=False).all()
    assert "Columna Region" not in " ".join(cw["raw_entity_name"].astype(str).tolist())


def test_oxford_2019_excluded_and_wipo_rank_excluded(panel):
    oxford_years = set(panel.loc[panel["source_id"].eq("oxford"), "year"].dropna().astype(int))
    assert 2019 not in oxford_years
    wipo = panel[panel["source_id"].eq("wipo")]
    assert not wipo["original_variable"].str.contains(r"_RANK_\d{4}$", case=False, regex=True, na=False).any()
    assert wipo["unit"].eq("score_0_100").all()


def test_chile_has_four_core_blocks(snapshot, dictionary):
    merged = snapshot[snapshot["iso3"].eq("CHL")].merge(dictionary[["variable_matriz", "bloque_tematico"]], on="variable_matriz", how="left")
    blocks = set(merged["bloque_tematico"].dropna())
    required = {"regulatory_treatment", "ecosystem_outcome", "socioeconomic_control", "institutional_control"}
    assert required.issubset(blocks)


def test_no_metadata_variables_in_dictionary(dictionary):
    forbidden = r"(?:^|_)iso3$|country_code|country_name|pais|fuente|fecha|pagina|region|income"
    hits = dictionary[dictionary["variable_matriz"].str.contains(forbidden, case=False, regex=True, na=False)]
    assert hits.empty


def test_dictionary_has_fase4_metadata(dictionary):
    required = {
        "tipo_original", "regla_transformacion", "n_countries_available",
        "fase4_role", "included_in_fase4_eda", "known_limitations", "human_review_status",
    }
    assert required.issubset(dictionary.columns)
    assert dictionary["redundant_with"].fillna("").ne("").sum() > 0
    assert (~dictionary["is_primary"].astype(bool)).sum() > 0
