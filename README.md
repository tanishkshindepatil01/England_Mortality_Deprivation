# England Mortality & Deprivation Analytics

**National mortality trends, local authority comparisons and deprivation inequalities in England.**

A descriptive analytics portfolio project covering five mortality indicators, 22 rolling three-year periods, fourteen Tableau worksheets and four dashboards. The latest reporting period is **2022–24**.

**Author:** Tanishk Nanasaheb Shinde  
**Tools:** Python, CSV, Tableau dashboard exports and PowerPoint

![Deprivation and mortality dashboard](assets/dashboards/deprivation_mortality_inequality.png)

## Project questions

- How have mortality rates changed between 2001–03 and 2022–24?
- Which local authorities have higher or lower mortality than England?
- How does infant mortality vary with area deprivation?
- How do confidence intervals, suppression and geography affect interpretation?

## Key findings

| Finding | Result | Interpretation |
|---|---|---|
| England infant mortality | 5.36 to 4.17 per 1,000, a 22.2% fall | Full-period improvement from 2001–03 to 2022–24 |
| Recent infant mortality | 7.5% above the 2014–16 low | The endpoint decline masks a recent increase |
| Infant comparison with England | 238 Similar, 28 Better, 25 Worse | 291 available rates, with five additional authorities Not compared |
| Assigned deprivation quintiles | Q1 mean 3.374, Q5 mean 5.096 per 1,000 | Q5/Q1 ratio 1.51, based on unweighted authority means |
| Quintile coverage | 241 authorities with available rates and assigned groups | 55 of 296 authorities have no assigned quintile |
| Missing mortality rates | 45 of 988 local records | Retained as missing, never replaced with zero |

All calculations use the supplied CSV values before rounding. See [reproduced findings](reports/findings.md), [methodology](docs/METHODOLOGY.md) and [known issues](docs/KNOWN_ISSUES.md).

## Start here

- [Final project presentation: 32 slides](presentations/England_Mortality_Deprivation_Project_Final.pptx)
- [Notebook walkthrough](notebooks/project_walkthrough.ipynb)
- [Dashboard and worksheet gallery](docs/DASHBOARD_GUIDE.md)
- [Data dictionary](docs/DATA_DICTIONARY.md)
- [GitHub upload instructions](docs/GITHUB_SETUP.md)

## Repository structure

| Folder/file | Contents |
|---|---|
| `data/processed/` | Five supplied analytical CSVs, with simplified filenames |
| `assets/dashboards/` | Four original dashboard PNGs |
| `assets/worksheets/` | Original worksheets S1–S14 |
| `presentations/` | Final project PowerPoint |
| `notebooks/` | New walkthrough of the reproducible CSV analysis |
| `scripts/analyze.py` | Dependency-free analysis and validation script |
| `tests/` | Tests for missing data, validation and key snapshot results |
| `reports/` | Generated summaries in CSV, JSON and Markdown |
| `docs/` | Methodology, field dictionary, provenance, limitations and upload guide |
| `references/` | Supplied finance PowerPoint, retained only as the design reference |
| `requirements.txt` | Explains the dependency-free core and optional notebook environment |
| `MANIFEST.sha256` | Checksums for the packaged project files |

## Reproduce the analysis

The command-line analysis needs **Python 3.10 or later** and uses only its standard library. It does not download data or need credentials.

After extracting the ZIP, open a terminal in the `england-mortality-deprivation-analytics` folder:

```bash
python scripts/analyze.py
python -m unittest discover -s tests -v
```

Use `python3` if that is how Python is installed on your computer. A successful analysis prints `"status": "passed"` and writes the reports listed below. The tests are tied to this supplied data snapshot, so review the expected figures when intentionally updating data.

To write reports elsewhere:

```bash
python scripts/analyze.py --output-dir reports/recheck
```

### Notebook

Open [project_walkthrough.ipynb](notebooks/project_walkthrough.ipynb) in an existing Jupyter or VS Code notebook environment. Select a Python 3 kernel and run all cells. The analysis itself requires no additional packages. The notebook includes executed results for this snapshot.

### Generated outputs

| File | Purpose |
|---|---|
| `reports/national_summary.csv` | Start, latest and lowest-period rates, with relative changes |
| `reports/local_coverage.csv` | Available/missing records and England comparison counts |
| `reports/infant_quintile_summary.csv` | Assigned and available counts with unweighted infant-rate means |
| `reports/infant_top15.csv` | Highest infant point estimates, intervals and comparison categories |
| `reports/analysis_summary.json` | Structured results and validation outcomes |
| `reports/findings.md` | Concise narrative of the reproduced findings |

