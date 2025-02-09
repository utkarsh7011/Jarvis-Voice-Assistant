import requests
import json
import pyttsx3
import speech_recognition

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

def latestnews(update_console):
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=1d38fc2203f74b2eb13ddebd84079e76",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=1d38fc2203f74b2eb13ddebd84079e76",
            "health" : "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=1d38fc2203f74b2eb13ddebd84079e76",
            "headlines from USA" :"https://newsapi.org/v2/top-headlines?country=us&apiKey=1d38fc2203f74b2eb13ddebd84079e76",
            "sports" :"https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=1d38fc2203f74b2eb13ddebd84079e76",
            "technology" :"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=1d38fc2203f74b2eb13ddebd84079e76"
}
    url = None
    update_console("Which field of news would you prefer, sir? The options are:")
    speak("Which field of news would you prefer, sir? The options are:")
    update_console("1. Headlines from USA")
    speak("1. Headlines from USA")
    update_console("2. Business")
    speak("2. Business")
    update_console("3. Health")
    speak("3. Health")
    update_console("4. Technology")
    speak("4. Technology")
    update_console("5. Sports")
    speak("5. Sports")
    update_console("6. Entertainment")
    speak("6. Entertainment")

    field = takeCommand()
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
    if url is None:
        update_console("Sorry, sir, I couldn't find any news category matching your request.")
        speak("Sorry, sir, I couldn't find any news category matching your request.")
        return
    try:
        news = requests.get(url).text
        news = json.loads(news)
        if'articles' in news and len(news['articles']) > 0:
            update_console("I have the first news update for you, sir.")
            speak("I have the first news update for you, sir.")
            for articles in news["articles"] :
                article = articles["title"]
                update_console(article)
                speak(article)
                news_url = articles["url"]
                update_console(f"for more info visit: {news_url}")
                speak("Shall I provide you with more updates, sir?")
                a = takeCommand()
                if str(a) == "yes":
                    pass
                else:
                    break
            update_console("That’s all for now, sir.")
            speak("That’s all for now, sir.")
        else:
            update_console("Sorry, sir, I couldn't find any news at the moment.")
            speak("Sorry, sir, I couldn't find any news at the moment.")
    except Exception as e:
        update_console(f"An error occurred while fetching the news: {str(e)}")
        speak(f"An error occurred while fetching the news: {str(e)}")
