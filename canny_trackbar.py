import numpy as np
import cv2 as cv
def nothing(x):
    pass
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
img = cv.imread('../data/images/counter.png',0)
edges = cv.Canny(img,100,200)

cv.namedWindow('image')
# create trackbars for color change
cv.createTrackbar('R','image',100,1000, nothing)
cv.createTrackbar('G','image',200,1000,nothing)
cv.createTrackbar('B','image',0,255,nothing)
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image',0,1,nothing)
while(1):
    # get current positions of four trackbars
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    #cv.imshow('image',img)
    edges = cv.Canny(img,r,g)
    cv.imshow('image',edges)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
