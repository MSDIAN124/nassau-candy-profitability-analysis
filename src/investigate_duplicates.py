import pandas as pd

df = pd.read_csv("data/raw/nassau_candy_distributor.csv")

dup = df[df.duplicated(["Order ID", "Product ID"], keep=False)].copy()

print("===== DUPLICATE COMBINATIONS =====")
print("Rows involved:", len(dup))
print("Unique Order-Product combinations:", dup.groupby(["Order ID", "Product ID"]).ngroups)

print("\n===== SAMPLE REPEATED COMBINATIONS =====")
print(
    dup.sort_values(["Order ID", "Product ID"])
       [["Row ID", "Order ID", "Product ID", "Product Name",
         "Sales", "Units", "Gross Profit", "Cost"]]
       .head(20).to_string(index=False)
)

print("\n===== IDENTICAL BUSINESS VALUES =====")
business_cols = ["Order ID", "Product ID", "Sales", "Units", "Gross Profit", "Cost"]
print("Repeated combinations with identical values:",
      dup.duplicated(business_cols, keep=False).sum())

print("\n===== MULTIPLE ROWS PER ORDER-PRODUCT =====")
counts = df.groupby(["Order ID", "Product ID"]).size()
print(counts.value_counts().sort_index().to_string())
