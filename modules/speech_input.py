# --- File: modules/speech_input.py ---
import speech_recognition as sr

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Calibrate to ambient noise
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google's speech recognition
            said = recognizer.recognize_google(audio)
            print("You said:", said)
            return said
        except Exception as e:
            print("Speech recognition failed:", e)
            return None
