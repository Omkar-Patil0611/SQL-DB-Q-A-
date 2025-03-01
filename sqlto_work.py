import pandas as pd
import sqlite3

# Load Excel file
df = pd.read_excel("C:\\Users\\HP\\Documents\\Parkdataset.xlsx")

# Connect to SQLite
conn = sqlite3.connect("data.db")
df.to_sql("work_two", conn, if_exists="replace", index=False)
conn.close()
