from tkinter import *
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

root = Tk()
root.title("VOICE ASSISSTANT")
root.geometry("950x800")

engine = pyttsx3.init('sapi5')  # to take voice as input
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)  # 1,0 -> female & male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:  # MORNING
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am JARVIS. Please tell me how may I help you")


def takeCommand():
    # takes microphone input from users and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # seconds of non-speaking audio before a phrase is considered complete
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please. ")
        return "None"

    return query


if __name__ == '__main__':
    # speak("Hello! Today is a good day")
    wishme()
    while (True):
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia,")
            print(results)
            speak(results)

        elif 'open' and 'youtube' in query:
            print("OTaking you to Youtube...")
            webbrowser.open("youtube.com")

        elif 'open' and 'google' in query:
            print("Taking you to Google...")
            webbrowser.open("google.com")

        elif 'open' and 'stackoverflow' in query:
            print("Taking you to StackOverflow...")
            webbrowser.open("stackoverflow.com")

        elif 'play' and 'music' in query:
            r = random.randint(0, 2)
            music_dir = r'E:\Esha\Feel good\mp3'
            songs = os.listdir(music_dir)
            print('Playing a random song from your library, hope you like it :)', songs)
            os.startfile(os.path.join(music_dir, songs[r]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}")

        elif 'open' and 'code' in query:
            cpath = r"C:\Users\HP\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            print("Taking you to Visual Studio Code")
            os.startfile(cpath)

        elif 'quit' in query:
            print("Thank you for your time. See you again!")
            exit()

root.mainloop()
