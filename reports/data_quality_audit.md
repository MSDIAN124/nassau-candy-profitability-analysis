# Nassau Candy Distributor � Data Quality Audit

## 1. Dataset Overview
- Source: Official Unified Mentor dataset
- File: nassau_candy_distributor.csv
- Rows: 10,194
- Columns: 18
- Unique orders: 8,549
- Products: 15
- Divisions: 3
- Regions: 4

## 2. Missing Values
No missing values found across the 18 columns.

## 3. Numeric Validation
- Sales: 1.25 to 260.00
- Units: 1 to 14
- Gross Profit: 0.25 to 130.00
- Cost: 0.60 to 130.00
- Zero/negative values: None
- Sales - Cost = Gross Profit: All rows consistent (tolerance 0.01).

## 4. Duplicate Analysis
- Exact duplicate rows: 0 (Row ID included)
- Duplicate Row IDs: 0
- Unique Order IDs: 8,549
- Repeated Order IDs: 1,645
- Repeated Order-Product combinations: 1,373
- Rows identical across all business columns: 620
- Exact duplicate candidate groups: 307
- Extra repeated rows: 313

Duplicate candidates will be flagged and retained unless source-level confirmation supports removal.

## 5. Date Validation
- Order Date range: 2024-01-02 to 2025-12-31
- Ship Date range: 2026-06-30 to 2030-06-28
- Invalid dates: 0
- Ship Date before Order Date: 0
- Shipping delay range: 904 to 1,642 days
- Median shipping delay: 1,274 days

Shipping dates are unusually distant from order dates. Original values will be preserved pending source clarification.

- Mean shipping delay: 1,320.84 days
- Records with shipping delays exceeding 30 days: 10,194 (100%)
- Records with shipping delays exceeding 365 days: 10,194 (100%)

These calculated intervals should not be interpreted as actual delivery performance because the source shipping dates require clarification.

## 6. Product and Category Validation
- 15 products have consistent Product ID mappings.
- Each product maps to exactly one division.
- No leading/trailing whitespace found in checked categorical columns.
- Order ID embedded year does not match Order Date year in any row.
- 200 Order IDs do not match the expected embedded-year pattern.

## 7. Cleaning Decisions
1. Preserve original raw dataset.
2. Convert date columns to proper datetime.
3. Retain all transaction rows.
4. Flag exact business duplicate candidates; do not silently delete.
5. Preserve source dates and document date anomalies.
6. Validate all derived KPIs against source totals.

## 8. Limitations
Shipping delay anomalies and duplicate candidates require source-owner clarification. No unsupported corrections or assumptions will be applied.

---
Status: Initial data-quality audit completed.
