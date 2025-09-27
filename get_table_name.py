import sqlite3

conn = sqlite3.connect(r"D:\SIH\New folder\New folder\taxonomy4blast.sqlite3")
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print("Tables:", tables)

conn.close()