## Data scope

| Extract | Rows | Grain |
|---|---:|---|
| `mortality_trends.csv` | 110 | Five England indicators × 22 periods |
| `local_authority_comparison.csv` | 988 | Indicator × latest local authority |
| `deprivation_inequality.csv` | 988 | Same local records with deprivation fields |
| `indicator_definitions.csv` | 5 | One summary per indicator |
| `data_quality_summary.csv` | 15 | One source-reported validation metric |

The two 988-row extracts describe the same mortality records. They should not be concatenated and counted as independent observations.

### Latest England indicators

| Indicator | Age | Rate scale | 2022–24 |
|---|---|---|---:|
| Child mortality | 1–17 years | per 100,000 | 11.59 |
| Infant mortality | Under 1 year | per 1,000 | 4.17 |
| Neonatal mortality | Under 28 days | per 1,000 | 3.07 |
| Post-neonatal mortality | 28 days to under 1 year | per 1,000 | 1.10 |
| Stillbirth | Source age field: 0 years | per 1,000 | 3.90 |

The supplied definitions are data-derived summaries. Formal Fingertips metadata was not supplied. Always retain the original rate scale and denominator.

## Dashboards

| Dashboard | Purpose | Preview |
|---|---|---|
| National Mortality Trends | Trends, latest KPI, endpoint change and uncertainty | [Open PNG](assets/dashboards/national_mortality_trends.png) |
| Local Authority Comparison | Rankings, gaps from England and confidence intervals | [Open PNG](assets/dashboards/local_authority_comparison.png) |
| Deprivation & Mortality Inequality | Scatterplots, quintile means and deprivation exposure | [Open PNG](assets/dashboards/deprivation_mortality_inequality.png) |
| Data Quality & Methodology | Coverage, quality flags and indicator summaries | [Open PNG](assets/dashboards/data_quality_methodology.png) |

The PNGs preserve the supplied dashboard states. No live Tableau URL or `.twb`/`.twbx` workbook was supplied.

## Methodology and limitations

- Adjacent reporting periods share two years. They are not independent annual observations.
- Local coverage varies by indicator: 296 authorities for infant mortality and stillbirth, 132 for the other indicators.
- Source-reported IMD matches cover 289 of 296 current authority codes. Seven boundary-related mismatches remain null.
- IMD 2019 and child population weights from 2015 precede the mortality outcomes. Age groups also differ.
- Quintile labels are supplied derived labels. Their original construction code is unavailable. The new analysis groups these labels without inventing the assignment method.
- Quintile means weight each authority equally. They are not pooled England or birth-weighted rates.
- Missing, suppressed and unassigned values remain unknown. Area-level association does not establish individual risk or causation.
- The national dashboard's trend panel shows **neonatal** mortality, whereas its other panels show **infant** mortality.
- The S2/dashboard KPI image shows a 95% interval of **4.08–4.27**. The supplied CSV gives **4.07–4.26** after rounding. The presentation flags this discrepancy and numerical summaries use the CSV.

## Provenance and reproducibility boundary

The package contains every supplied file, with the finance deck clearly separated as a design reference, plus the final mortality presentation. Original CSV and PNG contents are unchanged. [source_file_manifest.json](docs/source_file_manifest.json) maps original names to repository paths and SHA-256 hashes.

The Python script, notebook, tests and documentation were added for this repository package. They reproduce descriptive analysis from the supplied **processed** extracts. They are not the original extraction/cleaning pipeline and do not rebuild the Tableau workbook or the PowerPoint.

The source-reported 29,336 Fingertips raw records, Nomis source tables, 32,844 IMD LSOAs, original preparation notebook and formal indicator metadata were not supplied. Their full upstream validation cannot be rerun here.

## Attribution and reuse

The supplied extracts identify Fingertips mortality data, Nomis population estimates and England IMD 2019 as underlying sources. See [DATA_SOURCES.md](docs/DATA_SOURCES.md) and [NOTICE.md](NOTICE.md). This package makes no new claim about licensing of those materials and does not apply a blanket open-source license to them.

## Publish on GitHub

Suggested repository name: **england-mortality-deprivation-analytics**.

Upload the extracted project contents so that `README.md` appears at the repository root. The [upload guide](docs/GITHUB_SETUP.md) provides a step-by-step path. This ZIP is ready for upload; creating or publishing a remote repository is a separate action.
