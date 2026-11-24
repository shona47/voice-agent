from app.memory.memory import get_reminders

reminders = get_reminders()

print("\n===== SAVED REMINDERS =====")

for reminder in reminders:
    print(reminder)