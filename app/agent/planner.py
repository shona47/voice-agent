import json
from app.llm.qwen import ask_llm

def plan_task(user_input):

    prompt = f"""
You are the brain of an AI Voice Assistant.

Your job is to identify the user's intent.

Supported tools:
- email
- search
- reminder
- contact
- chat

Return ONLY JSON.

Example:

{{
    "intent":"email",
    "parameters":{{
        "recipient":"Rahul",
        "subject":"Meeting",
        "body":"Let's meet tomorrow."
    }}
}}

User:
{user_input}
"""

    response = ask_llm(prompt)

    try:
        return json.loads(response)
    except:
        print(response)
        return None