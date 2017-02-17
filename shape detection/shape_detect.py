import cv2
import numpy as np

img=cv2.imread('image.png')
rows,cols=img.shape[:2]

def shape_name(c):
    shape="unidentified"
    peri=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.04*peri,True)
    sides=len(approx)
    if(sides==3):
        shape="Triangle"
    elif sides==4:
        (x,y,w,h)=cv2.boundingRect(approx)
        r=w/h
        if(0.95<r<1.05):
            shape="Square"
        else:
            shape="Rectangle"
    elif sides==5:
        shape="Pentagon"
    elif sides==6:
        shape="Hexagon"
    else:
        shape="Circle"
    return shape


#RESIZE THE IMAGE
img=cv2.resize(img,None,fx=0.6,fy=0.6,interpolation=cv2.INTER_AREA)
cv2.imshow('original image',img)
cv2.waitKey(0)

#convert into gray, gaussian blur and then threshold
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(5,5),0)
_,thresh=cv2.threshold(blurred,220,255,cv2.THRESH_BINARY)
cv2.imshow('threshold ',thresh)
cv2.waitKey(0)


#find all the contours in the image
cnts,_ = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
del cnts[0]
cv2.drawContours(img, cnts,-1, (0,0,0), 3)
cv2.imshow('cont ',img)
cv2.waitKey(0)

#find the contour shape and then find the centroid and label it
for c in cnts:
    shape=shape_name(c)
    M=cv2.moments(c)
    cx=int((M["m10"]/M["m00"]))
    cy=int((M["m01"]/M["m00"]))
    cv2.putText(img, shape, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (0, 0, 0), 1)
cv2.imshow("image",img)
cv2.waitKey(0)
