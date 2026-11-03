
import pandas as pd
from pathlib import Path

INPUT_FILE = Path("data/processed/nassau_candy_kpi_data.csv")
OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

# Aggregate monthly financial performance
monthly = (
    df.groupby("Month", as_index=False)
    .agg(
        Orders=("Order ID", "nunique"),
        Units_Sold=("Units", "sum"),
        Revenue=("Sales", "sum"),
        Cost=("Cost", "sum"),
        Gross_Profit=("Gross Profit", "sum"),
        Duplicate_Candidate_Rows=("Duplicate Candidate Flag", "sum")
    )
)

# Calculate monthly gross margin using aggregated values
monthly["Gross_Margin_%"] = (
    monthly["Gross_Profit"] / monthly["Revenue"] * 100
)

# Month-on-month changes
monthly["MoM_Revenue_Change_%"] = (
    monthly["Revenue"].pct_change() * 100
)

monthly["MoM_Profit_Change_%"] = (
    monthly["Gross_Profit"].pct_change() * 100
)

monthly["MoM_Margin_Change_pp"] = (
    monthly["Gross_Margin_%"].diff()
)

# Save output
output_file = OUTPUT_DIR / "monthly_margin_analysis.csv"
monthly.to_csv(output_file, index=False)

# Identify highest and lowest margin months
highest = monthly.loc[monthly["Gross_Margin_%"].idxmax()]
lowest = monthly.loc[monthly["Gross_Margin_%"].idxmin()]

# Volatility statistics
margin_mean = monthly["Gross_Margin_%"].mean()
margin_std = monthly["Gross_Margin_%"].std()
margin_range = (
    monthly["Gross_Margin_%"].max()
    - monthly["Gross_Margin_%"].min()
)

print("===== MONTHLY FINANCIAL PERFORMANCE =====")
print(monthly.round(2).to_string(index=False))

print("\n===== MONTHLY MARGIN VOLATILITY =====")
print("Average monthly margin:", round(margin_mean, 2), "%")
print("Margin standard deviation:", round(margin_std, 2), "percentage points")
print("Margin range:", round(margin_range, 2), "percentage points")

print("\nHighest margin month:")
print(highest[["Month", "Gross_Margin_%"]].to_string())

print("\nLowest margin month:")
print(lowest[["Month", "Gross_Margin_%"]].to_string())

print("\n===== VALIDATION =====")
print("Months:", len(monthly))
print("Revenue total:", round(monthly["Revenue"].sum(), 2))
print("Gross profit total:", round(monthly["Gross_Profit"].sum(), 2))
print("Duplicate candidate rows:", int(
    monthly["Duplicate_Candidate_Rows"].sum()
))
print("Output:", output_file)
