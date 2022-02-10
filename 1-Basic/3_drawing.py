# /**
#  * @author Moh. Iqbal Fatchurozi
#  * @email mohiqbalf5@gmail.com
#  * @create date 2022-02-10 20:49:56
#  * @modify date 2022-02-10 20:49:56
#  * @desc [Menggambar dan menulis. Hilangkan komen untuk menjalankan program]


import cv2 as cv
import numpy as np

# # Menampilkan blank image
# blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)


# # 1. Menggambar dengan satu warna
# blank = np.zeros((500, 500, 3), dtype='uint8')
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Red', blank)

# # 2. Menggambar Persegi Panjang
# blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.rectangle(blank, (0, 0),
#              (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=-1)
# cv.imshow('Rectangle', blank)

# # 3. Menggambar lingkaran
# blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),
#           40, (0, 0, 255), thickness=-1)
# cv.imshow('Circle', blank)

# # 4. Menggambar garis
# blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)

# # 5. Menulis teks
# blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.putText(blank, 'Yap, Saya Ganteng!!!', (0, 225),
#            cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
# cv.imshow('Text', blank)

# Jangan Hapus kode dibawah ini
k = cv.waitKey(0)
# kondisi ketika q di keyboard dipencet
if k == 'q':
    cv.destroyAllWindows()
