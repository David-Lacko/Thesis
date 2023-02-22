import cv2
import numpy as np
import time
import os
import sys
import argparse
import math
import json
import glob



#load webcam video

def load_webcam():
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    #
    # load image from file img/t.jpg
    # cap = cv2.imread('img/t.jpg')
    return cap

def show_webcam(cap ,mirror=False):
    while True:
        ret_val, img = cap.read()
        # img = cap
        if mirror:
            img = cv2.flip(img, 1)
        cany = canny(img)
        #img = square(img)
        cv2.imshow('my webcam', cany)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()

def canny(img):
    ksize = (5, 5)
    image = cv2.blur(img, ksize)
    canny = cv2.Canny(image, 180, 200)
    kernel1 = np.ones((5, 5), np.uint8)
    kernel2 = np.ones((4, 4), np.uint8)

    delate = cv2.dilate(canny, kernel1, iterations=1)
    erode = cv2.erode(delate, kernel2, iterations=1)
    return erode


def square(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 50, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    print("Number of contours detected:", len(contours))

    for cnt in contours:
        x1, y1 = cnt[0][0]
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(cnt)
            ratio = float(w) / h
            if ratio >= 0.9 and ratio <= 1.1:
                img = cv2.drawContours(img, [cnt], -1, (0, 255, 255), 3)
    return img

show_webcam(load_webcam(),mirror=True)


