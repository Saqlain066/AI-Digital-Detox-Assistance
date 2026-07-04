import sqlite3

limit = float(input("Enter daily screen time limit (hours): "))

conn = sqlite3.connect("detox.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM settings")

cursor.execute(
    "INSERT INTO settings(daily_limit) VALUES (?)",
    (limit,)
)

conn.commit()
conn.close()

print("Limit saved successfully!")