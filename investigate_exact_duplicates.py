import pandas as pd

df = pd.read_csv("data/raw/nassau_candy_distributor.csv")

cols = ["Order ID", "Product ID", "Order Date", "Ship Date",
        "Customer ID", "Sales", "Units", "Gross Profit", "Cost"]

dup = df[df.duplicated(cols, keep=False)].copy()

print("Exact business duplicate groups:", dup.groupby(cols).ngroups)
print("Rows involved:", len(dup))
print("Extra repeated rows:", len(dup) - dup.groupby(cols).ngroups)

print("\nSample:")
print(dup[cols + ["Row ID"]].head(15).to_string(index=False))

print("\nTotal financial impact of these rows:")
print(dup[["Sales", "Gross Profit", "Cost", "Units"]].sum().to_string())
