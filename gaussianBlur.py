import cv2 as cv # Importing the cv library as cv2

img = cv.imread('photos/monkey.jpg') # Reading the image and storing it in a variable
cv.imshow('Monkey', img) # Displaying the image by the imshow method.


# Gaussian Blur
# Gaussian Blur blurs a bit less thatn the averaging technique
# but is more natural than the averaging technique.
gauss = cv.GaussianBlur(img, (7,7), 3,) # using the gaussian blur function on the variable img
# The (7,7) is basically the kernel size. In short the magnitude of blur.
# The 3 is the x and y standard deviation in casse you want to mention it.
# Otherwise you can also leave it as just (img, (7, 7)) where s.d will be none.
# You can keep different x and y deviation if you want
# GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None, /) ->
cv.imshow('Gaussian Blur', gauss) # Displaying the image by imshow method.


cv.waitKey(0) # Just a keyboard binding function