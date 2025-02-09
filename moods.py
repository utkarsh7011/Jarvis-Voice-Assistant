import webbrowser
import random
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

def music(update_console):
    c = (1,2,3,4,5)
    b = random.choice(c)
    if b==1:
        update_console("Playing Sucker for Pain by Lil Wayne.")
        speak("Playing Sucker for Pain by Lil Wayne.")
        webbrowser.open("https://youtu.be/-59jGD4WrmE?si=-30VHzKy8OwqQNqd")
    elif b==2:
        update_console("Playing Heathens by Twenty One Pilots")
        speak("Playing Heathens by Twenty One Pilots")
        webbrowser.open("https://youtu.be/nd2-q-WL07w?si=BLu1eZN5slQVyDfn")
    elif b==3:
        update_console("Playing Tobey by Eminem.")
        speak("Playing Tobey by Eminem.")
        webbrowser.open("https://youtu.be/CanCZktm0TQ?si=fnB0DLBv5pBwiwN5")
    elif b==4:
        update_console("Playing Him & I by G-Eazy.")
        speak("Playing Him & I by G-Eazy.")
        webbrowser.open("https://youtu.be/SA7AIQw-7Ms?si=Y_tj5Zabqe0hZy9i")
    elif b==5:
        update_console("Playing Godzilla by Eminem ")
        speak("Playing Godzilla by Eminem ")
        webbrowser.open("https://youtu.be/r_0JjYUe5jo?si=CQRQiun58LYgXC73")

def jokes(update_console):
    c = (1,2,3,4,5,6,7,8,9,10)
    b = random.choice(c)
    if b==1:
        update_console("have you ever heard of reverse exorcism")
        speak("have you ever heard of reverse exorcism")
        speak("")
        update_console("it's when the devil tells the priest to pull out of the child")
        speak("it's when the devil tells the priest to pull out of the child")
    elif b==2:
        update_console("what's the difference between children and basket")
        speak("what's the difference between children and basket")
        speak("")
        update_console("the basket don't cry when you put a sausage in it")
        speak("the basket don't cry when you put a sausage in it")
    elif b==3:
        update_console("Gender Equality")
        speak("Gender Equality")
        speak("")
    elif b==4:
        update_console("do you know i named my dog awesome.")
        speak("do you know i named my dog awesome.")
        speak("")
        update_console("so i can tell people im fucking awesome")
        speak("so i can tell people im fucking awesome")
    elif b==5:
        update_console("what's the difference between Gordan ramsay and Drake")
        speak("what's the difference between Gordan ramsay and Drake")
        speak("")
        update_console("Gordan has a soft spot for children")
        speak("Gordan has a soft spot for children")
    elif b==6:
        update_console("Dark humor is like a child with cancer")
        speak("Dark humor is like a child with cancer")
        speak("")
        update_console("it never gets old")
        speak("it never gets old")
    elif b==7:
        update_console("A guy walks into a bars with a 44 magnum and yells, who the fuck fucked my wife ")
        speak("A guy walks into a bars with a 44 magnum and yells, who the fuck fucked my wife ")
        update_console("Everbody's silent for a moment then the guy in the back of the bar says, Mate you ain't got enough bullets")
        speak("Everbody's silent for a moment then the guy in the back of the bar says, Mate you ain't got enough bullets")
    elif b==8:
        update_console("black people drive on the left side of the road")
        speak("black people drive on the left side of the road")
        speak("")
        update_console("because they don't have any rights")
        speak("because they don't have any rights")
    elif b==9:
        update_console("whats the difference between black people and rainbow people")
        speak("whats the difference between black people and rainbow people")
        speak("")
        update_console("at least black got accepted")
        speak("at least black got accepted")
    elif b==10:
        update_console("Do you know why the tower of pisa is leaning")
        speak("Do you know why the tower of pisa is leaning")
        speak("")
        update_console("Because it has better reflexes than the twin tower")
        speak("Because it has better reflexes than the twin tower")