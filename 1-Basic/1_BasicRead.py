# /*
# * @ author Moh. Iqbal Fatchurozi
# * @ email mohiqbalf5@gmail.com
# * @ create date 2022-02-09 16: 28: 48
# * @ modify date 2022-02-09 16: 28: 48
# * @ desc[file ini adalah file yang berisi fungsi-fungsi yang digunakan untuk mengambil gambar dari kamera, hilangkan komen untuk menjalankan program]
# */

import cv2 as cv
from cv2 import imread

# # Membaca/Menampilkan gambar
# img = cv.imread('../img/gojo.jpg')
# cv.imshow("Dis", img)


# # Mengubah gambar menjadi abu abu (Grayscale)
# img = cv.imread('../img/gojo.jpg')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)


# # Mengubah gambar menjadi blur
# img = cv.imread('../img/fish.jpg')
# blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', img)


# # Edge Cascading alias mencari tepian
# img = cv.imread('../img/fish.jpg')
# ec = cv.Canny(img, 125, 175)
# cv.imshow('Edge Cascading', ec)


# # Melebarkan gambar
# img = cv.imread('../img/rusa.jpg')
# dimg = cv.dilate(img, (7, 7), iterations=3)
# cv.imshow('Dilating Image', dimg)


# # Mengikis gambar
# img = cv.imread('../img/rusa.jpg')
# er = cv.erode(img, (7, 7), iterations=3)
# cv.imshow('Erode', er)


# # Resize atau merubah ukuran
# img = cv.imread('../img/rusa.jpg')
# rs = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('resiza', rs)

# # Cropping atau dicrop
# img = cv.imread('../img/rusa.jpg')
# cropped = img[10:500, 200:400]
# cv.imshow('Cropped', cropped)

# Jangan Hapus kode dibawah ini
k = cv.waitKey(0)
# kondisi ketika q di keyboard dipencet
if k == 'q':
    cv.destroyAllWindows()
