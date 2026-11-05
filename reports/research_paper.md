# Product Line Profitability & Margin Performance Analysis

**Project:** Nassau Candy Distributor  
**Organization:** Unified Mentor  
**Analysis Period:** January 2024 – December 2025  
**Prepared as:** Data Analytics Research Paper

---

## Abstract

This study examines product line profitability and gross margin performance using the Nassau Candy Distributor dataset. The analysis evaluates revenue, cost, gross profit, product-level margins, division-level performance, profit concentration, and monthly margin trends.

The dataset contains 10,194 transaction-level records, 8,549 unique orders, 15 products, and three divisions: Chocolate, Other, and Sugar. Overall recorded revenue was 141,783.63, gross profit was 93,442.80, and the weighted gross margin was 65.91%.

The findings indicate that profitability is concentrated in a small group of products. Five products contributed 92.88% of revenue and 95.06% of gross profit. The analysis also identifies products requiring margin review, particularly Kazookles, which recorded a gross margin of 7.69%.

The study provides data-driven observations and recommendations to support product portfolio review, cost monitoring, pricing evaluation, and profitability-focused business decisions.

## Keywords

Product Profitability, Gross Margin, Revenue Analysis, Cost Analysis, Pareto Analysis, Division Performance, Data Analytics, Nassau Candy Distributor

---

## 1. Introduction

### 1.1 Background

Profitability analysis is an important part of business performance management. Revenue alone does not provide a complete picture of financial performance because products with high sales may also have high associated costs. Therefore, evaluating gross profit and gross margin alongside revenue helps businesses understand which products contribute most effectively to profitability.

The Nassau Candy Distributor dataset provides transaction-level information covering product sales, units sold, gross profit, cost, customer orders, divisions, and geographical regions over the period January 2024 to December 2025.

### 1.2 Problem Statement

The business requires a structured analysis to identify:

- Products generating the highest gross profit.
- Products with high revenue but comparatively weak margins.
- Profitability differences across business divisions.
- The concentration of revenue and gross profit among products.
- Products that may require cost or margin review.
- Monthly changes and volatility in gross margin performance.

### 1.3 Objectives

The primary objectives of this study are:

1. Evaluate overall revenue, cost, gross profit, and gross margin.
2. Compare product-level profitability and margin performance.
3. Examine profitability across Chocolate, Other, and Sugar divisions.
4. Identify revenue and gross profit concentration using Pareto analysis.
5. Diagnose products with comparatively weak gross margins.
6. Evaluate monthly gross margin trends.
7. Develop practical recommendations based on the observed data.

### 1.4 Scope of the Study

The study focuses on the financial and product profitability dimensions of the supplied dataset. It covers 15 products across three divisions and uses transaction records dated from January 2024 through December 2025.

The analysis includes data quality assessment, exploratory data analysis, KPI engineering, product profitability, division performance, Pareto analysis, cost and margin diagnostics, and monthly performance analysis.

## 2. Data and Methodology

### 2.1 Dataset Description

The study uses the official Nassau Candy Distributor dataset provided as part of the Unified Mentor project.

The original dataset contains 10,194 rows and 18 columns, covering transaction-level sales and profitability information.

The principal fields include:

| Field | Description |
|---|---|
| Row ID | Unique transaction row identifier |
| Order ID | Order reference |
| Order Date | Date of order placement |
| Ship Date | Recorded shipping date |
| Customer ID | Customer reference |
| Division | Business division |
| Region | Sales region |
| Product ID | Product identifier |
| Product Name | Product description |
| Sales | Recorded sales value |
| Units | Quantity sold |
| Gross Profit | Recorded gross profit |
| Cost | Recorded product cost |

The dataset covers 15 products across three divisions: Chocolate, Other, and Sugar. The order date range is 2 January 2024 to 31 December 2025.

### 2.2 Data Quality Assessment

A structured data quality audit was performed before the financial analysis.

The major observations were:

- **Missing values:** No missing values were identified across the 18 original columns.
- **Exact duplicate rows:** No exact duplicate records were identified when all columns, including Row ID, were considered.
- **Row ID uniqueness:** No duplicate Row IDs were identified.
- **Financial consistency:** Sales minus Cost equalled Gross Profit across all transaction records.
- **Numeric validity:** Sales, Units, Gross Profit, and Cost contained no zero or negative values.
- **Product consistency:** Each product was associated with one Product ID and one division.

