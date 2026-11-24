
import time
from datetime import datetime

from app.memory.memory import get_reminders, mark_reminder_done


def check_reminders():

    while True:

        reminders = get_reminders()

        # Current time in the same format used when saving reminders
        current_time = datetime.now().strftime("%I:%M %p").lstrip("0")

        for reminder in reminders:

            reminder_id = reminder[0]
            task = reminder[1]
            reminder_time = reminder[2]

            # Both values should already be in the same format
            saved_time = reminder_time.strip().upper()
            now_time = current_time.strip().upper()

            if saved_time == now_time:

                print("\n")
                print("🔔 ===============================")
                print("🔔 REMINDER")
                print(f"🔔 Task : {task}")
                print(f"🔔 Time : {reminder_time}")
                print("🔔 ===============================")

                mark_reminder_done(reminder_id)

        time.sleep(30)

