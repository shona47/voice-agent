from app.agent.tool_registry import TOOLS


def execute(plan):

    intent = plan["intent"]
    parameters = plan["parameters"]

    tool = TOOLS.get(intent)

    if tool:
        return tool(parameters)
    else:
        print(f"Unknown tool: {intent}")
        return {
            "success": False,
            "message": f"Unknown tool: {intent}"
        }