
import numpy as np
import cv2

# Load an color image in grayscale
#cover image
cover = cv2.imread('small.jpg',0)
#secret image
cv2.imshow('cover image',cover)
secret= cv2.imread('monkey.jpg',0)
cv2.imshow('secret image',secret)
stego=np.zeros(cover.shape,dtype=cover.dtype)
destego=np.zeros(cover.shape,dtype=cover.dtype)
#print img.size
[x,y]=cover.shape
temp=0
#bit plane no 1 to 8 for grayscale images
b=6






for i in xrange(x):
    for j in xrange(y):
        #mask lower 3 bits of cover
        cover[i,j]=cover[i,j]  & 248
        #left shift  3 lsb of secret image
        secret[i,j]=(secret[i,j])>> 5

        secret[i,j]=secret[i,j] & 7

        stego[i,j]= cover[i,j] | secret[i,j]






cv2.imshow('stego image',stego)



for i in xrange(x):
    for j in xrange(y):
        destego[i,j]=stego[i,j] & 7
        destego[i,j]=(destego[i,j]<<5)


cv2.imshow('secret image back',destego)

cv2.waitKey(0)
cv2.destroyAllWindows()
