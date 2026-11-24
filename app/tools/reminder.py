
from datetime import datetime

from app.memory.memory import save_reminder


def normalize_time(time_text):

    # Remove spaces and dots from AM/PM
    cleaned = time_text.strip().upper()
    cleaned = cleaned.replace(".", "")
    cleaned = " ".join(cleaned.split())

    # Add space before AM/PM if missing
    if cleaned.endswith("AM") and not cleaned.endswith(" AM"):
        cleaned = cleaned[:-2] + " AM"

    if cleaned.endswith("PM") and not cleaned.endswith(" PM"):
        cleaned = cleaned[:-2] + " PM"

    # Try different possible time formats
    formats = [
        "%I %p",
        "%I:%M %p",
        "%H:%M",
    ]

    for fmt in formats:
        try:
            parsed_time = datetime.strptime(cleaned, fmt)

            # Always save as: 8:00 PM
            return parsed_time.strftime("%-I:%M %p")

        except ValueError:
            continue

    # Windows does not always support %-I
    # Fallback for systems where it fails
    for fmt in formats:
        try:
            parsed_time = datetime.strptime(cleaned, fmt)

            return parsed_time.strftime("%I:%M %p").lstrip("0")

        except ValueError:
            continue

    # If the format is invalid
    return None


def set_reminder(parameters):

    task = parameters.get("task")
    time = parameters.get("time")

    print("\n⏰ Reminder Tool Activated")
    print(f"Task : {task}")
    print(f"Original Time : {time}")

    # Normalize time before saving
    normalized_time = normalize_time(time)

    if normalized_time is None:

        return {
            "success": False,
            "message": f"Could not understand reminder time: {time}"
        }

    print(f"Saved Time : {normalized_time}")

    save_reminder(
        task=task,
        reminder_time=normalized_time
    )

    return {
        "success": True,
        "message": "Reminder created successfully",
        "task": task,
        "time": normalized_time
    }

