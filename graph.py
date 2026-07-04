import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("detox.db")

df = pd.read_sql_query(
    "SELECT * FROM usage",
    conn
)

plt.figure(figsize=(10, 5))
plt.plot(df["screen_time"])

plt.title("Screen Time Trend")
plt.xlabel("Days")
plt.ylabel("Hours")

plt.savefig("static/graph.png")

print("Graph created!")