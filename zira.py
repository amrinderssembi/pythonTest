from http import server
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import webbrowser as web
import wikipedia
import os
from playsound import playsound
from gtts import gTTS
import multiprocessing
# import pyglet
import vlc
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[11].id)
engine.setProperty('voices', voices[11].id)
engine.setProperty('rate', 200)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("good morning!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("hello sir, please tell me how may i help you")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
        # speak(query)
        # engine.say(f"User said: {query}\n")
    except Exception:
        # print(e)

        print("please said that again....")
        return "None"
    return query


def googleSearch(term):
    result = 'https://www.google.com/search?q='+term
    web.open(result)


def YouTubeSearch(term):
    result = 'https://www.youtube.com/results?search_query='+term
    web.open(result)


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("amrinder.singh1@antiersolutions.com", "qwerty@997#")
    server.sendmail('amrinder.singh1@antiersolutions.com', to, content)
    server.close()


if __name__ == "__main__":

    # speak('Good morning amrinder singh')
    while True:
        query = takeCommand().lower()
        if("aman" in query):
            wishMe()
        if("wikipedia" in query):
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            web.open("youtube.com")

        elif "search on youtube" in query:
            # web.open("youtube.com")
            YouTubeSearch(query)
        elif "search on google" in query:
            # web.open("youtube.com")
            googleSearch(query)
        elif 'play music' in query:
            music_dir = "music"
            songs = os.listdir(music_dir)

            player = vlc.MediaPlayer("aman.mp3")
            player.play()
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        # elif 'open code' in query:
        #     codePath = '/usr/bin/code'
        #     # os.open(codePath)
        #     os.fdopen(codePath)
        elif 'email to' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "amrinder.singh@antiersolutions.com"
                sendEmail(to, content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send the email")
        elif 'ok thank' in query:
            speak("Welcome sir")
            quit()
        elif 'leave it' in query:
            speak("Ok sir")
            quit()
        elif 'thank you' in query:
            speak("Any time sir")
            quit()
