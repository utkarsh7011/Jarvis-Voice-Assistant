from deep_translator import GoogleTranslator
import pyttsx3
import os
import time
from gtts import gTTS
from playsound import playsound
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def translate(query, update_console):
    translator_instance = GoogleTranslator()
    supported_languages = translator_instance.get_supported_languages(as_dict=True)
    
    speak("Of course, sir.")
    update_console(f"Supported Languages: {', '.join(supported_languages.keys())}")
    update_console("May I know the language for the translation, sir?")
    speak("May I know the language for the translation, sir?")
    target_language_name = takeCommand().lower()
    if target_language_name in supported_languages:
        target_language_code = supported_languages[target_language_name]
        try:
            translated_text = GoogleTranslator(source='auto', target=target_language_code).translate(query)
            tts = gTTS(text=translated_text, lang=target_language_code, slow=False)
            update_console(f"Translated Text: {translated_text}")
            audio_file = "Assets/Music/output.mp3"
            tts.save(audio_file)
            playsound(audio_file)
            time.sleep(2)
            os.remove(audio_file)
        except Exception as e:
            update_console(f"Unable to translate: {e}")
            speak(f"Sorry, sir, I can't speak the language but here's the translation")
            update_console(f"Translation: {translated_text}")
    else:
        update_console("Apologies, sir, but the language name is not valid. Could you please try again?")
        speak("Apologies, sir, but the language name is not valid. Could you please try again?")
