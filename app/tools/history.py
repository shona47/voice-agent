from app.memory.memory import get_history

def show_history(parameters=None):

    history = get_history()

    if not history:
        print("\n📂 No history found.")
        return

    print("\n===== HISTORY =====\n")

    for row in history:
        print(f"ID: {row[0]}")
        print(f"Command: {row[1]}")
        print(f"Tool: {row[2]}")
        print(f"Result: {row[3]}")
        print(f"Time: {row[4]}")
        print("-" * 40)