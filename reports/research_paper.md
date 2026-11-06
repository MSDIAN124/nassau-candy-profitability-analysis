# Product Line Profitability & Margin Performance Analysis
## A Business Intelligence and Data Analytics Study of Nassau Candy Distributor

**Organization:** Unified Mentor  
**Project:** Nassau Candy Distributor  
**Analysis Period:** January 2024 – December 2025  
**Prepared as:** Data Analytics Research Paper  
**Currency:** Not independently verified; monetary figures are presented in the source dataset's numerical units.

---

## Abstract

This study examines product line profitability and gross margin performance using the Nassau Candy Distributor dataset. The analysis evaluates revenue, cost, gross profit, product-level margins, division-level performance, profit concentration, cost efficiency, and monthly gross margin trends.

The dataset contains 10,194 transaction-level records, 8,549 unique orders, 15 products, and three business divisions: Chocolate, Other, and Sugar. The overall recorded revenue was 141,783.63, total cost was 48,340.83, and gross profit was 93,442.80, resulting in a weighted gross margin of 65.91%.

The findings indicate a high concentration of financial contribution among a small group of products. Five products accounted for 92.88% of total revenue and 95.06% of total gross profit. The analysis also identified products requiring margin review, particularly Kazookles, which recorded a gross margin of 7.69%.

A data quality assessment identified repeated business-record patterns and unusually long differences between order and shipping dates. These observations were retained and documented rather than corrected without source-owner confirmation. A sensitivity analysis was also conducted to assess the potential financial impact of excluding duplicate candidate records.

The study provides data-driven observations and practical recommendations to support product portfolio evaluation, cost monitoring, pricing review, and profitability-focused business decisions.

**Keywords:** Product Profitability, Gross Margin, Revenue Analysis, Cost Analysis, Pareto Analysis, Division Performance, Data Quality, Business Intelligence, Data Analytics.

---

# 1. Introduction

## 1.1 Background

Profitability analysis is an important component of business performance management. Revenue alone does not provide a complete picture of financial performance because products generating high sales may also involve proportionately high costs.

Evaluating revenue alongside cost, gross profit, and gross margin helps businesses understand which products contribute most effectively to overall profitability. It also helps identify products that may require pricing, sourcing, or cost-allocation reviews.

The Nassau Candy Distributor dataset provides transaction-level information covering product sales, units sold, gross profit, cost, customer orders, business divisions, and geographical regions over the period January 2024 to December 2025.

This study uses the available data to evaluate product and division profitability and identify areas that may benefit from further management investigation.

## 1.2 Problem Statement

The business requires a structured profitability analysis to identify:

- Products generating the highest gross profit.
- Products with high revenue but comparatively weak margins.
- Profitability differences across business divisions.
- The concentration of revenue and gross profit among products.
- Products that may require cost or margin review.
- Monthly changes and variation in gross margin performance.
- Data quality issues that may influence financial reporting.

## 1.3 Objectives

The primary objectives of this study are:

1. Evaluate overall revenue, cost, gross profit, and gross margin.
2. Compare product-level profitability and margin performance.
3. Examine profitability across Chocolate, Other, and Sugar divisions.
4. Identify revenue and gross profit concentration using Pareto analysis.
5. Diagnose products with comparatively weak gross margins.
6. Evaluate monthly gross margin trends.
7. Assess the potential financial impact of duplicate candidate records.
8. Develop practical recommendations based on the observed findings.

## 1.4 Scope of the Study

The study focuses on the financial and product profitability dimensions of the supplied dataset. It covers 15 products across three divisions and uses transaction records dated from January 2024 through December 2025.

The analysis includes:

- Data quality assessment.
- Data preparation and validation.
- Exploratory data analysis.
- Financial KPI calculation.
- Product-level profitability analysis.
- Division-level performance analysis.
- Revenue and gross profit Pareto analysis.
- Cost and margin diagnostics.
- Duplicate sensitivity analysis.
- Monthly gross margin trend analysis.
- Interactive dashboard development.

The study evaluates recorded gross profitability and does not attempt to calculate complete operating or net profitability.

---

# 2. Data and Methodology

## 2.1 Dataset Description

The study uses the Nassau Candy Distributor dataset supplied as part of the Unified Mentor project.

