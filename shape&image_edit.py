import cv2
import numpy as np

# Matrix of zeroes -> black, Matrix of ones -> white
img1 = np.zeroes(512, 512)
cv2.imshow("Image", img1)

# BGR color coding
img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

# to get only Image with Blue color for given dimesion
img[200:300, 300:400] = 255, 0, 0

# Drawing a line
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 1)

# Drawing a Rectangle
cv2.rectangle(img, (0, 0), (250, 350), (255, 255, 255), 2)

# Drawing a Circle
cv2.circle(img, (300, 400), 30, (0, 255, 0), 3)
# to create a filled Rectangle cv2.rectangle( (start dim), (end diagnol dim), (color coding), cv2.FILLED


# adding text to image
cv2.putText(img, "Hello World", (300 , 200), cv2.FONT_ITALIC, 1, (0, 250, 0), 2)

# Displaying all this
cv2.imshow("Image", img)
cv2.waitKey(0)

