# Power BI Dashboard Build Guide

## Goal
Build a simple Retail Sales Quality Dashboard from `data/orders_clean.csv`, then test the report using the Excel test pack.

## Suggested report layout
1. KPI cards: Total Sales, Distinct Orders, Average Order Value, Delivered Orders.
2. Clustered column chart: Sales by Category.
3. Bar chart: Sales by City.
4. Line chart: Monthly Sales.
5. Slicers: City, Category, Status, OrderDate.
6. Detail table: OrderID, OrderDate, City, Category, Product, Quantity, UnitPrice, SalesAmount, Status.

## Load data
1. Open Power BI Desktop.
2. Select **Get data → Text/CSV** and choose `data/orders_clean.csv`.
3. Check data types: OrderDate = Date; Quantity and OrderID = Whole number; UnitPrice and SalesAmount = Decimal number.
4. In Power Query, add a custom column if needed: `SalesAmount = [Quantity] * [UnitPrice]`.
5. Close & Apply.

## DAX measures
```DAX
Total Sales = SUM(Orders[SalesAmount])

Distinct Orders = DISTINCTCOUNT(Orders[OrderID])

Average Order Value = DIVIDE([Total Sales], [Distinct Orders], 0)

Delivered Orders =
CALCULATE(
    DISTINCTCOUNT(Orders[OrderID]),
    Orders[Status] = "Delivered"
)

Returned Orders =
CALCULATE(
    DISTINCTCOUNT(Orders[OrderID]),
    Orders[Status] = "Returned"
)
```

## Validation approach
- Use `orders_clean.csv` for baseline dashboard checks.
- Use `orders_with_issues.csv` to test how the report responds to duplicate IDs, blank city, zero quantity and unknown status. Do not assume Power BI automatically rejects bad data; define and document the expected handling.
- Compare KPI and chart values against `excel/dashboard_test_pack.xlsx` and `sql_validation_queries.sql`.
- Test each slicer individually and in combination. Confirm all relevant visuals respond consistently.
- Check sorting, date hierarchy, empty states, export results and refresh behavior.
- For access-control tests, use only authorized test accounts in a permitted environment. Do not attempt to bypass real access controls.

## Important
This package does not contain a `.pbix` report. You will create the report in Power BI Desktop by following this guide. Do not claim Power BI dashboard development or testing as completed on your resume until you have built the report, executed the test cases, and saved evidence.
