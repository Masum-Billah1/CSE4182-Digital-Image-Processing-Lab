import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

structuring_element = np.ones((5,5))
size = len(structuring_element)

def erosion_op(image, st_elemen):
    pad_h = size // 2
    padded_image = np.pad(image, pad_h, mode='constant')
    row,col = image.shape
    erosion_img = np.zeros_like(image)
    for i in range(row):
        for j in range(col):
            tmp_window = padded_image[i:i + size, j:j + size]
            erosion_img[i, j] = np.min(tmp_window * structuring_element)
    return erosion_img

def dilation_op(image, st_element):
    row,col = image.shape
    pad_h = size // 2
    padded_image = np.pad(image, pad_h, mode='constant')
    dilation_img = np.zeros_like(image)
    for i in range(row):
        for j in range(col):
            tmp_window = padded_image[i:i + size, j:j + size]
            dilation_img[i, j] = np.max(tmp_window * structuring_element)
    return dilation_img

image = cv.imread('Images/erdl.png',cv.IMREAD_GRAYSCALE)
image = cv.resize(image,(512,512))
row,column = image.shape
_, binary_image = cv.threshold(image,128,255,cv2.THRESH_BINARY) #converded gray image to binary

erosion_img = erosion_op(binary_image,structuring_element)
dilation_img = dilation_op(binary_image,structuring_element)

plt.subplot(1,3,1)
plt.imshow(binary_image,cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(erosion_img,cmap='gray')
plt.title('Erosion Image')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(dilation_img,cmap='gray')
plt.title('Dialation Image')
plt.axis('off')

plt.tight_layout()
plt.show()
