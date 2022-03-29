import cv2 as cv
from cv2 import threshold

img = cv.imread('photos/cat.jpg')
cv.imshow('Cat', img)

gray  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)


threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)



cv.waitKey(0)