import cv2
import os

files = []
name = "0"
place = 0
path = "face_toExtract/"
for i in os.listdir(path):
    file_path = path + i
    img = cv2.imread(file_path, cv2.IMREAD_COLOR)
    cascadeOne = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascadeOne.detectMultiScale(gray, 1.2, 5)
    for (x, y, w, h) in faces:
        roi = img[y:y + h, x:x + w]
        name = "output/" + name + ".jpg"
        cv2.imwrite(name, roi)
        place += 1
        name = str(place)