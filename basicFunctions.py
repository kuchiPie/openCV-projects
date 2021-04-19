import cv2 as cv

img = cv.imread('photos/small.jpg')

cv.imshow('momkey', img)

# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# Blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# Edge Cascade
canny  = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('dilated', dilated)

# Eroding
eroding = cv.erode(dilated, (3, 3), iterations= 3)
cv.imshow('eroded', eroding)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# Cropping
cropped = img[50:200, 20:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)
