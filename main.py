# --- main.py ---
from modules.voice_control import VoiceControl
from modules.speech_input import get_audio
from modules.actions import Actions
import pyttsx3
import keyboard as kb

# start speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_control = VoiceControl(engine, voices)
actions = Actions(engine)

  
while True:
    event = kb.read_event()
    if event.name == 'esc':
        break

    action = voice_control.handle_key_event(event)
    if not action:
        engine.say("What can I do for you?")
        engine.runAndWait()
        said = get_audio()

        if said:
            said = said.lower()
            if 'quit' in said or 'end' in said:
                engine.say("Goodbye")
                engine.runAndWait()
                break
            else:
                actions.handle_command(said)
        else:
            engine.say("I didn’t catch that")
            engine.runAndWait()
