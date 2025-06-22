# VoiceNotepad

A Python voice notebook with speech recognition capabilities, automatic language detection, saving notes in Markdown, and sending them to Telegram. It has a simple graphical interface on Tkinter.

# Opportunities
- Speech recognition via microphone

- Automatic language detection (Russian/English)

- Saving a note in .md format

- Sending the text of a note to Telegram

- Graphical interface on Tkinter

# Installation
 1. Clone the repository:
```
git clone https://github.com/your-username/voice-notepad.git
cd voice-notepad
```

2. Install the dependencies:
```
pip install -r requirements.txt
```

# Setup
Create a config.json in the root of the project and add your Telegram bot data:
```json
{
  "telegram_token": "YOUR_TELEGRAM_BOT_TOKEN",
  "chat_id": "YOUR_CHAT_ID"
}
```

telegram_token — your bot's token received through BotFather.

chat_id — your Telegram chat ID (you can get it using any Telegram bot or manually)

# Using
```
python voice_notepad.py
```
In the window that opens, click the "Start recording" button and speak the text.
The recognized speech will be:

- displayed in the window

- saved to a file note_YYYYMMDD_HHMMSS.md

- sent to Telegram (if chat_id is specified)

# Requirements 
- SpeechRecognition dependencies — for speech recognition

- pyaudio — for recording audio

- pyttsx3 — for voice response

- tkinter — graphical interface

- langdetect — text language detection

- requests — sending messages to Telegram
