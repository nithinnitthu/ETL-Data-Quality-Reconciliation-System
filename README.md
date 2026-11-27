# Dashboard Testing Project — Retail Sales Dashboard

A beginner-friendly portfolio project for practicing dashboard validation with Excel, Power BI, SQL and Python.

## Files
- `data/orders_clean.csv` — baseline dataset (40 rows).
- `data/orders_with_issues.csv` — test dataset containing deliberate data-quality issues.
- `excel/dashboard_test_pack.xlsx` — dashboard test cases, KPI reconciliation sheet, defect log and data dictionary.
- `power_bi/BUILD_GUIDE.md` — step-by-step Power BI report build instructions and DAX measures.
- `sql_validation_queries.sql` — SQL checks to independently validate dashboard metrics.
- `tests/validate_source.py` — Python reference checks for the clean source dataset.

## Setup and run Python checks
```bash
pip install pandas
python tests/validate_source.py
```

Expected: five PASS messages, followed by reference KPI totals and grouped sales.

## Your practical workflow
1. Run the Python checks and understand each assertion.
2. Open the Excel test pack. Review all 15 test cases and understand the expected results.
3. Build the Power BI report by following `power_bi/BUILD_GUIDE.md`.
4. Validate each KPI and chart against the source data and SQL queries.
5. Test slicers, cross-filtering, no-data states, export and refresh.
6. Import `orders_with_issues.csv` as a separate test run and record how the dashboard handles bad data.
7. Record actual results, status, defect IDs and evidence filenames in the Excel workbook.
8. Fix any defects you find, rerun tests and save screenshots in `evidence/`.

## Suggested evidence
- Screenshot of each KPI card and the complete dashboard.
- Screenshot of one City filter and one Category filter applied.
- Excel workbook with actual results and pass/fail statuses.
- A short defect report for any mismatch you find.

## Resume rule
This is a starter project package, not proof that you have completed dashboard testing. Add it to your resume only after building the Power BI report and executing the tests yourself. Be precise about which tasks you completed. Do not claim advanced Power BI, DAX, or production testing experience based only on this starter kit.                            








<img width="970" height="537" alt="Screenshot 2026-11-27 105743" src="https://github.com/user-attachments/assets/8f6fa134-d587-49bb-819a-7d39bbfcc19f" />

