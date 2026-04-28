# Objective 
# Analyze retail data to uncover profitability drivers and provide actionable business recommendations.
# Analyze retail sales data to uncover trends, identify top-performing categories, and generate business insights. 
# Dataset
# Source: Kaggle (Superstore Sales Dataset)
# Key Questions: 
# Which product categories generate the most revenue?
# Which regions perform best?
# How do sales change over time?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/superstore.csv", encoding='latin1')

# Preview data 
print(df.head())

# Total Sales 
total_sales = df['Sales'].sum()
print("n\TotalSales:", total_sales)

# Sales by Category 
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Category:\n",category_sales)

# Sales by region
region_sales = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:\n", region_sales)

# Monthly trend 
df['Order Daqte'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()
print("\nMonthly Sales Trend:\n", monthly_sales)

# Visualization Code 

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Monthly Sales 
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

# Plot
plt.figure(figsize=(10,5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Sales by Category 
plt.figure(figsize=(6,4))
sns.barplot(x='Category', y='Sales', data=df)
plt.title("Sales by Category")
plt.show() 

# Advanced Analysis 
# Convert dates 
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M')

# 1.Profit Analysis 
profit_by_category = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
print("\nProfit by Category:\n", profit_by_category)

# Identify loss-making products
loss_products = df.groupby('Sub-Category')['Profit'].sum().sort_values()
print("\nLeast Profitable Sub-Categories:\n",loss_products.head())

# 2. Discount Impact 
discount_profit = df.groupby('Discount')['Profit'].mean()
print("\nProfit by Discount Level:\n", discount_profit)

# 3.Top Customers
top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Customers:\n", top_customers)

# 4. Growth Trend 
monthly_sales = df.groupby('Month')['Sales'].sum()
growth_rate = monthly_sales.pct_change().mean()
print("\nAverage Monthly Growth Rate:", growth_rate)

# Advanced Visualizations
# Profit vs Discount 
plt.figure(figsize=(6,4))
sns.scatterplot(x='Discount', y='Profit', data=df)
plt.title("Discount vs Profit")
plt.show()

# Profit by Sub-Category 
plt.figure(figsize=(10,5))
sns.barplot(x='Sub-Categopry', y='Profit', data=df)
plt.xticks(rotation=45)
plt.title("Profit by Sub-Category")
plt.show()

# Monthly Sales Trend 
df['Order Date'] = pd.to_datetime(df['Order date'])
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales.plot(figsize=(10,5), title="Monthly Sales Trend")
plt.show()




