import pandas as pd

# Create DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Age": [25, 30, 35, 28, 40, 45],
    "Department": ["HR", "IT", "IT", "Finance", "Finance", "HR"],
    "Salary": [50000, 70000, 80000, 60000, 90000, 55000]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Add bonus (10% of salary)
df["Bonus"] = df["Salary"] * 0.10
print("\nDataFrame with Bonus:\n", df)

# Group by department for average salary and bonus
grouped = df.groupby("Department")[["Salary", "Bonus"]].mean()
print("\nAverage Salary and Bonus by Department:\n", grouped)

# Employee with highest salary in each department
highest_salary = df.loc[df.groupby("Department")["Salary"].idxmax()]
print("\nEmployee with highest salary in each department:\n", highest_salary)

# Pivot table for average salary by department and age group
df["Age_Group"] = pd.cut(df["Age"], bins=[20, 30, 40, 50], labels=["20-30", "30-40", "40-50"])
pivot = df.pivot_table(values="Salary", index="Department", columns="Age_Group", aggfunc="mean")
print("\nPivot Table (Average Salary by Department and Age Group):\n", pivot)
