
import json
from app.llm.qwen import ask_llm


def plan_task(user_input):

    prompt = f"""
You are the intent classifier for a voice AI personal assistant.

Classify the user's request into EXACTLY ONE supported intent.
Return ONLY valid JSON. No markdown or explanations.

SUPPORTED INTENTS:
email, search, reminder, history, memory, chat

CLASSIFICATION RULES (FOLLOW IN THIS ORDER):

1. EMAIL
Use email when the user wants to send, compose, or draft an email.

JSON:
{{
    "intent": "email",
    "parameters": {{
        "recipient": "...",
        "subject": "...",
        "body": "..."
    }}
}}

2. REMINDER
Use reminder when the user wants to create a reminder.

JSON:
{{
    "intent": "reminder",
    "parameters": {{
        "task": "...",
        "time": "..."
    }}
}}

3. MEMORY
Use memory when the user wants to store, retrieve, list, or delete
information from personal memory.

STORE examples:
- Remember that I like Python.
- Save my project details.
- Don't forget my preferences.

JSON:
{{
    "intent": "memory",
    "parameters": {{
        "action": "store",
        "content": "..."
    }}
}}

RETRIEVE examples:
- What is my favorite programming language?
- Which model does my project use?
- What did I tell you earlier?
- What technologies am I using in my voice assistant?

JSON:
{{
    "intent": "memory",
    "parameters": {{
        "action": "retrieve",
        "content": "{user_input}"
    }}
}}

LIST:
"What have you remembered about me?"

JSON:
{{
    "intent": "memory",
    "parameters": {{
        "action": "list"
    }}
}}

DELETE:
"Delete memory memory_2."

JSON:
{{
    "intent": "memory",
    "parameters": {{
        "action": "delete",
        "content": "memory_2"
    }}
}}

IMPORTANT:
Questions about the user's own information and previous conversations
must use memory retrieval, not search or chat.

4. SEARCH
Use search ONLY when the user explicitly requests internet information.

Examples:
- Search for the latest AI news.
- Find recent papers about computer vision.
- Look up the latest Python release.

JSON:
{{
    "intent": "search",
    "parameters": {{
        "query": "..."
    }}
}}

5. HISTORY
Use history when the user asks to see previous commands or actions.

JSON:
{{
    "intent": "history",
    "parameters": {{}}
}}

6. CHAT
Use chat for explanations, general knowledge, greetings,
and normal conversations that do not require personal memory
or internet search.

Examples:
- Explain how Whisper works.
- How do Qwen and Piper work together?
- Explain machine learning.
- Tell me a joke.
- What is the difference between CNN and RNN?

IMPORTANT CHAT EXAMPLE:

User: Explain how Whisper, Qwen, and Piper work together
Correct:
{{
    "intent": "chat",
    "parameters": {{
        "message": "{user_input}"
    }}
}}

Do NOT classify a normal explanation request as search.

FINAL CHECK:
- Personal information -> memory
- Explicit internet request -> search
- General explanation -> chat
- Send email -> email
- Set reminder -> reminder
- Previous commands -> history

USER REQUEST:
{user_input}
"""

    response = ask_llm(prompt)

    try:
        response = response.strip()

        if response.startswith("```"):
            response = response.replace("```json", "")
            response = response.replace("```", "")
            response = response.strip()

        plan = json.loads(response)

        allowed_intents = {
            "email", "search", "reminder",
            "history", "memory", "chat"
        }

        if plan.get("intent") not in allowed_intents:
            print("Invalid intent:", plan)
            return None

        if not isinstance(plan.get("parameters"), dict):
            print("Invalid parameters:", plan)
            return None

        return plan

    except Exception:
        print("\nInvalid JSON returned by LLM:\n")
        print(response)
        return None
