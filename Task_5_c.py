import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
image = cv.imread('Images/boundary.png',cv.IMREAD_GRAYSCALE)
image = cv.resize(image,(512,512))
_, binary_image = cv.threshold(image, 128, 255, cv.THRESH_BINARY)
row,column = image.shape

structuring_element = np.ones((3,3))
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

boundary_image = image-errosion_op(binary_image,structuring_element);

plt.subplot(121)
plt.imshow(binary_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(122)
plt.imshow(boundary_image,'gray')
plt.title('Image with boundary')
plt.axis('off')

plt.tight_layout()
plt.show()
