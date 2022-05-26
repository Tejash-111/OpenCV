import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier('C:\\Users\\12tej\\PycharmProjects\\OpencvPython\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
img = cv2.imread("resources/grp.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("image", img)
cv2.waitKey(0)
