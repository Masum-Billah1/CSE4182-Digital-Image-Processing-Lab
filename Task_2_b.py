import cv2 as cv

def IntensityResolution(N):
    div = int(256/N)

    for i in range(row):
        for j in range(col):
            levels = int((img[i,j])/div)
            img[i,j] = levels*div
    return img

img = cv.imread('images/gray_rose.jpg',0)
[row,col] = img.shape

gray_level = 256
for i in range(8):
    print(gray_level)
    new_img = IntensityResolution(gray_level)
    gray_level //= 2
    cv.imshow('Rose', new_img)
    cv.waitKey(0)
