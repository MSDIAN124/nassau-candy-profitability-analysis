import pandas as pd

df = pd.read_csv("data/raw/nassau_candy_distributor.csv")

print("===== PRODUCT MAPPING =====")
mapping = df.groupby("Product Name").agg(
    Product_IDs=("Product ID", "nunique"),
    Divisions=("Division", "nunique")
)
print(mapping.to_string())
print("\nProducts with multiple IDs:", (mapping["Product_IDs"] > 1).sum())
print("Products with multiple divisions:", (mapping["Divisions"] > 1).sum())

print("\n===== PRODUCT ID MAPPING =====")
id_mapping = df.groupby("Product ID").agg(
    Product_Names=("Product Name", "nunique"),
    Divisions=("Division", "nunique")
)
print("Product IDs mapped to multiple names:", (id_mapping["Product_Names"] > 1).sum())
print("Product IDs mapped to multiple divisions:", (id_mapping["Divisions"] > 1).sum())

print("\n===== ORDER ID YEAR CHECK =====")
df["Order Year"] = pd.to_datetime(df["Order Date"], dayfirst=True).dt.year
df["ID Year"] = df["Order ID"].str.extract(r"US-(\d{4})").astype(float)
print("Order ID embedded years:")
print(df["ID Year"].value_counts(dropna=False).sort_index().to_string())
print("Rows where ID year differs from Order Date year:", (df["ID Year"] != df["Order Year"]).sum())

print("\n===== TEXT CLEANLINESS =====")
for col in ["Division", "Region", "Product Name", "Ship Mode", "State/Province"]:
    dirty = df[col].astype(str).ne(df[col].astype(str).str.strip())
    print(f"{col} - leading/trailing whitespace rows: {dirty.sum()}")

print("\n===== TRANSACTION KEY =====")
print("Duplicate Order ID + Product ID combinations:",
      df.duplicated(subset=["Order ID", "Product ID"]).sum())
