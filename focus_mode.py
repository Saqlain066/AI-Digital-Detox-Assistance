import time

def start_focus_mode(minutes):

    print(
        f"Focus Mode started for {minutes} minutes."
    )

    time.sleep(minutes * 60)

    print(
        "Focus session completed!"
    )