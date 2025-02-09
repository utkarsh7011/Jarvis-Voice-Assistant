import pyautogui
import webbrowser
import pyttsx3
from time import sleep
import psutil
import subprocess

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def openappweb(query, update_console):
    speak("Understood, sir. Launching the application now.")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")

    elif "camera" in query:
        try:
            subprocess.Popen(["start", "microsoft.windows.camera:"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "command prompt" in query:
        try:
            subprocess.Popen(["start", "cmd.exe"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "paint" in query:
        try:
            subprocess.Popen(["start", "mspaint.exe"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "microsoft word" in query:
        try:
            subprocess.Popen(["start", "winword.exe"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "microsoft excel" in query:
        try:
            subprocess.Popen(["start", "excel.exe"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "vs code" in query:
        try:
            subprocess.Popen(["start", "code"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "chrome" in query:
        try:
            subprocess.Popen(["start", "chrome.exe"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "powerpoint" in query:
        try:
            subprocess.Popen(["start", "powerpnt.exe"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "media player" in query:
        try:
            subprocess.Popen(["start", "wmplayer.exe"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "file manager" in query:
        try:
            subprocess.Popen(["start", "explorer.exe"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "microsoft store" in query:
        try:
            subprocess.Popen(["start", "ms-windows-store:"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "settings" in query:
        try:
            subprocess.Popen(["start", "ms-settings:"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "photos" in query:
        try:
            subprocess.Popen(["start", "ms-photos:"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "microsoft edge" in query:
        try:
            subprocess.Popen(["start", "microsoft-edge:"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "whatsapp" in query:
        try:
            subprocess.Popen(["start", "whatsapp:"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "amazon prime" in query:
        try:
            subprocess.Popen(["start", "https://www.amazon.com/prime"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "netflix" in query:
        try:
            subprocess.Popen(["start", "https://www.netflix.com"], shell=True)
        except Exception as e:
            update_console("Error:", e)
    
    elif "spotify" in query:
        try:
            subprocess.Popen(["start","spotify.exe"], shell=True)
        except Exception as e:
            update_console("Error:", e)

    elif "notepad" in query:
        try:
            subprocess.Popen(["start","notepad.exe"], shell=True)
        except Exception as e:
            update_console("Error:", e)
        
def closeappweb(query, update_console):
    speak("Understood, sir. Closing the application now.")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        update_console("The tab has been closed, sir.")
        speak("The tab has been closed, sir.")
    elif "two tab" in query or "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        update_console("Two tabs have been closed, sir.")
        speak("Two tabs have been closed, sir.")
    elif "three tab" in query or "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        update_console("Three tabs have been closed, sir.")
        speak("Three tabs have been closed, sir.")
    elif "four tab" in query or "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        update_console("Four tabs have been closed, sir.")
        speak("Four tabs have been closed, sir.")
    elif "five tab" in query or "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        update_console("Five tabs have been closed, sir.")
        speak("Five tabs have been closed, sir.")
    elif "camera" in query:
        for proc in psutil.process_iter():
            if "Camera" in proc.name():
                proc.kill()
                update_console("The camera has been closed, sir.")
                speak("The camera has been closed, sir.")
                return
        update_console("The camera is not operational right now, sir.")
        speak("The camera is not operational right now, sir.")

    elif "command prompt" in query:
        for proc in psutil.process_iter():
            if "cmd.exe" in proc.name():
                proc.kill()
                update_console("Command Prompt has been closed, sir.")
                speak("Command Prompt has been closed, sir.")
                return
        update_console("Command Prompt is not operational right now, sir.")
        speak("Command Prompt is not operational right now, sir.")

    elif "paint" in query:
        for proc in psutil.process_iter():
            if "mspaint.exe" in proc.name():
                proc.kill()
                update_console("Paint has been closed, sir.")
                speak("Paint has been closed, sir.")
                return
        update_console("Paint is not operational right now, sir.")
        speak("Paint is not operational right now, sir.")

    elif "microsoft word" in query:
        for proc in psutil.process_iter():
            if "winword.exe" in proc.name():
                proc.kill()
                update_console("Microsoft Word has been closed, sir.")
                speak("Microsoft Word has been closed, sir.")
                return
        update_console("Microsoft Word has been closed, sir.")
        speak("Microsoft Word is not operational right now, sir.")

    elif "microsoft excel" in query:
        for proc in psutil.process_iter():
            if "excel.exe" in proc.name():
                proc.kill()
                update_console("Microsoft Excel has been closed, sir.")
                speak("Microsoft Excel has been closed, sir.")
                return
        update_console("Microsoft Excel is not operational right now, sir.")
        speak("Microsoft Excel is not operational right now, sir.")

    elif "vs code" in query:
        for proc in psutil.process_iter():
            if "code.exe" in proc.name():
                proc.kill()
                update_console("Visual Studio Code has been closed, sir.")
                speak("Visual Studio Code has been closed, sir.")
                return
        update_console("Visual Studio Code is not operational right now, sir.")
        speak("Visual Studio Code is not operational right now, sir.")

    elif "chrome" in query:
        for proc in psutil.process_iter():
            if "chrome.exe" in proc.name():
                proc.kill()
                update_console("Chrome has been closed, sir.")
                speak("Chrome has been closed, sir.")
                return
        update_console("Chrome is not operational right now, sir.")
        speak("Chrome is not operational right now, sir.")

    elif "powerpoint" in query:
        for proc in psutil.process_iter():
            if "powerpnt.exe" in proc.name():
                proc.kill()
                update_console("PowerPoint has been closed, sir.")
                speak("PowerPoint has been closed, sir.")
                return
        update_console("PowerPoint is not operational right now, sir.")
        speak("PowerPoint is not operational right now, sir.")

    elif "media player" in query:
        for proc in psutil.process_iter():
            if "wmplayer.exe" in proc.name():
                proc.kill()
                update_console("Media Player has been closed, sir.")
                speak("Media Player has been closed, sir.")
                return
        update_console("Media Player is not operational right now, sir.")
        speak("Media Player is not operational right now, sir.")

    elif "file manager" in query:
        for proc in psutil.process_iter():
            if "explorer.exe" in proc.name():
                proc.kill()
                update_console("file manager has been closed, sir.")
                speak("file manager has been closed, sir.")
                return
        update_console("file manager is not operational right now, sir.")
        speak("file manager is not operational right now, sir.")

    elif "microsoft store" in query:
        for proc in psutil.process_iter():
            if "ms-windows-store:" in proc.name():
                proc.kill()
                update_console("microsoft store has been closed, sir.")
                speak("microsoft store has been closed, sir.")
                return
        update_console("microsoft store is not operational right now, sir.")
        speak("microsoft store is not operational right now, sir.")

    elif "settings" in query:
        for proc in psutil.process_iter():
            if "ms-settings:" in proc.name():
                proc.kill()
                update_console("settings has been closed, sir.")
                speak("settings has been closed, sir.")
                return
        update_console("settings is not operational right now, sir.")
        speak("settings is not operational right now, sir.")

    elif "photos" in query:
        for proc in psutil.process_iter():
            if "ms-photos:" in proc.name():
                proc.kill()
                update_console("photos has been closed, sir.")
                speak("photos has been closed, sir.")
                return
        update_console("photos is not operational right now, sir.")
        speak("photos is not operational right now, sir.")

    elif "microsoft edge" in query:
        for proc in psutil.process_iter():
            if "microsoft-edge:" in proc.name():
                proc.kill()
                update_console("microsoft edge has been closed, sir.")
                speak("microsoft edge has been closed, sir.")
                return
        update_console("microsoft edge is not operational right now, sir.")
        speak("microsoft edge is not operational right now, sir.")

    elif "whatsapp" in query:
        for proc in psutil.process_iter():
            if "whatsapp:" in proc.name():
                proc.kill()
                update_console("whatsapp has been closed, sir.")
                speak("whatsapp has been closed, sir.")
                return
        update_console("whatsapp is not operational right now, sir.")
        speak("whatsapp is not operational right now, sir.")

    elif "spotify" in query:
        for proc in psutil.process_iter():
            if "spotify.exe" in proc.name():
                proc.kill()
                update_console("spotify has been closed, sir.")
                speak("spotify has been closed, sir.")
                return
        update_console("spotify is not operational right now, sir.")
        speak("spotify is not operational right now, sir.")

    elif "notepad" in query:
        for proc in psutil.process_iter():
            if "notepad.exe" in proc.name():
                proc.kill()
                update_console("notepad has been closed, sir.")
                speak("notepad has been closed, sir.")
                return
        update_console("notepad is not operational right now, sir.")
        speak("notepad is not operational right now, sir.")
