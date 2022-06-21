from time import time
import cv2 as cv
import os
 
#cascade=cv.CascadeClassifier('cascade.xml');
#img=cv.imread('122.jpg')
#img_gray=cv.cvtColor(img,cv2.COLOR_RGBA2GRAY)
#objects= cascade.detectMultiScale(img_gray)
#print(len(objects))
#img=cv2.rectangle(img,objects[0],(0,0,255))
#cv.imshow('title',img)
#cv.waitKey(0)
imges=os.listdir('cats')
for img in imges:
    img2=cv.imread('cats/'+img) 
    cv.imwrite('imgs/{}.jpg'.format(time()),img2)