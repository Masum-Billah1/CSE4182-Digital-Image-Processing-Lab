import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Images/gray_rose.jpg',0)
row,col = img.shape

frequency = np.zeros(256)

for i in range(row):
    for j in range(col):
        frequency[img[i,j]] += 1

#Histogram
plt.bar(range(256), np.array(frequency))

plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

for i in range(row):
    for j in range(col):
        if img[i,j] >= 100:
            img[i,j] = 255
        else:
            img[i,j] = 0

cv.imshow('Figure 2',img)
cv.waitKey(0)
