import whisper

print("Loading Whisper model...")

model = whisper.load_model("base")

print("Whisper Ready!")

def transcribe_audio(audio_file="input.wav"):

    result = model.transcribe(audio_file)

    return result["text"]