import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("detox.db")
cursor = conn.cursor()

for i in range(30):

    date = (
        datetime.now() -
        timedelta(days=i)
    ).strftime("%Y-%m-%d")

    screen_time = round(
        random.uniform(2, 9),
        2
    )

    cursor.execute(
        "INSERT INTO usage(date, screen_time) VALUES (?, ?)",
        (date, screen_time)
    )

conn.commit()
conn.close()

print("30 days of data inserted!")