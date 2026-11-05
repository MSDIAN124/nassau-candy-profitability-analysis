import pandas as pd

df = pd.read_csv("data/raw/nassau_candy_distributor.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

def summary(data):
    sales = data["Sales"].sum()
    profit = data["Gross Profit"].sum()
    cost = data["Cost"].sum()
    return pd.Series({
        "Orders": data["Order ID"].nunique(),
        "Units": data["Units"].sum(),
        "Revenue": round(sales, 2),
        "Cost": round(cost, 2),
        "Gross Profit": round(profit, 2),
        "Gross Margin %": round(profit / sales * 100, 2) if sales else 0
    })

print("===== OVERALL BUSINESS PERFORMANCE =====")
print(summary(df).to_string())

print("\n===== DIVISION PERFORMANCE =====")
print(df.groupby("Division").apply(summary, include_groups=False).round(2).to_string())

print("\n===== TOP 10 PRODUCTS BY GROSS PROFIT =====")
print(df.groupby("Product Name").apply(summary, include_groups=False)
      .sort_values("Gross Profit", ascending=False).head(10).to_string())

print("\n===== BOTTOM 5 PRODUCTS BY GROSS MARGIN =====")
print(df.groupby("Product Name").apply(summary, include_groups=False)
      .sort_values("Gross Margin %").head(5).to_string())

print("\n===== MONTHLY PERFORMANCE =====")
print(df.groupby("Month").apply(summary, include_groups=False).round(2).to_string())
