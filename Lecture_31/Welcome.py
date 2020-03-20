import  cv2

cap = cv2.VideoCapture(0)  # used to open the camera app and capture video

while True:

    retval, image = cap.read()  # used to read the video comming from cap

    if retval:

        x, y, w, h = 50, 60, 200, 300

        cut = image[y:y + h, x:x + w]  # selected an area of 300 X 300 from 250, 300

        cut[:, :, :2] = 0  # changing the color values of first two layers of cut as cv2 works on BGR the B&G layer
        # values will turn to 0 and only R values remain

        cv2.imshow("Whole", image)

    key = cv2.waitKey(10)  # to hold the video app

    if key == ord('q'):  # ord is used to make shure that when q is pressed the while loop is ended
        break

    if key == ord('c'):
        cv2.imwrite("Captured image.png", image)  # to capture image when c is pressed

cap.release()
cv2.destroyAllWindows()
