import random
import speech_recognition
import pyttsx3
import requests
from time import sleep

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

GENRES = ["Action", "Thriller", "Romantic", "Adventure", "Mythological", "Haunted"]

def search_books_by_genre(genre,update_console):
    url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{genre}"
    response = requests.get(url)
    data = response.json()
    if 'items' in data:
        books = data['items'][:1]
        update_console(f"These are the {genre} Books:")
        speak(f"these are the {genre} Books:")
        for book in books:
            title = book['volumeInfo']['title']
            authors = book['volumeInfo'].get('authors', 'Unknown')
            description = book['volumeInfo'].get('description', 'No description available')
            update_console(f"The Title of the book is {title}")
            speak(f"The Title of the book is {title}")
            update_console(f"It is Authored by {', '.join(authors)}")
            speak(f"It is authored by {', '.join(authors)}")
            sleep(1)
            update_console(f"The book covers {description}")
            speak(f"The book covers {description}")
            speak("")

def recommend_books(update_console):
    genre = random.choice(GENRES)
    search_books_by_genre(genre, update_console)