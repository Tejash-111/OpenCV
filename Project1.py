import cv2
import numpy as np

# min and max HSV values of each color
red = [160, 122, 61, 179, 255, 255]
green = [56, 79, 140, 112, 181, 255]
yellow = [17, 131, 161, 95, 209, 255]

# setting Web-cam, its resolution and brightness
cap = cv2.VideoCapture(0)
cap.set(3, 300)
cap.set(4, 400)
cap.set(10, 150)

# RGB values of each color taken into consideration
myColorValues = [[0, 0, 204],
                 [51, 255, 51],
                 [51, 255, 255]]

# myColors matrix containing the list the HSV values of each color
myColors = [[160, 122, 61, 179, 255, 255],
            [56, 79, 140, 112, 181, 255],
            [17, 131, 161, 95, 209, 255]]

# list to create a visited point array
myPoints = []  # x coordinate, y coordinate, color index


# function to add newPoints to points list and to convert image to mask
def findColor(img, myColors, myColorValues):
    count = 0
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResults, (x, y), 10, myColorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
    return newPoints


# function to draw bounding rectangle
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y


# function to draw for each point that marker moves
def drawOnCanvas(myPoints, myColorVallues):
    for point in myPoints:
        cv2.circle(imgResults, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


# main function type while, to call all the functions and display the images on output screen
while True:
    success, img = cap.read()
    imgResults = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow("Video", imgResults)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

