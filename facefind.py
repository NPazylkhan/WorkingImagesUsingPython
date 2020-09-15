# import cv2
# # from PIL import Image

# faceCascade = cv2.CascadeClassifier('C:\\Users\\Nurmakhan Pazylkhan\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
# eyeCascade = cv2.CascadeClassifier('C:\\Users\\Nurmakhan Pazylkhan\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')

# img = cv2.imread("C:\\Users\\Nurmakhan Pazylkhan\\source\\repos\\images\\faces.jpg")

# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FPS, 24)
# # img = Image.open("C:\\Users\\Nurmakhan Pazylkhan\\source\\repos\\images\\faces.jpg")
# while True:
#     ret, img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     faces = faceCascade.detectMultiScale(
#         gray,
#         scaleFactor=1.2,
#         minNeighbors=5,
#         minSize=(20, 20)
#     )

#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#     cv2.imshow("cam", img)
#     if cv2.waitKey(10) == 27: # Esc key
#         break
# cap.release()
# cv2.destroyAllWindows()

import cv2

faceCascade = cv2.CascadeClassifier('C:\\Users\\Nurmakhan Pazylkhan\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('C:\\Users\\Nurmakhan Pazylkhan\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')

img = cv2.imread("C:\\Users\\Nurmakhan Pazylkhan\\source\\repos\\images\\faces.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
        gray,               #
        scaleFactor=1.2,    # Находим лица на фото
        minNeighbors=5,     #
        minSize=(20, 20)    #
    )

for (x, y, w, h) in faces:
    roi_gray = gray[y:y + h, x:x + w] # Вырезаем область с лицами
    roi_color = img[y:y + h, x:x + w]
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    eyes = eyeCascade.detectMultiScale(
        roi_gray,              #
        scaleFactor=1.2,       # Ищем глаза в области с лицом
        minNeighbors=5,
        minSize=(5, 5),
    )
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)  # Рисуем область глаз

cv2.imshow("camera", img)
cv2.waitKey(0)
cv2.destroyAllWindows()