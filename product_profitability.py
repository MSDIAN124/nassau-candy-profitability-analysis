
import pandas as pd
from pathlib import Path

# Load engineered KPI dataset
INPUT_FILE = Path("data/processed/nassau_candy_kpi_data.csv")
OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

# Aggregate product-level metrics
product_summary = (
    df.groupby(["Product ID", "Product Name", "Division"], as_index=False)
    .agg(
        Orders=("Order ID", "nunique"),
        Units_Sold=("Units", "sum"),
        Revenue=("Sales", "sum"),
        Cost=("Cost", "sum"),
        Gross_Profit=("Gross Profit", "sum"),
        Duplicate_Candidate_Rows=("Duplicate Candidate Flag", "sum")
    )
)

# Calculate weighted product-level profitability
product_summary["Gross_Margin_%"] = (
    product_summary["Gross_Profit"] / product_summary["Revenue"] * 100
)

product_summary["Profit_Per_Unit"] = (
    product_summary["Gross_Profit"] / product_summary["Units_Sold"]
)

# Portfolio contribution
total_revenue = product_summary["Revenue"].sum()
total_profit = product_summary["Gross_Profit"].sum()

product_summary["Revenue_Contribution_%"] = (
    product_summary["Revenue"] / total_revenue * 100
)

product_summary["Profit_Contribution_%"] = (
    product_summary["Gross_Profit"] / total_profit * 100
)

# Sort by gross profit
product_summary = product_summary.sort_values(
    "Gross_Profit", ascending=False
).reset_index(drop=True)

# Save product summary
output_file = OUTPUT_DIR / "product_profitability_summary.csv"
product_summary.to_csv(output_file, index=False)

# Display results
display_columns = [
    "Product Name", "Division", "Orders", "Units_Sold",
    "Revenue", "Cost", "Gross_Profit", "Gross_Margin_%",
    "Profit_Per_Unit", "Revenue_Contribution_%",
    "Profit_Contribution_%", "Duplicate_Candidate_Rows"
]

print("===== PRODUCT PROFITABILITY ANALYSIS =====")
print(product_summary[display_columns].round(2).to_string(index=False))

print("\n===== VALIDATION =====")
print("Unique products:", product_summary["Product ID"].nunique())
print("Revenue total:", round(product_summary["Revenue"].sum(), 2))
print("Profit total:", round(product_summary["Gross_Profit"].sum(), 2))
print("Revenue contribution:", round(
    product_summary["Revenue_Contribution_%"].sum(), 2
))
print("Profit contribution:", round(
    product_summary["Profit_Contribution_%"].sum(), 2
))
print("Output:", output_file)
