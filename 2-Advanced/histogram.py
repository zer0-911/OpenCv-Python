# /**
#  * @author Moh. Iqbal Fatchurozi
#  * @email mohiqbalf5@gmail.com
#  * @create date 2022-02-13 21:38:52
#  * @modify date 2022-02-13 21:38:52
#  * @desc [Membuat Histogram]
#  */

import cv2
import matplotlib.pyplot as plt


img = cv2.imread('ex.jpg', 0)

# menemukan frekuensi piksel di range 0-255
histr = cv2.calcHist([img], [0], None, [256], [0, 256])

# menunjukkan grafik plot dari sebuah gambar
plt.plot(histr)
plt.show()
