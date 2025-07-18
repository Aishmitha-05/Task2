# -*- coding: utf-8 -*-
"""Task2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hlxus1TJk9JlNDHebAJShnGvl6x24Qm6
"""

pip install pipwin

!pip install pipwin

!pip install gTTS pydub

from gtts import gTTS
from pydub import AudioSegment

# Create a short speech file
text = "This is a sample audio for speech recognition testing."
tts = gTTS(text)
tts.save("sample.mp3")

# Convert to WAV format with correct specs
audio = AudioSegment.from_mp3("sample.mp3")
audio = audio.set_frame_rate(16000).set_channels(1)
audio.export("sample.wav", format="wav")

print("✅ Generated sample.wav successfully!")

!pip install SpeechRecognition

import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.AudioFile('sample.wav') as source:
    audio = recognizer.record(source)
    print("Transcription:", recognizer.recognize_google(audio))

# Step 1: Install required packages
!pip install gTTS pydub SpeechRecognition

# Step 2: Import libraries
from gtts import gTTS
from pydub import AudioSegment
import speech_recognition as sr

# Step 3: Generate sample audio
text = "This is a sample audio for speech recognition testing."
tts = gTTS(text)
tts.save("sample.mp3")

# Convert MP3 to WAV (16kHz, mono)
audio = AudioSegment.from_mp3("sample.mp3")
audio = audio.set_frame_rate(16000).set_channels(1)
audio.export("sample.wav", format="wav")

print("✅ sample.wav created.")

# Step 4: Transcribe the audio
recognizer = sr.Recognizer()
with sr.AudioFile("sample.wav") as source:
    audio_data = recognizer.record(source)
    try:
        result = recognizer.recognize_google(audio_data)
        print("🎧 Transcription:", result)
    except sr.UnknownValueError:
        print("Speech not recognized.")
    except sr.RequestError as e:
        print("API request error:", e)

# 1. Install required packages
!pip install gTTS pydub SpeechRecognition

# 2. Import libraries
from gtts import gTTS
from pydub import AudioSegment
import speech_recognition as sr

# 3. Generate sample.wav (you can also upload your own)
text = "This is a sample audio for speech recognition testing."
tts = gTTS(text)
tts.save("sample.mp3")

# Convert to proper .wav
audio = AudioSegment.from_mp3("sample.mp3")
audio = audio.set_frame_rate(16000).set_channels(1)
audio.export("sample.wav", format="wav")
print("✅ sample.wav created")

# 4. Speech-to-text transcription
recognizer = sr.Recognizer()
with sr.AudioFile("sample.wav") as source:
    audio = recognizer.record(source)
    try:
        result = recognizer.recognize_google(audio)
        print("🎧 Transcription:", result)
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
    except sr.RequestError as e:
        print("❌ API error:", e)

# 5. (Optional) Save to text file
with open("transcription.txt", "w") as f:
    f.write(result)

print("📄 Transcription saved to 'transcription.txt'")

from google.colab import files
files.download("sample.wav")          # Download audio
files.download("transcription.txt")   # Download result