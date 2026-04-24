"""
IAPP Global AI Law & Policy Tracker — X1 Coding Pipeline
=========================================================
Extracts, codes, and maps IAPP jurisdiction data to study sample ISO3 codes.
Produces X1 regulation variables consistent with OECD coding methodology.
"""
import json
import pandas as pd
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
IAPP_DIR = BASE / "data/raw/IAPP"
SOURCE_NAME = "IAPP_Global_AI_Law_Policy_Tracker"
SOURCE_DATE = "2026-02"

# ─── Load extracted IAPP data ───
with open(BASE / "data/raw/iapp_tracker_raw_extracted.json") as f:
    iapp_raw = json.load(f)

# ─── ISO3 Mapping ───
IAPP_TO_ISO3 = {
    'Argentina': 'ARG', 'Australia': 'AUS', 'Bangladesh': 'BGD',
    'Brazil': 'BRA', 'Canada': 'CAN', 'Chile': 'CHL',
    'China': 'CHN', 'Colombia': 'COL', 'Egypt': 'EGY',
    'Hong Kong': 'HKG', 'India': 'IND', 'Indonesia': 'IDN',
    'Israel': 'ISR', 'Japan': 'JPN', 'Kenya': 'KEN',
    'Mauritius': 'MUS', 'New Zealand': 'NZL', 'Nigeria': 'NGA',
    'Peru': 'PER', 'Saudi Arabia': 'SAU', 'Singapore': 'SGP',
    'South Korea': 'KOR', 'Taiwan': 'TWN', 'Turkey': 'TUR',
    'United Arab Emirates': 'ARE', 'United Kingdom': 'GBR',
    'United States': 'USA', 'Vietnam': 'VNM',
}

# EU member states in study sample
EU_MEMBERS_IN_STUDY = {
    'AUT': 'Austria', 'BEL': 'Belgium', 'BGR': 'Bulgaria',
    'CYP': 'Cyprus', 'CZE': 'Czechia', 'DEU': 'Germany',
    'DNK': 'Denmark', 'ESP': 'Spain', 'EST': 'Estonia',
    'FIN': 'Finland', 'FRA': 'France', 'GRC': 'Greece',
    'HRV': 'Croatia', 'HUN': 'Hungary', 'IRL': 'Ireland',
    'ITA': 'Italy', 'LTU': 'Lithuania', 'LUX': 'Luxembourg',
    'LVA': 'Latvia', 'MLT': 'Malta', 'NLD': 'Netherlands',
    'POL': 'Poland', 'PRT': 'Portugal', 'ROU': 'Romania',
    'SVK': 'Slovakia', 'SVN': 'Slovenia', 'SWE': 'Sweden',
}

study_iso3 = ['ARE','ARG','ARM','AUS','AUT','BEL','BGD','BGR','BHR','BLR','BLZ',
    'BRA','BRB','CAN','CHE','CHL','CHN','CMR','COL','CRI','CYP','CZE',
    'DEU','DNK','ECU','EGY','ESP','EST','FIN','FRA','GBR','GHA','GRC',
    'HRV','HUN','IDN','IND','IRL','ISL','ISR','ITA','JOR','JPN','KAZ',
    'KEN','KOR','LBN','LKA','LTU','LUX','LVA','MAR','MEX','MLT','MNG',
    'MUS','MYS','NGA','NLD','NOR','NZL','PAK','PAN','PER','PHL','POL',
    'PRT','ROU','RUS','SAU','SGP','SRB','SVK','SVN','SWE','SYC','THA',
    'TUN','TUR','TWN','UGA','UKR','URY','USA','VNM','ZAF']

# ════════════════════════════════════════════════════════════════════════
# EXPERT MANUAL CODING — Based on rigorous reading of IAPP PDF content
# ════════════════════════════════════════════════════════════════════════
#
# Coding rubric:
# has_ai_law (0/1): 1 iff country has ≥1 binding AI-SPECIFIC legislation IN FORCE
# regulatory_approach: none|light_touch|strategy_led|regulation_focused|comprehensive
# regulatory_intensity (0-10): composite depth score
# year_enacted: year of first binding AI-specific regulation
# enforcement_level: none|low|medium|high
# thematic_coverage: count of themes from 15-item checklist

