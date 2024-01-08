import random

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def add_noise(image):
    noisy_image = image.copy()
    row,col = noisy_image.shape

    number_of_salt_noise = 5000
    for i in range(number_of_salt_noise):
        x = random.randint(0,row-1)
        y = random.randint(0,col-1)
        noisy_image[x,y] = 255

    number_of_peeper_noise = 5000
    for i in range(number_of_peeper_noise):
        x = random.randint(0,row-1)
        y = random.randint(0,col-1)
        noisy_image[x,y] = 0

    return noisy_image

def pad_image(image, karnel):
    row,col = image.shape
    padding_row = (karnel-1)+row
    padding_column = (karnel-1)+col
    padding_image = np.zeros((padding_row,padding_column))
    Pad_size = karnel//2

    for i in range(Pad_size,padding_row-Pad_size):
        for j in range(Pad_size,padding_column-Pad_size):
            padding_image[i, j] = image[i - Pad_size, j - Pad_size]

    return padding_image

def averaging_filter(noisy_image,mask_size):
    averaging_filter_image = np.zeros_like(noisy_image)

    padding_image = pad_image(noisy_image,mask_size)
    mask = np.full((mask_size, mask_size), (1 / (mask_size * mask_size)))
    row,col = noisy_image.shape
    pad_size = int((mask_size-1)/2)

    for i in range(row):
        for j in range(col):
            window = padding_image[i:i+mask_size,j:j+mask_size]
            window = window*mask
            sum_window = np.sum(window)
            averaging_filter_image[i][j] = sum_window

    return averaging_filter_image

def median_filter(noisy_image,mask_size):
    median_filter_image = np.zeros_like(noisy_image)
    padding_image = pad_image(noisy_image, mask_size)
    mask = np.full((mask_size, mask_size), 1)
    row, col = noisy_image.shape
    pad_size = int((mask_size - 1) / 2)


    for i in range(row):
        for j in range(col):
            window = padding_image[i:i + mask_size, j:j + mask_size]
            median_value = np.median(window*mask)
            median_filter_image[i][j] = median_value
    return  median_filter_image

#PSNR = 10log10(Max^2/MSE) MSE-> Mean Squared Error
def PSNR(original_image,filtered_image):
    original_image = original_image.astype(np.float64)
    filtered_image = filtered_image.astype(np.float64)
    mse = np.mean((original_image-filtered_image)**2)
    max = 255
    psnr = 10*np.log10(max**2/mse)
    return psnr


image = cv.imread('Images/lena.jpg',0)
image = cv.resize(image,(512,512))
noisy_image = add_noise(image)
noisy_image_psnr = PSNR(image,noisy_image)
average_spatial_filter = averaging_filter(noisy_image,3)
average_spatial_filter_psnr = PSNR(image,average_spatial_filter)
median_spatial_filter = median_filter(noisy_image,3)
median_spatial_filter_psnr = PSNR(image,median_spatial_filter)

plt.subplot(2,2,1)
plt.imshow(image,cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(noisy_image,cmap='gray')
plt.title(f'Noisy Image PSNR: {noisy_image_psnr: .2f} DB')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(average_spatial_filter,cmap='gray')
plt.title(f'Average Filterd Image  PSNR: {average_spatial_filter_psnr:.2f} DB')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(median_spatial_filter,cmap='gray')
plt.title(f'Median Filter Image  PSNR: {median_spatial_filter_psnr:.2f} DB')
plt.axis('off')
plt.show()
