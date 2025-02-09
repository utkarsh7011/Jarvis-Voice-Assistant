import pywhatkit
import pyttsx3
import datetime
import platform
import urllib.parse
import speech_recognition
import webbrowser
import os 
from datetime import timedelta
from datetime import datetime

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

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendwhatsappMessage(update_console):
    update_console("Could you please provide the number, sir?")
    speak("Could you please provide the number, sir?")
    a = takeCommand()
    a = '+91' + a
    update_console(a)
    update_console("Could you please let me know what message I should send via WhatsApp, sir?")
    speak("Could you please let me know what message I should send via WhatsApp, sir?")
    message = takeCommand()
    update_console(message)
    pywhatkit.sendwhatmsg(a,message,time_hour=strTime,time_min=update)
    
def sendEmailMessage(update_console):
    update_console("Would you be able to share the email address, sir, without the '@gmail.com'?")
    speak("Would you be able to share the email address, sir, without the '@gmail.com'?")
    email_address = takeCommand().strip().replace(" ", "")
    update_console(email_address)
    if not email_address.endswith("@gmail.com"):
        email_address += "@gmail.com"
    update_console("Could you please let me know what message I should write in the email, sir?")
    speak("Could you please let me know what message I should write in the email, sir?")
    message_content = takeCommand()
    update_console(message_content)
    subject = "Your Subject Here"
    mailto_link = f"mailto:{email_address}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(message_content)}"
    current_os = platform.system()
    try:
        if current_os == 'Windows':
            os.startfile(mailto_link)
        elif current_os == 'Darwin':  # macOS
            os.system(f"open '{mailto_link}'")
        elif current_os == 'Linux':
            os.system(f"xdg-email '{mailto_link}'")
        else:
            webbrowser.open(mailto_link)
    except Exception as e:
        update_console(f"Apologies,Error: {str(e)}")
        speak(f"Apologies, sir, the mail application could not be opened due to an error: {str(e)}")
    update_console("The email client has been successfully opened, sir.")
    speak("The email client has been successfully opened, sir, with the necessary details pre-filled.")