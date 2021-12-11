import cv2 as cv 
import numpy as np 

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

while True: 
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_red = np.array([161,155,84])
    upper_red = np.array([179,255,255])
    red_mask = cv.inRange(hsv_frame, lower_red, upper_red)
    red = cv.bitwise_and(frame, frame, mask = red_mask)

    cv.imshow('Webcam', frame)
    # cv.imshow("Red Mask", red_mask)
    cv.imshow("Red", red)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break 

cap.release()
cv.destroyAllWindows()