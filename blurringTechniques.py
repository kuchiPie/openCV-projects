import cv2 as cv

img = cv.imread('photos/monkey.jpg')
cv.imshow('Monkey', img)

# Averaging 
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur
# Gaussian Blur blurs a bit less thatn the averaging technique
# but is more natural than the averaging technique.
gauss = cv.GaussianBlur(img, (7,7), 1)
cv.imshow('Gaussian Blur', gauss)


cv.waitKey(0)