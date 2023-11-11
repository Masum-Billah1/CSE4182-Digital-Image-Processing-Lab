import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
image = cv.imread('Images/errosion_dialation_fingerprint.png',cv.IMREAD_GRAYSCALE);
_,binary_image = cv.threshold(image, 128,256, cv.THRESH_BINARY)
cv.resize(image,(512,512))

row,column = image.shape
structuring_element = np.ones((3,3))

def errosion_operation(image, structuring_element):
    erosion_image = np.copy(binary_image)
    for i in range(1,row-1):
        for j in range(1,column-1):
            erosion_image[i,j] = np.min(image[i-1:i+2,j-1:j+2]*structuring_element)
    return erosion_image

def dialation_operation(image, structuring_element):
    dialation_image = np.copy(binary_image)
    for i in range(1, row-1):
        for j in range(1, column-1):
            dialation_image[i,j] = np.max(image[i-1:i+2,j-1:j+2]*structuring_element)
    return dialation_image

opening_img = dialation_operation(errosion_operation(image,structuring_element),structuring_element)
closing_img = errosion_operation(dialation_operation(image,structuring_element),structuring_element)

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
