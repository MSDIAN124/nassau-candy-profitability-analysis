
import pandas as pd
from pathlib import Path

INPUT_FILE = Path("data/processed/nassau_candy_kpi_data.csv")
OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

# Scenario A: retain all rows
scenario_a = df.copy()

# Scenario B: exclude flagged duplicate candidates for sensitivity only
scenario_b = df[
    ~df["Duplicate Candidate Flag"].astype(bool)
].copy()


def calculate_metrics(data, scenario_name):
    revenue = data["Sales"].sum()
    cost = data["Cost"].sum()
    profit = data["Gross Profit"].sum()

    return {
        "Scenario": scenario_name,
        "Transaction_Rows": len(data),
        "Revenue": revenue,
        "Cost": cost,
        "Gross_Profit": profit,
        "Gross_Margin_%": profit / revenue * 100 if revenue else 0
    }


# Overall comparison
overall = pd.DataFrame([
    calculate_metrics(scenario_a, "A - All Rows Retained"),
    calculate_metrics(scenario_b, "B - Duplicate Candidates Excluded")
])

# Absolute and percentage differences
metric_columns = ["Revenue", "Cost", "Gross_Profit", "Gross_Margin_%"]

for column in metric_columns:
    a_value = overall.loc[0, column]
    b_value = overall.loc[1, column]

    overall.loc[1, f"{column}_Difference"] = b_value - a_value

# Division-level comparison
division_results = []

for division in sorted(df["Division"].unique()):
    a = scenario_a[scenario_a["Division"] == division]
    b = scenario_b[scenario_b["Division"] == division]

    a_metrics = calculate_metrics(a, "A - All Rows Retained")
    b_metrics = calculate_metrics(b, "B - Duplicate Candidates Excluded")

    for metric in ["Revenue", "Cost", "Gross_Profit", "Gross_Margin_%"]:
        b_metrics[f"{metric}_Difference"] = (
            b_metrics[metric] - a_metrics[metric]
        )

    a_metrics["Division"] = division
    b_metrics["Division"] = division

    division_results.extend([a_metrics, b_metrics])

division_comparison = pd.DataFrame(division_results)

# Save outputs
overall_file = OUTPUT_DIR / "duplicate_sensitivity_overall.csv"
division_file = OUTPUT_DIR / "duplicate_sensitivity_by_division.csv"

overall.to_csv(overall_file, index=False)
division_comparison.to_csv(division_file, index=False)

# Display results
print("===== OVERALL SENSITIVITY COMPARISON =====")
print(overall.round(2).to_string(index=False))

print("\n===== DIVISION SENSITIVITY COMPARISON =====")
print(division_comparison.round(2).to_string(index=False))

print("\n===== VALIDATION =====")
print("Original rows:", len(scenario_a))
print("Sensitivity rows:", len(scenario_b))
print("Excluded candidate rows:", len(scenario_a) - len(scenario_b))
print("Candidate flags:", int(
    df["Duplicate Candidate Flag"].astype(bool).sum()
))

print("\nOutput files:")
print(overall_file)
print(division_file)
