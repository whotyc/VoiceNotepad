import speech_recognition as sr
import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech(lang='ru-RU'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите...")
        speak("Слушаю вас.")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language=lang)
        print("Распознано:", text)
        speak("Вы сказали: " + text)
        return text
    except sr.UnknownValueError:
        print("Не удалось распознать речь.")
        speak("Не удалось распознать речь.")
    except sr.RequestError as e:
        print(f"🔌 Ошибка сервиса: {e}")
        speak("Ошибка соединения с сервисом распознавания.")
    return None

def save_text(text):
    filename = f"note_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Сохранено в {filename}")
    speak("Заметка сохранена.")

if __name__ == "__main__":
    print("Умный блокнот запущен. Нажмите Ctrl+C для выхода.")
    speak("Умный блокнот запущен.")

    while True:
        try:
            result = recognize_speech()
            if result:
                save_text(result)
        except KeyboardInterrupt:
            print("\nДо встречи!")
            speak("До встречи!")
            break
