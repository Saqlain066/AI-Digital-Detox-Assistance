import sqlite3
from notification import show_notification

conn = sqlite3.connect("detox.db")
cursor = conn.cursor()

# Get today's latest screen time
cursor.execute("""
SELECT screen_time
FROM usage
ORDER BY id DESC
LIMIT 1
""")

usage = cursor.fetchone()

# Get user limit
cursor.execute("""
SELECT daily_limit
FROM settings
LIMIT 1
""")

limit = cursor.fetchone()

conn.close()

if usage and limit:

    screen_time = usage[0]
    daily_limit = limit[0]

    print("Today's Usage:", screen_time)
    print("Limit:", daily_limit)

    if screen_time > daily_limit:

        print("Limit exceeded!")

        show_notification(
            f"You exceeded your limit by {round(screen_time-daily_limit,2)} hours!"
        )

    else:
        print("Within limit.")