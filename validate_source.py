"""Reference checks for the dashboard source data.
Run from the project root: python tests/validate_source.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

def load_clean():
    return pd.read_csv(DATA / "orders_clean.csv", parse_dates=["OrderDate"])

def test_sales_amount_formula():
    df = load_clean()
    assert (df["SalesAmount"] == df["Quantity"] * df["UnitPrice"]).all()

def test_order_ids_unique_in_clean_file():
    df = load_clean()
    assert df["OrderID"].is_unique

def test_required_fields_present():
    df = load_clean()
    assert df[["OrderID", "OrderDate", "City", "Category", "Product", "Status"]].notna().all().all()

def test_positive_quantity():
    df = load_clean()
    assert (df["Quantity"] > 0).all()

def test_valid_status_values():
    df = load_clean()
    allowed = {"Delivered", "Shipped", "Cancelled", "Returned"}
    assert set(df["Status"]).issubset(allowed)

def print_reference_kpis():
    df = load_clean()
    print("Total sales:", int(df["SalesAmount"].sum()))
    print("Distinct orders:", int(df["OrderID"].nunique()))
    print("Average order value:", round(df["SalesAmount"].sum() / df["OrderID"].nunique(), 2))
    print("\\nSales by city:\\n", df.groupby("City")["SalesAmount"].sum())
    print("\\nSales by category:\\n", df.groupby("Category")["SalesAmount"].sum())

if __name__ == "__main__":
    for check in [test_sales_amount_formula, test_order_ids_unique_in_clean_file,
                  test_required_fields_present, test_positive_quantity, test_valid_status_values]:
        check()
        print("PASS:", check.__name__)
    print_reference_kpis()
