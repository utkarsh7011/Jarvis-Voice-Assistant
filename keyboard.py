import pyttsx3
import speech_recognition 
import pyautogui
import win32api
import win32con

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

def play_video(update_console):
    pyautogui.press('k')
    update_console("The video has been played.")
    speak("The video has been played.")

def stop_video(update_console):
    pyautogui.press('k')
    update_console("The video has been stopped.")
    speak("The video has been stopped.")

def mute_video(update_console):
    pyautogui.press('m')
    update_console("The video is muted.")
    speak("The video is muted.")

def theatre_mode(update_console):
    pyautogui.press('t')
    update_console("Theatre mode has been activated.")
    speak("Theatre mode has been activated.")

def full_screen(update_console):
    pyautogui.press("f")
    update_console("Full Screen mode is enabled.")
    speak("Full Screen mode is enabled.")

def volumnup(update_console):
    for i in range(2):
        win32api.keybd_event(win32con.VK_VOLUME_UP, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)

def volumndown(update_console):
    for i in range(2):
        win32api.keybd_event(win32con.VK_VOLUME_DOWN, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)