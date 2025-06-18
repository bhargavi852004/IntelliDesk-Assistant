import text_to_speech
import datetime
import webbrowser
import pyttsx3
import weather
import random
import os
import speech_recognition as sr
import wikipedia
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Action(data):
    if(data==None):
        text_to_speech.text_to_speech("I'm Not able to understand")
        return "I'm Not able to understand"
    user_data=data.lower()
    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is UB, A virtual Assistant")
        return "My name is UB, A virtual Assistant"
    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("Hi Mam,How can I help you?")
        return "Hi Mam,How can I help you?"
    elif "time now" in user_data:
        time=datetime.datetime.now()
        Time=(str)(time) +"Hour : ",(str)(time.minute) +"minutes"
        text_to_speech.text_to_speech(Time)
        return Time
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("Shutting down")
        return "Shutting down..."
    elif 'music' in user_data:
        music='C:\\Users\\Bhargavi Nagulapally\\Music'
        songs=os.listdir(music)
        sn=random.randint(0,39)
        os.startfile(os.path.join(music,songs[sn]))
    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        #https://www.youtube.com/results?search_query=
        text_to_speech.text_to_speech("youtube is ready for you")
        return "youtube is ready for you"
    elif "google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google is ready for you")
        return "google is ready for you"
    elif "weather" in user_data:
        res=weather.weather()
        text_to_speech.text_to_speech(res)
        return res
    elif 'open vscode' in user_data:
        vs_path="C:\\Users\\Bhargavi Nagulapally\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(vs_path)
    elif 'open pycharm' in user_data:
        pycharm="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\bin\\pycharm64.exe"
        os.startfile(pycharm)
    elif 'wikipedia' in user_data:
        speak('Searching wikipedia')
        user_data=user_data.replace("wikipedia","")
        results=wikipedia.summary(user_data,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif "bye" or "quit" in user_data:
        return "Yes,I'm Quitting Now"
    else:
        text_to_speech.text_to_speech("I'm Not able to understand")
        return "I'm Not able to understand"
    

