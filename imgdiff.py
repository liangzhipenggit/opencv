from skimage  import io as si
import  numpy as np
import  scipy as sp
import  matplotlib.pyplot as mp
import argparse
import imutils
import cv2 as cv
from skimage.metrics import structural_similarity as compare_ssim
def compare(imageA, imageB):
    grayA = cv.cvtColor(imageA, cv.COLOR_BGR2GRAY)
    grayB = cv.cvtColor(imageB, cv.COLOR_BGR2GRAY)
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8") #相似度
    # print("SSIM: {}".format(score))
    thresh = cv.threshold(diff, 0, 255,
    cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
    cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL,
    cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts[0]:
        (x, y, w, h) = cv.boundingRect(c)
        cv.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return imageB







