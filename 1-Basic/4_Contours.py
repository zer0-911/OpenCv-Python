

import cv2 as cv
import numpy as np


# Membaca gambar
img = cv.imread('../img/rusa.jpg')

# # 1. Membuat gambar menjadi blank
# blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', blank)

# # 2. Merubah warna menjadi keabu-abuan
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # 3. Mengubah gambar menjadi blur
# blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# # 4. Mendeteksi tepi
# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny Edges', canny)


canny = cv.Canny(img, 125, 175)
contours, hierarchies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(img, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', img)

# Jangan Hapus kode dibawah ini
k = cv.waitKey(0)
# kondisi ketika q di keyboard dipencet
if k == 'q':
    cv.destroyAllWindows()
