# /**
#  * @author Moh. Iqbal Fatchurozi
#  * @email mohiqbalf5@gmail.com
#  * @create date 2022-02-11 09:45:47
#  * @modify date 2022-02-11 09:45:47
#  * @desc [treshold. Hilangkan komen untuk menjalankan program]
#  */

import cv2 as cv

# Membaca gambar
img = cv.imread('../img/rusa.jpg')

# Mengubah menjadi keabu-abuan
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# # Simple Threshol
# threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# cv.imshow('Simple Thresholded', thresh)

# threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
# cv.imshow('Simple Thresholded Inverse', thresh_inv)

# # Adaptif Thresholding
# adaptive_thresh = cv.adaptiveThreshold(
#     gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
# cv.imshow('Adaptive Thresholding', adaptive_thresh)

# Jangan Hapus kode dibawah ini
k = cv.waitKey(0)
# kondisi ketika q di keyboard dipencet
if k == 'q':
    cv.destroyAllWindows()
