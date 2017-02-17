import cv2
import numpy as np

image=cv2.imread("input.jpg")
rows,cols=image.shape[:2]


gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray,7)
edges=cv2.Laplacian(gray,cv2.CV_8U,ksize=5)
ret,thresh=cv2.threshold(edges,100,255,cv2.THRESH_BINARY_INV)




cv2.imshow('Cartoon Image', thresh)
cv2.waitKey(0)
