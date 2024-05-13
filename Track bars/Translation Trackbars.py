import cv2
import numpy as np


def nothing(x):     # Function that takes dummy parameter and returns nothing
    pass


#cap = cv2.VideoCapture(0)   # Turn on web cam
#_, frame = cap.read()
frame = cv2.imread("Logo_resized.jpeg")
height, width = frame.shape[:2]     # Take width and height of live frame
# Creates 3 trackbars: Horizontal, Vertical and Rotation

cv2.namedWindow('Trackbars')
cv2.createTrackbar("Horizontal", "Trackbars", 0, width * 2, nothing)
cv2.createTrackbar("Vertical", "Trackbars", 0, height * 2, nothing)
cv2.createTrackbar("Rotation", "Trackbars", 0, 190, nothing)

cv2.setTrackbarPos("Horizontal", "Trackbars", width)
cv2.setTrackbarPos("Vertical", "Trackbars", height)

cv2.setTrackbarPos("Rotation", "Trackbars", 100)
# Sets the min rotation as 10 so it'd only rotate 180° CW/ACW
cv2.setTrackbarMin("Rotation", "Trackbars", 10)

cv2.imshow('Trackbars', np.zeros((60, 400, 3), np.uint8))

while True:
    #_, frame = cap.read()
    frame = cv2.imread("Logo_resized.jpeg")
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

    elif k == ord('r'):         # resets frame to original
        cv2.setTrackbarPos("Horizontal", "Trackbars", width)
        cv2.setTrackbarPos("Vertical", "Trackbars", height)
        cv2.setTrackbarPos("Rotation", "Trackbars", 100)
    # Takes in user input from trackbars
    Horizontal_Shift = cv2.getTrackbarPos("Horizontal", "Trackbars")
    Vertical_Shift = cv2.getTrackbarPos("Vertical", "Trackbars")
    Rotation_Shift = cv2.getTrackbarPos("Rotation", "Trackbars")

    # Calculates resultant transformation
    T = np.float32([[1, 0, Horizontal_Shift - width], [0, 1, Vertical_Shift - height]])
    X = width / 2
    Y = height / 2
    M = cv2.getRotationMatrix2D((Horizontal_Shift - X, Vertical_Shift - Y), 200 - Rotation_Shift * 2, 1.0)
    frame = cv2.warpAffine(frame, M, (width, height))
    frame = cv2.warpAffine(frame, T, (width, height))
    cv2.imshow("Live frame", frame)

cv2.destroyAllWindows()
