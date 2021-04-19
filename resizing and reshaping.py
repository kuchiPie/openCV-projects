import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    #images, video and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
def changeRes(width,height):
    #live video
    capture.set(3,width)
    capture.set(4,height)

    # Reading Videos
capture = cv.VideoCapture('videos/Haan-Main-Galat.mp4')
img = cv.imread("photos/citywalk.jpg")

img1 = cv.imread("photos/citywalk.jpg")

cv.imshow('monkey',img1)

resized_image = rescaleFrame(img,scale=0.2)

cv.imshow('Image', resized_image)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    

    if cv.waitKey(16) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()