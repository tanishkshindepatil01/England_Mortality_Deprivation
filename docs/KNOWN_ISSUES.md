# Known issues and scope limits

| Issue | Evidence | Treatment |
|---|---|---|
| KPI confidence-interval mismatch | S2 and the national dashboard show 4.08–4.27; infant CSV bounds round to 4.07–4.26 | Preserve the original images, use CSV values for calculations and flag the mismatch on presentation slide 11 |
| Mixed national dashboard indicators | S1 trend shows neonatal mortality; S2–S4 show infant mortality | Label the difference on slide 9 and in dashboard documentation |
| Unavailable local rates | 45 of 988 local records | Preserve missingness; never impute zero |
| IMD geography mismatch | Seven current authority codes have no IMD 2019 match | Retain nulls and document the affected codes |
| Missing derived quintiles | 55 of 296 infant authority records | Restrict Q1–Q5 summaries to assigned labels and report coverage |
| Unavailable original quintile code | Only derived labels are supplied | Do not claim a particular grouping algorithm |
| Historical deprivation weights | 2015 child population and IMD 2019 versus 2022–24 mortality | Avoid interpreting exposure as contemporaneous infant exposure |
| Static Tableau exports | Four dashboards and fourteen worksheets are PNGs | No working filters, actions or live workbook are included |
| Long ranking image | S5 contains many rows in a tall image | Preserve the image, provide a readable top-15 CSV and selected values in the PPT |
| Formal definitions absent | Indicator summaries explicitly say formal definitions were not supplied | Retain original scale and metadata note |
| Raw source data absent | Source raw rows, full Nomis tables and full IMD inputs were not uploaded | Reproducibility starts from the processed extracts |

The numerical CI discrepancy has no established cause in the available evidence. It should be checked against the originating workbook/source before updating the original dashboard image.
