import pyttsx3
import datetime
import pygame

pygame.mixer.init()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def alarm(Timing, update_console):
    altime = datetime.datetime.strptime(Timing, "%I:%M %p")
    Horeal = altime.hour
    Mireal = altime.minute
    update_console(f"Alarm set for {Timing}")
    speak(f"The alarm has been successfully set for {Timing}")
    while True:
        now = datetime.datetime.now()
        if Horeal == now.hour and Mireal == now.minute:
            update_console("Alarm is running")
            pygame.mixer.music.load("Assets/Music/Harley Quinn.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            break
if __name__ == '__main__':
    alarm('5:53 PM')
