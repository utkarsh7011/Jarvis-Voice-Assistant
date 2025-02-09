import cv2
import model_trainer
import os
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sample(update_console):
    cam= cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)
    detector = cv2.CascadeClassifier('Assets/Lock Detail/haarcascade_frontalface_default.xml')

    sample_dir = "Assets/Sample/PIC/"
    existing_files = os.listdir(sample_dir)
    existing_ids = [int(f.split('.')[1]) for f in existing_files if f.endswith('.jpg')]
    if existing_ids:
        Face_id = max(existing_ids) + 1
    else:
        Face_id = 1
    update_console(f"Sir, the assigned identification number is {Face_id}")
    speak(f"Sir, the assigned identification number is {Face_id}. I am now proceeding with the sample collection process. Kindly look directly at the camera to ensure the process is successful. Thank you for your cooperation.")
    count = 0

    while True:
        ret,img = cam.read()
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(converted_image,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            count +=1
            cv2.imwrite(f"{sample_dir}face.{Face_id}.{count}.jpg", converted_image[y:y+h, x:x+w])
            cv2.imshow('image', img)
        k = cv2.waitKey(10)
        if k ==27:
            break
        elif count >=10:
            break
    cam.release()
    cv2.destroyAllWindows()
    update_console("Sir, the sample has been successfully captured.")
    speak("Sir, the sample has been successfully captured. Please give me a moment while the model for your facial recognition is being prepared.")
    model_trainer.model(update_console)