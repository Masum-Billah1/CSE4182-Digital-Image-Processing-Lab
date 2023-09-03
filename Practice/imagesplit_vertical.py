import cv2 
image = cv2.imread('Images/resized_rose.jpg')
height, width, channels = image.shape
half = width//2
left = image[:, :half]
right = image[:, half:]

cv2.imshow('Right',right)
cv2.imshow('Left',left)
cv2.waitKey(0)
