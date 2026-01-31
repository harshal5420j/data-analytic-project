import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Clean_sales_data.csv")

#print(df.info())
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.to_period("M")

print(df.info())


# =================
# Sale performance
# =================

# Total Sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# Monthly Sales Trend
monthly_sales = df.groupby("Month")["Sales"].sum()
print("\nMonthly Sales Trend:")
print(monthly_sales)

monthly_sales.plot(kind="line", title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Year-over-Year Growth
yearly_sales = df.groupby("Year")["Sales"].sum()
yoy_growth = yearly_sales.pct_change() * 100

print("\nYearly Sales:")
print(yearly_sales)

print("\nYear-over-Year Growth (%):")
print(yoy_growth)

# =================
# Product analysis (BY CATEGORY)
# =================

# Sales by Product Category
category_sales = df.groupby("Product Category")["Sales"].sum().sort_values(ascending=False)

print("\nSales by Product Category:")
print(category_sales)

# Best & Worst Product Category
best_category = category_sales.idxmax()
worst_category = category_sales.idxmin()

print("\nBest Performing Category:", best_category)
print("Worst Performing Category:", worst_category)

# Category-wise Sales Share (%)
category_sales_pct = (category_sales / category_sales.sum()) * 100

print("\nCategory-wise Sales Contribution (%):")
print(category_sales_pct)

# Visualization
category_sales.plot(kind="bar", title="Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# ================
# Customer trends
# ================

# Repeat vs One-time Customers
customer_orders = df.groupby("Customer ID")["Product Category"].nunique()

repeat_customers = customer_orders[customer_orders > 1].count()
one_time_customers = customer_orders[customer_orders == 1].count()

print("\nRepeat Customers:", repeat_customers)
print("One-time Customers:", one_time_customers)

# Average Order Value per Customer
avg_order_value = (
    df.groupby("Customer ID")["Sales"].sum().mean()
)

print("\nAverage Order Value per Customer:", avg_order_value)