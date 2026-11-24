
import subprocess
import os
import sys
import sounddevice as sd
from scipy.io.wavfile import read

MODEL_PATH = "app/speech/models/en_US-lessac-medium.onnx"
OUTPUT_FILE = "app/speech/output.wav"


def speak(text):

    if not text or not text.strip():
        return

    try:
        os.makedirs("app/speech", exist_ok=True)

        command = [
            sys.executable,
            "-m",
            "piper",
            "-m", MODEL_PATH,
            "-f", OUTPUT_FILE
        ]

        subprocess.run(
            command,
            input=text.strip(),
            text=True,
            check=True,
            timeout=120
        )

        sample_rate, audio = read(OUTPUT_FILE)

        print("🔊 Speaking...")

        sd.play(audio, sample_rate)
        sd.wait()

        print("✅ Speech completed!")

    except subprocess.TimeoutExpired:
        print("TTS Error: Speech generation timed out.")

    except Exception as e:
        print("TTS Error:", e)
