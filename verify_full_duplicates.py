import pandas as pd

df = pd.read_csv("data/raw/nassau_candy_distributor.csv")

business_cols = [c for c in df.columns if c != "Row ID"]

duplicates = df[df.duplicated(business_cols, keep=False)]

print("Rows identical across all business columns:", len(duplicates))
print("Unique duplicate groups:", duplicates.groupby(business_cols).ngroups)
print("Extra repeated rows:", len(duplicates) - duplicates.groupby(business_cols).ngroups)

print("\nSample complete duplicate records:")
print(duplicates.head(10).to_string(index=False))
