import cv2 as cv
img = cv.imread('Images/gray_rose.jpg',0)
row,col = img.shape

for i in range(row):
    for j in range(col):
        if(img[i][j]>=64 and img[i][j]<128):
            img[i][j]+=100
        if(img[i][j]>255):
            img[i][j] = 255

cv.imshow('Bright Rose',img)
cv.waitKey(0)