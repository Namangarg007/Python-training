import cv2

cap = cv2.VideoCapture(0)

classifire = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    retval, image = cap.read()

    faces = classifire.detectMultiScale(image)

    for face in faces:

        x, y, w, h = face

        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 9)

    cv2.imshow("Whole", image)

    key = cv2.waitKey(10)

    if key == ord('q'):
        break

    if key == ord('c'):
        cv2.imwrite("Detected.png", image)

cap.release()
cv2.destroyAllWindows()