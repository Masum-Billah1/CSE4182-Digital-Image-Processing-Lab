import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def IntensityResolution(N):
    div = int(256/N)

    for i in range(row):
        for j in range(col):
            levels = int((img[i,j])/div)
            img[i,j] = levels*div
    return img

img = cv.imread('images/gray_ros.jpg',0)

row,col = img.shape
gray_level = 256
for i in range(8):
    new_img = IntensityResolution(gray_level)
    gray_level //= 2
    plt.subplot(3,3,(i+1))
    plt.title(f'Gray level: {int(np.log2(gray_level)+1)}')
    plt.imshow(new_img,cmap='gray')
    plt.axis('off')

plt.show()
