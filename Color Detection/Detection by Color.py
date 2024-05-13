import cv2
import datetime
import numpy as np

def ShowOneColor(frame, key):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if key == 'b':
        lower = np.array([100, 50, 50])  # Lower blue color range
        upper = np.array([140, 255, 255])  # Upper blue color range
    elif key == 'g':
        lower = np.array([36, 0, 0])  # Lower green color range
        upper = np.array([86, 255, 255])  # Upper green color range
    elif key == 'r':
        lower = np.array([0, 50, 50])  # Lower red color range
        upper = np.array([10, 255, 255])  # Upper red color range

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    return result


cap = cv2.VideoCapture(0)
color_key = None  # Initialize color key
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (60, 45), font, 1, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if color_key:  # Check if color key is selected
            result = ShowOneColor(frame, color_key)
            cv2.imshow('result', result)
        key = cv2.waitKey(1)
        if key == ord('b'):
            color_key = 'b'  # Set color key to blue
        elif key == ord('g'):
            color_key = 'g'  # Set color key to green
        elif key == ord('r'):
            color_key = 'r'  # Set color key to red
        elif key == ord('q'):
            break

cv2.destroyAllWindows()
cap.release()
