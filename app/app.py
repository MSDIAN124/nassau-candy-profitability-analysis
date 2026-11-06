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
st.markdown("""
<style>
    /* Main title */
    h1 {
        color: #FFFFFF !important;
        font-weight: 800 !important;
    }

    /* Subheadings */
    h2, h3 {
        color: #E2E8F0 !important;
        font-weight: 700 !important;
    }

    /* Captions and muted text */
    .stCaption {
        color: #CBD5E1 !important;
    }

    /* Markdown headings */
    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3 {
        color: #FFFFFF !important;
    }
</style>
""", unsafe_allow_html=True)

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
# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------

# Premium sidebar styling
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #190540 0%, #100326 100%);
    border-right: 1px solid #3B236B;
}

[data-testid="stSidebar"] h2 {
    color: #FFFFFF;
    font-size: 23px;
    font-weight: 700;
}

[data-testid="stSidebar"] label {
    color: #E9DFFF !important;
    font-weight: 600;
}

[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
    color: #E9DFFF !important;
}

[data-testid="stSidebar"] hr {
    border-color: #49316F;
}

[data-testid="stSidebar"] input,
[data-testid="stSidebar"] [data-baseweb="select"] {
    border-radius: 9px;
}

[data-testid="stSidebar"] .stButton button {
    background: linear-gradient(90deg, #7C3AED, #9333EA);
    color: white;
    border: none;
    border-radius: 9px;
    font-weight: 700;
    width: 100%;
    padding: 9px;
}

[data-testid="stSidebar"] .stButton button:hover {
    background: #6D28D9;
    color: white;
    border: none;
}

/* MAIN DASHBOARD BACKGROUND */
.stApp {
    background:
        linear-gradient(
            120deg,
            rgba(25, 5, 64, 0.86),
            rgba(16, 3, 38, 0.82)
        ),
        url("https://images.unsplash.com/photo-1744576409106-7b7685ed6cb4?auto=format&fit=crop&fm=jpg&q=80&w=2400");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* TRANSPARENT MAIN CONTAINER */
[data-testid="stAppViewContainer"] {
    background: transparent;
}

[data-testid="stHeader"] {
    background: rgba(16, 3, 38, 0.25);
}

/* GLASSMORPHISM KPI CARDS */
[data-testid="stMetric"] {
    background: rgba(55, 25, 90, 0.48);
    border: 1px solid rgba(216, 180, 254, 0.35);
    border-radius: 18px;
    padding: 18px 20px;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.22);
}

/* KPI LABELS */
[data-testid="stMetricLabel"] {
    color: #E9DFFF;
}

/* KPI VALUES */
[data-testid="stMetricValue"] {
    color: #FFFFFF;
    font-weight: 750;
}

/* KPI DELTA */
[data-testid="stMetricDelta"] {
    font-weight: 650;
}


/* CUSTOM KPI CARDS */

.custom-kpi-card {
    background: rgba(55, 25, 90, 0.55);
    border: 1px solid rgba(216, 180, 254, 0.35);
    border-radius: 18px;
    padding: 22px;
    min-height: 155px;
    margin-bottom: 18px;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.22);

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    width: 100%;
    box-sizing: border-box;
}

.custom-kpi-card .kpi-icon {
    width: 48px;
    height: 48px;
    margin: 0 auto 14px auto;
    display: flex;
    justify-content: center;
    align-items: center;
}

.custom-kpi-card .kpi-icon img {
    width: 100%;
    height: 100%;
    object-fit: contain;
}

.custom-kpi-card .kpi-title {
    color: #E9DFFF;
    font-size: 14px;
    font-weight: 600;
    margin: 0 0 8px 0;
    text-align: center !important;
    width: 100%;
    display: block;
}

.custom-kpi-card .kpi-value {
    color: #FFFFFF;
    font-size: 25px;
    font-weight: 750;
    overflow-wrap: anywhere;
    text-align: center !important;
    width: 100%;
    display: block;
}