IAPP_CODING = {
    # ── Countries with BINDING AI-specific legislation ──
    'China': {
        'has_ai_law': 1, 'regulatory_approach': 'comprehensive', 'regulatory_intensity': 9,
        'year_enacted': 2021, 'enforcement_level': 'high', 'thematic_coverage': 13,
        'evidence': 'PIPL 2021, Algorithm Recommendation Mgmt 2022, Deep Synthesis 2023, Generative AI Measures 2023, AI Safety Governance Framework, national AI strategy',
    },
    'EU': {
        'has_ai_law': 1, 'regulatory_approach': 'comprehensive', 'regulatory_intensity': 10,
        'year_enacted': 2024, 'enforcement_level': 'high', 'thematic_coverage': 14,
        'evidence': 'EU AI Act entered into force Aug 2024 (full application Aug 2026), GDPR, Digital Services Act, AI Liability Directive proposal, coordinated AI plan',
    },
    'South Korea': {
        'has_ai_law': 1, 'regulatory_approach': 'comprehensive', 'regulatory_intensity': 8,
        'year_enacted': 2025, 'enforcement_level': 'high', 'thematic_coverage': 12,
        'evidence': 'AI Basic Act passed Jan 2025, enforcement decrees from MSICT, National Strategy for AI, AI Safety Institute',
    },
    'Japan': {
        'has_ai_law': 1, 'regulatory_approach': 'comprehensive', 'regulatory_intensity': 7,
        'year_enacted': 2025, 'enforcement_level': 'medium', 'thematic_coverage': 12,
        'evidence': 'AI Promotion Act enacted May 2025 (light-touch binding), National AI Strategy 2022, AI Governance Guidelines, agile governance approach',
    },
    'Peru': {
        'has_ai_law': 1, 'regulatory_approach': 'comprehensive', 'regulatory_intensity': 6,
        'year_enacted': 2023, 'enforcement_level': 'medium', 'thematic_coverage': 9,
        'evidence': 'Law No. 31814 promoting AI innovation with rights safeguards, Law No. 32082 on AI interoperability, National AI Strategy',
    },

    # ── Countries with STRATEGY but NO binding AI-specific law ──
    'Argentina': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 4,
        'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 8,
        'evidence': 'National AI Plan, AI ethics recommendations, pending draft regulation bills',
    },
    'Australia': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 5,
        'year_enacted': None, 'enforcement_level': 'medium', 'thematic_coverage': 11,
        'evidence': 'Voluntary AI Ethics Framework, AI Action Plan, mandatory guardrails consultation 2024, proposed mandatory framework, strong existing regulators',
    },
    'Bangladesh': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 2,
        'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 4,
        'evidence': 'National Strategy for AI 2019, early stage, ICT Division engagement',
    },
    'Brazil': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 5,
        'year_enacted': None, 'enforcement_level': 'medium', 'thematic_coverage': 10,
        'evidence': 'BAIA strategy, AI regulation bill before Congress, strong LGPD framework, AI committee, multiple active bills',
    },
    'Canada': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 5,
        'year_enacted': None, 'enforcement_level': 'medium', 'thematic_coverage': 11,
        'evidence': 'Pan-Canadian AI Strategy, AIDA (Bill C-27) still before Parliament, Voluntary Code of Conduct, strong Privacy Act framework',
    },
    'Chile': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 4,
        'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 8,
        'evidence': 'National AI Policy, law on neurorights (world first), draft AI regulation law Mar 2024, Transparency Council guidance',
    },
    'Colombia': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 3,
        'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 7,
        'evidence': 'National AI Policy (CONPES 3975), AI ethics framework, no binding AI law',
    },
    'Egypt': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 3,
        'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 6,
        'evidence': 'National AI Strategy, AI Ethics Charter, hub for digital development, NCAI strategic role',
    },
    'India': {
        'has_ai_law': 0, 'regulatory_approach': 'light_touch', 'regulatory_intensity': 4,
        'year_enacted': None, 'enforcement_level': 'medium', 'thematic_coverage': 10,
        'evidence': 'MeitY AI Governance Guidelines Nov 2025 (non-binding), AI advisory on content moderation, AI task force, NITI Aayog papers, "AI for all" principle',
    },
    'Indonesia': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 3,
        'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 7,
        'evidence': 'National Strategy on AI 2020, Circular on AI Ethics (non-binding), preparing AI regulations Jan 2025, AI Roadmap announced',
    },
    'Israel': {
        'has_ai_law': 0, 'regulatory_approach': 'light_touch', 'regulatory_intensity': 4,
        'year_enacted': None, 'enforcement_level': 'medium', 'thematic_coverage': 8,
        'evidence': 'National Program for AI Apr 2025, voluntary standardization favored over lateral framework, sector-based self-regulation, sandbox approach',
    },
    'Kenya': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 3,
        'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 5,
        'evidence': 'National AI Strategy 2025, Draft AI Code of Practice, DLT/AI Taskforce, pending Robotics/AI Bill',
    },
    'Mauritius': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 2,
        'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 5,
        'evidence': 'AI Strategy 2018, Emerging Technologies Council, Financial Services AI Rules in force (sectoral), plans for AI Office',
    },
    'New Zealand': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 4,
        'year_enacted': None, 'enforcement_level': 'medium', 'thematic_coverage': 9,
        'evidence': 'AI Strategy Investing with Confidence Jul 2025, Algorithm Charter (voluntary), light-touch risk-based approach, Privacy Commissioner AI guidance',
    },
    'Nigeria': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 3,
        'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 7,
        'evidence': 'National AI Strategy Sep 2025, Draft Code of Practice Jul 2025, pending e-Governance Bill with AI provisions, multiple House bills',
    },
    'Saudi Arabia': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 4,
        'year_enacted': None, 'enforcement_level': 'medium', 'thematic_coverage': 7,
        'evidence': 'National Strategy on Data and AI, SDAIA AI Ethics Principles 2023, draft AI law Apr 2025, strong institutional framework',
    },
    'Singapore': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 6,
        'year_enacted': None, 'enforcement_level': 'medium', 'thematic_coverage': 12,
        'evidence': 'National AI Strategy updated 2023, Model AI Governance Framework (voluntary), AI Verify toolkit, numerous sector frameworks, AI Safety Institute, GenAI Sandbox',
    },
    'Taiwan': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 5,
        'year_enacted': None, 'enforcement_level': 'medium', 'thematic_coverage': 9,
        'evidence': 'AI Basic Act (executive draft, not yet enacted), AI Taiwan Action Plan 2.0, risk-based approach, Ministry of Digital Affairs, AI CoE',
    },
    'Turkey': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 3,
        'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 5,
        'evidence': 'National AI Strategy 2021, AI bill before parliament summer 2024, DPA recommendations on AI and personal data',
    },
    'United Arab Emirates': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 5,
        'year_enacted': None, 'enforcement_level': 'medium', 'thematic_coverage': 9,
        'evidence': 'AI Ministry since 2017 (world first), National Strategy for AI, AI Ethics Principles, AI coding license, draft AI law Apr 2025, DIFC AI regulation in force (sectoral)',
    },
    'United Kingdom': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 6,
        'year_enacted': None, 'enforcement_level': 'high', 'thematic_coverage': 13,
        'evidence': 'Pro-innovation approach to AI, National AI Strategy, AI Safety Institute, sector regulators empowered, AI Opportunities Action Plan, no horizontal binding law',
    },
    'United States': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 6,
        'year_enacted': None, 'enforcement_level': 'medium', 'thematic_coverage': 13,
        'evidence': 'EO 14110 on safe AI Oct 2023, NIST AI RMF, AI Bill of Rights blueprint, FTC enforcement actions, no comprehensive federal AI law',
    },
    'Vietnam': {
        'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 4,
        'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 6,
        'evidence': 'National Strategy on AI Development 2021, Decree 13/2023/ND-CP on data protection, National Digital Transformation Program',
    },
    # Hong Kong (HKG) — not in 86-country sample, coded for completeness
    'Hong Kong': {
        'has_ai_law': 0, 'regulatory_approach': 'light_touch', 'regulatory_intensity': 3,
        'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 6,
        'evidence': 'Ethical AI Framework for Hong Kong Financial Services, guidelines approach, sectoral guidance',
    },
}

