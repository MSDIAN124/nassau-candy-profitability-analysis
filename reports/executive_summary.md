# Executive Summary
## Product Line Profitability & Margin Performance Analysis
**Organization:** Unified Mentor  
**Business:** Nassau Candy Distributor  
**Analysis Period:** January 2024 – December 2025

---

## 1. Project Overview

This project evaluates the product line profitability and gross margin performance of Nassau Candy Distributor using transaction-level sales data covering January 2024 to December 2025.

The objective was to identify the products and divisions contributing most to financial performance, highlight products requiring margin review, and provide evidence-based recommendations for improving profitability monitoring.

The analysis used Python, Pandas, data quality validation, exploratory data analysis, financial KPI calculations, Pareto analysis, and an interactive Streamlit dashboard.

## 2. Key Financial Performance

The dataset contains 10,194 transaction records representing 8,549 unique orders.

| Key Performance Indicator | Result |
|---|---:|
| Total Revenue | 141,783.63 |
| Total Cost | 48,340.83 |
| Gross Profit | 93,442.80 |
| Weighted Gross Margin | 65.91% |
| Total Orders | 8,549 |
| Units Sold | 38,654 |
| Products Analyzed | 15 |
| Divisions Analyzed | 3 |

The overall weighted gross margin was 65.91%, providing a baseline for evaluating individual product and division performance.

## 3. Major Findings

### 3.1 Product Concentration

Five of the fifteen products contributed:

- 92.88% of total revenue.
- 95.06% of total gross profit.

All five leading products belonged to the Chocolate division. This demonstrates significant concentration of financial contribution among a relatively small number of products.

### 3.2 Division Performance

| Division | Revenue | Gross Profit | Gross Margin |
|---|---:|---:|---:|
| Chocolate | 131,692.90 | 88,824.62 | 67.45% |
| Other | 9,663.25 | 4,333.45 | 44.84% |
| Sugar | 427.48 | 284.73 | 66.61% |

Chocolate was the largest contributor to revenue and gross profit. The Other division recorded the lowest gross margin, at 44.84%, and may benefit from further product-level cost and pricing investigation.

### 3.3 Low-Margin Product Review

Kazookles recorded a gross margin of only 7.69%, with cost representing 92.31% of revenue.

This product is a priority candidate for detailed cost and pricing review.

Other products with comparatively low margins include Fun Dip, Nerds, SweeTARTS, and Lickable Wallpaper. Low-volume products should be assessed cautiously before making business decisions.

### 3.4 Monthly Performance

Across 24 months:

- Average monthly gross margin was 65.88%.
- Monthly margin standard deviation was 0.53 percentage points.
- Highest monthly margin was 66.75% in January 2025.
- Lowest monthly margin was 64.54% in March 2024.

The results indicate relatively limited historical variation in monthly gross margin.

## 4. Priority Recommendations

1. **Review Kazookles:** Investigate its recorded cost and selling price to understand its low gross margin.
2. **Protect leading products:** Monitor the five products responsible for most of the portfolio's revenue and gross profit.
3. **Investigate the Other division:** Examine product-level cost and pricing differences to identify potential improvement opportunities.
4. **Strengthen profitability monitoring:** Regularly track revenue, cost, gross profit, gross margin, and profit per unit.
5. **Validate source data:** Obtain clarification on the 313 duplicate candidate rows and unusual shipping-date differences before making data corrections.

These recommendations identify areas for investigation and do not imply automatic product discontinuation or confirmed operational problems.

## 5. Dashboard and Project Deliverable

An interactive Streamlit dashboard was developed with four analytical modules:

1. Product Profitability Overview.
2. Division Performance Dashboard.
3. Cost vs Margin Diagnostics.
4. Profit Concentration Analysis.

The dashboard provides date, division, minimum margin, and product search filters. Its calculations and filtering behavior were validated against the processed dataset.

## 6. Conclusion

The analysis shows that Nassau Candy Distributor's recorded financial performance is strongly concentrated in five Chocolate products. While the overall weighted gross margin is 65.91%, individual product and division margins vary considerably.

The findings highlight the importance of product-level cost monitoring, margin review, and concentration management. The interactive dashboard provides a practical tool for ongoing financial performance monitoring.

The results should be interpreted in the context of the available dataset and its documented limitations. Further source-data validation and detailed cost information would strengthen future decision-making.

---

**Prepared as part of the Unified Mentor Data Analytics Project.**