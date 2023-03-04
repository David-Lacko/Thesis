import cv2
import numpy as np

length = 480
width = 640
border_W = 10
border_H = 90
# rotare camera 90 grade

line_thickness = 2
line_color = (0, 255, 0)
line_color = (250, 250, 250)
# SET CAP PROPERTIES
def all_cameras():
    camera_list = []
    for i in range(10):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            camera_list.append("Camera " + str(i))
        cap.release()
    return camera_list

def setup(frame):
        image = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.rectangle(image, (border_W, border_H), (length - border_W, width - border_H), line_color, line_thickness)
        rack1 = image[border_H:width - border_H, 0:border_W]
        rack2 = image[border_H:width - border_H, length - border_W:length]
        rack3 = image[0:border_H, 0:length]
        rack4 = image[width - border_H:width, 0:length]
        image[border_H:width - border_H, 0:border_W] = cv2.addWeighted(rack1, 0.3, np.zeros(rack1.shape, rack1.dtype), 0, 0)
        image[border_H:width - border_H, length - border_W:length] = cv2.addWeighted(rack2, 0.3, np.zeros(rack2.shape, rack2.dtype), 0, 0)
        image[0:border_H, 0:length] = cv2.addWeighted(rack3, 0.3, np.zeros(rack3.shape, rack3.dtype), 0, 0)
        image[width - border_H:width, 0:length] = cv2.addWeighted(rack4, 0.3, np.zeros(rack4.shape, rack4.dtype), 0, 0)
        return image


