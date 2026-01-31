# Data Cleaning

import pandas as pd

# Load Dataset
df = pd.read_csv("retail_sales_dataset.csv")

print("Initial Data Shape:", df.shape)
print("Initial Data Info:")
print(df.info())

'''# Normalize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print("Columns:", df.columns)'''

# Rename Total Amount to sales
df = df.rename(columns={"Total Amount": "Sales"})

# Remove empty cells
df = df.dropna()
print("\nAfter removing null values")
print(df.shape)

# Fix date formats
df["Date"]=pd.to_datetime(df["Date"],errors="coerce")

df = df.dropna(subset=["Date"])
print("\nAfter Fixing Date Format:",df.shape)

# Remove  duplicate orders
df = df.drop_duplicates(subset=["Customer ID"])
print("\nAfter removing duplicate order",df.shape)

# Fix data types
df["Sales"] = df["Sales"].astype(float)
df["Quantity"] = df["Quantity"].astype(int)
df["Price per Unit"] = df["Price per Unit"].astype(float)
#df["Total Amount"] = df["Total Amount"].astype(float)

print("\nAfter fixing data type:")
print(df.dtypes)

# Save cleaned data
output_path = "Clean_sales_data.csv"
df.to_csv(output_path, index=False)

print("\n Data cleaning completed successfully. ")
print("Cleaned file saved as:",output_path)

