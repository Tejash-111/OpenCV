import cv2
import numpy as np


#########################
imgWidth = 640
imgHeight = 480
#########################


cap = cv2.VideoCapture(0)
cap.set(3, imgWidth)
cap.set(4, imgHeight)
cap.set(10, 150)


def stack_images(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def preprocessing(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 1)
    img_canny = cv2.Canny(img_blur, 200, 200)
    kernel = np.ones((5, 5))
    img_dial = cv2.dilate(img_canny, kernel, iterations=2)
    img_fin = cv2.erode(img_dial, kernel, iterations=2)
    return img_fin


def get_contours(image):
    biggest = np.array([])
    max_area = 0
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)

            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area
    cv2.drawContours(imgCon, biggest, -1, (255, 0, 0), 20)
    return biggest


def reorder(my_points):
    my_points = my_points.reshape((4, 2))
    my_points_new = np.zeros((4, 1, 2), np.int32)

    add = my_points.sum(1)

    my_points_new[0] = my_points[np.argmin(add)]
    my_points_new[3] = my_points[np.argmax(add)]

    diff = np.diff(my_points, axis=1)

    my_points_new[1] = my_points[np.argmin(diff)]
    my_points_new[2] = my_points[np.argmax(diff)]

    return my_points_new


def get_warp(image, biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [imgWidth, 0], [0, imgHeight], [imgWidth, imgHeight]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    img_output = cv2.warpPerspective(image, matrix, (imgWidth, imgHeight))

    # img_cropped = img_output[20:img_output.shape[0] - 20: img_output.shape[1] - 20]
    # img_cropped = cv2.resize(img_cropped, (imgWidth, imgHeight))

    return img_output


while True:
    success, img = cap.read()
    img = cv2.resize(img, (imgWidth, imgHeight))
    imgCon = img.copy()

    img_threshold = preprocessing(img)
    big = get_contours(img_threshold)
    if big.size != 0:
        imgWarped = get_warp(img, big)

        imageArray = ([img, img_threshold],
                      [imgCon, imgWarped])
    else:
        imageArray = ([img, img_threshold],
                      [img, img])

    stackImages = stack_images(0.6, imageArray)

    cv2.imshow("Result", stackImages)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
