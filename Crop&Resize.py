import cv2
import numpy as np

img = cv2.imread("resources/lambo.jpg")

imgResize = cv2.resize(img, (200, 400))

imgCropped = img[0:400, 200:700]

cv2.imshow("Image", img)
cv2.imshow("Image resize", imgResize)
cv2.imshow("Cropped resize", imgCropped)
cv2.waitKey(0)
