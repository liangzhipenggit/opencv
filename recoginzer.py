import cv2 as cv
import numpy as np
import os

recogniizer=cv.face.LBPHFaceRecognizer_create()
recogniizer.read('traningmodel.yml')
faceCascade=cv.CascadeClassifier("fontface.xml")
font=cv.FONT_HERSHEY_DUPLEX;
id=0
names=['Uknow','James','Rain']
cam=cv.VideoCapture(0)
cam.set(3,400)
cam.set(4,600)
minW=0.1*cam.get(3);
minH=0.1*cam.get(4);
while True:
    ret,img=cam.read()
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=10, minSize=(int(minW), int(minH)))
    for (x,y,w,h) in  faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        id ,confidence= recogniizer.predict(gray[y:y+h, x:x+w])
        if(confidence < 50):
            id=id
            confidence="{0}%".format(round(100*confidence))
        else:
            id=0
            confidence="{0}%".format(round(100*confidence))
        cv.putText(img, str(names[id]), (x+5, y-5), font, 1, (255, 255, 255, 2))
    cv.imshow('camera', img)
    k=cv.waitKey(100)& 0x11
    if k==27:
        break
cam.release()
cv.destroyWindow()



