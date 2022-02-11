import cv2 as cv
import numpy as np

# Membaca gambar
img = cv.imread('../img/rusa.jpg')
cv.imshow('Rusa', img)

# # Translasi atau menggeser objek


# def translate(img, x, y):
#     transMat = np.float32([[1, 0, x], [0, 1, y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMat, dimensions)

# # -x --> Kiri
# # -y --> Atas
# # x --> Kanan
# # y --> Bawah


# # translated = translate(img, -100, 100)
# # cv.imshow('Translated', translated)

# # Memutar gambar


# def rotate(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]

#     if rotPoint is None:
#         rotPoint = (width//2, height//2)

#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width, height)

#     return cv.warpAffine(img, rotMat, dimensions)


# rotated = rotate(img, -45)
# cv.imshow('Rotated', rotated)

# rotated_rotated = rotate(img, -90)
# cv.imshow('Rotated Rotated', rotated_rotated)

# # Mengubah ukuran
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# # Membalik
# flip = cv.flip(img, -1)
# cv.imshow('Flip', flip)

# Memotong gambar
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)


# Jangan Hapus kode dibawah ini
k = cv.waitKey(0)
# kondisi ketika q di keyboard dipencet
if k == 'q':
    cv.destroyAllWindows()
