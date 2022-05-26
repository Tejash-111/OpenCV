import cv2
import numpy as np

def empty(a):
    pass


path = "resources/me.jpg"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 7, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 74, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 183, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 100, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)


img = cv2.imread(path)
imgR = cv2.resize(img, (400, 500))
while True:
    imgHSV = cv2.cvtColor(imgR, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(imgR, imgR, mask=mask)

    # instead of displaying all these images we can add stackImages method to stack all the images and display
    cv2.imshow(imgR)
    cv2.imshow(imgHSV)
    cv2.imshow(mask)
    cv2.imsho2(imgResult)
    
    cv2.waitKey(1)
