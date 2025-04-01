import time
import json
import random
import tkinter as tk
from datetime import datetime, timedelta
from tkinter import messagebox

# Detox activities
DETOX_ACTIVITIES = [
    "🌿 Go for a nature walk",
    "🧘 Practice meditation",
    "📖 Read a book for 10 minutes",
    "💪 Do 10 push-ups",
    "✍ Write in a journal",
    "🎵 Listen to relaxing music",
    "🎨 Try a new hobby for 5 minutes"
]

class DigitalDetoxAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 Digital Detox Assistant 🌟")
        self.root.geometry("500x600")
        self.root.configure(bg="#2c3e50")
        
        self.start_time = datetime.now()
        self.usage_limit = timedelta(minutes=30)
        self.log_file = "screen_time_log.json"
        self.load_usage_data()

        # UI Elements
        self.label = tk.Label(root, text="Digital Detox Assistant", font=("Arial", 18, "bold"), bg="#2c3e50", fg="white")
        self.label.pack(pady=15)

        self.frame = tk.Frame(root, bg="#34495e", bd=5, relief="ridge")
        self.frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.info_label = tk.Label(self.frame, text="🌍 Stay mindful of your screen time!", font=("Arial", 12), bg="#34495e", fg="white")
        self.info_label.pack(pady=10)

        self.check_time_btn = tk.Button(self.frame, text="⏳ Check Screen Time", command=self.check_usage, font=("Arial", 12), bg="#3498db", fg="white", padx=10, pady=5)
        self.check_time_btn.pack(pady=5, fill="x")

        self.suggest_btn = tk.Button(self.frame, text="💡 Suggest Activity", command=self.suggest_activity, font=("Arial", 12), bg="#2ecc71", fg="white", padx=10, pady=5)
        self.suggest_btn.pack(pady=5, fill="x")

        self.alert_btn = tk.Button(self.frame, text="⚠ Show Alert", command=self.show_alert, font=("Arial", 12), bg="#e74c3c", fg="white", padx=10, pady=5)
        self.alert_btn.pack(pady=5, fill="x")

        self.quote_label = tk.Label(self.frame, text="💡 'Take breaks, refresh your mind!'", font=("Arial", 12, "italic"), bg="#34495e", fg="lightgray")
        self.quote_label.pack(pady=15)

        self.quit_btn = tk.Button(self.frame, text="🚪 Exit", command=root.quit, font=("Arial", 12), bg="#f39c12", fg="white", padx=10, pady=5)
        self.quit_btn.pack(pady=10, fill="x")

    def load_usage_data(self):
        try:
            with open(self.log_file, "r") as file:
                self.usage_data = json.load(file)
        except FileNotFoundError:
            self.usage_data = {}

    def save_usage_data(self):
        with open(self.log_file, "w") as file:
            json.dump(self.usage_data, file, indent=4)

    def check_usage(self):
        date = datetime.now().strftime("%Y-%m-%d")
        
        if date not in self.usage_data:
            self.usage_data[date] = 0
        
        elapsed_time = datetime.now() - self.start_time
        minutes_used = int(elapsed_time.total_seconds() // 60)
        
        self.usage_data[date] += minutes_used
        self.start_time = datetime.now()
        
        self.save_usage_data()
        
        messagebox.showinfo("📊 Screen Time", f"Today's Screen Time: {self.usage_data[date]} min")

    def suggest_activity(self):
        activity = random.choice(DETOX_ACTIVITIES)
        messagebox.showinfo("🎯 Detox Suggestion", f"{activity}")

    def show_alert(self):
        elapsed_time = datetime.now() - self.start_time
        if elapsed_time >= self.usage_limit:
            messagebox.showwarning("⚠ Warning", "You've been on the screen too long! Time for a break.")
        else:
            messagebox.showinfo("✅ Status", "You're within your screen time limit. Keep going!")

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalDetoxAssistant(root)
    root.mainloop()