A further investigation identified 620 records that were identical across business fields except for Row ID. These records formed 307 groups, representing 313 additional repeated rows. All 313 candidate duplicate rows belonged to the Chocolate division.

These records were retained in the primary analysis because their validity could not be confirmed from the available source data. A separate sensitivity analysis was conducted to understand their possible financial impact.

The dataset also contained unusually long differences between Order Date and Ship Date, ranging from 904 to 1,642 days. These dates were preserved without correction because the underlying source information could not independently establish the correct shipping dates.

Additionally, the year embedded in Order IDs did not match the year of the corresponding Order Date. These values were preserved and documented rather than modified without source-owner confirmation.

### 2.3 Data Preparation

The following preparation activities were performed:

1. Loaded the original CSV dataset using Python and Pandas.
2. Parsed Order Date and Ship Date into appropriate date formats.
3. Validated numeric fields for missing, zero, and negative values.
4. Verified the relationship between Sales, Cost, and Gross Profit.
5. Investigated duplicate candidates without automatically deleting them.
6. Generated derived fields for financial and time-based analysis.
7. Saved the prepared analytical dataset separately from the original source file.

The original dataset was preserved, while the processed dataset was used for subsequent analysis.

### 2.4 KPI Definitions

The study uses the following financial indicators:

**Total Revenue**

Sum of recorded Sales values across the selected transactions.

**Total Cost**

Sum of recorded Cost values across the selected transactions.

**Gross Profit**

Sum of recorded Gross Profit values across the selected transactions.

**Gross Margin Percentage**

Gross Margin represents the proportion of revenue retained as gross profit.

\[
Gross\ Margin\ (\%) =
\frac{Gross\ Profit}{Revenue}\times100
\]

**Profit per Unit**

\[
Profit\ per\ Unit =
\frac{Gross\ Profit}{Units\ Sold}
\]

**Revenue Contribution**

\[
Revenue\ Contribution\ (\%) =
\frac{Product\ Revenue}{Total\ Revenue}\times100
\]

**Gross Profit Contribution**

\[
Profit\ Contribution\ (\%) =
\frac{Product\ Gross\ Profit}{Total\ Gross\ Profit}\times100
\]

For aggregated analysis, gross margin is calculated using total gross profit divided by total revenue rather than taking a simple average of individual transaction margins.

### 2.5 Analytical Techniques and Tools

The following techniques and technologies were used:

| Technique / Tool | Purpose |
|---|---|
| Python | Analytical programming |
| Pandas | Data preparation and aggregation |
| NumPy | Numerical calculations |
| Matplotlib / Seaborn | Exploratory visual analysis |
| Plotly | Interactive charts |
| Streamlit | Interactive business dashboard |
| Descriptive statistics | Summary of financial performance |
| Grouped aggregation | Product and division comparisons |
| Pareto analysis | Revenue and profit concentration |
| Sensitivity analysis | Assessment of duplicate-candidate impact |
| Monthly trend analysis | Evaluation of gross margin movements |

### 2.6 Analytical Limitations

The findings are based on the supplied dataset and should be interpreted within its limitations.

- The validity of the 313 duplicate candidate rows could not be independently established.
- Unusually long Order Date–Ship Date differences require clarification from the source owner.
- Some products have very low transaction volumes, making their observed margins less representative.
- The dataset does not independently establish the reasons behind product cost or margin differences.
- The analysis evaluates recorded gross profitability and does not include unprovided operating expenses, overheads, taxes, or other financial adjustments.

Consequently, the results should support further business investigation rather than be treated as definitive evidence for product discontinuation or operational decisions.

## 3. Results and Key Findings

### 3.1 Overall Business Performance

The overall analysis of 10,194 transaction records identified the following financial performance:

| Performance Indicator | Result |
|---|---:|
| Total Orders | 8,549 |
| Total Units Sold | 38,654 |
| Total Revenue | 141,783.63 |
| Total Cost | 48,340.83 |
| Total Gross Profit | 93,442.80 |
| Weighted Gross Margin | 65.91% |

The business recorded a weighted gross margin of 65.91%, indicating that gross profit represented approximately 65.91% of recorded revenue.

These results provide the baseline for evaluating differences across products and divisions.

### 3.2 Product-Level Profitability

Product-level analysis identified considerable differences in revenue generation and gross profit contribution.

The five leading products by gross profit were:

