def chat_tool(parameters):
    message = parameters.get("message", "")

    if not message:
        return {
            "success": False,
            "message": "I couldn't understand your question."
        }

    from app.llm.qwen import ask_llm

    response = ask_llm(message)

    return {
        "success": True,
        "message": response
    }