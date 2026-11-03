
import pandas as pd
from pathlib import Path

INPUT_FILE = Path("data/processed/nassau_candy_kpi_data.csv")
OUTPUT_DIR = Path("data/processed")

df = pd.read_csv(INPUT_FILE)

# Division-level aggregation
division_summary = (
    df.groupby("Division", as_index=False)
    .agg(
        Orders=("Order ID", "nunique"),
        Units_Sold=("Units", "sum"),
        Revenue=("Sales", "sum"),
        Cost=("Cost", "sum"),
        Gross_Profit=("Gross Profit", "sum"),
        Transaction_Rows=("Row ID", "count"),
        Duplicate_Candidate_Rows=("Duplicate Candidate Flag", "sum")
    )
)

# Calculate profitability metrics
division_summary["Gross_Margin_%"] = (
    division_summary["Gross_Profit"] / division_summary["Revenue"] * 100
)

division_summary["Profit_Per_Unit"] = (
    division_summary["Gross_Profit"] / division_summary["Units_Sold"]
)

total_revenue = division_summary["Revenue"].sum()
total_profit = division_summary["Gross_Profit"].sum()

division_summary["Revenue_Contribution_%"] = (
    division_summary["Revenue"] / total_revenue * 100
)

division_summary["Profit_Contribution_%"] = (
    division_summary["Gross_Profit"] / total_profit * 100
)

# Sort by revenue
division_summary = division_summary.sort_values(
    "Revenue", ascending=False
).reset_index(drop=True)

# Save output
output_file = OUTPUT_DIR / "division_performance_summary.csv"
division_summary.to_csv(output_file, index=False)

# Display
print("===== DIVISION PERFORMANCE ANALYSIS =====")
print(division_summary.round(2).to_string(index=False))

print("\n===== VALIDATION =====")
print("Divisions:", division_summary["Division"].nunique())
print("Revenue total:", round(division_summary["Revenue"].sum(), 2))
print("Profit total:", round(division_summary["Gross_Profit"].sum(), 2))
print("Revenue contribution:", round(
    division_summary["Revenue_Contribution_%"].sum(), 2
))
print("Profit contribution:", round(
    division_summary["Profit_Contribution_%"].sum(), 2
))
print("Output:", output_file)
