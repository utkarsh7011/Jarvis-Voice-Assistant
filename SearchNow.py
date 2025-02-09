import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

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

query = takeCommand().lower()


def searchGoogle(query,update_console):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        update_console("Based on my research through Google, I have gathered the following information, sir.")
        speak("Based on my research through Google, I have gathered the following information, sir.")
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            update_console(result)
            speak(result)
        except:
            update_console("Regrettably, there is no speakable output available at this time, sir.")
            speak("Regrettably, there is no speakable output available at this time, sir.")

def searchYoutube(query,update_console):
    if "youtube" in query:
        update_console("Here is the information I found on YouTube regarding your search, sir.") 
        speak("Here is the information I found on YouTube regarding your search, sir.") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        update_console("The task has been completed, sir.")
        speak("The task has been completed, sir.")

def searchWikipedia(query,update_console):
    if "wikipedia" in query:
        speak("Please allow me a moment to search for that on Wikipedia, sir.")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 3)
        update_console("According to the information provided by Wikipedia, sir.")
        speak("According to the information provided by Wikipedia, sir.")
        update_console(results)
        speak(results)