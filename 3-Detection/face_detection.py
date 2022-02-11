# /**
#  * @author Moh. Iqbal Fatchurozi
#  * @email mohiqbalf5@gmail.com
#  * @create date 2022-02-11 11:12:01
#  * @modify date 2022-02-11 11:12:01
#  * @desc [description]
#  */

import cv2 as cv

# # Memakai Haar Cascade Classifier
# face_cascade = cv.CascadeClassifier('haar_face.xml')

# # Membuka WebCam atau kamera
# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     # Mendapatkan frame
#     ret, frame = cap.read()
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.2, 5)

#     for (x, y, w, h) in faces:
#         cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = frame[y:y+h, x:x+w]
#     # jika frame terbaca maka ret
#     if not ret:
#         print("ERROR")
#         break
#     # Menampilkan hasil
#     cv.imshow('frame', frame)
#     # Tekan q untuk exit
#     if cv.waitKey(1) == ord('q'):
#         break


img = cv.imread('../img/orang.jpg')
cv.imshow('Kabinet', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)
# Memakai Haar Cascade Classifier
haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.5, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected Faces', img)
# Jangan Hapus kode dibawah ini
k = cv.waitKey(0)
# kondisi ketika q di keyboard dipencet
if k == 'q':
    cv.destroyAllWindows()
