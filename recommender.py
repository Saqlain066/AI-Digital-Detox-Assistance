def classify(hours):

    if hours < 3:
        return "Healthy User"

    elif hours < 6:
        return "Moderate User"

    elif hours < 8:
        return "Heavy User"

    else:
        return "High Risk User"


def recommend(hours):

    if hours < 3:
        return (
            "Excellent digital balance! "
            "Keep maintaining your healthy habits."
        )

    elif hours < 6:
        return (
            "Your usage is moderate. "
            "Take a short break every hour and avoid unnecessary scrolling."
        )

    elif hours < 8:
        return (
            "Your screen time is high. "
            "Consider taking a 20-minute digital detox session."
        )

    else:
        return (
            "Your screen time is critically high. "
            "Enable Focus Mode and take a longer break to reduce digital fatigue."
        )