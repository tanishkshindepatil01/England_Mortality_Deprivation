# Data sources and provenance

This document records source identities described by the supplied files. It does not assert an independently verified download date, source URL or license.

| Source named in supplied evidence | Role | What this package contains |
|---|---|---|
| Fingertips | Mortality rates, counts, denominators and intervals | Processed national/local CSVs and data-derived indicator summaries |
| Nomis | Population estimates for denominator validation/context | Joined population columns and source-reported validation metrics |
| England IMD 2019 | Deprivation and child income-deprivation measures | Joined area-level fields and source-reported coverage |
| Tableau exports | Presentation of processed findings | Four dashboard PNGs and fourteen worksheet PNGs |

## File provenance

`source_file_manifest.json` maps all 24 supplied files plus the final mortality PPT to their packaged paths, with hashes of their original bytes. Filenames were simplified for GitHub. The underlying contents were not changed.

The finance presentation belongs to the design-reference material. Its finance data and conclusions are not evidence for this mortality project.

The new script, notebook, tests, reports and Markdown documents were created when preparing this repository package. They do not claim to be the original authoring artifacts for the supplied CSVs or Tableau views.

## Snapshot details

The mortality extracts cover 2001–03 to 2022–24 nationally and 2022–24 locally. These are data periods, not retrieval dates. A source retrieval timestamp was not supplied.

The quality summary reports 29,336 Fingertips raw rows, 32,844 IMD LSOAs and 317 IMD 2019 LADs. Those raw input datasets are not included, so raw-record validation cannot be rerun from this package alone.
