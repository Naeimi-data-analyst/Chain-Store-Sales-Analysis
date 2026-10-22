# ==========================================
# 1. ==========Import librareis ===========
# ==========================================
import pandas as pd
import matplotlib.pyplot as plt
# ==========================================
# 2. ========== Read Excel File ==========
# ==========================================
df = pd.read_excel('chain_store.xlsx')
# ==========================================
# 3. ========== Data Quality Check ==========
# ==========================================
#  Show first 5 rows 
print("\n ====== First 5 rows of data ======")
print(df.head())
#  Show Data Information 
print("\n =======Data Information =======")
df.info()
#  Descriptive statistics 
print("\n======= Descriptive Statistics =======")
print(df.describe())
# ==========================================
# 4. ========== Create New Columns ==========
# ==========================================
df["Profit"]= df["Sales"]-(df["Cost"]*df["Quantity"])
# ====== Create Time Features =======
df["Year"]=df["Date"].dt.year
df["Month"]=df["Date"].dt.month
df["Month_Name"]=df["Date"].dt.month_name()
# ==========================================
# 5. ========== Data Analysis ==========
#  ========================================== 
# Total profit for each product
profit_by_product=df.groupby("Product") ["Profit"].sum()
print(profit_by_product.sort_values(ascending=False))
# ==========================================
# Total sales for each product
sales_by_product = df.groupby('Product')['Sales'].sum()
print(sales_by_product.sort_values(ascending=False))
# ==========================================
# Total profit for each city
profit_by_city=df.groupby("City") ["Profit"].sum()
print(profit_by_city.sort_values(ascending=False))
# ==========================================
# Total sales for each city
sales_by_city =df.groupby("City") ["Sales"].sum()
print(sales_by_city .sort_values(ascending=False))
# ==========================================
# Total Profit of Mouse in Each City 
mouse_profit_by_city =df[df["Product"]=="Mouse"].groupby("City")["Profit"].sum()
print(mouse_profit_by_city.sort_values(ascending=False))
# ==========================================
table= pd.pivot_table(
       df,
       index="Product",
       columns="Employee",
       values="Profit",
       aggfunc="sum"
       )
print("\n====== Profit by Product and Employee ======")
print(table)
# ==========================================
sales_month = pd.pivot_table(
    df,
    values="Sales",
    index=["Month","Month_Name"],
    aggfunc="sum"
).reset_index()
print(sales_month)
# ==========================================
# 6. ========== Charts ==========
# ==========================================
# 6.A. Bar chart: profit by product
# ==========================================

plt.figure(figsize=(8, 5))
profit_by_product_sorted = profit_by_product.sort_values(
    ascending=False
)
ax = profit_by_product_sorted.plot(kind="bar", color="skyblue")
ax.bar_label(ax.containers[0], fmt="%.0f", padding=3)
plt.title("Profit by Product", fontsize=16)
plt.xlabel("Product", fontsize=12)
plt.ylabel("Total Profit", fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("profit_by_product.png")
plt.show()

# ==========================================
# 6.B. Bar chart: sales by product
# ==========================================
plt.figure(figsize=(8, 5))
sales_by_product_sorted = sales_by_product.sort_values(
    ascending=False
)
ax = sales_by_product_sorted.plot(kind="bar", color="skyblue")
ax.bar_label(ax.containers[0], fmt="%.0f", padding=3)
plt.title("Sales by Product" , fontsize=16)
plt.xlabel("Product" , fontsize=12)
plt.ylabel("Total Sales" , fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('sales_by_product.png')
plt.show()
# ==========================================
# 6.C. Bar chart: profit by city
# ==========================================
plt.figure(figsize=(8, 5))
profit_by_city_sorted = profit_by_city.sort_values(
    ascending=False
)
ax = profit_by_city_sorted.plot(kind="bar", color="skyblue")
ax.bar_label(ax.containers[0], fmt="%.0f", padding=3)
plt.title("Profit by City" , fontsize=16)
plt.xlabel("City" , fontsize=12)
plt.ylabel("Total Profit" , fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('profit_by_city.png')
plt.show()
# ==========================================
# 6.D. Line chart: sales by month
# ==========================================
plt.figure(figsize=(8, 5))
plt.plot(
    sales_month["Month_Name"],
    sales_month["Sales"],
    marker="o"
)
plt.title("Sales by Month" , fontsize=16)
plt.xlabel("Month" , fontsize=12)
plt.ylabel("Total Sales" , fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig('sales_by_m' \
'onth.png')
plt.show()
# ==========================================
print("\n Analysis and charts completed successfully!")







