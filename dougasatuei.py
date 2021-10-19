import cv2
import time
from datetime import datetime

def main()

    base_path = "/home/pi/PBL/"


    cam = cv2.VideoCapture(-1)

    if not cam.isOpened():
        return

    fps = int(cam.get(cv2.CAP_PROP_FPS))
    size = (int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    while True:
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        ret, frame3 = cam.read()

        if ret1 and ret2 and ret3:
            gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
            gray3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)


            diff1 = cv2.absdiff(gray
