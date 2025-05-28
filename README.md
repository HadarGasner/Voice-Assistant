# Voice-Assistant
smart voice assistant built with Python. It recognizes voice commands, speaks responses in English and Hebrew, fetches live information (weather, time, news), and supports search on Wikipedia and YouTube.


## 🚀 Features

- 🎤 Speech recognition using `speech_recognition`
- 🗣️ Text-to-speech with `pyttsx3` and `gTTS`
- 🌦️ Live weather and time using WeatherAPI
- 📰 Latest Israeli news via RSS (Ynet)
- 🌍 English to Hebrew translation
- 🔍 Wikipedia search via Selenium
- 📺 YouTube search and play
- ⌨️ Voice control via keyboard arrows

## 🧭 Keyboard Controls

| Key        | Action               |
|------------|----------------------|
| ← (left)   | Switch to David voice |
| → (right)  | Switch to Zara voice  |
| ↓ (down)   | Speak slower         |
| ↑ (up)     | Speak faster         |
| ESC        | Exit the assistant   |

## 📁 Project Structure

```
Voice Assistant/
├── main.py                 # Main control loop
├── web_service.py         # Web interaction: time, weather, Wikipedia, YouTube
├── requirements.txt        # Python dependencies
└── modules/
    ├── actions.py          # Handles spoken commands
    ├── speech_input.py     # Captures voice input
    └── voice_control.py    # Handles voice settings via keyboard
```

## 🛠️ Installation

```bash
pip install -r requirements.txt
```

## ▶️ Running the Assistant

```bash
python main.py
```

Make sure your microphone is connected and active.

## 🔧 Dependencies

Installed via `requirements.txt`, includes:
- `speechrecognition`, `pyaudio`
- `pyttsx3`, `gtts`, `playsound`
- `keyboard`, `selenium`, `webdriver-manager`
- `requests`, `feedparser`, `googletrans`

## 📌 Notes

- For Hebrew voice, `gTTS` is used instead of `pyttsx3`.
- For Wikipedia and YouTube search, Selenium will open a browser window.


