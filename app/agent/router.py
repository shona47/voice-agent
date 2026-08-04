def detect_intent(text):

    text = text.lower()

    if "email" in text or "mail" in text:
        return "email"

    elif "search" in text or "find" in text:
        return "search"

    elif "remind" in text:
        return "reminder"

    elif "contact" in text:
        return "contact"

    else:
        return "chat"