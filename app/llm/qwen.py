
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "qwen2.5:1.5b"

SYSTEM_PROMPT = """
You are a helpful and intelligent AI personal assistant.

Follow these rules:
1. Give technically accurate and relevant answers.
2. Explain concepts in simple, beginner-friendly English.
3. Avoid repeating the same information.
4. Do not invent features or capabilities of technologies.
5. Use examples when they help understanding.
6. Keep answers concise but informative.
7. For technical questions, explain the actual working
   of the technologies involved.
8. Never confuse speech recognition, language generation,
   and text-to-speech.
9. Respond naturally and conversationally.
"""


def ask_llm(prompt):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "system": SYSTEM_PROMPT,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.4
            }
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"].strip()
