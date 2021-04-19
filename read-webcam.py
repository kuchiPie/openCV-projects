import cv2 as cv

vid = cv.VideoCapture(0)

while True:

    ret, frame = vid.read()


    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF==ord('d'):
        break

vid.release()
cv.destroyAllWindows()
