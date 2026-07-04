from plyer import notification
import time

notification.notify(
    title="Test Notification",
    message="Hello from Python!",
    app_name="AI Digital Detox Assistant",
    timeout=20
)

time.sleep(5)