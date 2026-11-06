# 🍬 Product Line Profitability & Margin Performance Analysis

### Business Intelligence & Analytics Project | Nassau Candy Distributor

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white)](https://github.com/MSDIAN124/nassau-candy-profitability-analysis)

An end-to-end business analytics project focused on product profitability, gross margin performance, division-level contribution, cost efficiency, and revenue concentration. The project combines data quality assessment, KPI engineering, exploratory analysis, and an interactive Streamlit dashboard to translate business data into actionable insights.

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

This project analyzes product-level profitability, gross margin performance, division-level contribution, revenue concentration, and cost efficiency for Nassau Candy Distributor.

The primary objective is to identify high-performing products, investigate low-margin products, understand profitability differences across business divisions, and provide actionable recommendations through an interactive business intelligence dashboard.

The project follows an end-to-end analytics workflow:

**Data Auditing → Data Preparation → KPI Engineering → Exploratory Analysis → Business Insights → Dashboard Development**

## 2. Business Objectives

- Identify products generating the highest revenue and gross profit.
- Evaluate whether high-revenue products are also highly profitable.
- Compare revenue, cost, gross profit, and margins across business divisions.
- Identify products requiring margin and cost review.
- Analyze revenue and gross profit concentration using Pareto analysis.
- Examine monthly gross margin trends and volatility.
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
| Order Date Range | 02-Jan-2024 to 31-Dec-2025 |

**Data source:** Unified Mentor project dataset.

The raw dataset is maintained locally and excluded from public Git tracking.

## 4. Key Business Findings

### 4.1 Overall Financial Performance

| KPI | Result |
|---|---:|
| Total Revenue | 141,783.63 |
| Total Cost | 48,340.83 |
| Gross Profit | 93,442.80 |
| Gross Margin | 65.91% |
| Units Sold | 38,654 |
| Unique Orders | 8,549 |

### 4.2 Product Concentration

- Five out of fifteen products contribute **92.88% of total revenue**.
- These same five products contribute **95.06% of total gross profit**.
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

### 4.4 Margin Risk Analysis

- Kazookles has a gross margin of **7.69%**.
- Its cost-to-sales ratio is **92.31%**.
- Fun Dip, Nerds, SweeTARTS, and Lickable Wallpaper also have margins below the overall portfolio margin.

These products are flagged for further review rather than automatic discontinuation.

### 4.5 Monthly Performance

| Metric | Result |
|---|---:|
| Average Monthly Gross Margin | 65.88% |
| Monthly Margin Standard Deviation | 0.53 percentage points |
| Highest Monthly Margin | 66.75% (January 2025) |
| Lowest Monthly Margin | 64.54% (March 2024) |

Monthly gross margin remained relatively stable during the analyzed period.

---

## 5. Interactive Dashboard

The project includes an interactive Streamlit dashboard organized into four analytical modules.

### Module 1 — Product Profitability Overview

Analyzes product-level financial performance through:

- Revenue versus gross profit comparison.
- Gross margin by product.
- Highest gross profit product.
- Lowest margin product.
- Detailed product profitability table.

### Module 2 — Division Performance Dashboard

Evaluates performance across Chocolate, Other, and Sugar divisions through:

- Revenue comparison.
- Gross profit comparison.
- Gross margin comparison.
- Division-level financial summary table.

### Module 3 — Cost vs Margin Diagnostics

Identifies cost-efficiency issues and products requiring further review through:

- Cost versus margin comparison.
- Cost-to-sales analysis.
- Margin risk indicators.
- Detailed risk assessment table.

### Module 4 — Profit Concentration Analysis

Evaluates how revenue and gross profit are distributed across products using:

- Revenue contribution analysis.
- Gross profit contribution analysis.
- Cumulative contribution curves.
- 80% Pareto reference threshold.
- Product-level concentration tables.

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
| Plotly | Interactive business charts |
| Streamlit | Interactive dashboard development |
| SciPy & Scikit-learn | Supporting analytical tools |
| Git & GitHub | Version control and project management |

---

## 8. Repository Structure

```text
nassau-candy-profitability-analysis/
│
├── app/
│   └── app.py
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
│   ├── raw/
│   └── processed/
│
├── docs/
├── notebooks/
│
├── outputs/
│   └── figures/
│
├── reports/
│   ├── data_quality_audit.md
│   ├── executive_summary.md
│   └── research_paper.md
│
├── src/
├── tests/
│
├── .gitignore
├── README.md
└── requirements.txt
```

**Note:** Raw and processed datasets are excluded from Git tracking. The backup application file is also intentionally excluded from the project deliverables.

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

### Step 5 — Launch the Dashboard

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

Additional deliverables include:

- Interactive Streamlit dashboard.
- KPI engineering workflow.
- Custom dashboard icons.
- Product, division, cost, and profitability analysis.
- GitHub-hosted source code and documentation.

---

## 11. Data Quality & Analytical Limitations

The following considerations are documented to maintain analytical transparency:

- No missing values were identified in the original dataset.
- No exact duplicate rows or duplicate Row IDs were identified.
- **313 additional repeated business-record rows** were flagged as duplicate candidates and retained pending source-owner confirmation.
- Sensitivity analysis was performed to assess their potential impact.
- Unusually distant shipping dates and Order ID year inconsistencies were documented without modifying source values.
- Product-level margin thresholds are screening rules, not automatic discontinuation decisions.
- Some products have low transaction volumes, so their margins should be interpreted cautiously.
- The dataset does not independently establish the currency symbol; therefore, financial figures are presented without assigning a currency.

---

## 12. Quality Assurance

The completed dashboard underwent manual visual and functional verification.

| QA Area | Verification |
|---|---|
| Product Profitability | Both charts and product table verified |
| Division Performance | Three charts and division table verified |
| Cost vs Margin | Grouped bars and risk table verified |
| Profit Concentration | Both Pareto charts and 80% threshold verified |
| Dashboard Layout | No blank charts, overlapping labels, or horizontal scrolling observed |
| Sidebar Filters | Date, division, margin, and product search verified |
| Reset Filters | All filters successfully restored to default values |

**QA Status:** Manual dashboard verification completed successfully.

*Note: This status reflects manual UI and functional checks; it does not imply that an automated test suite has passed.*

---

## 13. Conclusion

This project demonstrates an end-to-end business analytics workflow, covering dataset auditing, KPI engineering, exploratory analysis, profitability assessment, interactive dashboard development, and business recommendations.

The analysis highlights:

- High product-level revenue and gross profit concentration.
- Differences in profitability across business divisions.
- Products requiring additional margin and cost investigation.
- Relatively stable monthly gross margin performance.

The interactive dashboard provides a practical way to explore business performance, investigate profitability patterns, and support data-informed decisions.

The project demonstrates practical application of Python, Pandas, Plotly, Streamlit, and business analytics techniques in a real-world-style profitability analysis scenario.

---

### 🔗 Project Repository

[**View Nassau Candy Profitability Analysis on GitHub**](https://github.com/MSDIAN124/nassau-candy-profitability-analysis)

**Project:** Product Line Profitability & Margin Performance Analysis  
**Organization:** Unified Mentor  
**Focus Areas:** Data Analytics | Business Intelligence | Profitability Analysis | Dashboard Development
