import os
os.system("cls")

import cv2
import cv2.data

model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)
while True:
    is_valid, image = camera.read()
    if is_valid:
        faces = model.detectMultiScale(image, 1.1, 4, minSize=(30,30))
        for face in faces:
            x,y,w,h = face
            cv2.rectangle(image, (x,y), (x+w, y+h), color=(12,27,240), thickness=2)
        cv2.imshow('Kamera', image)
    else:
        print("Kamerada nosozlik")

    if cv2.waitKey(1) & 0xFF == 32:
        break