| Product | Gross Profit | Gross Margin |
|---|---:|---:|
| Wonka Bar - Scrumdiddlyumptious | 19,357.50 | 69.44% |
| Wonka Bar - Triple Dazzle Caramel | 18,610.20 | 65.33% |
| Wonka Bar - Milk Chocolate | 17,443.37 | 64.92% |
| Wonka Bar - Nutty Crunch Surprise | 16,819.95 | 71.35% |
| Wonka Bar - Fudge Mallows | 16,593.60 | 66.67% |

Scrumdiddlyumptious generated the highest gross profit, while Nutty Crunch Surprise recorded the highest gross margin among these five products.

The results demonstrate that product performance should be assessed using both gross profit and gross margin. A product generating high gross profit is not necessarily the product with the highest margin percentage.

### 3.3 Products Requiring Margin Review

The analysis identified products with comparatively low gross margins.

| Product | Revenue | Gross Profit | Gross Margin |
|---|---:|---:|---:|
| Kazookles | 1,205.75 | 92.75 | 7.69% |
| Fun Dip | 12.00 | 4.80 | 40.00% |
| Nerds | 15.00 | 7.00 | 46.67% |
| SweeTARTS | 61.50 | 28.70 | 46.67% |
| Lickable Wallpaper | 7,860.00 | 3,930.00 | 50.00% |

Kazookles requires particular attention because its recorded cost represented approximately 92.31% of revenue, leaving a gross margin of only 7.69%.

Lickable Wallpaper also merits review because of its relatively low 50% gross margin despite generating substantially higher revenue than several other low-margin products.

Products such as Fun Dip, Nerds, and SweeTARTS have relatively small transaction volumes. Their observed margins should therefore be interpreted cautiously.

The margin categories used in the dashboard are analytical screening thresholds, not automatic product discontinuation decisions.

### 3.4 Division-Level Performance

The division-level analysis revealed differences in revenue contribution, gross profit, and gross margin.

| Division | Revenue | Gross Profit | Gross Margin |
|---|---:|---:|---:|
| Chocolate | 131,692.90 | 88,824.62 | 67.45% |
| Other | 9,663.25 | 4,333.45 | 44.84% |
| Sugar | 427.48 | 284.73 | 66.61% |

Chocolate was the largest division by both revenue and gross profit. It contributed approximately 92.88% of total revenue and 95.06% of total gross profit.

Sugar recorded a gross margin of 66.61%, which was close to the overall portfolio margin. However, its contribution to total revenue was only approximately 0.30%.

The Other division recorded the lowest gross margin at 44.84%. This indicates an opportunity to investigate its product-level cost and pricing structure.

The results suggest that division performance should be evaluated using both absolute financial contribution and margin percentage.

### 3.5 Pareto Analysis – Revenue and Gross Profit Concentration

Pareto analysis was conducted to evaluate how much of the portfolio's revenue and gross profit was generated by a relatively small number of products.

The results were:

| Indicator | Revenue | Gross Profit |
|---|---:|---:|
| Total Products | 15 | 15 |
| Products Required to Exceed 80% Contribution | 5 | 5 |
| Contribution of Top 5 Products | 92.88% | 95.06% |

Only five of the fifteen products were required to exceed the 80% contribution threshold for both revenue and gross profit.

This indicates a high level of product-level financial concentration. The five leading products were all Chocolate products.

The findings suggest that the business should monitor the performance and availability of these leading products carefully. However, concentration alone does not establish that the remaining products should be discontinued.

### 3.6 Cost and Margin Diagnostics

Cost-to-sales analysis was used to identify products where recorded costs consumed a comparatively large proportion of revenue.

Kazookles had the highest cost-to-sales ratio among the products reviewed, at 92.31%. Its gross margin was 7.69%.

The analysis also identified several products with gross margins below the overall portfolio margin of 65.91%.

These observations provide a basis for further investigation into product pricing, sourcing costs, and cost allocation. The dataset alone does not establish the underlying causes of these margin differences.

### 3.7 Duplicate Sensitivity Analysis

The duplicate sensitivity analysis compared two scenarios:

- **Scenario A:** All 10,194 original records retained.
- **Scenario B:** 313 additional duplicate candidate rows excluded for sensitivity assessment only.

| Indicator | Scenario A | Scenario B |
|---|---:|---:|
| Records | 10,194 | 9,881 |
| Revenue | 141,783.63 | 138,284.12 |
| Cost | 48,340.83 | 47,207.71 |
| Gross Profit | 93,442.80 | 91,076.41 |
| Gross Margin | 65.91% | 65.86% |

