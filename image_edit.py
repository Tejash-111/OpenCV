import cv2

#importing numpy for matrix
import numpy as np

kernel = np.ones((5,5), np.uint8)

# importing image
img = cv2.imread("resources/download.jpg")

# converting to black and white
imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

# Blur image
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 3)

# canny image
imgCanny = cv2.Canny(img, 100, 100)

# dialate image or make the lines of canny image thick
imgDialation = cv2.dilate(imgCanny, kernel, iterations = 1)

#erode image: make canny dilated image thin
imgEroded = cv2.erode(imgCanny, kernel, iterations= 1)

# displaying both the images
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilated Image", imgDialate)
cv2.imshow("Eroded Image", imgErode)
cv2.waitKey(0)



