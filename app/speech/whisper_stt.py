
import whisper

print("Loading Whisper model...")

model = whisper.load_model("base")

print("Whisper Ready!")


def transcribe_audio(audio_file="input.wav"):

    try:
        result = model.transcribe(
            audio_file,
            language="en",
            task="transcribe",
            fp16=False,
            beam_size=5,
            condition_on_previous_text=False,
            initial_prompt=(
                "This is a conversation with a voice AI personal assistant. "
                "Technical words include Whisper, Qwen, Piper, Python, "
                "machine learning, artificial intelligence, LLM, "
                "speech recognition, and voice assistant."
            )
        )

        text = result["text"].strip()

        return text

    except Exception as e:
        print("Transcription Error:", e)
        return ""
