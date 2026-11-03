import pandas as pd

df = pd.read_csv("data/raw/nassau_candy_distributor.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

print("===== ORDER STRUCTURE =====")
print("Total transaction rows:", len(df))
print("Unique orders:", df["Order ID"].nunique())
print("Orders with multiple rows:", (df.groupby("Order ID").size() > 1).sum())

print("\nRows per order:")
print(df.groupby("Order ID").size().value_counts().sort_index().to_string())

print("\n===== ORDER CONSISTENCY =====")
order_check = df.groupby("Order ID").agg(
    order_dates=("Order Date", "nunique"),
    ship_dates=("Ship Date", "nunique"),
    customers=("Customer ID", "nunique")
)
print("Orders with multiple Order Dates:", (order_check["order_dates"] > 1).sum())
print("Orders with multiple Ship Dates:", (order_check["ship_dates"] > 1).sum())
print("Orders with multiple Customers:", (order_check["customers"] > 1).sum())

print("\n===== SHIPPING DELAY (DAYS) =====")
df["Shipping_Days"] = (df["Ship Date"] - df["Order Date"]).dt.days
print(df["Shipping_Days"].describe(percentiles=[.25, .50, .75, .90, .95]).to_string())

print("\n===== SAMPLE RECORDS =====")
print(df[["Order ID", "Order Date", "Ship Date", "Shipping_Days"]].head(10).to_string(index=False))
