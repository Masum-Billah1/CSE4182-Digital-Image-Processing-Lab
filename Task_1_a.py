import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def downsampling(image, scale):
    row,col = image.shape
    row = row//scale
    col = col//scale
    resized_image = np.zeros((row,col))

    for i in range(row):
        for j in range(col):
            resized_image[i,j] = image[i *scale , j*scale]
    return resized_image

try:
    image = cv.imread('Images/lena.jpg',0)
    if image is None:
        raise FileNotFoundError("Image not found or cannot be read.")

    image = cv.resize(image,(512,512))

    dim = 3
    height,width = image.shape
    for k in range(1,10):
        plt.subplot(dim, dim, k)
        plt.title(f'{height//(2**(k-1))} X {width//(2**(k-1))}')
        plt.imshow(image, cmap='gray')
        image = downsampling(image,2)
        plt.axis('off')

    plt.show()
    plt.tight_layout()

except FileNotFoundError as e:
    print("Error:",e)