/* CENTER ALIGN EXECUTIVE KPI CARDS */

.custom-kpi-card {
    text-align: center;
}

.kpi-icon {
    width: 48px;
    height: 48px;
    margin: 0 auto 14px auto;
}

.kpi-title {
    text-align: center;
}

.kpi-value {
    text-align: center;
}

/* CENTER ALIGN PRODUCT METRICS */

[data-testid="stMetric"] {
    text-align: center;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricValue"],
[data-testid="stMetricDelta"] {
    justify-content: center;
    text-align: center;
}

/* FORCE CENTER ALIGNMENT FOR KPI CARDS */

.custom-kpi-card {
    text-align: center !important;
}

.custom-kpi-card .kpi-icon {
    display: block !important;
    margin: 0 auto 14px auto !important;
}

.custom-kpi-card .kpi-title {
    display: block !important;
    width: 100% !important;
    text-align: center !important;
}

.custom-kpi-card .kpi-value {
    display: block !important;
    width: 100% !important;
    text-align: center !important;
}

/* CENTER ALIGNMENT - MODULE KPI LABELS */

div[data-testid="stMetric"] {
    text-align: center !important;
}

div[data-testid="stMetricLabel"] {
    justify-content: center !important;
    width: 100% !important;
    text-align: center !important;
}

div[data-testid="stMetricLabel"] > div {
    width: 100% !important;
    justify-content: center !important;
    text-align: center !important;
}

div[data-testid="stMetricValue"] {
    justify-content: center !important;
    text-align: center !important;
}

div[data-testid="stMetricDelta"] {
    justify-content: center !important;
    text-align: center !important;
}

</style>

""", unsafe_allow_html=True)


min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

def reset_filters():
    st.session_state["date_filter"] = (min_date, max_date)
    st.session_state["division_filter"] = sorted(
        df["Division"].dropna().unique()
    )
    st.session_state["margin_filter"] = 0
    st.session_state["product_filter"] = ""

with st.sidebar:

    st.markdown("## 🎛️ FILTER PANEL")
    st.caption("Customize your profitability analysis")
    st.divider()

    st.markdown("### 📅 Date Selection")

    selected_dates = st.date_input(
        "Order Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        key="date_filter"
    )

    st.divider()

    st.markdown("### 🏢 Business Division")

    divisions = sorted(df["Division"].dropna().unique())

    selected_divisions = st.multiselect(
        "Select Division",
        options=divisions,
        default=divisions,
        key="division_filter"
    )

    st.divider()

    st.markdown("### 📊 Margin Threshold")

    margin_threshold = st.slider(
        "Minimum Gross Margin (%)",
        min_value=0,
        max_value=100,
        value=0,
        step=5,
        key="margin_filter"
    )

    st.divider()

    st.markdown("### 🔎 Product Search")

    product_search = st.text_input(
        "Search Product",
        placeholder="Enter product name...",
        key="product_filter"
    )

    st.divider()

    st.caption("Reset all dashboard filters")

    st.button(
    "↺ Reset Filters",
    use_container_width=True,
    on_click=reset_filters
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


import base64

ICON_PATH = PROJECT_ROOT / "assets" / "icons"


def get_icon_base64(filename):
    icon_file = ICON_PATH / filename

    with open(icon_file, "rb") as f:
        return base64.b64encode(f.read()).decode()


def render_kpi_card(title, value, icon):
    icon_data = get_icon_base64(icon)

    st.markdown(
        f"""
        <div class="custom-kpi-card">
            <div class="kpi-icon">
                <img src="data:image/png;base64,{icon_data}">
            </div>
            <div class="kpi-title">{title}</div>
            <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("## Business Performance Overview")

# First row
c1, c2, c3 = st.columns(3)

with c1:
    render_kpi_card(
        "Total Revenue",
        f"${total_revenue:,.2f}",
        "total_revenue.png"
    )

with c2:
    render_kpi_card(
        "Gross Profit",
        f"${total_profit:,.2f}",
        "gross_profit.png"
    )

with c3:
    render_kpi_card(
        "Total Cost",
        f"${total_cost:,.2f}",
        "total_cost.png"
    )

# Second row
c4, c5 = st.columns(2)

with c4:
    render_kpi_card(
        "Gross Margin",
        f"{overall_margin:.2f}%",
        "gross_margin.png"
    )

with c5:
    render_kpi_card(
        "Total Orders",
        f"{total_orders:,}",
        "total_orders.png"
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

    # Top-level product metrics

    st.metric(
        label="Highest Gross Profit Product",
        value=best_product["Product Name"],
        delta=f"${best_product['Gross_Profit']:,.2f}"
    )

    st.metric(
        label="Lowest Margin Product",
        value=lowest_margin_product["Product Name"],
        delta=f"{lowest_margin_product['Gross_Margin_%']:.2f}%"
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
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(25,5,64,0.25)",
    font=dict(
        family="Arial",
        color="#E9DFFF",
        size=12
    ),
    title_font=dict(
        size=19,
        color="#FFFFFF"
    ),
    xaxis=dict(
        showgrid=False,
        tickangle=-35,
        color="#D8B4FE"
    ),
    yaxis=dict(
        gridcolor="rgba(216,180,254,0.12)",
        zeroline=False,
        color="#D8B4FE"
    ),
    legend=dict(
        title="Financial Metric",
        orientation="h",
        y=1.12,
        x=0
    ),
    margin=dict(l=25, r=25, t=80, b=80),
    bargap=0.25,
    height=450
    )

    fig_product.update_traces(
        marker_line_width=0
    )

    fig_product.update_traces(
        marker_color="#8B5CF6",
        selector=dict(name="Revenue")
    )

    fig_product.update_traces(
        marker_color="#22D3EE",
        selector=dict(name="Gross_Profit")
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
    fig_margin.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(25,5,64,0.25)",
    font=dict(
        family="Arial",
        color="#E9DFFF",
        size=12
    ),
    title_font=dict(size=19, color="#FFFFFF"),
    xaxis=dict(
        title="Gross Margin (%)",
        gridcolor="rgba(216,180,254,0.12)",
        color="#D8B4FE"
    ),
    yaxis=dict(
        showgrid=False,
        color="#D8B4FE"
    ),
    margin=dict(l=25, r=25, t=65, b=35),
    height=480
    )

    fig_margin.update_traces(
        marker_color="#A78BFA",
        marker_line_width=0,
        opacity=0.9
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

    styled_products = (
    display_products.style
    .format({
        "Revenue": "${:,.2f}",
        "Gross_Profit": "${:,.2f}",
        "Cost": "${:,.2f}",
        "Gross Margin (%)": "{:.2f}%",
        "Profit per Unit ($)": "${:,.2f}"
    }, na_rep="-")
    .set_properties(**{
        "background-color": "#241044",
        "color": "#F3E8FF",
        "border-color": "#4C267A",
        "text-align": "center"
    })
    .set_table_styles([
        {
            "selector": "th",
            "props": [
                ("background-color", "#4C1D95"),
                ("color", "#FFFFFF"),
                ("font-weight", "bold"),
                ("text-align", "center"),
                ("border", "1px solid #6D28D9")
            ]
        },
        {
            "selector": "td",
            "props": [
                ("padding", "10px"),
                ("border", "1px solid #4C267A")
            ]
        },
        {
            "selector": "table",
            "props": [
                ("border-collapse", "collapse"),
                ("width", "100%")
            ]
        }
    ])
)

    st.dataframe(
        styled_products,
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

    fig_division_revenue.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(25,5,64,0.25)",
    font=dict(family="Arial", color="#E9DFFF", size=12),
    title_font=dict(size=19, color="#FFFFFF"),
    xaxis=dict(showgrid=False, color="#D8B4FE"),
    yaxis=dict(
        title="Revenue ($)",
        gridcolor="rgba(216,180,254,0.12)",
        color="#D8B4FE",
        zeroline=False
    ),
    margin=dict(l=25, r=25, t=65, b=35),
    height=400,
    showlegend=False
   )

    fig_division_revenue.update_traces(
        marker_color="#8B5CF6",
        marker_line_width=0,
        opacity=0.9,
        textposition="outside",
        textfont=dict(color="#FFFFFF", size=12)
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

    fig_division_profit.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(25,5,64,0.25)",
    font=dict(family="Arial", color="#E9DFFF", size=12),
    title_font=dict(size=19, color="#FFFFFF"),
    xaxis=dict(showgrid=False, color="#D8B4FE"),
    yaxis=dict(
        title="Gross Profit ($)",
        gridcolor="rgba(216,180,254,0.12)",
        color="#D8B4FE",
        zeroline=False
    ),
    margin=dict(l=25, r=25, t=65, b=35),
    height=400,
    showlegend=False
    )

    fig_division_profit.update_traces(
        marker_color="#22D3EE",
        marker_line_width=0,
        opacity=0.9,
        textposition="outside",
        textfont=dict(color="#FFFFFF", size=12)
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

fig_division_margin.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(25,5,64,0.25)",
    font=dict(family="Arial", color="#E9DFFF", size=12),
    title_font=dict(size=19, color="#FFFFFF"),
    xaxis=dict(
        showgrid=False,
        color="#D8B4FE"
    ),
    yaxis=dict(
        title="Gross Margin (%)",
        gridcolor="rgba(216,180,254,0.12)",
        color="#D8B4FE",
        zeroline=False
    ),
    margin=dict(l=25, r=25, t=65, b=35),
    height=400,
    showlegend=False
)

fig_division_margin.update_traces(
    marker_color="#A78BFA",
    marker_line_width=0,
    opacity=0.9,
    textposition="outside",
    textfont=dict(color="#FFFFFF", size=12)
)

st.plotly_chart(
    fig_division_margin,
    use_container_width=True
)


st.subheader("Division Performance Details")

display_divisions = division_summary.sort_values(
    "Gross_Profit", ascending=False
).copy()

styled_divisions = (
    display_divisions.style
    .format({
        "Orders": "{:,.0f}",
        "Units_Sold": "{:,.0f}",
        "Revenue": "${:,.2f}",
        "Cost": "${:,.2f}",
        "Gross_Profit": "${:,.2f}",
        "Gross_Margin_%": "{:.2f}%",
        "Revenue_Contribution_%": "{:.2f}%",
        "Profit_Contribution_%": "{:.2f}%"
    })
    .set_properties(**{
        "background-color": "#241044",
        "color": "#F3E8FF",
        "border-color": "#4C267A",
        "text-align": "center"
    })
    .set_table_styles([
        {
            "selector": "th",
            "props": [
                ("background-color", "#4C1D95"),
                ("color", "#FFFFFF"),
                ("font-weight", "bold"),
                ("text-align", "center"),
                ("border", "1px solid #6D28D9")
            ]
        },
        {
            "selector": "td",
            "props": [
                ("padding", "10px"),
                ("border", "1px solid #4C267A")
            ]
        },
        {
            "selector": "table",
            "props": [
                ("border-collapse", "collapse"),
                ("width", "100%")
            ]
        }
    ])
)

st.dataframe(
    styled_divisions,
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
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(25,5,64,0.25)",
    font=dict(
        family="Arial",
        color="#E9DFFF",
        size=12
    ),
    title_font=dict(
        size=19,
        color="#FFFFFF"
    ),
    xaxis=dict(
        title="Product",
        showgrid=False,
        tickangle=-35,
        color="#D8B4FE"
    ),
    yaxis=dict(
        title="Percentage (%)",
        gridcolor="rgba(216,180,254,0.12)",
        color="#D8B4FE",
        zeroline=False
    ),
    legend=dict(
        title="Financial Metric",
        orientation="h",
        y=1.15,
        x=0
    ),
    margin=dict(l=25, r=25, t=90, b=100),
    height=500,
    bargap=0.25
    )

    fig_cost_margin.update_traces(
        marker_line_width=0,
        opacity=0.9
    )

    st.plotly_chart(fig_cost_margin, use_container_width=True)
    # Cost vs Sales Scatter Plot
    st.divider()
    st.subheader("Cost vs Sales — Product-Level Analysis")

    fig_cost_sales = px.scatter(
        diagnostics,
        x="Revenue",
        y="Cost",
        size="Units_Sold",
        color="Division",
        hover_name="Product Name",
        hover_data={
            "Revenue": ":,.2f",
            "Cost": ":,.2f",
            "Units_Sold": ":,.0f",
            "Gross_Profit": ":,.2f",
            "Gross_Margin_%": ":.2f",
            "Cost_to_Sales_%": ":.2f",
            "Division": True
        },
        size_max=38,
        color_discrete_sequence=[
            "#A78BFA",
            "#22C55E",
            "#F97316"
        ],
        title="Product Revenue vs Cost Distribution",
        labels={
            "Revenue": "Revenue",
            "Cost": "Total Cost",
            "Units_Sold": "Units Sold",
            "Division": "Product Division"
        }
    )

    fig_cost_sales.update_traces(
        marker=dict(
            opacity=0.85,
            line=dict(
                width=1,
                color="#E9DFFF"
            )
        )
    )

    fig_cost_sales.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(25,5,64,0.25)",
        font=dict(
            family="Arial",
            color="#E9DFFF",
            size=12
        ),
        title_font=dict(
            size=19,
            color="#FFFFFF"
        ),
        xaxis=dict(
            title="Revenue",
            showgrid=True,
            gridcolor="rgba(216,180,254,0.12)",
            color="#D8B4FE",
            zeroline=False
        ),
        yaxis=dict(
            title="Total Cost",
            showgrid=True,
            gridcolor="rgba(216,180,254,0.12)",
            color="#D8B4FE",
            zeroline=False
        ),
        legend=dict(
            title="Division",
            orientation="h",
            y=1.12,
            x=0
        ),
        margin=dict(l=25, r=25, t=90, b=60),
        height=520
    )

    st.plotly_chart(
        fig_cost_sales,
        use_container_width=True
    )


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

                .set_properties(
            **{
                "background-color": "#241044",
                "color": "#F3E8FF",
                "border-color": "#4C267A",
                "text-align": "center"
            }
        )
        .set_table_styles([
            {
                "selector": "th",
                "props": [
                    ("background-color", "#4C1D95"),
                    ("color", "#FFFFFF"),
                    ("font-weight", "bold"),
                    ("text-align", "center"),
                    ("border", "1px solid #6D28D9")
                ]
            },
            {
                "selector": "td",
                "props": [
                    ("padding", "10px"),
                    ("border", "1px solid #4C267A")
                ]
            },
            {
                "selector": "table",
                "props": [
                    ("border-collapse", "collapse"),
                    ("width", "100%")
                ]
            }
        ])
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
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(25,5,64,0.25)",
    font=dict(family="Arial", color="#E9DFFF", size=12),
    title_font=dict(size=19, color="#FFFFFF"),
    xaxis=dict(
        title="Product",
        showgrid=False,
        tickangle=-35,
        color="#D8B4FE"
    ),
    yaxis=dict(
        title="Cumulative Revenue (%)",
        range=[0, 105],
        gridcolor="rgba(216,180,254,0.12)",
        color="#D8B4FE",
        ticksuffix="%"
    ),
    margin=dict(l=25, r=25, t=75, b=100),
    height=480,
    showlegend=False
    )

    fig_revenue_pareto.update_traces(
        marker_line_width=0,
        opacity=0.9,
        hovertemplate="<b>%{x}</b><br>Cumulative Revenue: %{y:.2f}%<extra></extra>"
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
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(25,5,64,0.25)",
    font=dict(family="Arial", color="#E9DFFF", size=12),
    title_font=dict(size=19, color="#FFFFFF"),
    xaxis=dict(
        title="Product",
        showgrid=False,
        tickangle=-35,
        color="#D8B4FE"
    ),
    yaxis=dict(
        title="Cumulative Gross Profit (%)",
        range=[0, 105],
        gridcolor="rgba(216,180,254,0.12)",
        color="#D8B4FE",
        ticksuffix="%"
    ),
    margin=dict(l=25, r=25, t=75, b=100),
    height=480,
    showlegend=False
    )

    fig_profit_pareto.update_traces(
        marker_line_width=0,
        opacity=0.9,
        hovertemplate="<b>%{x}</b><br>Cumulative Gross Profit: %{y:.2f}%<extra></extra>"
    )

    st.plotly_chart(
        fig_profit_pareto,
        use_container_width=True
    )

    # Top products summary
    st.subheader("Revenue Pareto Details")

    revenue_details = revenue_pareto[
    [
        "Product Name",
        "Division",
        "Revenue",
        "Revenue_Contribution_%",
        "Cumulative_Revenue_%"
    ]
    ].copy()

    styled_revenue_details = (
        revenue_details.style
        .format({
            "Revenue": "${:,.2f}",
            "Revenue_Contribution_%": "{:.2f}%",
            "Cumulative_Revenue_%": "{:.2f}%"
        })
        .set_properties(**{
            "background-color": "#241044",
            "color": "#F3E8FF",
            "border-color": "#4C267A",
            "text-align": "center"
        })
        .set_table_styles([
            {
                "selector": "th",
                "props": [
                    ("background-color", "#4C1D95"),
                    ("color", "#FFFFFF"),
                    ("font-weight", "bold"),
                    ("text-align", "center"),
                    ("border", "1px solid #6D28D9")
                ]
            },
            {
                "selector": "td",
                "props": [
                    ("padding", "10px"),
                    ("border", "1px solid #4C267A")
                ]
            },
            {
                "selector": "table",
                "props": [
                    ("border-collapse", "collapse"),
                    ("width", "100%")
                ]
            }
        ])
    )

    st.dataframe(
        styled_revenue_details,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Gross Profit Pareto Details")

    profit_details = profit_pareto[
    [
        "Product Name",
        "Division",
        "Gross_Profit",
        "Profit_Contribution_%",
        "Cumulative_Profit_%"
    ]
    ].copy()

    styled_profit_details = (
        profit_details.style
        .format({
            "Gross_Profit": "${:,.2f}",
            "Profit_Contribution_%": "{:.2f}%",
            "Cumulative_Profit_%": "{:.2f}%"
        })
        .set_properties(**{
            "background-color": "#241044",
            "color": "#F3E8FF",
            "border-color": "#4C267A",
            "text-align": "center"
        })
        .set_table_styles([
            {
                "selector": "th",
                "props": [
                    ("background-color", "#4C1D95"),
                    ("color", "#FFFFFF"),
                    ("font-weight", "bold"),
                    ("text-align", "center"),
                    ("border", "1px solid #6D28D9")
                ]
            },
            {
                "selector": "td",
                "props": [
                    ("padding", "10px"),
                    ("border", "1px solid #4C267A")
                ]
            },
            {
                "selector": "table",
                "props": [
                    ("border-collapse", "collapse"),
                    ("width", "100%")
                ]
            }
        ])
    )

    st.dataframe(
        styled_profit_details,
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