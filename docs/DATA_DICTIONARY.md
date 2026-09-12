# Data dictionary

Field descriptions follow the supplied schemas and labels. Formal indicator definitions and upstream transformation code were not supplied.

## Missing values

Empty CSV cells and literal `nan` values represent missing/unassigned fields. The analysis never converts them to zero. Suppression can affect the rate while leaving a count or denominator present.

## data_quality_summary.csv

15 rows, excluding the header.

| Field | Meaning |
|---|---|
| `Metric` | Name of a source-reported validation metric. |
| `Value` | Mortality rate in RateUnit for mortality extracts. For quality_summary, the display text of a validation metric. |
| `NumericValue` | Optional numerical representation of the validation metric. |
| `Status` | Source-reported PASS or WARN status. |
| `Notes` | Source explanation of a quality result. |

## deprivation_inequality.csv

988 rows, excluding the header.

| Field | Meaning |
|---|---|
| `IndicatorID` | Official indicator identifier. Treat as an identifier, not a measure. |
| `IndicatorName` | Supplied mortality indicator label. |
| `AreaCode` | Official local authority code, used as the geography join key. |
| `AreaName` | Supplied local authority display name. |
| `AreaType` | Supplied authority type label, UA or District in the local extract. |
| `Age` | Indicator age group as supplied. Different indicators cover different ages. |
| `Sex` | Supplied sex grouping; Persons in these extracts. |
| `TimePeriod` | Reported three-year period label. |
| `TimePeriodSortable` | Numeric ordering key for reporting periods; not a rate. |
| `Value` | Mortality rate in RateUnit for mortality extracts. For quality_summary, the display text of a validation metric. |
| `LowerCI95` | Reported lower 95% confidence bound for Value. |
| `UpperCI95` | Reported upper 95% confidence bound for Value. |
| `Count` | Reported event count for the complete reporting period. May remain present when the rate is suppressed. |
| `Denominator` | Authoritative supplied indicator denominator. Definition and scale vary by indicator. |
| `ValueNote` | Source explanation of suppression, unavailability or another value condition. |
| `RecentTrend` | Supplied trend assessment. Do not substitute an inferred significance result. |
| `ComparedToEngland` | Supplied comparison category: Similar, Better, Worse or Not compared. |
| `RateScale` | Rate multiplier, 100000 for child mortality and 1000 for the other indicators. |
| `RateUnit` | Human-readable rate scale, per 100,000 or per 1,000. |
| `EnglandValue` | England benchmark rate for the same indicator and reporting period. |
| `EnglandLowerCI95` | England lower 95% confidence bound. |
| `EnglandUpperCI95` | England upper 95% confidence bound. |
| `DifferenceFromEngland` | Local Value minus EnglandValue in the same rate units. |
| `DataAvailability` | Value available or Suppressed / unavailable. |
| `Population1to17_2022` | Joined Nomis population estimate for ages 1–17 in 2022. |
| `Population1to17_2023` | Joined Nomis population estimate for ages 1–17 in 2023. |
| `Population1to17_2024` | Joined Nomis population estimate for ages 1–17 in 2024. |
| `Population1to17_ThreeYearSum` | Sum of the three supplied annual population estimates, for validation/context. |
| `Population1to17_ThreeYearMean` | Mean of the three supplied annual population estimates. |
| `NomisDenominatorValidationPctDiff` | Supplied child-denominator percentage difference measure versus Nomis. Not populated for the other indicators. |
| `IMD2019AreaName` | Name of matched IMD 2019 local authority. |
| `LSOACount` | Supplied number of LSOAs for the matched authority. |
| `ChildPopulation0to15_2015` | Historical child population weighting base, ages 0–15 in 2015. |
| `ChildPopWeightedIMDScore` | Supplied child-population-weighted IMD score. Original weighting code is not included. |
| `ChildPopWeightedIDACIScore` | Supplied child-population-weighted IDACI score. Preserve its supplied numeric scale. |
| `PctChildrenInMostDeprived20pctIMDLSOAs` | Percentage of children in the most deprived 20% of IMD LSOAs. Null does not establish zero exposure. |
| `PctChildrenInMostDeprived20pctIDACILSOAs` | Percentage of children in the most deprived 20% of IDACI LSOAs. Null does not establish zero exposure. |
| `DerivedLADeprivationQuintile` | Supplied derived Q1–Q5 label. Original cut points/assignment code are unavailable. nan denotes an unassigned label. |
| `IMDJoinStatus` | Supplied indication of IMD match status. |

## indicator_definitions.csv

5 rows, excluding the header.

