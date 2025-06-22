import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import messagebox
from langdetect import detect
import requests
import json
from datetime import datetime

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

TELEGRAM_TOKEN = config["telegram_token"]
CHAT_ID = config["chat_id"]

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Слушаю...")
        status_label.config(text="🎙️ Говорите...")
        audio = r.listen(source)

    try:
        raw_text = r.recognize_google(audio)
        lang = detect(raw_text)
        lang_code = {"ru": "ru-RU", "en": "en-US"}.get(lang, "en-US")
        recognized = r.recognize_google(audio, language=lang_code)
        return recognized
    except sr.UnknownValueError:
        speak("Не удалось распознать речь.")
        return None
    except sr.RequestError as e:
        speak("Ошибка соединения с сервисом.")
        return None

def save_note(text):
    filename = f"note_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Заметка\n\n{text}")
    return filename

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": f"Заметка:\n\n{text}"}
    response = requests.post(url, data=data)
    return response.status_code == 200

def run_notepad():
    recognized = recognize_speech()
    if recognized:
        note_text.insert(tk.END, recognized + "\n")
        filename = save_note(recognized)
        telegram_ok = send_to_telegram(recognized)
        status = f"Сохранено: {filename}"
        if telegram_ok:
            status += " | Отправлено в Telegram"
        status_label.config(text=status)
        speak("Заметка сохранена и отправлена.")
    else:
        status_label.config(text="Не удалось распознать речь.")

root = tk.Tk()
root.title("Умный голосовой блокнот")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

note_text = tk.Text(frame, height=10, width=60, font=("Arial", 12))
note_text.pack(pady=10)

btn = tk.Button(frame, text="Начать запись", font=("Arial", 12), command=run_notepad)
btn.pack(pady=5)

status_label = tk.Label(frame, text="Готов к работе", font=("Arial", 10))
status_label.pack(pady=5)

root.mainloop()
