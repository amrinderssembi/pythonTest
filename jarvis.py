from email.mime import audio
from unittest import result
import pyttsx3
from playsound import playsound
from gtts import gTTS
import pyaudio
import speech_recognition as sr
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[11].id)
engine.setProperty('voice', voices[11].id)
engine.setProperty('rate', 100)


def Speak(audio):
    kk = gTTS(audio)
    kk.save('Assis.mp3')
    playsound('aman.mp3')




# def Speak(path):
#     playsound(path)


# Speak('welcomeback.mp3')
# def Takecommand():
#     print(sr.__version__)
#     recognizer = sr.Recognizer()
#     recognizer.energy_threshold = 300
#     res = sr.Microphone()
#     print(res)
# r = speech_recognition.Recognizer()


# print(sr.Microphone.list_microphone_names())
# with speech_recognition.Microphone() as source:
# print(":Listening...")
#     r.pause_threshold = 1
#     audio = r.listen(source)
# try:
#     print(":Recognizing...")
#     query = r.recognize_google(audio, language='en-in')
#     print(f":Your command:{query}\n")
# except:
#     return ""
# return query.lower()


# Takecommand()
# def YouTubeSearch(term):
#     result = 'https://www.youtube.com/results?search_query='+term
