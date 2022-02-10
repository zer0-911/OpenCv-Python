# /**
#  * @author Moh. Iqbal Fatchurozi
#  * @email mohiqbalf5@gmail.com
#  * @create date 2022-02-10 15:20:35
#  * @modify date 2022-02-10 15:20:35
#  * @desc [Membaca video, menyimpan video, menampilkan video. Hilangkan komen untuk menjalankan program]
#  */


import cv2 as cv
import numpy as np

# # Membaca/menampilkan video
# # Buat objek VideoCapture dan baca dari file input
# # Jika inputnya adalah kamera, diberi 0. Jika tidak beri nama file
# cap = cv.VideoCapture('../videos/kitten.mp4')

# # Memeriksa apakah kamera berhasil dibuka
# if (cap.isOpened() == False):
#     print("ERROR")

# # Membaca hingga video selesai
# while(cap.isOpened()):
#     # Mendapatkan frame
#     ret, frame = cap.read()
#     if ret == True:

#         # Menampilkan hasil dari frame
#         cv.imshow('Frame', frame)

#         # Tekan q untuk exit
#         if cv.waitKey(25) & 0xFF == ord('q'):
#             break
#     else:
#         break

# cap.release()
# cv.destroyAllWindows()

# # Membuka WebCam atau kamera
# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     # Mendapatkan frame
#     ret, frame = cap.read()
#     # jika frame terbaca maka ret
#     if not ret:
#         print("ERROR")
#         break
#     # Menampilkan hasil
#     cv.imshow('frame', frame)
#     # Tekan q untuk exit
#     if cv.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()

# # Menyimpan Video
# cap = cv.VideoCapture(0)

# # Tentukan codec dan buat objek VideoWriter
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# # looping
# while(True):
#     # membaca frame
#     # ret mengecek setiap frame
#     ret, frame = cap.read()

#     # output per frame
#     out.write(frame)

#     # window
#     cv.imshow('Original', frame)

#     # tekan q untuk exit
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# out.release()

# cv.destroyAllWindows()
