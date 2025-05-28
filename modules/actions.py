# --- File: modules/actions.py ---
from web_service import translate, get_time, get_weather, get_israel_news, infow, youtube_play
from gtts import gTTS
import playsound
import tempfile
import os

class Actions:
    def __init__(self, engine):
        self.engine = engine

    def speak_hebrew(self, text):
        # Use gTTS to speak Hebrew text
        tts = gTTS(text=text, lang='iw')
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmpfile:
            filename = tmpfile.name
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

    def handle_command(self, said):
        if "translate" in said:
            text = said.replace("translate", "").strip()
            t = translate()
            translated = t.get_translate(text)
            if translated:
                self.engine.say(f"The translation of '{text}' to Hebrew")
                self.engine.runAndWait()
                self.speak_hebrew(translated)
                print(translated[::-1])  # Print RTL for console display

        elif "time in" in said:
            city = said.split("time in")[-1].strip()
            text = get_time(city)
            print(text)
            self.engine.say(text)
            self.engine.runAndWait()

        elif "weather in" in said:
            city = said.split("weather in")[-1].strip()
            text = get_weather(city)
            print(text)
            self.engine.say(text)
            self.engine.runAndWait()

        elif "news" in said:
            self.engine.say("Here is the latest Israeli news in Hebrew")
            self.engine.runAndWait()
            feed = get_israel_news()
            for entry in feed:
                print(entry.title[::-1])
                self.speak_hebrew(entry.title)

        elif "search" in said or "look for" in said:
            query = said.replace("look for", "").replace("search", "").strip()
            if query:
                info = infow()
                print(f"Searching {query} on Wikipedia...")
                result = info.get_info(query)
                self.engine.say(result)
                self.engine.runAndWait()
            else:
                self.engine.say("What should I search?")
                self.engine.runAndWait()

        elif "play" in said or "player" in said:
            query = said.replace("play", "").replace("player", "").strip()
            if query:
                print(f"Playing {query} on YouTube...")
                player = youtube_play()
                player.get_play(query)
            else:
                self.engine.say("What should I play?")
                self.engine.runAndWait()

        else:
            self.engine.say("You said: " + said)
            self.engine.runAndWait()
