
import pandas as pd
from pathlib import Path

INPUT_FILE = Path("data/processed/product_profitability_summary.csv")
OUTPUT_DIR = Path("data/processed")

df = pd.read_csv(INPUT_FILE)

# Revenue Pareto
revenue_pareto = df.sort_values(
    "Revenue", ascending=False
).copy()

revenue_pareto["Revenue_Contribution_%"] = (
    revenue_pareto["Revenue"] / revenue_pareto["Revenue"].sum() * 100
)

revenue_pareto["Cumulative_Revenue_%"] = (
    revenue_pareto["Revenue_Contribution_%"].cumsum()
)

# Profit Pareto
profit_pareto = df.sort_values(
    "Gross_Profit", ascending=False
).copy()

profit_pareto["Profit_Contribution_%"] = (
    profit_pareto["Gross_Profit"] / profit_pareto["Gross_Profit"].sum() * 100
)

profit_pareto["Cumulative_Profit_%"] = (
    profit_pareto["Profit_Contribution_%"].cumsum()
)

# Number of products required to reach at least 80%
revenue_80_count = int(
    (revenue_pareto["Cumulative_Revenue_%"] < 80).sum() + 1
)

profit_80_count = int(
    (profit_pareto["Cumulative_Profit_%"] < 80).sum() + 1
)

# Save detailed Pareto outputs
revenue_file = OUTPUT_DIR / "revenue_pareto_analysis.csv"
profit_file = OUTPUT_DIR / "profit_pareto_analysis.csv"

revenue_pareto.to_csv(revenue_file, index=False)
profit_pareto.to_csv(profit_file, index=False)

# Summary
print("===== REVENUE PARETO ANALYSIS =====")
print(
    revenue_pareto[
        ["Product Name", "Revenue", "Revenue_Contribution_%",
         "Cumulative_Revenue_%"]
    ].round(2).to_string(index=False)
)

print("\n===== PROFIT PARETO ANALYSIS =====")
print(
    profit_pareto[
        ["Product Name", "Gross_Profit", "Profit_Contribution_%",
         "Cumulative_Profit_%"]
    ].round(2).to_string(index=False)
)

print("\n===== 80% CONCENTRATION SUMMARY =====")
print("Products needed for 80% revenue:", revenue_80_count)
print("Products needed for 80% profit:", profit_80_count)

print("\nTop products reaching 80% revenue:")
print(revenue_pareto.head(revenue_80_count)["Product Name"].to_list())

print("\nTop products reaching 80% profit:")
print(profit_pareto.head(profit_80_count)["Product Name"].to_list())

print("\nOutput files:")
print(revenue_file)
print(profit_file)
