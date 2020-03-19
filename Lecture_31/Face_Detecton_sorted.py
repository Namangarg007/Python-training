import cv2

cap = cv2.VideoCapture(0)

classifire = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    retval, image = cap.read()

    faces = classifire.detectMultiScale(image)
    faces = sorted(faces, key=lambda face: face[2]*face[3], reverse=True)

    if len(faces) >= 2:

        x1, y1, w1, h1 = faces[0]
        x2, y2, w2, h2 = faces[1]

        face1 = image[y1:y1+h1, x1:x1+w1]
        face2 = image[y2:y2+h2, x2:x2+w2]

        face1_f = cv2.resize(face2, face1.shape())
        face2_f = cv2.resize(face1, face2.shape())

        face1[:] = face1_f
        face2[:] = face2_f

        cv2.imshow("Swap", image)

    key = cv2.waitKey(10)

    if key == ord('q'):
        break

    if key == ord('c'):
        cv2.imwrite("Detected.png", image)

cap.release()
cv2.destroyAllWindows()