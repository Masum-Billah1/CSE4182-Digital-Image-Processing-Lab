import cv2
image = cv2.imread('Images/resized_rose.jpg')
height, width, channels = image.shape
half = height//2
top = image[:half, :]
bottom = image[half:, :]

cv2.imshow('Top',top)
cv2.imshow('Bottom',bottom)
cv2.waitKey(0)