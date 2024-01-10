import speech_recognition as sr
import pyttsx3
from datetime import datetime

def get_date_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    current_date = now.strftime("%Y-%m-%d")
    return f"The current time is {current_time} and the date is {current_date}"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I did not understand.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

if __name__ == "__main__":
    speak("Hello! I am veronica,how can i help you?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I help you?")
        elif "time" in command:
            time_text = get_date_time()
            print(time_text)
            speak(time_text)
        elif "date" in command:
            date_text = get_date_time()
            print(date_text)
            speak(date_text)
        elif "exit" in command:
            speak("Goodbye! Have a great day.")
            break
