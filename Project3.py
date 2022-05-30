import cv2

######################################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier('C:\\Users\\12tej\\PycharmProjects\\OpencvPython\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_russian_plate_number.xml')
minArea = 500
color = (255, 0, 255)
#######################################

count = 0
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

while True:
    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlate = nPlateCascade.detectMultiScale(imgGray, 1.3, 5)
    for (x, y, w, h) in numberPlate:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, "Number Plate", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("resources/scanned folder/NoPlate_"+str(count)+".jpg", imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "scan saved", (150, 265), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        cv2.imshow("result", img)
        cv2.waitKey(500)
        count += 1
