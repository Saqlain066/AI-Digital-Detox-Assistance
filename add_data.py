import sqlite3
from datetime import datetime

screen_time = 4.5

conn = sqlite3.connect("detox.db")
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO usage(date, screen_time) VALUES (?, ?)",
    (
        datetime.now().strftime("%Y-%m-%d"),
        screen_time
    )
)

conn.commit()
conn.close()

print("Data inserted successfully!")