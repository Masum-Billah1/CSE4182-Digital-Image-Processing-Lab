import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def Basic_global_thresholding(image):
    temp1 = len(frequency)//2
    temp2 = 0
    T_inf = 1e-5

    while(1):
        temp2 = temp1
        G1 = image > temp1
        G2 = image <= temp1

        mu1 = np.mean(image[G1])
        mu2 = np.mean(image[G2])

        temp1 = (mu1 + mu2) / 2

        if abs(temp2- temp1) < T_inf:
            break

    return  temp1


img = cv.imread('Images/lena.jpg',0)
row,col = img.shape
plt.subplot(2,1,1)
plt.imshow(img,cmap='gray')
plt.title('Original image')
frequency = np.zeros(256)

for i in range(row):
    for j in range(col):
        frequency[img[i,j]] += 1

#Histogram
plt.subplot(2,2,3)
plt.bar(range(256), np.array(frequency))

plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.title('Histogram')

thresold_frequency = np.zeros(256)
Final_Threshold = Basic_global_thresholding(img)
for i in range(255):
    if(i<Final_Threshold):
        thresold_frequency[0] += frequency[i]
    else:
        thresold_frequency[255] +=frequency[i]

plt.subplot(2,2,4)
plt.bar(range(256), np.array(thresold_frequency),width=2)
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.title('Histogram after Single Treshold')
plt.show()
plt.close()
