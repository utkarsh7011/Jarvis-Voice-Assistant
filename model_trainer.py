import cv2
import numpy as np
from PIL import Image
import os
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

path = "Assets/Sample/PIC/"

recognizer =  cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('Assets/Lock Detail/haarcascade_frontalface_default.xml')

def model(update_console):
    def Image_and_Labels(path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
        faceSamples=[]
        ids = []
        for imagePath in imagePaths:
            grey_img = Image.open(imagePath).convert('L')
            img_arr = np.array(grey_img,'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_arr)
            for (x,y,w,h) in faces:
                faceSamples.append(img_arr[y:y+h,x:x+w])
                ids.append(id)
        return faceSamples,ids
    faces,ids = Image_and_Labels(path)
    if not faces or not ids:
        update_console("Sir, I wanted to kindly remind you to collect the sample images before proceeding with the model training")
        speak("Sir, I wanted to kindly remind you to collect the sample images before proceeding with the model training")
    else:
        recognizer.train(faces, np.array(ids))
        recognizer.write('trainer/trainer.yml')
        update_console("Sir, the face lock model has been successfully trained.")
        speak("Sir, the face lock model has been successfully trained. Authorization for access through your facial recognition is now fully enabled.")