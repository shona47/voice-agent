
import threading

from app.tools.reminder_checker import check_reminders
from app.speech.recorder import record_audio
from app.speech.whisper_stt import transcribe_audio
from app.speech.tts import speak

from app.agent.planner import plan_task
from app.agent.executor import execute
from app.agent.confirmation import confirm


def main():

    # Start reminder checker in background
    reminder_thread = threading.Thread(
        target=check_reminders,
        daemon=True
    )

    reminder_thread.start()

    print("\n======================================")
    print("🎙️  VOICE AI PERSONAL ASSISTANT")
    print("======================================")
    print("Assistant is ready...")
    print("Speak a command anytime.")
    print("Press Ctrl+C to stop.\n")

    # Welcome message
    speak("Hello! Your personal assistant is ready. How can I help you?")

    # Continuous assistant loop
    while True:

        try:
            # Step 1: Record user's voice
            record_audio()

            # Step 2: Convert speech to text
            text = transcribe_audio()

            # Ignore empty or silent recordings
            if not text or not text.strip():
                print("\nNo speech detected. Listening again...")
                continue

            print("\nYou said:")
            print(text)

            # Step 3: Create execution plan
            plan = plan_task(text)

            print("\nExecution Plan:")
            print(plan)

            # Check if LLM understood the request
            if plan is None:
                message = "Sorry, I could not understand your request."
                print(message)
                speak(message)
                continue

            # Step 4: Ask for confirmation
            if confirm(plan):

                # Step 5: Execute selected tool
                result = execute(plan)

                if result:
                    print("\n========== RESULT ==========")
                    print(result)

                    # Extract response message
                    if plan["intent"] == "search" and isinstance(result, dict):

                        search_results = result.get("results", [])

                        titles = [
                            item.get("title", "")
                            for item in search_results[:3]
                            if item.get("title")
                        ]

                        if titles:
                            response = (
                                 "I found some search results. "
                                 "Here are the top results: "
                                 + ". ".join(titles)
                                 + ". Full details are displayed in the terminal."
                            )
                        else:
                            response = "Search completed. Full details are displayed in the terminal."

                    elif isinstance(result, dict):
                        response = result.get("message", "Action completed successfully.")

                    else:
                        response = str(result)

                    # Speak the response
                    speak(response)

            else:
                message = "Okay, action cancelled."
                print(message)
                speak(message)

            print("\nListening for your next command...")

        except KeyboardInterrupt:

            print("\n\nVoice Assistant stopped.")
            break

        except Exception as e:

            print("\nError occurred:")
            print(e)

            speak("Sorry, something went wrong. Please try again.")

            print("\nContinuing assistant...")


if __name__ == "__main__":
    main()
