import cv2
import cv2 as cv
import numpy as np
import pyautogui as mouse
#############
#print(mouse.position())
#x, y=mouse.position();
#mouse.moveTo(x-10, y+10)
#print(mouse.position())
#########

capture=cv.VideoCapture(0)
capture.set(3, 600)
capture.set(4, 600)
def initial_Main():
    while True:
        ret, img=capture.read();
        if ret:
            #fgmask = bgModel.apply(frame)
            img = _remove_background(img)
            # 图像预处理
            ycrcb = cv.cvtColor(img,cv2.COLOR_BGR2YCrCb)
            (_, cr, _) = cv2.split(ycrcb)
            cr1 = cv2.GaussianBlur(cr, (5, 5), 0)  # 高斯滤波
            _, skin = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # OTSU








            cv.imshow('Gueture', skin)


        if cv.waitKey(1) & 0xFF == ord('q'):
           break
    capture.release()
    cv2.destroyWindow()

def _remove_background(frame):
    fgbg = cv2.createBackgroundSubtractorMOG2()  # 利用BackgroundSubtractorMOG2算法消除背景
    # fgmask = bgModel.apply(frame)
    fgmask = fgbg.apply(frame)
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    # res = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res
if __name__ == "__main__":
    initial_Main()

