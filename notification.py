from plyer import notification

def show_notification(message):

    notification.notify(
        title="AI Digital Detox Assistant",
        message=message,
        timeout=10
    )