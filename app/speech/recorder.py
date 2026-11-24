
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from collections import deque
import time

SAMPLE_RATE = 16000
CHUNK_DURATION = 0.1

SILENCE_DURATION = 1.5
START_TIMEOUT = 10
MAX_RECORD_SECONDS = 25

THRESHOLD = 300
PRE_ROLL_CHUNKS = 5


def record_audio(filename="input.wav"):

    print("\n🎤 Speak now...")

    chunk_size = int(SAMPLE_RATE * CHUNK_DURATION)

    audio_chunks = []
    pre_roll = deque(maxlen=PRE_ROLL_CHUNKS)

    recording_started = False
    silence_chunks = 0
    volumes = []
    peaks = []

    required_silence_chunks = int(
        SILENCE_DURATION / CHUNK_DURATION
    )

    max_chunks = int(MAX_RECORD_SECONDS / CHUNK_DURATION)
    start_time = time.monotonic()

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
        blocksize=chunk_size
    ) as stream:

        for _ in range(max_chunks):

            audio, overflowed = stream.read(chunk_size)
            audio = audio.copy()

            audio_float = audio.astype(np.float32)

            volume = np.sqrt(np.mean(audio_float ** 2))
            peak = np.max(np.abs(audio_float))

            volumes.append(volume)
            peaks.append(peak)

            if not recording_started:

                pre_roll.append(audio)

                if volume > THRESHOLD:
                    recording_started = True
                    audio_chunks.extend(list(pre_roll))
                    print("🔴 Recording...")
                    silence_chunks = 0

            else:

                # Save EVERY audio chunk, including speech.
                audio_chunks.append(audio)

                if volume > THRESHOLD:
                    silence_chunks = 0
                else:
                    silence_chunks += 1

                if silence_chunks >= required_silence_chunks:
                    break

            if (
                not recording_started
                and time.monotonic() - start_time >= START_TIMEOUT
            ):
                print("No speech detected.")
                break

    if audio_chunks:
        audio_data = np.concatenate(audio_chunks, axis=0)
    else:
        audio_data = np.zeros((SAMPLE_RATE, 1), dtype="int16")

    write(filename, SAMPLE_RATE, audio_data)

    print("\n========== AUDIO DIAGNOSTICS ==========")
    print("Average RMS:", round(float(np.mean(volumes)), 2))
    print("Maximum RMS:", round(float(np.max(volumes)), 2))
    print("Peak level:", round(float(np.max(peaks)), 2))
    print(
        "Recording duration:",
        round(len(audio_data) / SAMPLE_RATE, 2),
        "seconds"
    )
    print("=======================================")

    print("✅ Recording completed!")
