# PoC for calibration
#
# pip doesn't seem to work !? (on HP455G7, due to security measures ?)
# instead use python -m pip
# python -m pip install autopep8 -U
# venv
# $ kill  $(ps | grep ssh-agent | cut -d " " -f 5-10 | head -n 2)

import logging
import cv2
import numpy as np

import utils


def set_calibration(img, x, y, width, height):
    """"
    allows to move a rectangle on top of a given image and returns the x,y coordinates of the top left corner 
    of the rectangle
    """
    dist = 3  # distance (in pixels) to move the rectangle with each move
    while True:
        img2 = np.copy(img)
        cv2.putText(img=img2, text=f'Hello {y} - dist : {dist}', org=(
            50, 50), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=2, color=(0, 255, 0), thickness=1)

        cv2.rectangle(img2, (x, y), (x + width, y + height), (255, 0, 0), 2)
        cv2.imshow("with rectangle", img2)
        k = cv2.waitKeyEx(0)

        # print(k)

        myenv = "Windows"
        if myenv == "Windows":
            esc = 27
            up = 2490368
            down = 2621440
            left = 2424832
            right = 2555904
            plus = 43
            minus = 45
        if myenv == "Linux":
            esc = 27
            up = 82
            down = 84
            left = 81
            right = 83
            # plus = 43
            # minus = 45

        if k == esc:
            break
        elif k == -1:  # normally -1 returned,so don't print it
            continue
        elif k == up:
            y -= dist
        elif k == down:
            y += dist
        elif k == left:
            x -= dist
        elif k == right:
            x += dist
        elif k == plus:
            dist += 1
        elif k == minus:
            dist -= 1
        else:
            print(k)  # else print its value

    return x, y


def main():
    utils.init_logger('INFO')
    logging.info(
        "------------------------------------------------------------")
    logging.info("Starting calibration PoC")

    replace_param("params.py", "new_pw", "super_new_value")

    exit()

    filename = "img.jpg"
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    calib_x = 620
    calib_width = 580
    calib_y = 445
    calib_height = 135

    calib_x, calib_y = set_calibration(
        img, calib_x, calib_y, calib_width, calib_height)

    logging.info(
        f'x:{calib_x}, y:{calib_y}, width:{calib_width}, height:{calib_height}')
    logging.info("Ending Calibration PoC")
    utils.shutdown_logger()


interactive = False

if __name__ == '__main__':
    # interactive = True
    main()