The original dataset contains 10,194 rows and 18 columns, covering transaction-level sales and profitability information.

The following table presents selected fields relevant to the profitability analysis.

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

The dataset covers 15 products across three divisions: Chocolate, Other, and Sugar.

The recorded order date range is 2 January 2024 to 31 December 2025.

All monetary figures in this paper are reported in the numerical units provided by the source dataset. The currency denomination was not independently verified; therefore, no specific currency symbol is assigned.

## 2.2 Data Quality Assessment

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

These observations were treated as data quality concerns rather than automatically classified as confirmed source errors.

## 2.3 Data Preparation

The following preparation activities were performed:

1. Loaded the original CSV dataset using Python and Pandas.
2. Parsed Order Date and Ship Date into appropriate date formats.
3. Validated numeric fields for missing, zero, and negative values.
4. Verified the relationship between Sales, Cost, and Gross Profit.
5. Investigated duplicate candidates without automatically deleting them.
6. Generated derived fields for financial and time-based analysis.
7. Aggregated data for product, division, and monthly performance analysis.
8. Saved the prepared analytical dataset separately from the original source file.

The original dataset was preserved, while the processed dataset was used for subsequent analysis.

## 2.4 KPI Definitions

The study uses the following financial indicators.

### Total Revenue

Sum of recorded Sales values across the selected transactions.

\[
Total\ Revenue = \sum Sales
\]

### Total Cost

Sum of recorded Cost values across the selected transactions.

\[
Total\ Cost = \sum Cost
\]

### Gross Profit

Sum of recorded Gross Profit values across the selected transactions.

\[
Gross\ Profit = \sum Gross\ Profit
\]

### Gross Margin Percentage

Gross Margin represents the proportion of revenue retained as gross profit.

\[
Gross\ Margin\ (\%) =
\frac{Gross\ Profit}{Revenue}\times100
\]

### Profit per Unit

\[
Profit\ per\ Unit =
\frac{Gross\ Profit}{Units\ Sold}
\]

### Revenue Contribution

\[
Revenue\ Contribution\ (\%) =
\frac{Product\ Revenue}{Total\ Revenue}\times100
\]

### Gross Profit Contribution

\[
Gross\ Profit\ Contribution\ (\%) =
\frac{Product\ Gross\ Profit}{Total\ Gross\ Profit}\times100
\]

For aggregated analysis, gross margin is calculated using total gross profit divided by total revenue rather than taking a simple average of individual transaction margins.

For monthly trend analysis, the average monthly gross margin is calculated as the arithmetic mean of the individual monthly gross margin percentages. This is different from the overall portfolio gross margin, which uses aggregate gross profit divided by aggregate revenue.

## 2.5 Analytical Techniques and Tools

The following technologies and analytical techniques were used.

| Technique / Tool | Purpose |
|---|---|
| Python | Analytical programming |
| Pandas | Data preparation and aggregation |
| NumPy | Numerical calculations |
| Matplotlib | Exploratory visual analysis |
| Seaborn | Statistical data visualization |
| Plotly | Interactive charts |
| Streamlit | Interactive business dashboard |
| Descriptive statistics | Summary of financial performance |
| Grouped aggregation | Product and division comparisons |
| Pareto analysis | Revenue and profit concentration |
| Sensitivity analysis | Assessment of duplicate-candidate impact |
| Monthly trend analysis | Evaluation of gross margin movements |

## 2.6 Analytical Limitations

The findings are based on the supplied dataset and should be interpreted within its limitations.

- The validity of the 313 duplicate candidate rows could not be independently established.
- Unusually long Order Date–Ship Date differences require clarification from the source owner.
- The year embedded in Order IDs did not consistently match the corresponding Order Date year.
- Some products have very low transaction volumes, making their observed margins less representative.
- The dataset does not independently establish the reasons behind product cost or margin differences.
- The currency denomination was not independently verified.
- The analysis evaluates recorded gross profitability and does not include unprovided operating expenses, overheads, taxes, or other financial adjustments.

Consequently, the results should support further business investigation rather than be treated as definitive evidence for product discontinuation or operational decisions.

---

# 3. Results and Key Findings

## 3.1 Overall Business Performance

