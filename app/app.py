from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Nassau Candy | Profitability Intelligence",
    page_icon="🍫",
    layout="wide"
)

st.title("Nassau Candy Distributor")
st.subheader("Product Line Profitability & Margin Performance Analysis")
st.caption("Business intelligence dashboard | Unified Mentor Project")


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = PROJECT_ROOT / "data" / "processed" / "nassau_candy_kpi_data.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)

    df["Order Date"] = pd.to_datetime(
    df["Order Date"], format="%Y-%m-%d", errors="coerce"
    )

    numeric_columns = [
        "Sales", "Cost", "Gross Profit", "Units"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["Gross Margin %"] = (
        df["Gross Profit"] / df["Sales"] * 100
    )

    return df


try:
    df = load_data()
except FileNotFoundError:
    st.error(f"Dataset not found: {DATA_PATH}")
    st.stop()
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()


# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.header("Dashboard Filters")

min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

selected_dates = st.sidebar.date_input(
    "Order Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

divisions = sorted(df["Division"].dropna().unique())

selected_divisions = st.sidebar.multiselect(
    "Select Division",
    options=divisions,
    default=divisions
)

margin_threshold = st.sidebar.slider(
    "Minimum Gross Margin (%)",
    min_value=0,
    max_value=100,
    value=0,
    step=5
)

product_search = st.sidebar.text_input(
    "Search Product",
    placeholder="Enter product name..."
)


# --------------------------------------------------
# APPLY FILTERS
# --------------------------------------------------

if len(selected_dates) == 2:
    start_date, end_date = selected_dates
else:
    start_date = selected_dates[0]
    end_date = selected_dates[0]

filtered_df = df[
    (df["Order Date"].dt.date >= start_date)
    & (df["Order Date"].dt.date <= end_date)
    & (df["Division"].isin(selected_divisions))
].copy()

if start_date.year == 2025 and end_date.year == 2025:
    st.write("DEBUG - Filtered Rows:", len(filtered_df))
    st.write("DEBUG - Filtered Orders:", filtered_df["Order ID"].nunique())
    st.write("DEBUG - Revenue:", filtered_df["Sales"].sum())
    st.write("DEBUG - Cost:", filtered_df["Cost"].sum())
    st.write("DEBUG - Gross Profit:", filtered_df["Gross Profit"].sum())

if filtered_df.empty:
    st.warning("No records found for the selected filters.")
    st.stop()


# --------------------------------------------------
# KPI CALCULATIONS
# --------------------------------------------------

total_revenue = filtered_df["Sales"].sum()
total_cost = filtered_df["Cost"].sum()
total_profit = filtered_df["Gross Profit"].sum()
total_units = filtered_df["Units"].sum()
total_orders = filtered_df["Order ID"].nunique()

overall_margin = (
    total_profit / total_revenue * 100
    if total_revenue else 0
)


# --------------------------------------------------
# EXECUTIVE KPI CARDS
# --------------------------------------------------

st.markdown("## Business Performance Overview")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Total Revenue",
    f"${total_revenue:,.2f}"
)

c2.metric(
    "Gross Profit",
    f"${total_profit:,.2f}"
)

c3.metric(
    "Total Cost",
    f"${total_cost:,.2f}"
)

c4, c5 = st.columns(2)

c4.metric(
    "Gross Margin",
    f"{overall_margin:.2f}%"
)

c5.metric(
    "Total Orders",
    f"{total_orders:,}"
)

st.caption(
    f"Units sold: {total_units:,.0f} | "
    f"Records analysed: {len(filtered_df):,}"
)

st.divider()


# ==================================================
# MODULE 1: PRODUCT PROFITABILITY OVERVIEW
# ==================================================

st.header("1. Product Profitability Overview")

product_summary = (
    filtered_df
    .groupby(
        ["Product ID", "Product Name", "Division"],
        as_index=False
    )
    .agg(
        Orders=("Order ID", "nunique"),
        Units_Sold=("Units", "sum"),
        Revenue=("Sales", "sum"),
        Cost=("Cost", "sum"),
        Gross_Profit=("Gross Profit", "sum")
    )
)

product_summary["Gross_Margin_%"] = (
    product_summary["Gross_Profit"]
    / product_summary["Revenue"] * 100
)

product_summary["Profit_Per_Unit"] = (
    product_summary["Gross_Profit"]
    / product_summary["Units_Sold"]
)

product_summary = product_summary[
    product_summary["Gross_Margin_%"] >= margin_threshold
]

if product_search:
    product_summary = product_summary[
        product_summary["Product Name"].str.contains(
            product_search, case=False, na=False
        )
    ]

if product_summary.empty:
    st.info("No products match the selected filters.")
else:
    # Top-level product metrics
    best_product = product_summary.loc[
        product_summary["Gross_Profit"].idxmax()
    ]

    lowest_margin_product = product_summary.loc[
        product_summary["Gross_Margin_%"].idxmin()
    ]

    p1, p2 = st.columns(2)

    p1.metric(
        "Highest Gross Profit Product",
        best_product["Product Name"],
        f"${best_product['Gross_Profit']:,.2f}"
    )

    p2.metric(
        "Lowest Margin Product",
        lowest_margin_product["Product Name"],
        f"{lowest_margin_product['Gross_Margin_%']:.2f}%"
    )

    # Product profitability chart
    st.subheader("Revenue vs Gross Profit by Product")

    chart_data = product_summary.sort_values(
        "Gross_Profit", ascending=False
    )

    fig_product = px.bar(
        chart_data,
        x="Product Name",
        y=["Revenue", "Gross_Profit"],
        barmode="group",
        title="Product-wise Revenue and Gross Profit",
        labels={
            "value": "Amount ($)",
            "Product Name": "Product"
        }
    )

    fig_product.update_layout(
        xaxis_tickangle=-35,
        legend_title="Financial Metric"
    )

    st.plotly_chart(fig_product, use_container_width=True)

    # Margin chart
    st.subheader("Gross Margin by Product")

    margin_data = product_summary.sort_values(
        "Gross_Margin_%", ascending=True
    )

    fig_margin = px.bar(
        margin_data,
        x="Gross_Margin_%",
        y="Product Name",
        orientation="h",
        title="Product-wise Gross Margin",
        labels={
            "Gross_Margin_%": "Gross Margin (%)",
            "Product Name": "Product"
        }
    )

    st.plotly_chart(fig_margin, use_container_width=True)

    # Product table
    st.subheader("Product Profitability Details")

    display_products = product_summary.sort_values(
        "Gross_Profit", ascending=False
    ).copy()

    display_products = display_products.rename(
        columns={
            "Gross_Margin_%": "Gross Margin (%)",
            "Profit_Per_Unit": "Profit per Unit ($)"
        }
    )

    st.dataframe(
        display_products,
        use_container_width=True,
        hide_index=True
    )


st.divider()


# ==================================================
# MODULE 2: DIVISION PERFORMANCE DASHBOARD
# ==================================================

st.header("2. Division Performance Dashboard")

division_summary = (
    filtered_df
    .groupby("Division", as_index=False)
    .agg(
        Orders=("Order ID", "nunique"),
        Units_Sold=("Units", "sum"),
        Revenue=("Sales", "sum"),
        Cost=("Cost", "sum"),
        Gross_Profit=("Gross Profit", "sum")
    )
)

division_summary["Gross_Margin_%"] = (
    division_summary["Gross_Profit"]
    / division_summary["Revenue"] * 100
)

division_summary["Revenue_Contribution_%"] = (
    division_summary["Revenue"]
    / division_summary["Revenue"].sum() * 100
)

division_summary["Profit_Contribution_%"] = (
    division_summary["Gross_Profit"]
    / division_summary["Gross_Profit"].sum() * 100
)

d1, d2 = st.columns(2)

with d1:
    fig_division_revenue = px.bar(
        division_summary.sort_values(
            "Revenue", ascending=False
        ),
        x="Division",
        y="Revenue",
        title="Revenue by Division",
        text_auto=".2s"
    )

    st.plotly_chart(
        fig_division_revenue,
        use_container_width=True
    )

with d2:
    fig_division_profit = px.bar(
        division_summary.sort_values(
            "Gross_Profit", ascending=False
        ),
        x="Division",
        y="Gross_Profit",
        title="Gross Profit by Division",
        text_auto=".2s"
    )

    st.plotly_chart(
        fig_division_profit,
        use_container_width=True
    )


st.subheader("Division Gross Margin Comparison")

fig_division_margin = px.bar(
    division_summary.sort_values(
        "Gross_Margin_%", ascending=False
    ),
    x="Division",
    y="Gross_Margin_%",
    text_auto=".2f",
    title="Gross Margin (%) by Division"
)

st.plotly_chart(
    fig_division_margin,
    use_container_width=True
)


st.subheader("Division Performance Details")

st.dataframe(
    division_summary.sort_values(
        "Gross_Profit", ascending=False
    ),
    use_container_width=True,
    hide_index=True
)




# --------------------------------------------------
# MODULE 3: COST VS MARGIN DIAGNOSTICS
# --------------------------------------------------

st.header("3. Cost vs Margin Diagnostics")

# Build product-level diagnostics using currently filtered data
diagnostics = (
    filtered_df.groupby(
        ["Product ID", "Product Name", "Division"],
        as_index=False
    )
    .agg(
        Orders=("Order ID", "nunique"),
        Units_Sold=("Units", "sum"),
        Revenue=("Sales", "sum"),
        Cost=("Cost", "sum"),
        Gross_Profit=("Gross Profit", "sum")
    )
)

# Calculate profitability metrics
diagnostics["Gross_Margin_%"] = (
    diagnostics["Gross_Profit"] / diagnostics["Revenue"] * 100
)

diagnostics["Cost_to_Sales_%"] = (
    diagnostics["Cost"] / diagnostics["Revenue"] * 100
)

diagnostics["Profit_Per_Unit"] = (
    diagnostics["Gross_Profit"] / diagnostics["Units_Sold"]
)

# Classify margin risk using screening thresholds
def classify_margin(margin):
    if margin < 30:
        return "Critical Margin Review"
    elif margin < 50:
        return "Low Margin Review"
    elif margin < 60:
        return "Moderate Margin Review"
    return "Healthy Margin"

diagnostics["Margin_Status"] = diagnostics["Gross_Margin_%"].apply(
    classify_margin
)

diagnostics["Below_Portfolio_Margin"] = (
    diagnostics["Gross_Margin_%"] < overall_margin
)

# Apply product-level sidebar filters
diagnostics = diagnostics[
    diagnostics["Gross_Margin_%"] >= margin_threshold
]

if product_search:
    diagnostics = diagnostics[
        diagnostics["Product Name"].str.contains(
            product_search,
            case=False,
            na=False
        )
    ]

if diagnostics.empty:
    st.warning("No products match the selected filters.")

else:
    # Risk category counts
    risk_counts = diagnostics["Margin_Status"].value_counts()

    critical_count = risk_counts.get("Critical Margin Review", 0)
    low_count = risk_counts.get("Low Margin Review", 0)
    moderate_count = risk_counts.get("Moderate Margin Review", 0)

    r1, r2, r3 = st.columns(3)

    r1.metric("Critical Margin Products", f"{critical_count:,}")
    r2.metric("Low Margin Products", f"{low_count:,}")
    r3.metric("Moderate Margin Products", f"{moderate_count:,}")

    st.divider()

    # Cost vs margin comparison
    st.subheader("Cost-to-Sales vs Gross Margin")

    cost_margin_chart = diagnostics.sort_values(
        "Gross_Margin_%", ascending=True
    )

    fig_cost_margin = px.bar(
        cost_margin_chart,
        x="Product Name",
        y=["Cost_to_Sales_%", "Gross_Margin_%"],
        barmode="group",
        title="Product Cost-to-Sales and Gross Margin (%)",
        labels={
            "value": "Percentage (%)",
            "Product Name": "Product"
        },
        color_discrete_sequence=["#F97316", "#22C55E"]
    )

    fig_cost_margin.update_layout(
        xaxis_tickangle=-35,
        legend_title_text="Metric",
        height=480
    )

    st.plotly_chart(fig_cost_margin, use_container_width=True)

    # Margin risk details
    st.subheader("Product Margin Risk Details")

    risk_table = diagnostics[
        [
            "Product Name",
            "Division",
            "Orders",
            "Revenue",
            "Cost",
            "Gross_Profit",
            "Gross_Margin_%",
            "Cost_to_Sales_%",
            "Margin_Status",
            "Below_Portfolio_Margin"
        ]
    ].sort_values("Gross_Margin_%", ascending=True)

    risk_table = risk_table.rename(
    columns={"Below_Portfolio_Margin": "Below Avg. Margin?"}
    )

    risk_table["Below Avg. Margin?"] = (
        risk_table["Below Avg. Margin?"]
        .map({True: "Yes", False: "No"})
    )

    numeric_columns = [
        "Orders",
        "Revenue",
        "Cost",
        "Gross_Profit",
        "Gross_Margin_%",
        "Cost_to_Sales_%"
    ]

    styled_risk_table = (
        risk_table.style
        .format({
            "Orders": "{:,.0f}",
            "Revenue": "{:,.2f}",
            "Cost": "{:,.2f}",
            "Gross_Profit": "{:,.2f}",
            "Gross_Margin_%": "{:.2f}%",
            "Cost_to_Sales_%": "{:.2f}%"
        })
        .set_properties(
            subset=numeric_columns,
            **{"text-align": "center"}
        )
    )

    st.dataframe(
        styled_risk_table,
        use_container_width=True,
        hide_index=True,
        height=520
    )


    st.caption(
        "Margin categories are screening thresholds for further review, "
        "not automatic product discontinuation recommendations. "
        "Products with low order volumes should be interpreted cautiously."
    )



# --------------------------------------------------
# MODULE 4: PROFIT CONCENTRATION ANALYSIS
# --------------------------------------------------

st.header("4. Profit Concentration Analysis")

# Product-level aggregation using selected date and division filters
pareto_data = (
    filtered_df.groupby(
        ["Product ID", "Product Name", "Division"],
        as_index=False
    )
    .agg(
        Revenue=("Sales", "sum"),
        Gross_Profit=("Gross Profit", "sum")
    )
)


if pareto_data.empty:
    st.warning("No product data available for Pareto analysis.")

else:
    # Revenue Pareto
    revenue_pareto = pareto_data.sort_values(
        "Revenue", ascending=False
    ).reset_index(drop=True)

    total_revenue_pareto = revenue_pareto["Revenue"].sum()

    revenue_pareto["Revenue_Contribution_%"] = (
        revenue_pareto["Revenue"] / total_revenue_pareto * 100
    )

    revenue_pareto["Cumulative_Revenue_%"] = (
        revenue_pareto["Revenue_Contribution_%"].cumsum()
    )

    revenue_80_count = (
        revenue_pareto["Cumulative_Revenue_%"].ge(80).idxmax() + 1
        if (revenue_pareto["Cumulative_Revenue_%"] >= 80).any()
        else len(revenue_pareto)
    )

    # Profit Pareto
    profit_pareto = pareto_data.sort_values(
        "Gross_Profit", ascending=False
    ).reset_index(drop=True)

    total_profit_pareto = profit_pareto["Gross_Profit"].sum()

    profit_pareto["Profit_Contribution_%"] = (
        profit_pareto["Gross_Profit"] / total_profit_pareto * 100
    )

    profit_pareto["Cumulative_Profit_%"] = (
        profit_pareto["Profit_Contribution_%"].cumsum()
    )

    profit_80_count = (
        profit_pareto["Cumulative_Profit_%"].ge(80).idxmax() + 1
        if (profit_pareto["Cumulative_Profit_%"] >= 80).any()
        else len(profit_pareto)
    )

    # Concentration KPI cards
    p1, p2 = st.columns(2)

    p1.metric(
        "Products Required for 80% Revenue",
        f"{revenue_80_count} of {len(revenue_pareto)}"
    )

    p2.metric(
        "Products Required for 80% Gross Profit",
        f"{profit_80_count} of {len(profit_pareto)}"
    )

    st.divider()

    # Revenue concentration chart
    st.subheader("Revenue Contribution Analysis")

    fig_revenue_pareto = px.bar(
        revenue_pareto,
        x="Product Name",
        y="Cumulative_Revenue_%",
        title="Cumulative Revenue Contribution by Product",
        labels={
            "Product Name": "Product",
            "Cumulative_Revenue_%": "Cumulative Revenue (%)"
        },
        color_discrete_sequence=["#A78BFA"]
    )

    fig_revenue_pareto.add_hline(
        y=80,
        line_dash="dash",
        line_color="#F97316",
        annotation_text="80% Threshold"
    )

    fig_revenue_pareto.update_layout(
        xaxis_tickangle=-35,
        yaxis_range=[0, 105],
        height=450
    )

    st.plotly_chart(
        fig_revenue_pareto,
        use_container_width=True
    )

    # Profit concentration chart
    st.subheader("Gross Profit Contribution Analysis")

    fig_profit_pareto = px.bar(
        profit_pareto,
        x="Product Name",
        y="Cumulative_Profit_%",
        title="Cumulative Gross Profit Contribution by Product",
        labels={
            "Product Name": "Product",
            "Cumulative_Profit_%": "Cumulative Gross Profit (%)"
        },
        color_discrete_sequence=["#22C55E"]
    )

    fig_profit_pareto.add_hline(
        y=80,
        line_dash="dash",
        line_color="#F97316",
        annotation_text="80% Threshold"
    )

    fig_profit_pareto.update_layout(
        xaxis_tickangle=-35,
        yaxis_range=[0, 105],
        height=450
    )

    st.plotly_chart(
        fig_profit_pareto,
        use_container_width=True
    )

    # Top products summary
    st.subheader("Revenue Pareto Details")

    st.dataframe(
        revenue_pareto[
            [
                "Product Name",
                "Division",
                "Revenue",
                "Revenue_Contribution_%",
                "Cumulative_Revenue_%"
            ]
        ].style.format({
            "Revenue": "{:,.2f}",
            "Revenue_Contribution_%": "{:.2f}%",
            "Cumulative_Revenue_%": "{:.2f}%"
        }),
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Gross Profit Pareto Details")

    st.dataframe(
        profit_pareto[
            [
                "Product Name",
                "Division",
                "Gross_Profit",
                "Profit_Contribution_%",
                "Cumulative_Profit_%"
            ]
        ].style.format({
            "Gross_Profit": "{:,.2f}",
            "Profit_Contribution_%": "{:.2f}%",
            "Cumulative_Profit_%": "{:.2f}%"
        }),
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "Pareto analysis uses all products in the selected date and division "
        "filters. Minimum margin and product search filters are intentionally "
        "not applied because they would distort total portfolio concentration."
    )



# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Nassau Candy Distributor | Product Line Profitability Analysis | "
    "Data source: Official Unified Mentor project dataset"
)