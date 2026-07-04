from flask import Flask, render_template, request, redirect, send_file
from chatbot import ask_wellness_bot
from report import export_report
from flask import send_file
from flask import Flask, render_template, request, redirect
import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
from recommender import classify, recommend
from wellness import get_quote, get_activity
from notification import show_notification

app = Flask(__name__)


@app.route("/")
def home():

    # Connect to database
    conn = sqlite3.connect("detox.db")
    cursor = conn.cursor()

    # Get all usage records
    cursor.execute("SELECT * FROM usage")
    data = cursor.fetchall()

    # Read usage data into DataFrame
    df = pd.read_sql_query(
        "SELECT * FROM usage",
        conn
    )

    # Get current daily limit
    cursor.execute(
        "SELECT daily_limit FROM settings LIMIT 1"
    )

    result = cursor.fetchone()

    if result:
        current_limit = result[0]
    else:
        current_limit = None

    conn.close()

    # If there is no data
    if len(df) == 0:
        return render_template(
            "index.html",
            records=[],
            prediction=0,
            category="No Data",
            suggestion="Add some screen time data first.",
            total_days=0,
            average_usage=0,
            highest_usage=0,
            current_limit=current_limit,
            warning=False,
            quote="",
            activity=""
        )

    # Create day numbers
    df["day"] = range(
        1,
        len(df) + 1
    )

    X = df[["day"]]
    y = df["screen_time"]

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Predict tomorrow's usage
    tomorrow = pd.DataFrame({
        "day": [len(df) + 1]
    })

    prediction = round(
        model.predict(tomorrow)[0],
        2
    )

    # Recommendation system
    category = classify(prediction)
    suggestion = recommend(prediction)

    # Statistics
    total_days = len(df)
    average_usage = round(
        df["screen_time"].mean(),
        2
    )

    highest_usage = round(
        df["screen_time"].max(),
        2
    )

    wellness_score = max(
        0,
        min(
            100,
            int(
                100 - (prediction * 10)
            )
        )
    )



    # Warning system
    warning = False
    quote = ""
    activity = ""

    if current_limit is not None and prediction > current_limit:
        warning = True
        quote = get_quote()
        activity = get_activity()

        show_notification(
            "You are likely to exceed your screen-time limit today!"
        )


    return render_template(
        "index.html",
        records=data,
        prediction=prediction,
        category=category,
        suggestion=suggestion,
        total_days=total_days,
        average_usage=average_usage,
        highest_usage=highest_usage,
        current_limit=current_limit,
        warning=warning,
        quote=quote,
        activity=activity,
        wellness_score=wellness_score,
    )


@app.route("/set_limit", methods=["POST"])
def set_limit():

    limit = float(
        request.form["daily_limit"]
    )

    conn = sqlite3.connect("detox.db")
    cursor = conn.cursor()

    # Remove old limit
    cursor.execute(
        "DELETE FROM settings"
    )

    # Insert new limit
    cursor.execute(
        "INSERT INTO settings(daily_limit) VALUES (?)",
        (limit,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/focus")
def focus():

    return """
    <h1>🧘 Focus Mode Started</h1>

    <p>Put your device away and relax for 20 minutes.</p>

    <h3>Suggestions:</h3>

    <ul>
        <li>Drink water</li>
        <li>Stretch</li>
        <li>Meditate</li>
        <li>Take a short walk</li>
    </ul>

    <a href='/'>
        <button>Back to Dashboard</button>
    </a>
    """

@app.route("/report")
def report():

    export_report()

    return send_file(
        "screen_time_report.csv",
        as_attachment=True
    )


@app.route("/chat", methods=["GET", "POST"])
def chat():

    if "chat_history" not in app.config:
        app.config["chat_history"] = []

    if request.method == "POST":

        question = request.form["question"]

        try:
            response = ask_wellness_bot(question)

            app.config["chat_history"].append(
                {
                    "question": question,
                    "answer": response
                }
            )

        except Exception as e:
            app.config["chat_history"].append(
                {
                    "question": question,
                    "answer": f"Error: {e}"
                }
            )

    return render_template(
        "chat.html",
        history=app.config["chat_history"]
    )


@app.route("/clear_chat")
def clear_chat():

    app.config["chat_history"] = []

    return redirect("/chat")


if __name__ == "__main__":
    app.run(debug=True)