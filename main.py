from flask import Flask, render_template, request, jsonify
import random
import json
from datetime import datetime, timedelta
import os

app = Flask(__name__)

DETOX_ACTIVITIES = [
    "🌿 Go for a nature walk",
    "🧘 Practice meditation",
    "📖 Read a book for 10 minutes",
    "💪 Do 10 push-ups",
    "✍ Write in a journal",
    "🎵 Listen to relaxing music",
    "🎨 Try a new hobby for 5 minutes"
]

LOG_FILE = "screen_time_log.json"
USAGE_LIMIT = timedelta(minutes=30)

# Ensure usage log file exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w') as f:
        json.dump({}, f)

def load_usage_data():
    with open(LOG_FILE, "r") as file:
        return json.load(file)

def save_usage_data(data):
    with open(LOG_FILE, "w") as file:
        json.dump(data, file, indent=4)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check_time", methods=["POST"])
def check_time():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    usage_data = load_usage_data()
    last_used = usage_data.get("last_used", now.isoformat())
    last_used_time = datetime.fromisoformat(last_used)
    minutes_used = int((now - last_used_time).total_seconds() // 60)

    if date not in usage_data:
        usage_data[date] = 0
    usage_data[date] += minutes_used
    usage_data["last_used"] = now.isoformat()

    save_usage_data(usage_data)
    return jsonify({"message": f"Today's screen time: {usage_data[date]} minutes"})

@app.route("/suggest_activity", methods=["GET"])
def suggest_activity():
    activity = random.choice(DETOX_ACTIVITIES)
    return jsonify({"activity": activity})

@app.route("/check_alert", methods=["GET"])
def check_alert():
    usage_data = load_usage_data()
    now = datetime.now()
    last_used = usage_data.get("last_used", now.isoformat())
    last_used_time = datetime.fromisoformat(last_used)
    elapsed = now - last_used_time

    if elapsed >= USAGE_LIMIT:
        return jsonify({"alert": "⚠ You've been on the screen too long! Time for a break."})
    else:
        return jsonify({"alert": "✅ You're within your screen time limit. Keep going!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port, debug=True)
