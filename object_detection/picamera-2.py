import cv2
import os

os.system('sudo modprobe bcm2835-vl2')
cam_Mode = 0
cap = cv2.VideoCapture(cam_Mode)
cap.set(3, 1920)
cap.set(4, 1080)

while True:
    ret, frame = cap.read()
    if not(ret):
        break

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xff == 27:
        break

if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()
