
import pandas as pd
import plotly.express as px
from pathlib import Path

# --------------------------------------------------
# PATHS
# --------------------------------------------------

INPUT_FILE = Path("data/processed/nassau_candy_kpi_data.csv")
OUTPUT_DIR = Path("data/processed")
FIGURE_DIR = Path("outputs/figures")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
FIGURE_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

# --------------------------------------------------
# 1. PRODUCT-LEVEL COST VS SALES ANALYSIS
# --------------------------------------------------

product_cost_analysis = (
    df.groupby(["Product Name", "Division"], as_index=False)
    .agg(
        Revenue=("Sales", "sum"),
        Cost=("Cost", "sum"),
        Gross_Profit=("Gross Profit", "sum"),
        Units_Sold=("Units", "sum")
    )
)

product_cost_analysis["Gross_Margin_%"] = (
    product_cost_analysis["Gross_Profit"]
    / product_cost_analysis["Revenue"] * 100
)

product_cost_analysis["Cost_to_Sales_%"] = (
    product_cost_analysis["Cost"]
    / product_cost_analysis["Revenue"] * 100
)

product_cost_analysis.to_csv(
    OUTPUT_DIR / "product_cost_sales_analysis.csv",
    index=False
)

fig = px.scatter(
    product_cost_analysis,
    x="Revenue",
    y="Cost",
    color="Division",
    size="Units_Sold",
    hover_name="Product Name",
    hover_data={
        "Gross_Profit": ":,.2f",
        "Gross_Margin_%": ":.2f",
        "Cost_to_Sales_%": ":.2f"
    },
    title="Product-Level Cost vs Sales Analysis",
    labels={
        "Revenue": "Total Sales",
        "Cost": "Total Cost",
        "Units_Sold": "Units Sold"
    }
)

fig.update_layout(template="plotly_dark")

fig.write_html(
    FIGURE_DIR / "cost_vs_sales_scatter.html"
)

# --------------------------------------------------
# 2. REGION-LEVEL PROFITABILITY
# --------------------------------------------------

region_summary = (
    df.groupby("Region", as_index=False)
    .agg(
        Orders=("Order ID", "nunique"),
        Units_Sold=("Units", "sum"),
        Revenue=("Sales", "sum"),
        Cost=("Cost", "sum"),
        Gross_Profit=("Gross Profit", "sum")
    )
)

region_summary["Gross_Margin_%"] = (
    region_summary["Gross_Profit"]
    / region_summary["Revenue"] * 100
)

region_summary["Revenue_Contribution_%"] = (
    region_summary["Revenue"]
    / region_summary["Revenue"].sum() * 100
)

region_summary["Profit_Contribution_%"] = (
    region_summary["Gross_Profit"]
    / region_summary["Gross_Profit"].sum() * 100
)

region_summary = region_summary.sort_values(
    "Revenue", ascending=False
)

region_summary.to_csv(
    OUTPUT_DIR / "region_profitability_analysis.csv",
    index=False
)

# --------------------------------------------------
# 3. STATE-LEVEL PROFITABILITY
# --------------------------------------------------

state_summary = (
    df.groupby("State/Province", as_index=False)
    .agg(
        Orders=("Order ID", "nunique"),
        Units_Sold=("Units", "sum"),
        Revenue=("Sales", "sum"),
        Cost=("Cost", "sum"),
        Gross_Profit=("Gross Profit", "sum")
    )
)

state_summary["Gross_Margin_%"] = (
    state_summary["Gross_Profit"]
    / state_summary["Revenue"] * 100
)

state_summary["Revenue_Contribution_%"] = (
    state_summary["Revenue"]
    / state_summary["Revenue"].sum() * 100
)

state_summary["Profit_Contribution_%"] = (
    state_summary["Gross_Profit"]
    / state_summary["Gross_Profit"].sum() * 100
)

state_summary = state_summary.sort_values(
    "Revenue", ascending=False
)

state_summary.to_csv(
    OUTPUT_DIR / "state_profitability_analysis.csv",
    index=False
)

# --------------------------------------------------
# 4. VALIDATION
# --------------------------------------------------

print("\n===== COST VS SALES ANALYSIS =====")
print(product_cost_analysis.round(2).to_string(index=False))

print("\n===== REGION PROFITABILITY =====")
print(region_summary.round(2).to_string(index=False))

print("\n===== TOP 10 STATES BY REVENUE =====")
print(state_summary.head(10).round(2).to_string(index=False))

print("\n===== VALIDATION =====")

print("Products:", len(product_cost_analysis))
print("Regions:", len(region_summary))
print("States:", len(state_summary))

print("Revenue total:", round(df["Sales"].sum(), 2))
print("Region revenue total:", round(region_summary["Revenue"].sum(), 2))
print("State revenue total:", round(state_summary["Revenue"].sum(), 2))

print("Profit total:", round(df["Gross Profit"].sum(), 2))
print("Region profit total:", round(region_summary["Gross_Profit"].sum(), 2))
print("State profit total:", round(state_summary["Gross_Profit"].sum(), 2))

print("\nGenerated files:")
print("1. data/processed/product_cost_sales_analysis.csv")
print("2. data/processed/region_profitability_analysis.csv")
print("3. data/processed/state_profitability_analysis.csv")
print("4. outputs/figures/cost_vs_sales_scatter.html")

print("\nAnalysis completed successfully.")