The overall analysis of 10,194 transaction records identified the following financial performance.

| Performance Indicator | Result |
|---|---:|
| Total Transaction Records | 10,194 |
| Total Orders | 8,549 |
| Total Units Sold | 38,654 |
| Total Revenue | 141,783.63 |
| Total Cost | 48,340.83 |
| Total Gross Profit | 93,442.80 |
| Weighted Gross Margin | 65.91% |

The business recorded a weighted gross margin of 65.91%, indicating that gross profit represented approximately 65.91% of recorded revenue.

The financial relationship between revenue, cost, and gross profit was consistent across the transaction records.

These results provide the baseline for evaluating differences across products and divisions.

## 3.2 Product-Level Profitability

Product-level analysis identified considerable differences in revenue generation and gross profit contribution.

The five leading products by gross profit were:

| Product | Gross Profit | Gross Margin |
|---|---:|---:|
| Wonka Bar - Scrumdiddlyumptious | 19,357.50 | 69.44% |
| Wonka Bar - Triple Dazzle Caramel | 18,610.20 | 65.33% |
| Wonka Bar - Milk Chocolate | 17,443.37 | 64.92% |
| Wonka Bar - Nutty Crunch Surprise | 16,819.95 | 71.35% |
| Wonka Bar - Fudge Mallows | 16,593.60 | 66.67% |

Scrumdiddlyumptious generated the highest gross profit among these products, while Nutty Crunch Surprise recorded the highest gross margin.

The results demonstrate that product performance should be assessed using both gross profit and gross margin. A product generating high gross profit is not necessarily the product with the highest margin percentage.

## 3.3 Products Requiring Margin Review

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

## 3.4 Division-Level Performance

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

## 3.5 Pareto Analysis – Revenue and Gross Profit Concentration

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

## 3.6 Cost and Margin Diagnostics

Cost-to-sales analysis was used to identify products where recorded costs consumed a comparatively large proportion of revenue.

Kazookles had the highest cost-to-sales ratio among the products reviewed, at 92.31%. Its gross margin was 7.69%.

The analysis also identified several products with gross margins below the overall portfolio margin of 65.91%.

These observations provide a basis for further investigation into product pricing, sourcing costs, and cost allocation. The dataset alone does not establish the underlying causes of these margin differences.

## 3.7 Duplicate Sensitivity Analysis

The duplicate sensitivity analysis compared two scenarios.

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

The weighted gross margin changed by approximately 0.05 percentage points when rounded to two decimal places.

This sensitivity assessment demonstrates that the candidate rows affect absolute financial totals, although the overall gross margin percentage remains relatively close between the two scenarios.

Scenario B is not treated as corrected financial data. All candidate records remain in the primary analysis pending confirmation from the source owner.

## 3.8 Monthly Gross Margin Performance

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

The average monthly gross margin of 65.88% represents the arithmetic mean of the 24 monthly percentages. It should not be confused with the overall weighted portfolio margin of 65.91%.

These observations describe historical performance and do not establish the reasons behind monthly changes.

---

# 4. Business Recommendations

Based on the analytical findings, the following recommendations are proposed.

## 4.1 Review Low-Margin Products

Kazookles should receive priority attention because its gross margin was only 7.69%.

Management should review its recorded purchase or production costs, selling price, and cost allocation before deciding on corrective action.

Other products with margins below the portfolio average should also be reviewed, while considering their transaction volumes and revenue contribution.

## 4.2 Protect High-Contribution Products

The five leading Chocolate products generated 92.88% of revenue and 95.06% of gross profit.

Management should monitor their sales performance, cost changes, and product availability. Any significant deterioration in these products could have a substantial effect on overall financial performance.

## 4.3 Investigate Division-Level Differences

The Other division recorded a gross margin of 44.84%, compared with 67.45% for Chocolate and 66.61% for Sugar.

A detailed review of product-level costs and pricing within the Other division could help identify potential improvement opportunities.

## 4.4 Improve Product-Level Monitoring

A regular profitability review should track:

- Revenue.
- Gross profit.
- Gross margin.
- Cost-to-sales ratio.
- Profit per unit.
- Product revenue contribution.
- Gross profit contribution.

Products with low transaction volumes should be evaluated over a longer period before making significant business decisions.

