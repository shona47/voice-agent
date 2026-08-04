import sounddevice as sd
from scipy.io.wavfile import write

SAMPLE_RATE = 16000
DURATION = 5

def record_audio(filename="input.wav"):
    print("🎤 Speak now...")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(filename, SAMPLE_RATE, audio)

    print("✅ Audio saved!")