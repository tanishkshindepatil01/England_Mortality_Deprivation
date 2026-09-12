# Reproducibility record

The packaged snapshot was checked with Python 3.12.14.

- The CLI analysis completed without third-party dependencies.
- All four unit/integration tests passed.
- All six notebook code cells executed without errors.
- All 25 provenance entries match their original file hashes: 24 supplied files and the final mortality PowerPoint.
- All Markdown image and document links resolve within the repository.
- The package includes four dashboard images and fourteen worksheet images.

Run `python scripts/analyze.py` and `python -m unittest discover -s tests -v` from the project root to reproduce the analysis and tests. Generated summaries reflect the packaged data snapshot. They do not verify unavailable upstream raw data or recreate the Tableau workbook.

`MANIFEST.sha256` records every packaged file except the checksum file itself. An intentional edit changes the associated hash.
