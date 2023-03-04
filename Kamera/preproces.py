import cv2
import numpy as np
import math

height = 480
width = 640

black = [150,150,150]
brown = [220,256,256]

colors = None



def load_webcam(cam):
    # select camera based on name
    cap = cv2.VideoCapture(cam)
    # crop camera to size 460x460
    cap.set(3, height)
    cap.set(4, width)

    return cap

def crop_image(image):
    # crop image to size 460x460
    border_W = 10
    border_H = 90
    crop = image[border_H:width - border_H, border_W:height - border_W]
    return crop

def rgb_to_gray(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def gaussian_blur(image):
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    return blur
def adjust_gamma(image, gamma=1.0):
    alpha = 1.5  # Contrast control (1.0-3.0)
    beta = 0  # Brightness control (0-100)
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted

def find_corners(image):
    ret, corners = cv2.findChessboardCorners(image, (7, 7), None)
    bord_corners = []

    if ret:
        for i in range(0, len(corners), 7):
            for j in range(7):
                bord_corners.append(corners[i + j][0])
    return bord_corners

def find_centers(corners):
    lengh = 0
    if len(corners) > 0:
        lengh = int(abs(corners[0][0] - corners[1][0]))
    centers = []
    print("lengh: ", lengh)
    if lengh > 10:
        for square in corners:
            for i in range(-int(lengh/2), int(lengh/2) +1, int(lengh/2)):
                for j in range(-int(lengh/2), int(lengh/2)+1, int(lengh/2)):
                    if i == 0 or j == 0:
                        continue
                    x, y = int(square[0]), int(square[1])
                    centers.append((x + i, y + j))
        # remuve centers that are to close to eat other
        for i in range(len(centers)):
            for j in range(len(centers)):
                if i == j:
                    continue
                if abs(centers[i][0] - centers[j][0]) < int(lengh/2) and abs(centers[i][1] - centers[j][1]) < int(lengh/2):
                    centers[j] = (0, 0)
        # POP centers that are (0,0)
    new_centers = []
    for i in range(len(centers)):
        if centers[i] != (0, 0):
            new_centers.append(centers[i])
    return new_centers

def is_white(image, x, y):
    # check if pixel is white
    if image[y, x] > 100:
        return True
    else:
        return False

def avarage_color(image, x, y):
    # get avarage color of 10x10 pixel
    pixel_avarage = np.zeros(3)
    for i in range(-3, 3):
        for j in range(-3, 3):
            pixel_avarage += image[y + i, x + j]
    pixel_avarage = pixel_avarage / 36
    return pixel_avarage

def pick_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
            print("brown: ", avarage_color(param, x, y))


def number_of_row(centers):
# get centers that are in first row
    if len(centers) < 20:
        return []
    rows = [[], [], [], [], [], [], [], []]
    centers.sort(key=lambda x: x[1])
    for i in range(4):
        rows[0].append(centers[i])
        rows[0].sort(key=lambda x: x[0])
    for i in range(4, 8):
        rows[1].append(centers[i])
        rows[1].sort(key=lambda x: x[0])
    for i in range(8, 12):
        rows[2].append(centers[i])
        rows[2].sort(key=lambda x: x[0])
    for i in range(12, 16):
        rows[3].append(centers[i])
        rows[3].sort(key=lambda x: x[0])
    for i in range(16, 20):
        rows[4].append(centers[i])
        rows[4].sort(key=lambda x: x[0])
    for i in range(20, 24):
        rows[5].append(centers[i])
        rows[5].sort(key=lambda x: x[0])
    for i in range(24, 28):
        rows[6].append(centers[i])
        rows[6].sort(key=lambda x: x[0])
    for i in range(28, 32):
        rows[7].append(centers[i])
        rows[7].sort(key=lambda x: x[0])

    return rows

def set_color(col):
    # set color of 10x10 pixel
    global colors
    colors = col


def euclidean(img, x, y):
    point = avarage_color(img, x, y)
    distances = [
        math.sqrt((point[0] - color[0]) ** 2 + (point[1] - color[1]) ** 2 + (point[2] - color[2]) ** 2)
        for color in colors
    ]
    return distances.index(min(distances))











