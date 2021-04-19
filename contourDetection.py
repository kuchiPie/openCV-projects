# Contour is an outline representing or bounding the shape or form of something.

import cv2 as cv
import numpy as np

img = cv.imread('photos/small.jpg')
cv.imshow('small', img)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# This is the First way to detect contour using canny function
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Canny means the outlines of different shapes and figures inside the image.
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

# Alternative way to detect contour is Threshold.
# Threshold looks at an image and tries to binarize it.
# Don't worry much about it now we will cover it up ahead.
ret, thresh = cv.threshold(gray, 123, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# The above function returns number of contours
# Mode: cv.RETR_TREE for hirarchial contours
# Mode: cv.RETR_EXTERNAL for external contours 
# Mode: cv.RETR_LIST for all contours 
# Method: cv.CHAIN_APPROX_NONE for just returns all contours 
# Method: cv.CHAIN_APPROX_SIMPE for compresses all the contours 


print(f'{len(contours)} contour(s) found!')

#lets draw contours on the blank canvas

cv.drawContours(blank, contours, - 1, (0,0,255), 1)
cv.imshow('Conoturs Drawn', blank)
# Canny is better than threshold since it's simpler.
# Simple thresholding has some disadvantages because it directly binarizes the image.


cv.waitKey(0)
