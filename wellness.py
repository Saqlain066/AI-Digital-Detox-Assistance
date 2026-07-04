import random

quotes = [
    "Take a deep breath and give your mind some rest.",
    "Disconnect to reconnect with yourself.",
    "A short break can boost your productivity.",
    "Your mental health is more important than your screen.",
    "Step away from the screen and enjoy the present moment.",
    "Small breaks today prevent burnout tomorrow.",
    "Balance your digital life with real-life experiences.",
    "Rest your eyes and refresh your mind.",
    "Productivity grows when you take care of yourself.",
    "Go outside and enjoy nature for a few minutes."
]

activities = [
    "Drink a glass of water.",
    "Stretch for 5 minutes.",
    "Take a short walk.",
    "Meditate for 10 minutes.",
    "Listen to relaxing music.",
    "Practice deep breathing exercises.",
    "Talk to a friend or family member.",
    "Read a few pages of a book.",
    "Close your eyes and relax for 2 minutes.",
    "Do some light exercise."
]


def get_quote():
    return random.choice(quotes)


def get_activity():
    return random.choice(activities)