import cv2
import time
from datetime import datetime

def main():

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

            diff1 = cv2.absdiff(gray2,gray1)
            diff2 = cv2.absdiff(gray3,gray2)
            
            diff_and = cv2.bitwise_and(diff1, diff2)
            
            th = cv2.threshold(diff_and, 50, 255, cv2.THRESH_BINARY)[1]
            
            wh_pixels = cv2.countNonZero(th)
            
            if wh_pixels > 500:
                date = datetime.now().strftime("%Y%m%d_%H%M%S")
                print(date + "WhitePixels:"+str(wh_pixels))
                                      
                fourcc = cv.2VideoEriter_fourcc('m', 'p', '4', 'v')
                out = cv.2VideoWriter(base_path + date + '.mp4',fourcc, fps, size)
                         
                for i in range(400):
                    ret_rec, frame_rec = cam.read()
                                               
                    if ret_rec:
                        out.write(frame_rec)
                                               
                out.release()
                                               
            time.sleep(1) 
                                               
    cam.release()
                                               
if __name__ == '__main__':
    main()
     
            
            
