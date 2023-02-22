import cv2
import numpy as np

cap = cv2.VideoCapture(1)
#resize the image
cap.set(3, 312)
cap.set(4, 416)

while(True):
    # Capture frame-by-frame
    ret, image = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # brightness and contrast
    alpha = 1.5  # Contrast control (1.0-3.0)
    beta = 0  # Brightness control (0-100)
    adjusted = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)
    blur = cv2.GaussianBlur(adjusted, (5, 5), 0)

    ret,thresh = cv2.threshold(blur,150,255,0)

    # finde squares
    edges = cv2.Canny(thresh, 70, 150, apertureSize=3)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        cv2.drawContours(image, [approx], 0, (0), 5)




    # # haf transform to find lines
    # edges = cv2.Canny(adjusted, 70, 150, apertureSize=3)
    # # dilatastew
    # kernel = np.ones((3, 3), np.uint8)
    # dilation = cv2.dilate(edges, kernel, iterations=1)
    # # erode
    # kernel = np.ones((4, 4), np.uint8)
    # erosion = cv2.erode(dilation, kernel, iterations=1)
    #
    # # keap only the lines
    # lines = cv2.HoughLinesP(erosion, 1, np.pi / 180, 100, minLineLength=150, maxLineGap=10)
    #
    # # draw lines
    # if lines is not None:
    #     for line in lines:
    #         print(line)
    #         x1, y1, x2, y2 = line[0]
    #         cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 1)
    #
    # print(lines)
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break