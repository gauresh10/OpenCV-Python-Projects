import cv2
import numpy as np


#algorithm to get highest pixel value in an image for RGB space individually
def domColor(img):
    for x in xrange(3):
        for i in xrange( rows):
            for j in xrange(cols-1):
                if(img[:,:,x][i,j] < img[:,:,x][i,j+1]):
                    img[:,:,x][i,j+1]=img[:,:,x][i,j+1]
                else:
                    img[:,:,x][i,j+1]=img[:,:,x][i,j]
        for i in xrange(rows-1):
            for j in xrange(cols-1,cols):
                    if(img[:,:,x][i,j]<img[:,:,x][i+1,j] ):
                        pass
                    else:
                        img[:,:,x][i+1,j]=img[:,:,x][i,j]
                        
        b= img[:,:,0][rows-1,cols-1]
        g= img[:,:,1][rows-1,cols-1]
        r= img[:,:,2][rows-1,cols-1]
    return b,g,r

def drawRect(img):
    blue,green,red=domColor(temp)
    if(blue==red==green==0):
        blue=red=green=255
    elif(blue==red==green==255):
        blue=red=green=0

    for i in xrange(0, rows):
        for j in xrange(cols-8,cols):
            img[i,j]=[blue,green,red]

    for i in xrange(0, rows):
        for j in xrange(0,8):
            img[i,j]=[blue,green,red]

    for i in xrange(0, 8):
        for j in xrange(0,cols):
            img[i,j]=[blue,green,red]

    for i in xrange(rows-8, rows):
        for j in xrange(0,cols):
            img[i,j]=[blue,green,red]

    cv2.imshow('image with borders',img)
    cv2.waitKey(0)


if __name__=="__main__":
    image=cv2.imread('input.jpg')
    image=cv2.resize(image,None,fx=0.6,fy=0.6, interpolation=cv2.INTER_AREA)
    rows,cols=image.shape[:2]
    temp=image.copy()
    cv2.imshow('Input Image',image)
    cv2.waitKey(0)
    drawRect(image)
