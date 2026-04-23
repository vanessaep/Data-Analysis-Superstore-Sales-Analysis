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
# Load dataset
df = pd.read_csv("data/superstore.csv", encoding='latin1')

# Convert dates 
df['Order Date']
