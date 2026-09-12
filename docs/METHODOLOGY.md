# Methodology

## Evidence base

The supplied CSVs are processed analytical extracts. This repository preserves their values and derives descriptive summaries. It does not reconstruct missing upstream extraction or transformation code.

## National trends

The analytical key is `IndicatorID + TimePeriod`. Sort by `TimePeriodSortable`; labels are three-year reporting periods. Each indicator has 22 records. Retain `RateScale` and `RateUnit` when interpreting the measure.

- Absolute change = latest rate − earliest rate.
- Relative change (%) = 100 × (latest rate / earliest rate − 1).
- Change from low (%) = 100 × (latest rate / lowest observed rate − 1).

Calculations use full-precision CSV values. Comparisons describe change; they do not supply a significance test. The latest `RecentTrend` field says “Cannot be calculated”.

## Latest local comparison

The analytical key is `IndicatorID + AreaCode`. The latest extract includes 988 records across five indicators. Authority counts vary with the supplied indicator coverage.

`DifferenceFromEngland` is an absolute rate difference in the indicator's rate units. The official comparison category comes from `ComparedToEngland` and is retained rather than inferred from ranking or simple confidence-interval overlap. No new significance classification is calculated.

The top-15 report sorts available infant point estimates in descending order. Rank does not imply a precise ordering of underlying risk. Counts and intervals remain relevant.

## Population and geography

According to the source quality summary, Nomis matches 296/296 current authority codes. Its population estimates are used for validation/context. The Fingertips denominator remains authoritative.

The source-reported median absolute percentage difference between the child mortality denominator and the Nomis 2022–24 population sum is 0.95%. This statistic comes from the supplied quality summary; the new script does not recreate upstream population preparation.

IMD 2019 matches 289 of 296 authority codes. The following current areas have unmatched codes:

| Code | Authority |
|---|---|
| E06000060 | Buckinghamshire UA |
| E06000063 | Cumberland |
| E06000061 | North Northamptonshire |
| E06000065 | North Yorkshire UA |
| E06000066 | Somerset UA |
| E06000062 | West Northamptonshire |
| E06000064 | Westmorland and Furness |

These mismatches reflect the different geography vintages identified in the source summary. No speculative boundary crosswalk is applied.

## Deprivation measures

The local extract includes child-population-weighted IMD/IDACI scores and percentages of children exposed to the most deprived 20% of LSOAs. Weighting fields refer to children aged 0–15 in 2015. The original weighting implementation was not supplied.

The analysis uses `DerivedLADeprivationQuintile` exactly as provided. It does not run `qcut`, infer cut points or relabel missing groups. The displayed Q1–Q5 infant means reproduce worksheet S10:

| Quintile | Available rates | Mean per 1,000 |
|---|---:|---:|
| Q1 Least deprived | 47 | 3.374 |
| Q2 | 48 | 3.574 |
| Q3 | 48 | 3.777 |
| Q4 | 47 | 4.318 |
| Q5 Most deprived | 51 | 5.096 |

Each available authority contributes one rate to its group mean. There is no weighting by population, births or denominator. The 241 authorities in this table are a restricted subset. Of all 296 infant authority rows, 55 have no assigned quintile, including the seven with unmatched IMD geography.

The Q5–Q1 gap is approximately 1.72 per 1,000 and the ratio is 1.51. These are differences between authority means, not causal estimates or national pooled rates.

## Validation layers

The supplied `data_quality_summary.csv` records checks on the original workflow. The repository script separately checks:

1. Unique national and local keys, including the deprivation extract.
2. Identical local/deprivation record keys and unchanged mortality values.
3. Valid bounds for complete reported confidence intervals.
4. Agreement between the latest England trend rate and indicator summary.

It preserves missing numeric fields as missing and rejects malformed numeric values. It writes deterministic summaries, without remote access or credentials.

## Limits

Overlapping periods, uncertain small-area rates, incomplete coverage, historical deprivation measures and ecological confounding limit interpretation. No causal model, forecast, individual risk model or evaluation of an intervention is included. The priority matrix uses chart averages, rather than a validated threshold or the England benchmark.
