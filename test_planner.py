from app.agent.planner import plan_task


commands = [
    "Remember that my favourite language is Python.",
    "Which model does my project use for image-based defect detection?",
    "Search for the latest developments in agentic AI.",
    "Remind me to study at 7 PM.",
    "Hello, how are you?"
]


for command in commands:

    print("\n====================================")
    print("USER:", command)

    result = plan_task(command)

    print("\nPLANNER OUTPUT:")
    print(result)