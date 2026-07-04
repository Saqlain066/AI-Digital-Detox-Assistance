import sqlite3

conn = sqlite3.connect("detox.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM usage")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()