## 4.5 Validate Source Data

The 313 duplicate candidate rows and unusually long Order Date–Ship Date differences should be reviewed with the source data owner.

The mismatch between the year embedded in Order IDs and the corresponding Order Dates should also be investigated.

A documented validation process would improve confidence in future financial reporting.

## 4.6 Use Dashboard-Based Monitoring

The Streamlit dashboard can support recurring business reviews by allowing users to filter profitability results by date range, division, product, and minimum gross margin threshold.

Management can use these interactive views to identify changes in product and division performance more efficiently.

---

# 5. Conclusion

This study evaluated the product line profitability and gross margin performance of Nassau Candy Distributor using 10,194 transaction records covering January 2024 to December 2025.

The analysis recorded total revenue of 141,783.63, total cost of 48,340.83, gross profit of 93,442.80, and a weighted gross margin of 65.91%.

The findings identified Chocolate as the dominant division, contributing 92.88% of total revenue and 95.06% of total gross profit. Five products accounted for the same respective shares of portfolio revenue and gross profit, demonstrating substantial product-level financial concentration.

The analysis also highlighted Kazookles as a priority for margin review because of its 7.69% gross margin. The Other division recorded the lowest division-level gross margin at 44.84%.

Monthly gross margin remained relatively stable, with an average of 65.88% and a standard deviation of 0.53 percentage points.

The duplicate sensitivity analysis demonstrated that excluding 313 candidate rows affected absolute revenue and gross profit totals, while the weighted gross margin remained relatively close to the primary scenario.

Overall, the study demonstrates the importance of evaluating revenue, cost, gross profit, and gross margin together rather than relying on sales volume alone. The findings provide a structured basis for further product pricing, cost investigation, portfolio monitoring, data validation, and profitability-focused management decisions.

---

# 6. Study Limitations and Future Scope

The analysis is limited to the fields and historical period available in the supplied dataset. It does not include operating expenses, taxes, overhead allocations, or independently verified supplier and production cost information.

The currency denomination and the validity of duplicate candidate records could not be independently confirmed. The unusual shipping-date differences and Order ID year mismatches also require further clarification.

Future analysis could be improved through:

- Validation of duplicate candidate records with the source owner.
- Clarification of unusual shipping-date differences.
- Verification of Order ID and Order Date consistency.
- Access to verified supplier, production, and operating cost details.
- Longer-term monitoring of low-volume products.
- Additional analysis of customer-level profitability and regional performance, where appropriate data is available.
- Incorporation of operating expenses and overhead allocations to develop a broader profitability view.
- Regular monitoring of product and division KPIs through the interactive dashboard.

These extensions could provide a more comprehensive understanding of business profitability and support more informed management decisions.

---

# 7. References

1. Unified Mentor. (n.d.). *Nassau Candy Distributor dataset* [Project dataset provided as part of the internship project].

2. Python Software Foundation. (n.d.). *Python documentation*. https://docs.python.org/3/

3. pandas development team. (n.d.). *pandas documentation*. https://pandas.pydata.org/docs/

4. NumPy Developers. (n.d.). *NumPy documentation*. https://numpy.org/doc/

5. Matplotlib Development Team. (n.d.). *Matplotlib documentation*. https://matplotlib.org/stable/

6. seaborn development team. (n.d.). *seaborn documentation*. https://seaborn.pydata.org/

7. Plotly Technologies Inc. (n.d.). *Plotly Python documentation*. https://plotly.com/python/

8. Streamlit, Inc. (n.d.). *Streamlit documentation*. https://docs.streamlit.io/

---

# Appendix A: Project Deliverable

An interactive Streamlit dashboard was developed to present the profitability findings and support exploratory business analysis.

The dashboard includes four analytical modules:

1. Product Profitability Overview.
2. Division Performance Dashboard.
3. Cost vs Margin Diagnostics.
4. Profit Concentration Analysis.

The dashboard provides filters for date range, division, minimum gross margin, and product search.

**Project Repository:**  
https://github.com/MSDIAN124/nassau-candy-profitability-analysis

**Deployed Dashboard:**  
https://msdian124-nassau-candy-profitability-analysis-appapp-y4gioq.streamlit.app/

---

**End of Research Paper**