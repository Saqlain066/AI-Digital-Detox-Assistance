import sqlite3
from datetime import datetime
import random

screen_time = round(
    random.uniform(2, 9),
    2
)

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

print(
    f"{screen_time} hours saved."
)