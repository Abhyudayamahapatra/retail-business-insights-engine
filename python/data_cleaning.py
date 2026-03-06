import pandas as pd

# Load dataset
df = pd.read_csv("../data/raw/Sample - Superstore.csv", encoding="latin1")

# Show first 5 rows
print(df.head())

# Check missing values
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv("../data/processed/cleaned_superstore.csv", index=False)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/raw/Sample - Superstore.csv", encoding="latin1")

print(df.head())

print(df.isnull().sum())

df = df.drop_duplicates()

df.to_csv("../data/processed/cleaned_superstore.csv", index=False)

print("Data cleaning completed successfully!")

# EDA
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

region_sales = df.groupby("Region")["Sales"].sum()
print(region_sales)

region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

import sqlite3

# Create database connection
conn = sqlite3.connect("../sql/retail_sales.db")

# Load cleaned dataset
clean_df = pd.read_csv("../data/processed/cleaned_superstore.csv")

# Insert data into SQL table
clean_df.to_sql("sales_data", conn, if_exists="replace", index=False)

print("Data inserted into SQL database successfully!")

# Close connection
conn.close()
import sqlite3

conn = sqlite3.connect("retail.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

print("Data loaded into SQLite database successfully!")

conn.close()
import sqlite3

conn = sqlite3.connect("retail.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

print("Data loaded into SQLite database successfully!")

conn.close()

import sqlite3

# connect to database
conn = sqlite3.connect("retail.db")

# create cursor
cursor = conn.cursor()

# Query 1: Total Sales
cursor.execute("SELECT SUM(Sales) FROM sales")
print("Total Sales:", cursor.fetchone())

# Query 2: Sales by Region
cursor.execute("SELECT Region, SUM(Sales) FROM sales GROUP BY Region")
print("Sales by Region:")
for row in cursor.fetchall():
    print(row)

# Query 3: Top 5 Products by Sales
cursor.execute("""
SELECT "Product Name", SUM(Sales) as total_sales
FROM sales
GROUP BY "Product Name"
ORDER BY total_sales DESC
LIMIT 5
""")

print("Top 5 Products:")
for row in cursor.fetchall():
    print(row)

conn.close()