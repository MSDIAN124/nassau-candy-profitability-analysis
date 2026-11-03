
import pandas as pd
from pathlib import Path

INPUT_FILE = Path("data/processed/product_profitability_summary.csv")
OUTPUT_DIR = Path("data/processed")

df = pd.read_csv(INPUT_FILE)

# Cost and profitability diagnostics
df["Cost_to_Sales_%"] = df["Cost"] / df["Revenue"] * 100

df["Profit_Per_Revenue_Rupee"] = (
    df["Gross_Profit"] / df["Revenue"]
)

# Rank products by margin
df["Margin_Rank"] = df["Gross_Margin_%"].rank(
    ascending=False, method="min"
).astype(int)

# Flag products for investigation (screening, not final decisions)
def classify_margin(row):
    if row["Gross_Margin_%"] < 30:
        return "Critical Margin Review"
    elif row["Gross_Margin_%"] < 50:
        return "Low Margin Review"
    elif row["Gross_Margin_%"] < 60:
        return "Moderate Margin Review"
    else:
        return "Healthy Margin"

df["Margin_Status"] = df.apply(classify_margin, axis=1)

# Identify high-revenue products with below-portfolio margin
portfolio_margin = (
    df["Gross_Profit"].sum() / df["Revenue"].sum() * 100
)

df["Below_Portfolio_Margin"] = (
    df["Gross_Margin_%"] < portfolio_margin
)

# Sort by lowest margin
diagnostics = df.sort_values(
    "Gross_Margin_%", ascending=True
).reset_index(drop=True)

# Save full diagnostics
output_file = OUTPUT_DIR / "cost_margin_diagnostics.csv"
diagnostics.to_csv(output_file, index=False)

# Display relevant columns
columns = [
    "Product Name", "Division", "Revenue", "Cost",
    "Gross_Profit", "Gross_Margin_%", "Cost_to_Sales_%",
    "Profit_Per_Unit", "Margin_Status",
    "Below_Portfolio_Margin"
]

print("===== COST VS MARGIN DIAGNOSTICS =====")
print(diagnostics[columns].round(2).to_string(index=False))

print("\n===== PORTFOLIO BENCHMARK =====")
print("Portfolio gross margin:", round(portfolio_margin, 2), "%")

print("\n===== PRODUCTS REQUIRING REVIEW =====")
review = diagnostics[
    diagnostics["Margin_Status"].isin([
        "Critical Margin Review", "Low Margin Review"
    ])
]
print(review[columns].round(2).to_string(index=False))

print("\n===== VALIDATION =====")
print("Products:", len(diagnostics))
print("Revenue total:", round(diagnostics["Revenue"].sum(), 2))
print("Gross profit total:", round(diagnostics["Gross_Profit"].sum(), 2))
print("Output:", output_file)
