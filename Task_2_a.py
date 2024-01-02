import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('Images/gray_rose.jpg',0)
row,col = img.shape

enhanced_image = img
for i in range(row):
    for j in range(col):
        if(enhanced_image[i][j]>=64 and enhanced_image[i][j]<128):
            enhanced_image[i][j]+=100
        if(enhanced_image[i][j]>255):
            enhanced_image[i][j] = 255


plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,2,2)
plt.axis('off')
plt.imshow(img,cmap='gray')
plt.title('Brightness Enhancement Image')
plt.show()
