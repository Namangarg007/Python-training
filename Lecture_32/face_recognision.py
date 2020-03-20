import cv2
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier

data = np.load("faces.npy")

X = data[:, 1:].astype(np.uint8)
y = data[:, 0]

model = KNeighborsClassifier()
model.fit(X, y)

cap = cv2.VideoCapture(0)

classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    retval, image = cap.read()

    if retval:

        faces = classifier.detectMultiScale(image)

        faces = sorted(faces, key=lambda face: face[2] * face[3], reverse=True)

        if len(faces) >= 1:
            x, y, w, h = faces[0]

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 10)

            face = image[y:y + h, x:x + w]

            t_face = cv2.resize(face, (100, 100))

            gray = cv2.cvtColor(t_face, cv2.COLOR_BGR2GRAY)

            text = str(model.predict([gray.flatten()])[0])

            cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 3)

            cv2.imshow("Image", image)

    key = cv2.waitKey(10)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
