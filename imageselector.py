__author__ = 'Kyle Long'
# This is a sibling program to fadedetector.py
#Use the millisecond value from fadedetection.py to input it in this file to save a image
#Use the image given to represent as a matrix
import cv2
ms = int(raw_input("What is the millisecond of the value you want to save?"))
videocapture = cv2.VideoCapture(#videofile)
videocapture.set(cv2.cv.CV_CAP_PROP_POS_MSEC,ms)
success, image = videocapture.read()
if success:
    cv2.imwrite("frame.jpg", image)
    cv2.imshow("frame", image)
    cv2.waitKey()

