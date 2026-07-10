# 📊 Superstore Sales Dashboard

Data analysis and interactive dashboard for a retail Superstore dataset (2015–2018), built using **Python** for data cleaning/EDA and **Power BI** for visualization.

## 🎯 Project Overview
Analyzed 9,800+ orders from a Superstore dataset to uncover sales trends, regional performance, and top-performing products. Cleaned the raw data using Python (Pandas), performed exploratory data analysis, and built an interactive Power BI dashboard for business insights.

## 🛠️ Tools & Technologies
- **Python** (Pandas, Matplotlib, Seaborn) – Data cleaning & EDA
- **Power BI** – Interactive dashboard & visualization
- **SQL concepts** – Data aggregation & grouping

## 📈 Key Insights
- Total Sales: **$2.26M** across **4,922 orders** from **793 unique customers**
- Sales grew steadily year-over-year, from $479K (2015) to $722K (2018)
- **West region** generated the highest sales, followed by East, Central, and South
- **Technology** was the top-performing category by sales
- **Phones** and **Chairs** were the best-selling sub-categories
- Average delivery time was consistent across all regions (~4 days)

## 📂 Files in this Repository
- `train.csv` – Raw dataset
- `01_cleaning_eda.py` – Python script for data cleaning and exploratory analysis
- `Superstore_cleaned.csv` – Cleaned dataset used for the dashboard
- `Sales_Dashboard.pbix` – Power BI dashboard file
- `*.png` – Charts generated during EDA (sales trend, region-wise sales, top sub-categories, etc.)

## 📊 Dashboard Preview
The dashboard includes:
- KPI cards for Total Sales, Total Orders, and Total Customers
- Month-wise sales trend line chart (2015–2018)
- Region-wise sales comparison
- Top-selling sub-categories
- Interactive category filter (slicer)

  🔗 **Live Dashboard**: [View Interactive Dashboard](https://app.powerbi.com/groups/me/reports/6676e009-6239-4a6c-9fb6-58cb578afe6b/f84839be7385b4859b78?experience=power-bi)

## 🚀 How to Run
1. Clone this repository
2. Run `01_cleaning_eda.py` using Python (requires pandas, matplotlib, seaborn)
3. Open `Sales_Dashboard.pbix` in Power BI Desktop to explore the interactive dashboard
