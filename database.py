import sqlite3

# Connect to database (creates detox.db if it doesn't exist)
conn = sqlite3.connect("detox.db")

# Create cursor
cursor = conn.cursor()

# Create usage table
cursor.execute("""
CREATE TABLE IF NOT EXISTS usage(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    screen_time REAL
)
""")

# Create settings table
cursor.execute("""
CREATE TABLE IF NOT EXISTS settings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    daily_limit REAL
)
""")

# Save changes
conn.commit()

# Close connection
conn.close()

print("Database and tables created successfully!")