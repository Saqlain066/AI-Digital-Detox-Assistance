import sqlite3
import pandas as pd

def export_report():

    conn = sqlite3.connect(
        "detox.db"
    )

    df = pd.read_sql_query(
        "SELECT * FROM usage",
        conn
    )

    conn.close()

    df.to_csv(
        "screen_time_report.csv",
        index=False
    )