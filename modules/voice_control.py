# --- File: modules/voice_control.py ---
import pyttsx3

class VoiceControl:
    def __init__(self, engine, voices):
        self.engine = engine
        self.voices = voices
        self.rate_diff = 25  # Difference in speech rate adjustment

    def david_voice(self):
        # Switch to the first voice (assumed to be "David")
        self.engine.setProperty('voice', self.voices[0].id)
        self.engine.say("Voice changed to David")
        self.engine.runAndWait()

    def zara_voice(self):
        # Switch to the second voice (assumed to be "Zara")
        self.engine.setProperty('voice', self.voices[1].id)
        self.engine.say("Voice changed to Zara")
        self.engine.runAndWait()

    def slower(self):
        # Decrease speaking rate
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate - self.rate_diff)
        self.engine.say("I'm slower")
        self.engine.runAndWait()

    def faster(self):
        # Increase speaking rate
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate + self.rate_diff)
        self.engine.say("I'm faster")
        self.engine.runAndWait()

    def handle_key_event(self, event):
        # Only respond to key press down events
        if event.event_type != 'down':
            return False

        # Define key bindings for voice control
        actions = {
            'left': self.david_voice,
            'right': self.zara_voice,
            'down': self.slower,
            'up': self.faster
        }

        # Execute corresponding action if key is mapped
        action = actions.get(event.name)
        if action:
            action()
            return True
        return False
