import cv2 as cv
import numpy as np

img = cv.imread('photos/small.jpg')
img1 = cv.imread('photos/shreyas.jpg')
img2 = cv.imread('photos/tree.jpg')

cv.imshow('eiffel', img)

# Transformation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, -100, -100)
cv.imshow('translated', translated)

# Rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv. warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, 45)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) 
# Since we are increasing the dimensions of the image we are using INTER_CUBIC
# If we want to decrease the dimensions we should us INTER_LINER or INTER_AREA
cv.imshow('risized', resized)

# Flipping
flip = cv.flip(img1, 1)
# 1 for flipping along x-axis and 0 for flipping along y-axis
# -1 for both x and y axis
cv.imshow('Flip', flip)

# Cropping
cropped = img2[200:400, 300:400]
cv.imshow('Crop', cropped)

cv.waitKey(0)
