
import pandas as pd
import numpy as np
from pathlib import Path

# Paths
RAW_FILE = Path("data/raw/nassau_candy_distributor.csv")
OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load original dataset
df = pd.read_csv(RAW_FILE)

# Parse dates without modifying source data
df["Order Date"] = pd.to_datetime(
    df["Order Date"], format="%d-%m-%Y", errors="coerce"
)
df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], format="%d-%m-%Y", errors="coerce"
)

# Derived time fields
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
df["Year"] = df["Order Date"].dt.year
df["Quarter"] = df["Order Date"].dt.to_period("Q").astype(str)

# Core profitability KPIs
df["Gross Margin %"] = np.where(
    df["Sales"] != 0,
    (df["Gross Profit"] / df["Sales"]) * 100,
    np.nan
)

df["Profit per Unit"] = np.where(
    df["Units"] > 0,
    df["Gross Profit"] / df["Units"],
    np.nan
)

df["Revenue per Unit"] = np.where(
    df["Units"] > 0,
    df["Sales"] / df["Units"],
    np.nan
)

df["Cost per Unit"] = np.where(
    df["Units"] > 0,
    df["Cost"] / df["Units"],
    np.nan
)

# Duplicate candidate flag:
# Business fields identical, excluding Row ID
duplicate_columns = [
    "Order ID", "Product ID", "Order Date", "Ship Date",
    "Customer ID", "Sales", "Units", "Gross Profit", "Cost"
]

df["Duplicate Candidate Flag"] = df.duplicated(
    subset=duplicate_columns,
    keep="first"
)

# Revenue and profit contribution at transaction level
total_revenue = df["Sales"].sum()
total_profit = df["Gross Profit"].sum()

df["Revenue Contribution %"] = (
    df["Sales"] / total_revenue * 100
    if total_revenue != 0 else np.nan
)

df["Profit Contribution %"] = (
    df["Gross Profit"] / total_profit * 100
    if total_profit != 0 else np.nan
)

# Save processed dataset
output_file = OUTPUT_DIR / "nassau_candy_kpi_data.csv"
df.to_csv(output_file, index=False)

# Validation summary
print("===== KPI ENGINEERING VALIDATION =====")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Missing values:", int(df.isna().sum().sum()))
print("Duplicate candidates:", int(df["Duplicate Candidate Flag"].sum()))
print("Total revenue:", round(df["Sales"].sum(), 2))
print("Total gross profit:", round(df["Gross Profit"].sum(), 2))
print("Overall gross margin %:", round(
    df["Gross Profit"].sum() / df["Sales"].sum() * 100, 2
))
print("Revenue contribution total:", round(
    df["Revenue Contribution %"].sum(), 2
))
print("Profit contribution total:", round(
    df["Profit Contribution %"].sum(), 2
))
print("Output:", output_file)
