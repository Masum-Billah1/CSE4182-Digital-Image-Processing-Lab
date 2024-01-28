import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
image = cv.imread('Images/open.png',0)
image = cv.resize(image,(512,512))
_,binary_image = cv.threshold(image, 128,256, cv.THRESH_BINARY)

row,column = image.shape
structuring_element = np.ones((50,50))
size = len(structuring_element)

def errosion_op(image, st_elemen):
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

opening_img = dilation_op(errosion_op(binary_image,structuring_element),structuring_element)
closing_img = errosion_op(dilation_op(binary_image,structuring_element),structuring_element)

plt.subplot(131)
plt.imshow(binary_image,cmap='gray')
plt.title('Original Image')

plt.subplot(132)
plt.imshow(opening_img,cmap='gray')
plt.title('Opening Image')

plt.subplot(133)
plt.imshow(closing_img,cmap='gray')
plt.title('Closing Image')

plt.tight_layout()
plt.show()
