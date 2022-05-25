import cv2

# to output an image to screen.
img = cv2.imread("resources/test.png")
cv2.imshow("Output", img)
cv2.waitKey(1000)

# to output a video to screem
cap = cv2.VideoCapture("resources/test1.mp4")
# to display video as a set of images.
while True:
    success, img2 = cap.read()
    cv2.imshow("Video", img2)
    # exit the video when "q" is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

