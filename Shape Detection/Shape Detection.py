import cv2


cap = cv2.VideoCapture(0)       
while True:
    SUCCESS, img = cap.read()
    print(img.shape)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # Turn image to grayscale first

    _, thresh = cv2.threshold(gray_img, 120, 150, cv2.THRESH_BINARY)
    canny = cv2.Canny(thresh, 50, 150)
    
    contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        # According to number of 'edges' we determine the shape
        if len(approx) == 3:
            cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 0, 0))

        elif len(approx) == 4:
            x1, y1, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w) / h
            print(aspectRatio)
            if (aspectRatio >= 0.95) and (aspectRatio <= 1.05):
                cv2.putText(img, "Sqaure", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            else:
                cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

        elif len(approx) == 5:
            cv2.putText(img,
                        "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 0, 0))

        else:
            cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            
    img = cv2.flip(img, 1)
    cv2.imshow("trial", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
