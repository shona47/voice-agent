def confirm(plan):

    intent = plan["intent"]
    params = plan["parameters"]

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

    choice = input("\nProceed? (yes/no): ")

    return choice.lower() == "yes"