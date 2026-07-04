import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression

# Connect to database
conn = sqlite3.connect("detox.db")

# Read data
df = pd.read_sql_query(
    "SELECT * FROM usage",
    conn
)

conn.close()

# Create day numbers
df["day"] = range(1, len(df) + 1)

# Features and target
X = df[["day"]]
y = df["screen_time"]

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Predict tomorrow
tomorrow = pd.DataFrame({
    "day": [len(df) + 1]
})

prediction = model.predict(tomorrow)

print(
    "Predicted screen time for tomorrow:",
    round(prediction[0], 2),
    "hours"
)