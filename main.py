import pyttsx3
import speech_recognition
import requests
import asyncio
import datetime
import os
from requests import get
from PIL import ImageGrab
import sys
import time
import cv2
import webbrowser
from plyer import notification
from bs4 import BeautifulSoup
import speedtest
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer , QTime,QDate,Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from SearchNow import searchGoogle, searchWikipedia,searchYoutube
from keyboard import stop_video,play_video,theatre_mode,full_screen,volumndown,volumnup,mute_video
from GreetMe import greetMe,iamfine,hii,howru,thankyou
from messages import sendEmailMessage,sendwhatsappMessage
from moods import jokes, music
from folderopening import Zombie_game
from Dictapp import openappweb,closeappweb
from Detection import Detector
from JarvisGui import Ui_JarvisUI
import Sample

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def countdown(seconds):
    for i in range(seconds, 1, -1):
        engine.say(str(i))
        engine.runAndWait()
        time.sleep(1)

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()
    
    def update_console(self, message):
        app = QApplication.instance()
        if app is not None:
            main_window = app.main_window
            if main_window is not None:
                main_window.update_console(message)
        else:
            self.update_console(message)

    def update_and_speak(self, message):
        self.update_console(message)
        speak(message)

    def takeCommand(self):
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            self.update_console("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source,0,8)
        try:
            self.update_console("Understanding..")
            self.query  = r.recognize_google(audio,language='en-in')
            self.update_console(f"Command: {self.query}\n")
        except Exception as e:
            self.update_console("Say that again")
            return "None"
        return self.query
    
    def TaskExecution(self):
        greetMe(self.update_console)
        while True:
                    self.query = self.takeCommand().lower()

                    if "go to sleep" in self.query:
                        self.update_and_speak("Ok sir , You can call me anytime")
                        break 

                    elif "schedule my day" in self.query:
                        self.update_and_speak("Would you like to clear the old tasks? Please confirm by responding with YES or NO.")
                        self.query = self.takeCommand().lower()
                        
                        with open("tasks.txt", "w" if "yes" in self.query else "a") as file:
                            self.update_and_speak("How many tasks would you like to schedule?")
                            no_tasks = int(self.takeCommand())

                            for i in range(no_tasks):
                                self.update_and_speak("Please tell me the task.")
                                task = self.takeCommand()
                                file.write(f"{i}. {task}\n")
                                self.update_and_speak("The task has been added to your schedule.")
                        
                        self.update_and_speak("The day has been scheduled properly.")

                    elif "show my schedule" in self.query:
                        with open("tasks.txt","r") as file:
                            content = file.read()
                            self.update_and_speak(f"Here is your schedule {content}")
                        
                    elif "translate" in self.query:
                        from Translator import translate
                        self.query = self.query.replace("jarvis","")
                        self.query = self.query.replace("translate","")
                        translate(self.query,self.update_console)

                    elif "internet speed" in self.query:
                        wifi  = speedtest.Speedtest()
                        upload_net = wifi.upload()/1048576      
                        download_net = wifi.download()/1048576
                        upload_net_formatted = "{:.2f}".format(upload_net)
                        download_net_formatted = "{:.2f}".format(download_net)
                        self.update_and_speak("Wifi Upload Speed is", upload_net)
                        self.update_and_speak("Wifi download speed is ",download_net)

                    elif "ipl score" in self.query:
                        url = "https://www.cricbuzz.com/"
                        page = requests.get(url)
                        soup = BeautifulSoup(page.text,"html.parser")
                        team_scores = soup.find_all(class_="cb-ovr-flo")
                        if len(team_scores) >= 11:
                            team1 = team_scores[0].get_text()
                            team2 = team_scores[1].get_text()
                            team1_score = team_scores[8].get_text()
                            team2_score = team_scores[10].get_text()
                            self.update_and_speak(f"{team1} has scored {team1_score}. {team2} has scored {team2_score}.")
                            notification.notify(
                                title="IPL SCORE :- ",
                                message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
                                timeout=10
                            )
                        else:
                            self.update_and_speak("Unable to retrieve scores.")                    

                    elif "movie" in self.query:
                        from folderopening import movie
                        movie(self.update_console)

                    elif "take screenshot" in self.query:
                        timestamp = time.strftime("Screenshot %d%m%Y")
                        sequence_number = 1
                        filename = f"Assets/Images/Screenshot/{timestamp} {sequence_number}.jpg"
                        while os.path.exists(filename):
                            sequence_number += 1
                            filename = f"Assets/Images/Screenshot/{timestamp} {sequence_number}.jpg"
                        im = ImageGrab.grab()
                        im.save(filename)
                        self.update_and_speak("Done sir")

                    elif "click picture" in self.query  or "take picture" in self.query:
                        self.update_and_speak("The picture will be taken in 5 seconds")
                        countdown(4)
                        self.update_and_speak("Smile Please")
                        cap = cv2.VideoCapture(0)
                        ret, frame = cap.read()
                        if ret:
                            cv2.imshow("Captured Image", frame)
                            timestamp = time.strftime("Captured Image")
                            sequence_number = 1
                            filename = f"Assets/Images/Captured/{timestamp} {sequence_number}.jpg"
                            while os.path.exists(filename):
                                sequence_number += 1
                                filename = f"Assets/Images/Captured/{timestamp} {sequence_number}.jpg"
                            cv2.imwrite(filename, frame)
                            cap.release()
                            cv2.destroyAllWindows()

                    elif "hello" in self.query:
                        hii(self.update_console)
                    elif "i am fine" in self.query:
                        iamfine(self.update_console)
                    elif "how are you" in self.query:
                        howru(self.update_console)
                    elif "thank you" in self.query:
                        thankyou(self.update_console)

                    elif "upset" in self.query or "favourite" in self.query:
                        self.update_and_speak("The playlist with your favorite songs is now on, Sir!")
                        music(self.update_console)

                    elif "jokes" in self.query or "funny" in self.query:
                        self.update_and_speak("I may only know a few jokes, but here it is")
                        jokes(self.update_console) 

                    elif "stop" in self.query:
                        stop_video(self.update_console)

                    elif "play" in self.query:
                        play_video(self.update_console)

                    elif "mute" in self.query:
                        mute_video(self.update_console)

                    elif "theatre" in self.query:
                        theatre_mode(self.update_console)

                    elif "fullscreen" in self.query or "full screen" in self.query:
                        full_screen(self.update_console)

                    elif "volume up" in self.query:
                        volumnup()
                        self.update_and_speak("The volume has been increased.")

                    elif "volume down" in self.query:
                        volumndown()
                        self.update_and_speak("The volume has been decreased.")

                    elif "books" in self.query:
                        from Books import recommend_books
                        recommend_books(self.update_console)

                    elif "open" in self.query:
                        openappweb(self.query,self.update_console)

                    elif "close" in self.query:
                        closeappweb(self.query,self.update_console)

                    elif "google" in self.query:
                        searchGoogle(self.query,self.update_console)

                    elif "youtube" in self.query:
                        searchYoutube(self.query,self.update_console)

                    elif "wikipedia" in self.query:
                        searchWikipedia(self.query,self.update_console)

                    elif "news" in self.query:
                        from NewsRead import latestnews
                        latestnews(self.update_console)

                    elif "calculate" in self.query:
                        from Calculatenumbers import Calc
                        self.query = self.query.replace("calculate","")
                        self.query = self.query.replace("Jarvis","")
                        Calc(self.query,self.update_console)

                    elif "whatsapp" in self.query:
                        sendwhatsappMessage(self.update_console)

                    elif "email" in self.query:
                        sendEmailMessage(self.update_console)

                    elif "ip address" in self.query or "IP adress" in self.query:
                        ip = get('https://api.ipify.org').text
                        self.update_and_speak(f"The IP address associated with your device is {ip}")

                    elif "space research" in self.query:
                        url = "https://stars.chromeexperiments.com/"
                        webbrowser.open(url)
                        self.update_console(f"Opening {url}...")
                        self.update_and_speak("Please click the play button located at the top left to begin the animation. You can use your fingers to zoom in and zoom out")

                    elif "temperature" in self.query  or "weather" in self.query:
                        search = ""+ self.query
                        url = f"https://www.google.com/search?q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        self.update_and_speak(f"The temperature at the moment is {temp}")

                    elif "set alarm" in self.query:
                        self.update_and_speak("Sir, could you please provide the time so I can set the alarm accordingly?")
                        tt = self.takeCommand()
                        tt = tt.replace("set alarm to","")
                        tt = tt.replace(".","")
                        tt = tt.replace("jarvis","")
                        tt = tt.replace("set an alarm","")
                        tt = tt.replace(" and ",":")
                        tt = tt.upper()
                        import alarm
                        alarm.alarm(tt,self.update_console)

                    elif "the date" in self.query:
                        import Date
                        Date.main(self.update_console)

                    elif "the time" in self.query:
                        strTime = datetime.datetime.now().strftime("%H:%M")
                        self.update_and_speak(f"Sir, the current time is {strTime}")

                    elif "good bye" in self.query or "goodbye" in self.query:
                        self.update_and_speak("Thank you, Sir. Wishing you a pleasant time. Goodbye.")
                        exit()

                    elif "remember that" in self.query:
                        rememberMessage = self.query.replace("remember that","")
                        rememberMessage = self.query.replace("Jarvis","")
                        self.update_and_speak("You told me that"+rememberMessage)
                        remember = open("Remember.txt","a")
                        remember.write(rememberMessage)
                        remember.close()
                        
                    elif "what do you remember" in self.query:
                        remember = open("Remember.txt","r")
                        self.update_and_speak("As per your previous instructions" + remember.read())

                    elif "shutdown" in self.query or "shut down" in self.query:
                        self.update_and_speak("Do you confirm that you would like to shut down? Please respond with 'Yes' or 'No.")
                        response = self.takeCommand()
                        if response == "yes":
                            self.update_and_speak("Access has been granted. Proceeding with system shutdown.")
                            os.system("shutdown /s /t 1")
                        elif response == "no":
                            self.update_and_speak("Access is restricted. Please try again.")
                            break

                    elif "restart" in self.query:
                        self.update_and_speak("Do you confirm that you would like to restart? Kindly respond with 'Yes' or 'No.")
                        response = self.takeCommand()
                        if response == "yes":
                            self.update_and_speak("Access has been granted. Proceeding with system restart.")
                            os.system("shutdown /s /t 5")
                        elif response == "no":
                            self.update_and_speak("Access is restricted. Please try again.")
                            break

                    elif "sleep mode" in self.query:
                        self.update_and_speak("Do you confirm that you would like to enter sleep mode? Kindly respond with 'Yes' or 'No.")
                        response = self.takeCommand()
                        if response == "yes":
                            self.update_and_speak("Access has been granted. Proceeding with sleep mode activation.")
                            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                        elif response == "no":
                            self.update_and_speak("Access is restricted. Please try again.")
                            break
#============================================================================Special Functions=============================================================================#
                    
                    elif "zombie game" in self.query:
                        folder_path = "DOOM Game"
                        file_name = "main.py"
                        Zombie_game(folder_path,file_name,self.update_console)
                        self.update_console("I sincerely hope the experience was enjoyable for you.")

                    elif "security mode"in self.query:
                        self.update_and_speak("Security mode has been successfully initiated.")
                        Sample.sample(self.update_console)

                    elif "generate" in self.query:
                        from Generation_of_image import generate_image
                        self.update_and_speak("Could you please provide the details or the prompt for the image you'd like me to create? I will do my best to ensure it is high-quality and accurate.")
                        prompt = self.takeCommand()
                        self.update_and_speak("I would appreciate a moment of your time.")
                        asyncio.run(generate_image(prompt,self.update_console))
                        self.update_console("Image Generated")

                    elif "start detection" in self.query or "detection mode" in self.query:
                        self.update_and_speak("Detection mode has been successfully initiated.")
                        videoPath = 0
                        configPath = os.path.join("model_data","ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt")
                        modelPath = os.path.join("model_data","frozen_inference_graph.pb")
                        classesPath = os.path.join("model_data","coco.names")
                        detector = Detector(videoPath,configPath,modelPath,classesPath)
                        detector.onVideo()
                        self.update_and_speak("Detection mode has been successfully terminated.")

#==========================================================================Gui-Multithreading=========================================================================#

startExecution = MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.terminal_output = self.ui.terminalOutputBox

    def update_console(self, message):
        self.terminal_output.appendPlainText(message)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("Assets/Images/Interface/Jarvis2.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Assets/Images/Interface/Jarvis1.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
#==============================================================================FaceLock===============================================================================#

if __name__ =="__main__":
    
    speak("Verification process initiated.")
    def capture_and_save_image(image, folder_path, sequence_number):
        timestamp = time.strftime("%d%m%Y %I%M%p")
        image_name = os.path.join(folder_path, f'Unlock Image {timestamp} {sequence_number}.jpg')
        while os.path.exists(image_name):
            sequence_number += 1
            image_name = os.path.join(folder_path, f'Unlock Image {timestamp} {sequence_number}.jpg')
        cv2.imwrite(image_name, image)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = 'Assets/Lock Detail/haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font =cv2.FONT_HERSHEY_SIMPLEX
    
    id = 2
    names = ['','Harsh']
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4,480)
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    
    Folder_path = 'Assets/Lock Detail/Unlock Detail/'
    sequence_number = 1
    while True:
        ret,img = cam.read()
        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(converted_image, scaleFactor=1.2, minNeighbors= 5, minSize = (int(minW),int(minH)))
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)
            id,accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])
            if(accuracy<100):
                id = names[id]
                accuracy = "{0}%".format(round(100-accuracy))
                cam.release()
                cv2.destroyAllWindows()
                capture_and_save_image(img, Folder_path, sequence_number)
                sequence_number += 1
                speak("Authorization confirmed.")
                app = QApplication(sys.argv)
                jarvis = Main()
                app.main_window = jarvis
                jarvis.show()
                exit(app.exec_()) 
            else:
                id = "unknown"
                accuracy = "{0}%".format(round(100-accuracy))
            cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
            cv2.putText(img, str(accuracy),(x+5,y+h-5),font,1,(255,255,0),1)

        cv2.imshow('camera',img)
        k = cv2.waitKey(10) & 0xff
        if k ==27:
            break
    
    cam.release()
    cv2.destroyAllWindows()
#=================================================================================End=================================================================================#