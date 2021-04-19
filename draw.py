import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Painting the entire image to a color
# blank[:] = 0,255,0 #RGB
# cv.imshow('Green', blank)


# 2. Painting part of the image to a color
blank[200:300, 300:400] = 0,255,0 #RGB
cv.imshow('Green', blank)

# 3. Draw a rectangle only boundry
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=2)
# cv.imshow('Rectangle', blank)

# 4. Draw rectangle and fill colour inside it.
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED) # We can write 
# cv.imshow('Rectangle', blank)

# 5. Draw rectangle and fill colour inside it WITH RATIO COORDINATES.
cv.rectangle(blank, (0,0), (blank.shape[1]//3, blank.shape[1]//3), (0,255,0), thickness=cv.FILLED) 
cv.imshow('Rectangle', blank)

# 6. Draw a circle
cv.circle(blank, (blank.shape[1]//3, blank.shape[0]//3), 40, (0, 0, 255), thickness=-1) # -1  Also works to fill completely.
cv.imshow('Circle', blank)


# 7. Draw a line
cv.line(blank, (0,0), (500,500), (255,255,255), thickness=1)
cv.imshow('Line', blank)

# 8. Write text
cv.putText(blank, 'Hello, Myself Shreyas.', (100, 100), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,2), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)

