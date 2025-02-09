import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe(update_console):
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        update_console("Good morning, My name is Jarvis. How may I assist you today?" )
        speak("Good morning, my name is Jarvis. How may I assist you today?" )
    elif 12 <= hour < 13:
        update_console("Good noon, My name is Jarvis. How may I assist you today?")
        speak("Good noon, my name is Jarvis. How may I assist you today?")
    elif 13 <= hour < 17:
        update_console("Good afternoon, I'm Jarvis. How can I be of service to you today?")
        speak("Good afternoon, I'm Jarvis. How can I be of service to you today?")
    else:
        update_console("Good evening, Sir. This is Jarvis. How may I assist you this evening?")
        speak("Good evening, Sir. This is Jarvis. How may I assist you this evening?")

def hii(update_console):
    update_console("Hello, Sir. How are you today?")
    speak("Hello, Sir. How are you today?")
def iamfine(update_console):
    update_console("I'm glad to hear that, Sir.")
    speak("I'm glad to hear that, Sir.")
def howru(update_console):
    update_console("I'm doing well, thank you for asking, Sir.")
    speak("I'm doing well, thank you for asking, Sir.")
def thankyou(update_console):
    update_console("It's my pleasure, Sir.")
    speak("It's my pleasure, Sir.")