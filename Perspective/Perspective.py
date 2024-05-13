import cv2
import numpy as np


cap = cv2.VideoCapture(0)                           # Initialise web cam               
points = []                                         # Create empty list to store mouse clicks' co ordinates

def click_event(event, x, y, flags, params):        # Function that checks if left click was pressed
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])
       

cv2.namedWindow("frame")
cv2.setMouseCallback('frame', click_event)          # Read user's clicks
c = 0
while True:
     
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)              
    if len(points) == 4:
        pts1 = np.float32(points)                   # User's inputted co ordinates
        pts2 = np.float32([[0, 0], [480, 0],        # Size of picture
                        [0, 640], [480, 640]])
        
        # Apply Perspective Transform Algorithm
        matrix = cv2.getPerspectiveTransform(pts1, pts2)        
        result = cv2.warpPerspective(frame, matrix, (640, 480))
        if not c:       # If ROI is selected, close the original window
            cv2.destroyWindow("frame")
            c += 1
        cv2.imshow('Changed Perspective', result) # Transformed Capture
        key = cv2.waitKey(1)
        if key == 27:   # if escape was pressed, exit code
            break
        elif key == ord('r'):       
            points.clear()
            cv2.destroyAllWindows()
            c = 0
    else:
        cv2.imshow('frame', frame) # Initial Capture 
        key = cv2.waitKey(1)
        if key == 27:
            break

        elif key == ord('r'):
            points.clear()

        cv2.setMouseCallback('frame', click_event)

        
    

        
    
