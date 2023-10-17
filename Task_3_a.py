import random
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def add_noise(img):
    row, col = img.shape
    pixel = 5000
    for i in range(pixel):
        x = random.randint(0,row-1)
        y = random.randint(0,col-1)
        img[x][y] = 255

    pixel = 5000
    for i in range(pixel):
        x = random.randint(0,row-1)
        y = random.randint(0,col-1)
        img[x][y] = 0

    return img

def padding_add(n, noise_image):
    row,col = img.shape
    mask = np.ones((n, n), dtype=np.float32) / (n * n * 1.0)
    pad_height = n // 2
    pad_width = n // 2
    new_height = row + 2 * pad_height
    new_width = col + 2 * pad_width
    pad_image = np.zeros((new_height, new_width), dtype=np.uint8)
    pad_image[pad_height:pad_height + row, pad_width:pad_width + col] = noise_image

    return pad_image, mask


def spatial_filler(noise_image):
    height,width = img.shape
    spatial_image = np.zeros((height, width))
    n = 5

    pad_image, mask = padding_add(n, noise_image)

    for h in range(height):
        for w in range(width):
            window = pad_image[h:h + n, w:w + n]
            weight = np.sum(window * mask)
            spatial_image[h, w] = weight

    return spatial_image

def median_filter(noise_image):
    row,col = img.shape
    n=5
    spatial_image=np.zeros_like(noise_image)
    pad_image,mask=padding_add(n,noise_image)

    for h in range(row):
        for w in range(col):
            window=pad_image[h:h+n,w:w+n]
            weight=np.median(window*mask)
            spatial_image[h,w]=weight

    return spatial_image

def psnr_func(original,noisy):
   mse = np.mean((original.astype(np.float32) - noisy.astype(np.float32)) ** 2)
   max_pixel_value = 255.0
   psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))
   return psnr

img = cv.imread('images/lena.jpg', 0)
img = cv.resize(img, (512,512))

original_image = img.copy()
noisy_img = add_noise(img)
spatial_filler_img = spatial_filler(noisy_img)
median_filter_img = median_filter(noisy_img)
calculate_psnr_spatial = psnr_func(original_image, spatial_filler_img)
calculate_psnr_median = psnr_func(original_image,median_filter_img)

plt.subplot(2,2,1)
plt.imshow(original_image,cmap='gray')
plt.title('Original Image')

plt.subplot(2,2,2)
plt.imshow(noisy_img,cmap='gray')
plt.title('Peeper-Salt Noise Image')

plt.subplot(2,2,3)
plt.imshow(spatial_filler_img,cmap='gray')
plt.title(f'Spatial filter-> PSNR: {calculate_psnr_spatial: .2f} dB')

plt.subplot(2,2,4)
plt.imshow(median_filter_img,cmap='gray')
plt.title(f'Median Filer-> PSNR: {calculate_psnr_median:.2f} dB')

plt.tight_layout()
plt.show()
