from app.agent.tool_registry import TOOLS


def execute(plan):

    intent = plan["intent"]
    parameters = plan["parameters"]

    tool = TOOLS.get(intent)

    if tool:
        tool(parameters)
    else:
        print(f"Unknown tool: {intent}")