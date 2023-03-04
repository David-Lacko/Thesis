import numpy as np
import cv2
from bot.config import *

# Create a black image
img = np.zeros((800,800,3), np.uint8)

for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            cv2.rectangle(img,(i*100,j*100),(i*100+100,j*100+100),(255,255,255),-1)
        else:
            cv2.rectangle(img,(i*100,j*100),(i*100+100,j*100+100),(0,0,0),-1)

imag = img.copy()
bord = setup_bord
w = cv2.imread("./Img/W.png")
b = cv2.imread("./Img/B.png")
wq = cv2.imread('./Img/WQ.png')
bq = cv2.imread('./Img/BQ.png')
# set image size
w = cv2.resize(w, (80, 80))
b = cv2.resize(b, (80, 80))
wq = cv2.resize(wq, (80, 80))
bq = cv2.resize(bq, (80, 80))
# replace black pixels with white pixels
w[np.where((w==[0,0,0]).all(axis=2))] = [255,255,255]
b[np.where((b==[0,0,0]).all(axis=2))] = [255,255,255]
wq[np.where((wq==[0,0,0]).all(axis=2))] = [255,255,255]
bq[np.where((bq==[0,0,0]).all(axis=2))] = [255,255,255]


for i in range(8):
    for j in range(8):
        if bord[i][j] == 1:
            imag[i*100+10:i*100+80+10,j*100+10:j*100+80+10] = w
        elif bord[i][j] == 2:
            imag[i*100+10:i*100+80+10,j*100+10:j*100+80+10] = b
        elif bord[i][j] == 3:
            imag[i*100+10:i*100+80+10,j*100+10:j*100+80+10] = wq
        elif bord[i][j] == 4:
            imag[i*100+10:i*100+80+10,j*100+10:j*100+80+10] = bq
