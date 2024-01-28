import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("Images/lena.jpg",0)
image = cv.resize(image,(512,512))

D0 = 10
def gaussian(fft_image):
    m,n = fft_image.shape
    gaussian_filter = np.zeros((m,n))

    for u in range(m):
        for v in range(n):
            d = np.sqrt((u-m/2)**2+(v-n/2)**2)
            gaussian_filter[u][v] = np.exp(-d**2/(2*D0**2))

    gaussian_constant = gaussian_filter*fft_image
    gaussian_image = np.abs(np.fft.ifft2(gaussian_constant))
    gaussian_image = gaussian_image/255
    return gaussian_image;

def butterworth_filter(fft_image,filter_order):
    m,n = fft_image.shape
    butterworth_filter = np.zeros((m,n))
    for u in range(m):
        for v in range(n):
            d = np.sqrt((u-m/2)**2+(v-n/2)**2)
            butterworth_filter[u][v] = 1/(1+(d/D0)**(2*filter_order))

    butterworth_constant = butterworth_filter*fft_image
    butterworth_image = np.abs(np.fft.ifft2(butterworth_constant))
    butterworth_image = butterworth_image/255
    return butterworth_image

mean = 0;
deviation = 25;
filter_order = 4
noise = np.random.normal(mean,deviation,image.shape).astype(np.uint8)
noisy_image = cv.add(image,noise);
fft_image = np.fft.fftshift(np.fft.fft2(noisy_image))

gaussian_image = gaussian(fft_image)
butterworth_image = butterworth_filter(fft_image,filter_order)

plt.subplot(2,2,1)
plt.imshow(image,cmap="gray")
plt.title("Original Image")

plt.subplot(2,2,2)
plt.imshow(noisy_image,cmap="gray")
plt.title("Noisy Image")

plt.subplot(2,2,3)
plt.imshow(gaussian_image,cmap="gray")
plt.title("Gaussian Image")

plt.subplot(2, 2, 4)
plt.imshow(butterworth_image, cmap="gray")
plt.title("Butterworth Image")


plt.tight_layout()
plt.show()
