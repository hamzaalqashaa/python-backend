import pandas as pd

# Load CSV file
df = pd.read_csv("sales_data.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Basic statistics
print("\nSummary Statistics:")
print(df.describe())

# Filter data (e.g., sales > 500)
high_sales = df[df['Sales'] > 500]
print("\nHigh Sales (>500):")
print(high_sales)

# Group by category and calculate average sales
avg_sales = df.groupby('Category')['Sales'].mean()
print("\nAverage Sales by Category:")
print(avg_sales)

# Save filtered data to new file
high_sales.to_csv("high_sales.csv", index=False)
print("\nFiltered data saved as 'high_sales.csv'")