Excluding the candidate rows reduced recorded revenue by 3,499.51 and gross profit by 2,366.39.

The weighted gross margin changed by approximately 0.04 percentage points.

This sensitivity assessment demonstrates that the candidate rows affect absolute financial totals, although the overall gross margin percentage remains relatively close between the two scenarios.

Scenario B is not treated as corrected financial data. All candidate records remain in the primary analysis pending confirmation from the source owner.

### 3.8 Monthly Gross Margin Performance

Monthly analysis was conducted across 24 months, covering January 2024 to December 2025.

The key findings were:

| Indicator | Result |
|---|---:|
| Number of Months | 24 |
| Average Monthly Gross Margin | 65.88% |
| Standard Deviation | 0.53 percentage points |
| Highest Monthly Gross Margin | 66.75% |
| Highest Margin Month | January 2025 |
| Lowest Monthly Gross Margin | 64.54% |
| Lowest Margin Month | March 2024 |
| Gross Margin Range | 2.21 percentage points |

The monthly gross margin remained within a relatively narrow range throughout the analysis period.

The standard deviation of approximately 0.53 percentage points indicates limited variation in monthly gross margin. January 2025 recorded the highest monthly margin, while March 2024 recorded the lowest.

These observations describe historical performance and do not establish the reasons behind monthly changes.

## 4. Business Recommendations

Based on the analytical findings, the following recommendations are proposed.

### 4.1 Review Low-Margin Products

Kazookles should receive priority attention because its gross margin was only 7.69%. Management should review its recorded purchase or production costs, selling price, and cost allocation before deciding on corrective action.

Other products with margins below the portfolio average should also be reviewed.

### 4.2 Protect High-Contribution Products

The five leading Chocolate products generated 92.88% of revenue and 95.06% of gross profit.

Management should monitor their sales performance, cost changes, and product availability. Any significant deterioration in these products could have a substantial effect on overall financial performance.

### 4.3 Investigate Division-Level Differences

The Other division recorded a gross margin of 44.84%, compared with 67.45% for Chocolate and 66.61% for Sugar.

A detailed review of product-level costs and pricing within the Other division could help identify potential improvement opportunities.

### 4.4 Improve Product-Level Monitoring

A regular profitability review should track revenue, gross profit, gross margin, cost-to-sales ratio, and profit per unit.

Products with low transaction volumes should be evaluated over a longer period before making significant business decisions.

### 4.5 Validate Source Data

The 313 duplicate candidate rows and unusually long Order Date–Ship Date differences should be reviewed with the source data owner.

A documented validation process would improve confidence in future financial reporting.

### 4.6 Use Dashboard-Based Monitoring

The Streamlit dashboard can support recurring business reviews by allowing users to filter profitability results by date range, division, product, and minimum margin threshold.

Management can use these interactive views to identify changes in product and division performance more efficiently.

## 5. Conclusion

This study evaluated the product line profitability and gross margin performance of Nassau Candy Distributor using 10,194 transaction records covering January 2024 to December 2025.

The analysis recorded total revenue of 141,783.63, gross profit of 93,442.80, and a weighted gross margin of 65.91%.

The findings identified Chocolate as the dominant division, contributing 92.88% of total revenue and 95.06% of total gross profit. Five products accounted for the same respective shares of portfolio revenue and gross profit, demonstrating substantial product-level concentration.

The analysis also highlighted Kazookles as a priority for margin review because of its 7.69% gross margin. Monthly gross margin remained relatively stable, with an average of 65.88% and a standard deviation of 0.53 percentage points.

Overall, the study demonstrates the importance of evaluating revenue, cost, gross profit, and gross margin together rather than relying on sales volume alone. The findings provide a structured basis for further product pricing, cost investigation, portfolio monitoring, and profitability-focused management decisions.

## 6. Study Limitations and Future Scope

The analysis is limited to the fields and historical period available in the supplied dataset. It does not include operating expenses, taxes, overhead allocations, or independently verified supplier and production cost information.

Future analysis could be improved through:

- Validation of duplicate candidate records with the source owner.
- Clarification of unusual shipping-date differences.
- Access to verified supplier, production, and operating cost details.
- Longer-term monitoring of low-volume products.
- Additional analysis of customer-level profitability and regional performance, where appropriate data is available.

These extensions could provide a more comprehensive understanding of business profitability and support more informed management decisions.

---

**End of Research Paper**