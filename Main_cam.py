from Kamera.preproces import *
import cv2
import numpy as np
from skimage import io, color

def load_board(cap):
    first = True
    while(first):
        white_squares = []
        black_squares = []
        ret, frame = cap.read()
        rot = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        crop = crop_image(rot)
        adjust = adjust_gamma(crop, 1.5)
        gray = rgb_to_gray(adjust)
        # blur = gaussian_blur(gray)
        if first:
            corners = find_corners(gray)
            centers = find_centers(corners)
            for center in centers:
                first = False
                x, y = int(center[0]), int(center[1])
                if (is_white(gray, x, y)):
                    white_squares.append(center)
                else:
                    black_squares.append(center)
            rows = number_of_figures(white_squares)
            black_rows = number_of_figures(black_squares)
    return rows, black_rows

def get_color(cap,rows):
    ret, frame = cap.read()
    rot = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    crop = crop_image(rot)
    lab = color.rgb2lab(crop)

    col = []
    for row in rows[-1]:
        x, y = int(row[0]), int(row[1])
        col.append(list(avarage_color(lab, x, y)))
    r = rows[0][0]
    x, y = int(r[0]), int(r[1])
    col.append(list(avarage_color(lab, x, y)))
    set_color(col)
    print(col)

def show(cap):
    ret, frame = cap.read()
    rot = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    crop = crop_image(rot)
    cv2.imshow('crop', crop)


def get_board(cap,rows,black_rows):
    ret, frame = cap.read()
    rot = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    crop = crop_image(rot)
    # adjust = adjust_gamma(crop, 1.5)
    lab = color.rgb2lab(crop)

    row_n = 0
    col_n = 0
    load_data = True
    for brows in black_rows:
        if row_n % 2 != 0:
            col_n = 1
        for center in brows:
            x, y = int(center[0]), int(center[1])
            val = euclidean(lab, x, y)
            if (val != 1):
                print(val)
                load_data = False
    if load_data:
        bord = np.zeros((8, 8), np.uint8)
        for row in rows:
            if row_n % 2 != 0:
                col_n = 1
            for center in row:
                x, y = int(center[0]), int(center[1])
                val = euclidean(lab, x, y)
                if val == 0:
                    cv2.circle(crop, (x, y), 5, (0, 0, 255), -1)
                    bord[row_n][col_n] = 1
                elif val == 1:
                    cv2.circle(crop, (x, y), 5, (0, 255, 0), -1)
                    bord[row_n][col_n] = 2
                elif val == 2:
                    cv2.circle(crop, (x, y), 5, (255, 0, 255), -1)
                    bord[row_n][col_n] = 3
                elif val == 3:
                    cv2.circle(crop, (x, y), 5, (255, 255, 0), -1)
                    bord[row_n][col_n] = 4
                else:
                    cv2.circle(crop, (x, y), 5, (255, 0, 0), -1)
                col_n += 2
            row_n += 1
            col_n = 0
        cv2.imshow('crop', crop)
        return bord
    else:
        cv2.imshow('crop', crop)
        return np.zeros((8, 8), np.uint8)


def main():
    color = True
    cap = load_webcam()
    rows, black_rows = load_board(cap)
    while(True):
        show(cap)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    get_color(cap, rows)
    while(True):
        bord = get_board(cap,rows,black_rows)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()