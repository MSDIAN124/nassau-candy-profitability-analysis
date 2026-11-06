# 🍬 Product Line Profitability & Margin Performance Analysis

### Business Intelligence & Analytics Project | Nassau Candy Distributor

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white)](https://github.com/MSDIAN124/nassau-candy-profitability-analysis)

An end-to-end business analytics project focused on product profitability, gross margin performance, division-level contribution, cost efficiency, geographic profitability, and revenue concentration. The project combines data quality assessment, KPI engineering, exploratory analysis, supplementary analytical outputs, and an interactive Streamlit dashboard to translate business data into actionable insights.

---

## 📌 Table of Contents

1. [Project Overview](#1-project-overview)
2. [Business Objectives](#2-business-objectives)
3. [Dataset Overview](#3-dataset-overview)
4. [Key Business Findings](#4-key-business-findings)
5. [Interactive Dashboard](#5-interactive-dashboard)
6. [Dashboard Design & User Experience](#6-dashboard-design--user-experience)
7. [Technology Stack](#7-technology-stack)
8. [Repository Structure](#8-repository-structure)
9. [Installation & Setup](#9-installation--setup)
10. [Reports & Deliverables](#10-reports--deliverables)
11. [Data Quality & Analytical Limitations](#11-data-quality--analytical-limitations)
12. [Quality Assurance](#12-quality-assurance)
13. [Conclusion](#13-conclusion)

---

## 1. Project Overview

This project analyzes product-level profitability, gross margin performance, division-level contribution, revenue concentration, cost efficiency, and geographic profitability for Nassau Candy Distributor.

The primary objective is to identify high-performing products, investigate low-margin products, understand profitability differences across business divisions and regions, and provide actionable recommendations through an interactive business intelligence dashboard.

The project follows an end-to-end analytics workflow:

**Data Auditing → Data Preparation → KPI Engineering → Exploratory Analysis → Profitability & Concentration Analysis → Dashboard Development → Business Recommendations**

## 2. Business Objectives

- Identify products generating the highest revenue and gross profit.
- Evaluate whether high-revenue products are also highly profitable.
- Compare revenue, cost, gross profit, and margins across business divisions.
- Calculate product-level profit per unit.
- Identify products requiring margin and cost review.
- Analyze the relationship between product revenue and cost.
- Analyze revenue and gross profit concentration using Pareto analysis.
- Examine monthly gross margin trends and volatility.
- Evaluate regional and state-wise profitability distribution.
- Develop an interactive dashboard for business performance monitoring.
- Translate analytical findings into practical business recommendations.

## 3. Dataset Overview

The analysis uses the official Unified Mentor project dataset for Nassau Candy Distributor.

| Attribute | Value |
|---|---:|
| Total Records | 10,194 |
| Original Columns | 18 |
| Unique Orders | 8,549 |
| Products | 15 |
| Business Divisions | 3 |
| Regions | 4 |
| States / Provinces | 59 |
| Order Date Range | 02-Jan-2024 to 31-Dec-2025 |

**Data source:** Unified Mentor project dataset.

The raw dataset is maintained locally and excluded from public Git tracking. Processed datasets are also excluded from Git tracking.

## 4. Key Business Findings

### 4.1 Overall Financial Performance

| KPI | Result |
|---|---:|
| Total Revenue | 141,783.63 |
| Total Cost | 48,340.83 |
| Gross Profit | 93,442.80 |
| Weighted Gross Margin | 65.91% |
| Units Sold | 38,654 |
| Unique Orders | 8,549 |

### 4.2 Product Concentration — Pareto Analysis

- Five out of fifteen products contribute **92.88% of total revenue**.
- These same five products contribute **95.06% of total gross profit**.
- Five products are sufficient to cross the 80% threshold for both revenue and gross profit.
- All five leading products belong to the Chocolate division.

**Business implication:** Revenue and profitability are highly concentrated among a small group of products. Their availability, pricing, and cost structure deserve close monitoring.

### 4.3 Division Performance

| Division | Revenue | Gross Profit | Gross Margin |
|---|---:|---:|---:|
| Chocolate | 131,692.90 | 88,824.62 | 67.45% |
| Other | 9,663.25 | 4,333.45 | 44.84% |
| Sugar | 427.48 | 284.73 | 66.61% |

Chocolate is the largest contributor to revenue and gross profit.

The Other division has the lowest gross margin and warrants further investigation into product mix, pricing, and cost efficiency.

### 4.4 Margin Risk & Product Cost Diagnostics

- Kazookles has a gross margin of **7.69%**.
- Its cost-to-sales ratio is **92.31%**.
- Fun Dip, Nerds, SweeTARTS, and Lickable Wallpaper also have comparatively low margins.

Product-level cost and sales analysis provides additional visibility into differences in cost structures across the 15 products.

These products are flagged for further review rather than automatic discontinuation. Profit per unit is also calculated to support product-level profitability assessment.

### 4.5 Monthly Gross Margin Performance

| Metric | Result |
|---|---:|
| Analysis Period | 24 months |
| Average Monthly Gross Margin | 65.88% |
| Monthly Margin Standard Deviation | 0.53 percentage points |
| Highest Monthly Margin | 66.75% (January 2025) |
| Lowest Monthly Margin | 64.54% (March 2024) |

Monthly gross margin remained relatively stable during the analyzed period. The standard deviation represents variation across monthly gross margin percentages.

### 4.6 Geographic Profitability

Geographic profitability was evaluated across four regions and 59 states/provinces.

| Region | Revenue | Gross Profit | Gross Margin |
|---|---:|---:|---:|
| Pacific | 46,301.53 | 30,485.94 | 65.84% |
| Atlantic | 41,197.24 | 26,973.70 | 65.47% |
| Interior | 32,037.60 | 21,282.49 | 66.43% |
| Gulf | 22,247.26 | 14,700.67 | 66.08% |

Key observations:

- Pacific contributed the highest regional revenue at 32.66%.
- Interior recorded the highest regional gross margin at 66.43%.
- Atlantic recorded the lowest regional gross margin at 65.47%.
- California was the highest-revenue state, contributing 19.69% of total revenue.

Regional gross margins were relatively consistent, ranging from 65.47% to 66.43%.

This analysis evaluates geographic profitability distribution; it does not establish shipping congestion or delivery efficiency.

---

## 5. Interactive Dashboard

The project includes an interactive Streamlit dashboard organized into four analytical modules.

### Module 1 — Product Profitability Overview

Analyzes product-level financial performance through:

- Revenue versus gross profit comparison.
- Gross margin by product.
- Highest gross profit product.
- Lowest margin product.
- Product-level profit per unit.
- Detailed product profitability table.

### Module 2 — Division Performance Dashboard

Evaluates performance across Chocolate, Other, and Sugar divisions through:

- Revenue comparison.
- Gross profit comparison.
- Gross margin comparison.
- Division-level financial summary table.

### Module 3 — Cost vs Margin Diagnostics

Identifies cost-efficiency issues and products requiring further review through:

- Cost-to-sales versus gross margin comparison.
- **Interactive Cost vs Sales Scatter Plot.**
- Product-level cost and revenue distribution.
- Bubble size representing units sold.
- Division-based bubble color.
- Hover details for product revenue, cost, gross profit, gross margin, and cost-to-sales ratio.
- Margin risk indicators.
- Detailed product risk assessment table.

### Module 4 — Profit Concentration Analysis

Evaluates how revenue and gross profit are distributed across products using:

- Revenue contribution analysis.
- Gross profit contribution analysis.
- Cumulative contribution curves.
- 80% Pareto reference threshold.
- Product-level concentration tables.
- Product-count indicators for reaching 80% revenue and gross profit contribution.

### Interactive Dashboard Filters

Users can dynamically customize the analysis using:

| Filter | Function |
|---|---|
| Order Date Range | Select the analysis period |
| Business Division | Focus on selected divisions |
| Minimum Gross Margin | Apply a margin threshold |
| Product Search | Search for specific products |
| Reset Filters | Restore all filters to their default values |

---

## 6. Dashboard Design & User Experience

The dashboard includes a custom visual design intended to make financial insights easier to interpret.

### Visual Design Features

- Dark purple dashboard theme with a subtle blurred candy-themed background.
- Glassmorphism-inspired KPI cards.
- Custom financial icons for key performance indicators.
- Consistent chart styling and readable labels.
- Interactive Plotly visualizations.
- Dark-styled tables with clear headers and financial formatting.
- Responsive sidebar filter panel.
- Reset Filters functionality for restoring the default dashboard view.

### KPI Cards

The Executive Overview highlights five core performance indicators:

1. Total Revenue
2. Gross Profit
3. Total Cost
4. Gross Margin
5. Total Orders

The dashboard also displays additional operational context, including units sold and records analyzed.

---

## 7. Technology Stack

| Technology | Application |
|---|---|
| Python | Core analysis and application development |
| Pandas | Data cleaning, transformation, and aggregation |
| NumPy | Numerical analysis |
| Matplotlib & Seaborn | Supporting statistical visualizations |
| Plotly | Interactive business charts and scatter plots |
| Streamlit | Interactive dashboard development |
| SciPy & Scikit-learn | Supporting analytical tools |
| Git & GitHub | Version control and project management |

---

## 8. Repository Structure

```text
nassau-candy-profitability-analysis/
│
├── app/
│   ├── app.py
│   └── app_PreDesignBackup.py       # Local backup; not a deliverable
│
├── assets/
│   └── icons/
│       ├── gross_margin.png
│       ├── gross_profit.png
│       ├── total_cost.png
│       ├── total_orders.png
│       └── total_revenue.png
│
├── data/
│   ├── raw/                         # Excluded from Git
│   └── processed/                   # Excluded from Git
│
├── docs/
├── notebooks/
│
├── outputs/
│   └── figures/
│       └── cost_vs_sales_scatter.html
│
├── reports/
│   ├── data_quality_audit.md
│   ├── executive_summary.md
│   └── research_paper.md
│
├── src/
│   ├── audit_day1.py
│   ├── cost_margin_diagnostics.py
│   ├── division_analysis.py
│   ├── duplicate_sensitivity.py
│   ├── eda_day1.py
│   ├── geographic_and_cost_analysis.py
│   ├── investigate_duplicates.py
│   ├── investigate_exact_duplicates.py
│   ├── investigate_orders.py
│   ├── investigate_products.py
│   ├── kpi_engineering.py
│   ├── monthly_margin_analysis.py
│   ├── pareto_analysis.py
│   ├── product_profitability.py
│   └── verify_full_duplicates.py
│
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

**Note:** Raw and processed datasets are excluded from Git tracking. The local backup application file is intentionally excluded from the project deliverables.

---

## 9. Installation & Setup

### Prerequisites

- Python 3.10 or later
- Git
- Official project dataset

### Step 1 — Clone the Repository

```bash
git clone https://github.com/MSDIAN124/nassau-candy-profitability-analysis.git

cd nassau-candy-profitability-analysis
```

### Step 2 — Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Add the Dataset

Place the official dataset in the following location:

```text
data/raw/nassau_candy_distributor.csv
```

Generate the processed KPI dataset using:

```bash
python src/kpi_engineering.py
```

### Step 5 — Run Supplementary Analysis (Optional)

Run the analysis scripts when their required processed input files are available:

```bash
python src/monthly_margin_analysis.py
python src/pareto_analysis.py
python src/geographic_and_cost_analysis.py
```

The supplementary scripts generate analytical CSV outputs and an interactive HTML scatter plot.

### Step 6 — Launch the Dashboard

```bash
python -m streamlit run app/app.py
```

The dashboard will open in your default browser.

---

## 10. Reports & Deliverables

The `reports/` directory contains three supporting analytical documents.

| Report | Description |
|---|---|
| `data_quality_audit.md` | Dataset quality assessment, validation checks, and documented anomalies |
| `executive_summary.md` | Concise business-focused summary of findings and priorities |
| `research_paper.md` | Detailed methodology, analysis, findings, and recommendations |

Additional analytical deliverables include:

- Interactive Streamlit dashboard.
- KPI engineering workflow.
- Custom dashboard icons.
- Product-level profitability and profit-per-unit analysis.
- Product cost versus sales analysis.
- Interactive Cost vs Sales Scatter Plot.
- Region-wise profitability analysis.
- State-wise profitability analysis.
- Monthly gross margin and volatility analysis.
- Revenue and gross profit Pareto analysis.
- Supporting CSV reports and interactive HTML visualization.

---

## 11. Data Quality & Analytical Limitations

The following considerations are documented to maintain analytical transparency:

- No missing values were identified across the 18 original dataset columns.
- No exact duplicate rows or duplicate Row IDs were identified.
- No zero or negative Sales, Units, Gross Profit, or Cost values were identified.
- All rows satisfy `Sales - Cost = Gross Profit` within the 0.01 tolerance.
- **313 additional repeated business-record rows** were flagged as duplicate candidates and retained pending source-owner confirmation.
- Sensitivity analysis was performed to assess their potential impact.
- Repeated Order IDs are not automatically treated as duplicate transactions because an order can contain multiple product records.
- Shipping dates are unusually distant from order dates. The calculated shipping-date gaps range from 904 to 1,642 days, with a median of 1,274 days.
- All 10,194 records have calculated shipping-date gaps exceeding 365 days. These values should not be interpreted as actual delivery performance.
- Order ID year inconsistencies were documented without modifying source values.
- Original source records and dates were preserved; no unsupported corrections or deletions were applied.
- Product-level margin thresholds are screening rules, not automatic discontinuation decisions.
- Some products have low transaction volumes, so their margins should be interpreted cautiously.
- The dataset does not independently establish the currency symbol; therefore, financial figures are presented without assigning a currency.
- Geographic profitability analysis does not establish shipping congestion, delivery delays, or route efficiency. Shipment-level operational evidence would be required for those conclusions.

---

## 12. Quality Assurance

The completed dashboard underwent manual visual and functional verification.

| QA Area | Verification |
|---|---|
| Product Profitability | Both charts and product table verified |
| Division Performance | Three charts and division table verified |
| Cost vs Margin | Grouped bars, scatter plot, and risk table verified |
| Scatter Plot | Product bubbles, hover details, and filters verified |
| Profit Concentration | Both Pareto charts and 80% threshold verified |
| Dashboard Layout | No blank charts, overlapping labels, or horizontal scrolling observed |
| Sidebar Filters | Date, division, margin, and product search verified |
| Reset Filters | All filters successfully restored to default values |

**QA Status:** Manual dashboard verification completed successfully.

*Note: This status reflects manual UI and functional checks; it does not imply that an automated test suite has passed.*

---

## 13. Conclusion

This project demonstrates an end-to-end business analytics workflow, covering dataset auditing, KPI engineering, exploratory analysis, product and division profitability assessment, cost diagnostics, geographic profitability, concentration analysis, interactive dashboard development, and business recommendations.

The analysis highlights:

- High product-level revenue and gross profit concentration among five Chocolate products.
- Differences in profitability across business divisions.
- Products requiring additional margin and cost investigation.
- Relatively stable monthly gross margin performance.
- Geographic differences in revenue contribution, with relatively consistent regional gross margins.
- The importance of monitoring product-level cost structures and portfolio concentration.

The interactive dashboard and supplementary analytical reports provide practical tools to explore business performance, investigate profitability patterns, and support data-informed product and portfolio decisions.

The results should be interpreted in the context of the available dataset and its documented limitations. Further source-data validation and more detailed operational cost information would strengthen future decision-making.

---

### 🔗 Project Repository

[**View Nassau Candy Profitability Analysis on GitHub**](https://github.com/MSDIAN124/nassau-candy-profitability-analysis)

**Project:** Product Line Profitability & Margin Performance Analysis  
**Organization:** Unified Mentor  
**Focus Areas:** Data Analytics | Business Intelligence | Profitability Analysis | Dashboard Development