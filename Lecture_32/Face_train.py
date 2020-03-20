import cv2
import numpy as np
import os

cap = cv2.VideoCapture(0)

classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

X = []

name = input("Enter your Name : ")
count = int(input("Enter number of samples : "))

while True:

    retval, image = cap.read()

    if retval:

        faces = classifier.detectMultiScale(image)

        faces = sorted(faces, key=lambda face: face[2]*face[3], reverse=True)

        if len(faces) >= 1:

            x, y, w, h = faces[0]

            face = image[y:y+h, x:x+w]

            t_face = cv2.resize(face, (100, 100))

            gray = cv2.cvtColor(t_face, cv2.COLOR_BGR2GRAY)

            cv2.imshow("Image", gray)

    key = cv2.waitKey(10)

    if key == ord('c'):

        X.append(gray.flatten())
        count -= 1
        print("Faces remaining", count)
        if count == 0:
            break

cap.release()
cv2.destroyAllWindows()

X_mod = np.array(X)
y_mod = np.full((len(X), 1), name)

data = np.hstack([y_mod, X_mod])

if os.path.exists("face.npy"):
    old = np.load("faces.npy")
    data = np.vstack([old, data])

np.save("faces.npy", data)