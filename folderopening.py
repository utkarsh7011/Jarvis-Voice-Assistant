import pyttsx3
import speech_recognition
import os
import random
import subprocess

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def Zombie_game(folder_path,file_name,update_console):
    update_console("Welcome to the Doom Zombie Game. I hope you enjoy the experience.")
    speak("Welcome to the Doom Zombie Game. I hope you enjoy the experience.")
    os.chdir(folder_path)
    subprocess.Popen(["python",file_name])

def open_random_file(folder_path,update_console):
    files = os.listdir(folder_path)
    random_file = random.choice(files)
    file_name, _ = os.path.splitext(random_file)
    update_console(f"Playing {file_name}")
    speak(f"Playing {file_name}")
    file_path = os.path.join(folder_path, random_file)
    os.startfile(file_path)

def open_specific_file(folder_path, file_name,update_console):
    for file in os.listdir(folder_path):
        if file_name.lower() in os.path.splitext(file)[0].lower():
            update_console(f"Playing {os.path.splitext(file)[0]}")
            speak(f"Playing {os.path.splitext(file)[0]}")
            file_path = os.path.join(folder_path, file)
            os.startfile(file_path)
            return
    speak("Apologies, the specified file could not be found.")

def movie(update_console):
    folder_path = "C:/Users/wwwde/Videos/Movies/"
    update_console("Would you like me to recommend a movie for you, sir?")
    speak("Would you like me to recommend a movie for you, sir?")
    response = takeCommand()
    if "suggest me" in response:
        open_random_file(folder_path)
    elif "no" in response:
        update_console("Which movie would you prefer to watch, sir?")
        speak("Which movie would you prefer to watch, sir?")
        file_name = takeCommand()
        if file_name:
            open_specific_file(folder_path, file_name)
    else:
        update_console("Apologies, I wasn't able to fully understand. Could you please clarify which movie you would prefer to watch, sir?")
        speak("Apologies, I wasn't able to fully understand. Could you please clarify which movie you would prefer to watch, sir?")