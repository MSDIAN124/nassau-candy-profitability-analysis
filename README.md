# Product Line Profitability & Margin Performance Analysis

**Business Analytics Project | Nassau Candy Distributor**

## 1. Project Overview

This project analyzes product-level profitability, gross margin performance, division-level contribution, revenue concentration, and cost efficiency for Nassau Candy Distributor.

The objective is to identify high-performing products, investigate low-margin products, understand profitability differences across divisions, and provide actionable recommendations through an interactive Streamlit dashboard.

## 2. Business Objectives

- Identify products generating the highest gross profit and gross margins.
- Evaluate whether high-revenue products are also highly profitable.
- Compare profitability across business divisions.
- Identify products requiring margin and cost review.
- Analyze revenue and gross profit concentration using Pareto analysis.
- Examine monthly gross margin trends and volatility.
- Build an interactive dashboard for business performance monitoring.

## 3. Dataset Overview

The analysis uses the official Unified Mentor project dataset for Nassau Candy Distributor.

| Attribute | Value |
|---|---:|
| Records | 10,194 |
| Columns | 18 original columns |
| Unique Orders | 8,549 |
| Products | 15 |
| Divisions | 3 |
| Regions | 4 |
| Order Date Range | 02-Jan-2024 to 31-Dec-2025 |

The raw dataset is maintained locally and is not included in this public repository.

## 4. Key Business Findings

### Overall Performance

| KPI | Result |
|---|---:|
| Revenue | 141,783.63 |
| Total Cost | 48,340.83 |
| Gross Profit | 93,442.80 |
| Gross Margin | 65.91% |
| Units Sold | 38,654 |
| Unique Orders | 8,549 |

### Product Concentration

- Five out of fifteen products contribute 92.88% of total revenue.
- The same five products contribute 95.06% of total gross profit.
- These five leading products belong to the Chocolate division.

### Division Performance

| Division | Revenue | Gross Profit | Gross Margin |
|---|---:|---:|---:|
| Chocolate | 131,692.90 | 88,824.62 | 67.45% |
| Other | 9,663.25 | 4,333.45 | 44.84% |
| Sugar | 427.48 | 284.73 | 66.61% |

Chocolate is the largest contributor to revenue and gross profit. The Other division has the lowest gross margin and warrants further investigation.

### Margin Risk

- Kazookles has a gross margin of 7.69%.
- Its cost-to-sales ratio is 92.31%.
- Fun Dip, Nerds, SweeTARTS, and Lickable Wallpaper also have margins below the overall portfolio margin.

These products are flagged for review, not automatic discontinuation.

### Monthly Performance

- Average monthly gross margin: 65.88%.
- Monthly margin standard deviation: 0.53 percentage points.
- Highest monthly margin: 66.75% (January 2025).
- Lowest monthly margin: 64.54% (March 2024).

## 5. Interactive Dashboard

The Streamlit application contains four analytical modules:

1. **Product Profitability Overview** — Product-level revenue, gross profit, and margin analysis.
2. **Division Performance Dashboard** — Comparison of revenue, cost, gross profit, and margins across divisions.
3. **Cost vs Margin Diagnostics** — Cost-to-sales ratios, margin classifications, and products requiring review.
4. **Profit Concentration Analysis** — Revenue and gross profit contribution with cumulative Pareto analysis.

### Dashboard Filters

- Order date range
- Division
- Minimum gross margin threshold
- Product search

## 6. Technology Stack

- **Python** — Core analysis and application development
- **Pandas & NumPy** — Data preparation and numerical analysis
- **Matplotlib & Seaborn** — Statistical visualization
- **Plotly** — Interactive charts
- **Streamlit** — Interactive dashboard
- **SciPy & Scikit-learn** — Supporting analytical tools
- **Git & GitHub** — Version control and project management

## 7. Repository Structure

```text
nassau-candy-profitability-analysis/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
├── notebooks/
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

Raw and processed datasets are excluded from Git tracking. The required source dataset must be placed locally in `data/raw/` before running the project scripts.

## 8. Installation and Setup

### Prerequisites

- Python 3.10 or later
- Git

### Clone the Repository

```bash
git clone https://github.com/MSDIAN124/nassau-candy-profitability-analysis.git
cd nassau-candy-profitability-analysis
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add the Dataset

Place the official project dataset at:

```text
data/raw/nassau_candy_distributor.csv
```

Run the KPI engineering script to generate the processed dataset:

```bash
python src/kpi_engineering.py
```

### Launch the Dashboard

```bash
python -m streamlit run app/app.py
```

The dashboard will open in your default browser.

## 9. Reports and Deliverables

The `reports/` directory contains:

- **data_quality_audit.md** — Dataset quality assessment, validation checks, and documented anomalies.
- **research_paper.md** — Detailed methodology, analysis, findings, and recommendations.
- **executive_summary.md** — Concise business-focused summary of results and priorities.

## 10. Data Quality and Analytical Limitations

- No missing values were identified in the original dataset.
- No exact duplicate rows or duplicate Row IDs were identified.
- 313 additional repeated business-record rows were flagged as duplicate candidates and retained pending source-owner confirmation.
- A sensitivity analysis was performed to assess their potential impact.
- Unusually distant shipping dates and Order ID year inconsistencies were documented without modifying source values.
- Product-level margin thresholds are screening rules, not automatic discontinuation decisions.
- Some products have low transaction volumes, so their margins should be interpreted cautiously.
- The dataset does not independently establish the currency symbol; financial figures are therefore presented without assigning a currency.

## 11. Conclusion

This project demonstrates an end-to-end business analytics workflow, from dataset auditing and KPI engineering to profitability analysis, interactive dashboard development, and business recommendations.

The findings highlight significant product concentration, differences in division-level profitability, and specific products requiring margin review. The dashboard provides a practical way to monitor these measures and support data-informed business decisions.

---

**Project Repository:** [MSDIAN124/nassau-candy-profitability-analysis](https://github.com/MSDIAN124/nassau-candy-profitability-analysis)