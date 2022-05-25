import cv2
import numpy as np

img = cv2.imread("resources/cards.jpg")

width, height = 400, 500
# pixels of the real image
pts1 = np.float32([[745, 116], [1131, 260], [507, 684], [872, 846]])

# which corner wraps to which side
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)
