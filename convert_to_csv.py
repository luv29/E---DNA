import sqlite3
import pandas as pd

# Path to your SQLite DB
db_path = r"D:\SIH\New folder\New folder\taxonomy4blast.sqlite3"

# Connect to the database
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Inspect columns to make sure
cur.execute("PRAGMA table_info(TaxidInfo);")
columns = cur.fetchall()
print("Columns in TaxidInfo:", columns)

# Assuming columns are something like: seq_accession, tax_id
# Replace 'seq_accession' and 'tax_id' with actual column names if different
df = pd.read_sql("SELECT * FROM TaxidInfo;", conn)

# Save to CSV
df.to_csv(r"D:\SIH\New folder\New folder\accession_taxid.csv", index=False)
print("CSV saved: accession_taxid.csv")

conn.close()
