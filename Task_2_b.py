
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('images/night.png',0)
img = cv.resize(img,(512,512))
original_img = img
row,col = img.shape

gama = 0.6

c = 255/ (np.log(1+np.max(img)))
power_img = np.zeros((row, col))
inverse_img = np.zeros((row, col))

for i in range(row):
    for j in range(col):
        power_img[i,j] = (img[i,j]**gama)
        inverse_img[i,j] = np.exp(img[i,j] / c) - 1
        # inverse_img[i][j] = np.exp(img1[i][j])**(1/c) - 1

plt.subplot(1,3,1)
plt.imshow(original_img,cmap='gray')
plt.title('Original Image')
plt.subplot(1,3,2)
plt.imshow(power_img,cmap='gray')
plt.title('Original Image')
plt.subplot(1,3,3)
plt.imshow(inverse_img,cmap='gray')
plt.title('Original Image')
plt.show()
