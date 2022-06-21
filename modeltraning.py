import cv2 as cv
import numpy as np
import os
import random
import PIL as pil

recognizer = cv.face.LBPHFaceRecognizer_create()
detector = cv.CascadeClassifier("fontface.xml" )
video_capture = cv.VideoCapture(0, cv.CAP_DSHOW)
path = 'radiate'
video_capture.set(3, 400)
video_capture.set(4, 600)
def data_initial():
    user_id = input('Please input your name:');
    count = 0
    cv.waitKey(0)
    while True:
        ret, img = video_capture.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1
            cv.imwrite('radiate/' + user_id + "." + str(random.randrange(1, 1000, 5)) + ".jpg", gray[y:y + h, x:x + w])
        k = cv.waitKey(100) & 0xff
        if k == 27:
            break
        elif 300 <= count:
            break
    cv.destroyAllWindows()


def traning (path):
    imgpaths = [os.path.join(path, f) for f in os.listdir(path)]
    facesamples = []
    ids = []
    for imgPath in imgpaths:
        pilImg = pil.Image.open(imgPath).convert('L')
        img_np = np.array(pilImg, 'uint8')
        temp = os.path.split(imgPath)
        id = int(os.path.split(imgPath)[-1].split('.')[0])
        faces = detector.detectMultiScale(img_np)
        for (x, y, w, h) in faces:
            facesamples.append(img_np[y:y + h, x:x + w])
            ids.append(id)
    return facesamples, ids


if __name__ == '__main__':
    data_initial()
    faces, ids = traning(path)
    recognizer.train(faces, np.array(ids))
    recognizer.write('traningmodel.yml')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
