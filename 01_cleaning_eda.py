# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the dataset
df = pd.read_csv("train.csv")
print("Shape before cleaning:", df.shape)

# ---------------------------------------------------
# STEP 1: DATA CLEANING
# ---------------------------------------------------

# 1.1 Convert Order Date and Ship Date to proper datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors="coerce")

# 1.2 Check missing values
print("\nMissing values:\n", df.isnull().sum()[df.isnull().sum() > 0])

# 1.3 Fill missing Postal Code with 0 (not critical for analysis)
df["Postal Code"] = df["Postal Code"].fillna(0)

# 1.4 Check and remove duplicates (if any)
print("\nDuplicates found:", df.duplicated().sum())
df = df.drop_duplicates()

# ---------------------------------------------------
# STEP 2: FEATURE ENGINEERING (new columns)
# ---------------------------------------------------

# 2.1 Extract Year and Month from Order Date
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Order YearMonth"] = df["Order Date"].dt.to_period("M").astype(str)

# 2.2 Calculate delivery time (days between Order Date and Ship Date)
df["Delivery Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

# Save cleaned dataset for Power BI
df.to_csv("Superstore_cleaned.csv", index=False)
print("\nCleaned file saved as Superstore_cleaned.csv")
print("Shape after cleaning:", df.shape)

# ---------------------------------------------------
# STEP 3: EDA - EXPLORATORY DATA ANALYSIS
# ---------------------------------------------------

# 3.1 Overall summary
print("\n--- OVERALL SUMMARY ---")
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Orders:", df["Order ID"].nunique())
print("Unique Customers:", df["Customer ID"].nunique())
print("Unique Products:", df["Product ID"].nunique())
print("Average Delivery Days:", round(df["Delivery Days"].mean(), 1))

# 3.2 Year-wise Sales Trend
yearly_sales = df.groupby("Order Year")["Sales"].sum()
print("\nYear-wise Sales:\n", yearly_sales)

# 3.3 Month-wise Sales Trend (across all years, chronological)
monthly_sales = df.groupby("Order YearMonth")["Sales"].sum().sort_index()
print("\nMonth-wise Sales (first 5):\n", monthly_sales.head())

plt.figure(figsize=(14, 6))
monthly_sales.plot(kind="line", marker="o")
plt.title("Month-wise Sales Trend (2015-2018)")
plt.xlabel("Year-Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=90, fontsize=7)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.close()

# 3.4 Region-wise Sales
region_summary = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nRegion-wise Sales:\n", region_summary)

plt.figure(figsize=(8, 5))
sns.barplot(x=region_summary.index, y=region_summary.values)
plt.title("Region-wise Sales")
plt.ylabel("Total Sales")
plt.savefig("region_sales.png")
plt.close()

# 3.5 Category and Sub-Category wise Sales
category_summary = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nCategory-wise Sales:\n", category_summary)

subcat_summary = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Sub-Categories by Sales:\n", subcat_summary)

plt.figure(figsize=(10, 6))
sns.barplot(x=subcat_summary.values, y=subcat_summary.index)
plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Total Sales")
plt.tight_layout()
plt.savefig("top_subcategories.png")
plt.close()

# 3.6 Top 10 Customers by Sales
top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Customers by Sales:\n", top_customers)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_customers.values, y=top_customers.index)
plt.title("Top 10 Customers by Sales")
plt.xlabel("Total Sales")
plt.tight_layout()
plt.savefig("top_customers.png")
plt.close()

# 3.7 Average Delivery Days by Region
delivery_summary = df.groupby("Region")["Delivery Days"].mean().sort_values()
print("\nAverage Delivery Days by Region:\n", delivery_summary)

plt.figure(figsize=(8, 5))
sns.barplot(x=delivery_summary.index, y=delivery_summary.values)
plt.title("Average Delivery Days by Region")
plt.ylabel("Avg Delivery Days")
plt.savefig("delivery_days_by_region.png")
plt.close()

print("\nAll charts saved as PNG files in the current folder.")
print("EDA complete! Use Superstore_cleaned.csv in Power BI next.")
