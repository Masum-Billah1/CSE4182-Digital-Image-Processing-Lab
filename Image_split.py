import cv2
image = cv2.imread('images/resized_rose.jpg')
height,width,channels = image.shape
half_height = height//2
half_width = width//2
top_Right = image[:half_height,:half_width]
top_Left = image[:half_height,half_width:]
bottom_Right = image[half_height:,:half_width]
bottom_Left = image[half_height:,half_width:]

cv2.imshow('Top Right',top_Right)
cv2.imshow('Top Left',top_Left)
cv2.imshow('Bottom_Right',bottom_Left)
cv2.imshow('Bottom_Left',bottom_Right)
cv2.waitKey(0)