def build_iapp_x1():
    """Build X1 coded dataframe from IAPP with ISO3 mapping."""
    rows = []
    for jurisdiction, coding in IAPP_CODING.items():
        iso3 = IAPP_TO_ISO3.get(jurisdiction)
        if iso3 is None and jurisdiction != 'EU':
            print(f"  WARNING: No ISO3 for {jurisdiction}")
            continue
        
        row = {
            'iso3': iso3,
            'jurisdiction_iapp': jurisdiction,
            'has_ai_law': coding['has_ai_law'],
            'regulatory_approach': coding['regulatory_approach'],
            'regulatory_intensity': coding['regulatory_intensity'],
            'year_enacted': coding['year_enacted'],
            'enforcement_level': coding['enforcement_level'],
            'thematic_coverage': coding['thematic_coverage'],
            'evidence_summary': coding['evidence'],
            'source': SOURCE_NAME,
            'source_date': SOURCE_DATE,
        }
        
        if jurisdiction == 'EU':
            # Propagate EU AI Act to all EU member states in study
            for eu_iso3, eu_name in EU_MEMBERS_IN_STUDY.items():
                eu_row = row.copy()
                eu_row['iso3'] = eu_iso3
                eu_row['jurisdiction_iapp'] = f'EU ({eu_name})'
                eu_row['evidence_summary'] = f'EU AI Act (propagated to {eu_name} as EU member state). ' + coding['evidence']
                rows.append(eu_row)
        else:
            rows.append(row)
    
    return pd.DataFrame(rows)


