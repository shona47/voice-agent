import json
from app.llm.qwen import ask_llm

def extract_email_details(command):

    prompt = f"""
You are an AI assistant.

Extract the email details from the user's request.

Return ONLY valid JSON.

Example:

{{
    "recipient":"",
    "subject":"",
    "body":""
}}

User Request:
{command}
"""

    response = ask_llm(prompt)

    try:
        return json.loads(response)

    except Exception:
        print("Couldn't parse JSON.")
        print(response)
        return None