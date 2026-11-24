
def confirm(plan):

    intent = plan["intent"]
    params = plan["parameters"]

    # Chat and memory retrieval don't need confirmation
    if intent == "chat":
        return True

    if intent == "memory" and params.get("action") == "retrieve":
        return True

    print("\n========== CONFIRM ==========")

    if intent == "email":
        print("Action    : Send Email")
        print("Recipient :", params.get("recipient"))
        print("Subject   :", params.get("subject"))
        print("Body      :", params.get("body"))

    elif intent == "search":
        print("Action : Web Search")
        print("Query  :", params.get("query"))

    elif intent == "reminder":
        print("Action :", "Reminder")
        print("Task   :", params.get("task"))

    elif intent == "memory":
        if params.get("action") == "store":
            print("Action : Store Memory")
            print("Content:", params.get("content"))

        elif params.get("action") == "delete":
            print("Action : Delete Memory")
            print("Memory ID:", params.get("content"))

    choice = input("\nProceed? (yes/no): ")

    return choice.strip().lower() == "yes"