| Field | Meaning |
|---|---|
| `IndicatorID` | Official indicator identifier. Treat as an identifier, not a measure. |
| `IndicatorName` | Supplied mortality indicator label. |
| `Age` | Indicator age group as supplied. Different indicators cover different ages. |
| `RateScale` | Rate multiplier, 100000 for child mortality and 1000 for the other indicators. |
| `RateUnit` | Human-readable rate scale, per 100,000 or per 1,000. |
| `EarliestPeriod` | First reporting period in the indicator summary. |
| `LatestPeriod` | Most recent reporting period in the indicator summary. |
| `PeriodCount` | Number of reported national periods for the indicator. |
| `LatestEnglandValue` | Latest reported England rate. |
| `LatestEnglandCount` | Latest England event count. |
| `LatestEnglandDenominator` | Latest authoritative England denominator. |
| `LatestEnglandLowerCI95` | Latest England lower 95% confidence bound. |
| `LatestEnglandUpperCI95` | Latest England upper 95% confidence bound. |
| `MetadataNote` | Notes on derivation of the indicator summary and absent formal definitions. |

## local_authority_comparison.csv

988 rows, excluding the header.

| Field | Meaning |
|---|---|
| `IndicatorID` | Official indicator identifier. Treat as an identifier, not a measure. |
| `IndicatorName` | Supplied mortality indicator label. |
| `AreaCode` | Official local authority code, used as the geography join key. |
| `AreaName` | Supplied local authority display name. |
| `AreaType` | Supplied authority type label, UA or District in the local extract. |
| `Age` | Indicator age group as supplied. Different indicators cover different ages. |
| `Sex` | Supplied sex grouping; Persons in these extracts. |
| `TimePeriod` | Reported three-year period label. |
| `TimePeriodSortable` | Numeric ordering key for reporting periods; not a rate. |
| `Value` | Mortality rate in RateUnit for mortality extracts. For quality_summary, the display text of a validation metric. |
| `LowerCI95` | Reported lower 95% confidence bound for Value. |
| `UpperCI95` | Reported upper 95% confidence bound for Value. |
| `Count` | Reported event count for the complete reporting period. May remain present when the rate is suppressed. |
| `Denominator` | Authoritative supplied indicator denominator. Definition and scale vary by indicator. |
| `ValueNote` | Source explanation of suppression, unavailability or another value condition. |
| `RecentTrend` | Supplied trend assessment. Do not substitute an inferred significance result. |
| `ComparedToEngland` | Supplied comparison category: Similar, Better, Worse or Not compared. |
| `RateScale` | Rate multiplier, 100000 for child mortality and 1000 for the other indicators. |
| `RateUnit` | Human-readable rate scale, per 100,000 or per 1,000. |
| `EnglandValue` | England benchmark rate for the same indicator and reporting period. |
| `EnglandLowerCI95` | England lower 95% confidence bound. |
| `EnglandUpperCI95` | England upper 95% confidence bound. |
| `DifferenceFromEngland` | Local Value minus EnglandValue in the same rate units. |
| `DataAvailability` | Value available or Suppressed / unavailable. |
| `Population1to17_2022` | Joined Nomis population estimate for ages 1–17 in 2022. |
| `Population1to17_2023` | Joined Nomis population estimate for ages 1–17 in 2023. |
| `Population1to17_2024` | Joined Nomis population estimate for ages 1–17 in 2024. |
| `Population1to17_ThreeYearSum` | Sum of the three supplied annual population estimates, for validation/context. |
| `Population1to17_ThreeYearMean` | Mean of the three supplied annual population estimates. |
| `NomisDenominatorValidationPctDiff` | Supplied child-denominator percentage difference measure versus Nomis. Not populated for the other indicators. |

## mortality_trends.csv

110 rows, excluding the header.

| Field | Meaning |
|---|---|
| `IndicatorID` | Official indicator identifier. Treat as an identifier, not a measure. |
| `IndicatorName` | Supplied mortality indicator label. |
| `Age` | Indicator age group as supplied. Different indicators cover different ages. |
| `Sex` | Supplied sex grouping; Persons in these extracts. |
| `TimePeriod` | Reported three-year period label. |
| `TimePeriodSortable` | Numeric ordering key for reporting periods; not a rate. |
| `PeriodStart` | First year of the reported period. |
| `PeriodEnd` | Last year of the reported period. |
| `PeriodMidYear` | Midpoint year used to position rolling periods. |
| `Value` | Mortality rate in RateUnit for mortality extracts. For quality_summary, the display text of a validation metric. |
| `LowerCI95` | Reported lower 95% confidence bound for Value. |
| `UpperCI95` | Reported upper 95% confidence bound for Value. |
| `Count` | Reported event count for the complete reporting period. May remain present when the rate is suppressed. |
| `Denominator` | Authoritative supplied indicator denominator. Definition and scale vary by indicator. |
| `ValueNote` | Source explanation of suppression, unavailability or another value condition. |
| `RecentTrend` | Supplied trend assessment. Do not substitute an inferred significance result. |
| `RateScale` | Rate multiplier, 100000 for child mortality and 1000 for the other indicators. |
| `RateUnit` | Human-readable rate scale, per 100,000 or per 1,000. |
| `IsLatestPeriod` | Boolean flag for the latest England reporting period. |

