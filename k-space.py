import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images\brain.jpeg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude = 20*np.log(np.abs(fshift))
magnitude=np.asarray(magnitude , dtype=np.uint8)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude, cmap = 'gray')
plt.title('k-space'), plt.xticks([]), plt.yticks([])
plt.show()          