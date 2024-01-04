
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('images/night.png',0)
img = cv.resize(img,(512,512))
original_img = img.copy()
row,col = img.shape

gama = 0.6

# c is the scaling factor. It is considered as constant also
# main equation: s = c*(1+r). c is calculated for maximum value of input and output
c = 255/ (np.log(1+np.max(img)))
power_img = np.zeros((row, col))
logarithomic_img = np.zeros((row, col))
inverse_img = np.zeros((row, col))

for i in range(row):
    for j in range(col):
        power_img[i,j] = (img[i,j]**gama)
        logarithomic_img[i,j] = c*np.log(1+img[i,j])
        inverse_img[i, j] = np.exp(logarithomic_img[i, j] / c) - 1


plt.subplot(1,4,1)
plt.imshow(original_img,cmap='gray')
plt.title('Original Image')
plt.subplot(1,4,2)
plt.imshow(power_img,cmap='gray')
plt.title('Power Law Image')
plt.subplot(1,4,3)
plt.imshow(logarithomic_img,cmap='gray')
plt.title('logarithmic Image')
plt.subplot(1,4,4)
plt.imshow(inverse_img,cmap='gray')
plt.title('Inverse logarithmic Image')
plt.show()