def build_iapp_raw_table():
    """Return the raw IAPP extraction as a structured table with page provenance."""
    rows = []
    for jurisdiction, entry in iapp_raw.items():
        pages = entry.get('pages', [])
        rows.append({
            'jurisdiction_iapp': jurisdiction,
            'policy_text': entry.get('policy', ''),
            'authorities_text': entry.get('authorities', ''),
            'other_laws_text': entry.get('other_laws', ''),
            'context_text': entry.get('context', ''),
            'pages': '|'.join(str(page) for page in pages),
            'page_count': len(pages),
            'page_start': min(pages) if pages else None,
            'page_end': max(pages) if pages else None,
            'source': SOURCE_NAME,
            'source_date': SOURCE_DATE,
        })

    return pd.DataFrame(rows).sort_values('jurisdiction_iapp').reset_index(drop=True)


def build_additional_countries():
    """
    Research-based coding for countries NOT in IAPP tracker but in study sample.
    These use public information from UNESCO, OECD, Stanford AI Index and other sources.
    Only coded where sufficient public evidence exists.
    """
    additional = {
        # ── Countries with known AI regulation / policy based on public sources ──
        'ARM': {  # Armenia
            'has_ai_law': 0, 'regulatory_approach': 'light_touch', 'regulatory_intensity': 1,
            'year_enacted': None, 'enforcement_level': 'none', 'thematic_coverage': 2,
            'evidence': 'No AI-specific legislation or strategy. Digital Armenia Strategy touches AI peripherally. UNESCO AI ethics recommendation adopted.',
        },
        'BHR': {  # Bahrain
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 2,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 3,
            'evidence': 'National AI Strategy under Economic Vision 2030, AI Committee established, no binding AI law.',
        },
        'BLR': {  # Belarus
            'has_ai_law': 0, 'regulatory_approach': 'light_touch', 'regulatory_intensity': 1,
            'year_enacted': None, 'enforcement_level': 'none', 'thematic_coverage': 1,
            'evidence': 'Hi-Tech Park decree supports tech sector, no AI-specific legislation or strategy.',
        },
        'BLZ': {  # Belize
            'has_ai_law': 0, 'regulatory_approach': 'none', 'regulatory_intensity': 0,
            'year_enacted': None, 'enforcement_level': 'none', 'thematic_coverage': 0,
            'evidence': 'No AI-specific legislation, strategy or governance framework identified.',
        },
        'BRB': {  # Barbados
            'has_ai_law': 0, 'regulatory_approach': 'none', 'regulatory_intensity': 0,
            'year_enacted': None, 'enforcement_level': 'none', 'thematic_coverage': 0,
            'evidence': 'No AI-specific legislation, strategy or governance framework identified.',
        },
        'CHE': {  # Switzerland
            'has_ai_law': 0, 'regulatory_approach': 'light_touch', 'regulatory_intensity': 3,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 7,
            'evidence': 'No AI-specific binding law; relies on existing legal framework. Federal Council AI guidelines. OECD AI principles adherent. Strong data protection (nDSG). Geneva AI Lab.',
        },
        'CMR': {  # Cameroon
            'has_ai_law': 0, 'regulatory_approach': 'none', 'regulatory_intensity': 0,
            'year_enacted': None, 'enforcement_level': 'none', 'thematic_coverage': 0,
            'evidence': 'No AI-specific legislation or strategy identified. UNESCO AI ethics recommendation adopted.',
        },
        'CRI': {  # Costa Rica
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 2,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 4,
            'evidence': 'National Strategy for Digital Transformation includes AI, OECD AI principles adherent, no binding AI law.',
        },
        'ECU': {  # Ecuador
            'has_ai_law': 0, 'regulatory_approach': 'light_touch', 'regulatory_intensity': 1,
            'year_enacted': None, 'enforcement_level': 'none', 'thematic_coverage': 2,
            'evidence': 'White paper on AI governance 2022, UNESCO AI ethics adopted, no binding AI law or strategy.',
        },
        'GHA': {  # Ghana
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 2,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 3,
            'evidence': 'National AI Strategy launched, Data Protection Act 2012, UNESCO AI ethics adopted, no binding AI law.',
        },
        'ISL': {  # Iceland
            'has_ai_law': 0, 'regulatory_approach': 'light_touch', 'regulatory_intensity': 2,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 4,
            'evidence': 'EEA member (follows some EU regulation), OECD AI principles adherent, no AI-specific binding law.',
        },
        'JOR': {  # Jordan
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 2,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 3,
            'evidence': 'National AI Strategy, MODEE engagement, UNESCO AI ethics adopted, no binding AI law.',
        },
        'KAZ': {  # Kazakhstan
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 2,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 3,
            'evidence': 'Digital Kazakhstan program, AI development roadmap, UNESCO AI ethics adopted, no binding AI law.',
        },
        'LBN': {  # Lebanon
            'has_ai_law': 0, 'regulatory_approach': 'none', 'regulatory_intensity': 0,
            'year_enacted': None, 'enforcement_level': 'none', 'thematic_coverage': 1,
            'evidence': 'No AI-specific legislation or comprehensive strategy identified. Data protection law under discussion.',
        },
        'LKA': {  # Sri Lanka
            'has_ai_law': 0, 'regulatory_approach': 'light_touch', 'regulatory_intensity': 1,
            'year_enacted': None, 'enforcement_level': 'none', 'thematic_coverage': 2,
            'evidence': 'National Policy on AI discussed, ICTA engagement, no binding AI law or formal strategy.',
        },
        'MAR': {  # Morocco
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 2,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 4,
            'evidence': 'AI Morocco Initiative, Digital Strategy 2030, UNESCO AI ethics adopted, no binding AI law.',
        },
        'MEX': {  # Mexico
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 3,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 6,
            'evidence': 'AI Strategy MX, OECD AI principles adherent, draft AI regulation proposals, no binding AI law.',
        },
        'MNG': {  # Mongolia
            'has_ai_law': 0, 'regulatory_approach': 'light_touch', 'regulatory_intensity': 1,
            'year_enacted': None, 'enforcement_level': 'none', 'thematic_coverage': 1,
            'evidence': 'Vision 2050 mentions digitalization, no AI-specific legislation or strategy.',
        },
        'MYS': {  # Malaysia
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 3,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 6,
            'evidence': 'National AI Roadmap, AI Governance and Ethics Framework, MDEC digital economy, no binding AI law.',
        },
        'NOR': {  # Norway
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 4,
            'year_enacted': None, 'enforcement_level': 'medium', 'thematic_coverage': 8,
            'evidence': 'National Strategy for AI 2020, EEA member (EU AI Act applicability expected), OECD AI principles adherent, strong DPA.',
        },
        'PAK': {  # Pakistan
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 2,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 3,
            'evidence': 'National AI Policy 2023, Presidential Initiative for AI and Computing, UNESCO AI ethics adopted, no binding AI law.',
        },
        'PAN': {  # Panama
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 2,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 2,
            'evidence': 'National AI Strategy 2024, AIG Panama, no binding AI law.',
        },
        'PHL': {  # Philippines
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 2,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 4,
            'evidence': 'National AI Strategy Roadmap, DICT engagement, pending AI regulation bills filed in Congress, no binding AI law.',
        },
        'RUS': {  # Russia
            'has_ai_law': 1, 'regulatory_approach': 'comprehensive', 'regulatory_intensity': 7,
            'year_enacted': 2020, 'enforcement_level': 'high', 'thematic_coverage': 8,
            'evidence': 'Federal Law on experimental AI regulation (Moscow sandbox) 2020, National AI Strategy 2019, AI Development Concept to 2030, ethical AI code. Decree No. 490 signed by President.',
        },
        'SRB': {  # Serbia
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 2,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 3,
            'evidence': 'AI Strategy 2020-2025, Office for IT and eGovernment, no binding AI law.',
        },
        'SYC': {  # Seychelles
            'has_ai_law': 0, 'regulatory_approach': 'none', 'regulatory_intensity': 0,
            'year_enacted': None, 'enforcement_level': 'none', 'thematic_coverage': 0,
            'evidence': 'No AI-specific legislation or strategy identified.',
        },
        'THA': {  # Thailand
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 3,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 6,
            'evidence': 'National AI Strategy 2022-2027, AI Governance Guidelines, AIAT standard, OECD AI principles adherent, no binding AI law.',
        },
        'TUN': {  # Tunisia
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 2,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 3,
            'evidence': 'National AI Strategy, UNESCO AI ethics adopted, Digital Tunisia 2025, no binding AI law.',
        },
        'UGA': {  # Uganda
            'has_ai_law': 0, 'regulatory_approach': 'light_touch', 'regulatory_intensity': 1,
            'year_enacted': None, 'enforcement_level': 'none', 'thematic_coverage': 1,
            'evidence': 'National 4IR Strategy mentions AI, no AI-specific legislation or strategy.',
        },
        'UKR': {  # Ukraine
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 2,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 3,
            'evidence': 'AI Development Concept 2020, Ministry of Digital Transformation engagement, no binding AI law.',
        },
        'URY': {  # Uruguay
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 3,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 5,
            'evidence': 'National AI Strategy 2019, AGESIC AI guide, OECD AI principles adherent, no binding AI law.',
        },
        'ZAF': {  # South Africa
            'has_ai_law': 0, 'regulatory_approach': 'strategy_led', 'regulatory_intensity': 3,
            'year_enacted': None, 'enforcement_level': 'low', 'thematic_coverage': 5,
            'evidence': 'Presidential Commission on 4IR, AI Institute, draft AI policy framework, UNESCO AI ethics adopted, no binding AI law.',
        },
    }
    
    rows = []
    for iso3, coding in additional.items():
        rows.append({
            'iso3': iso3,
            'jurisdiction_iapp': f'Additional research ({iso3})',
            'has_ai_law': coding['has_ai_law'],
            'regulatory_approach': coding['regulatory_approach'],
            'regulatory_intensity': coding['regulatory_intensity'],
            'year_enacted': coding['year_enacted'],
            'enforcement_level': coding['enforcement_level'],
            'thematic_coverage': coding['thematic_coverage'],
            'evidence_summary': coding['evidence'],
            'source': 'IAPP_supplementary_research',
            'source_date': SOURCE_DATE,
        })
    return pd.DataFrame(rows)


