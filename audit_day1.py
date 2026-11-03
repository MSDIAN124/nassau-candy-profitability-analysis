import pandas as pd

df = pd.read_csv("data/raw/nassau_candy_distributor.csv")

order_date = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")
ship_date = pd.to_datetime(df["Ship Date"], dayfirst=True, errors="coerce")

print("===== DUPLICATE CHECK =====")
print("Exact duplicate rows:", df.duplicated().sum())
print("Duplicate Row IDs:", df["Row ID"].duplicated().sum())
print("Duplicate Order IDs:", df["Order ID"].duplicated().sum())

print("\n===== NUMERIC VALIDATION =====")
for col in ["Sales", "Units", "Gross Profit", "Cost"]:
    print(f"{col}: min={df[col].min()}, max={df[col].max()}, zero={(df[col] == 0).sum()}, negative={(df[col] < 0).sum()}")

print("\n===== PROFIT-COST CONSISTENCY =====")
difference = (df["Sales"] - df["Cost"] - df["Gross Profit"]).abs()
print("Mismatches (tolerance > 0.01):", (difference > 0.01).sum())
print("Maximum absolute difference:", round(difference.max(), 4))

print("\n===== DATE VALIDATION =====")
print("Invalid Order Dates:", order_date.isna().sum())
print("Invalid Ship Dates:", ship_date.isna().sum())
print("Order Date Range:", order_date.min(), "to", order_date.max())
print("Ship Date Range:", ship_date.min(), "to", ship_date.max())
print("Ship before Order:", (ship_date < order_date).sum())

print("\n===== CATEGORY VALIDATION =====")
for col in ["Division", "Region", "Ship Mode", "Product Name"]:
    print(f"\n{col} ({df[col].nunique()} unique):")
    print(sorted(df[col].dropna().unique().tolist()))
