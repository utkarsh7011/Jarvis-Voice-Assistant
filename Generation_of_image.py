import requests
from random import randint
import asyncio
import os
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

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {open('huggingface').read()}"}

async def query(payload, update_console):
    try:
        response = await asyncio.to_thread(requests.post, API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.content
    except Exception as e:
        update_console(f"Error occurred during API request: {e}")
        speak("Apologies, sir. There seems to be an error.")
        return None

async def generate_image(prompt: str,update_console):
    serial_number = 1
    while os.path.exists(f"Assets/Images/Gererated image/image_{serial_number}.jpg"):
        serial_number += 1
    tasks = []
    for _ in range(3):
        payload = {
            "inputs": f"{prompt} seed={randint(0, 100000)}",
        }
        task = asyncio.create_task(query(payload,update_console))
        tasks.append(task)
    image_bytes_list = await asyncio.gather(*tasks)
    for i, image_bytes in enumerate(image_bytes_list):
        if image_bytes:
            with open(f"Assets/Images/Gererated image/image_{serial_number + i}.jpg", "wb") as f:
                f.write(image_bytes)
    update_console("Sir, I have completed the image you requested, and it is now ready for your inspection.")
    speak("Sir, I have completed the image you requested, and it is now ready for your inspection.")
