from app.speech.recorder import record_audio
from app.speech.whisper_stt import transcribe_audio
from app.agent.planner import plan_task
from app.agent.executor import execute
from app.agent.confirmation import confirm


def main():

    # Step 1: Record user's voice
    record_audio()

    # Step 2: Convert speech to text
    text = transcribe_audio()

    print("\nYou said:")
    print(text)

    # Step 3: Let the LLM create an execution plan
    plan = plan_task(text)

    print("\nExecution Plan:")
    print(plan)

    # Step 4: Ask for confirmation
    if confirm(plan):
        execute(plan)
    else:
        print("❌ Action Cancelled.")


if __name__ == "__main__":
    main()