if __name__ == '__main__':
    print("=" * 70)
    print("IAPP X1 CODING PIPELINE")
    print("=" * 70)

    df_raw = build_iapp_raw_table()
    print(f"\nStructured raw jurisdictions: {df_raw.shape[0]}")
    
    # Build IAPP coded data
    df_iapp = build_iapp_x1()
    print(f"\nIAPP direct jurisdictions: {df_iapp.shape[0]} rows")
    print(f"  In study sample: {df_iapp[df_iapp['iso3'].isin(study_iso3)].shape[0]}")
    
    # Build additional countries
    df_additional = build_additional_countries()
    print(f"\nAdditional research-coded countries: {df_additional.shape[0]}")
    
    # Combine
    df_all = pd.concat([df_iapp, df_additional], ignore_index=True)
    
    # Filter to study sample only
    df_study = df_all[df_all['iso3'].isin(study_iso3)].copy()
    df_study = df_study.sort_values('iso3').reset_index(drop=True)
    
    print(f"\nTotal study sample coverage: {df_study['iso3'].nunique()}/{len(study_iso3)}")
    
    # Which study countries are still missing?
    covered = set(df_study['iso3'])
    still_missing = sorted(set(study_iso3) - covered)
    print(f"Still missing: {len(still_missing)} → {still_missing}")
    
    # Distribution
    print(f"\n{'='*70}")
    print("X1 DISTRIBUTIONS (study sample)")
    print(f"{'='*70}")
    print(f"\nhas_ai_law:")
    print(df_study['has_ai_law'].value_counts().to_string())
    print(f"\nregulatory_approach:")
    print(df_study['regulatory_approach'].value_counts().to_string())
    print(f"\nenforcement_level:")
    print(df_study['enforcement_level'].value_counts().to_string())
    print(f"\nregulatory_intensity: mean={df_study['regulatory_intensity'].mean():.1f}")
    print(f"thematic_coverage: mean={df_study['thematic_coverage'].mean():.1f}")
    
    # Save outputs
    df_raw.to_csv(IAPP_DIR / "iapp_tracker_structured_raw.csv", index=False)
    df_all.to_csv(IAPP_DIR / "iapp_all_coded.csv", index=False)
    df_study.to_csv(IAPP_DIR / "iapp_x1_core.csv", index=False)
    
    # Also save the flat regulatory.csv as requested by methodology
    df_reg = df_study[['iso3', 'has_ai_law', 'regulatory_approach', 'regulatory_intensity',
                        'year_enacted', 'enforcement_level', 'thematic_coverage', 'evidence_summary', 'source']].copy()
    df_reg.to_csv(BASE / "data/raw/iapp_regulatory.csv", index=False)
    
    print(f"\nSaved:")
    print(f"  data/raw/IAPP/iapp_tracker_structured_raw.csv ({df_raw.shape})")
    print(f"  data/raw/IAPP/iapp_all_coded.csv ({df_all.shape})")
    print(f"  data/raw/IAPP/iapp_x1_core.csv ({df_study.shape})")
    print(f"  data/raw/iapp_regulatory.csv ({df_reg.shape})")
    
    # Show all coded countries
    print(f"\n{'='*70}")
    print("ALL CODED STUDY COUNTRIES")
    print(f"{'='*70}")
    for _, row in df_study.iterrows():
        yr = int(row['year_enacted']) if pd.notna(row['year_enacted']) else 'N/A'
        print(f"  {row['iso3']} | law={row['has_ai_law']} | {row['regulatory_approach']:20s} | int={row['regulatory_intensity']:2} | yr={yr:>4} | enf={row['enforcement_level']:6s} | th={row['thematic_coverage']:2} | {row['source'][:20]}")
