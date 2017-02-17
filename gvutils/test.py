import cv2
import numpy as np
'''
put gvutils.py in the main folder
from gvutils(python file) import gvutilsa(class name)
'''
from gvutils import gvutilsa

#make an instance of the class
gv=gvutilsa()


#input an image
img=cv2.imread('lena.jpg')
rows,cols=img.shape[:2]
#show the input image
cv2.imshow('Input Image',img)
cv2.waitKey(0)

######################functions in the class##########################
#image properties
data=gv.printproperties(img)
cv2.waitKey(0)

#convert color space source and destination
#RGB TO YUV
#RGB TO HSV
#RGB TO GRAY
#YUV TO RGB
#HSV TO RGB
#GRAY TO RGB
image=gv.convertColor(img,"RGB","GRAY")
cv2.imshow('Color transfored Image',image)
cv2.waitKey(0)


#image translation
#xshift to shift by x pixels right
#yshift to shift by y pixels down
#xpad to add x pixels to right
#ypad to add y pixels at bottom
xshift,yshift,xpad,ypad=70,110,170,170
image=gv.imgTranslate(img,xshift,yshift,xpad,ypad)
cv2.imshow('Translated Image',image)
cv2.waitKey(0)


#image rotation
#angle specified in +ve clock wise direction
angle=30
image=gv.imgRotate(img,angle)
cv2.imshow('Rotated Image '+str(angle),image)
cv2.waitKey(0)

#image resize
xval=0.3
yval=0.3
#resize  x by x*xval
#resize y by y*yval
image=gv.imgResize(img,xval,yval)
cv2.imshow('Resized Images',image)
cv2.waitKey(0)

#affine transform
#H_FLIP TO flip image horizontally
#V_FLIP to fli image vertically
#or specify sr1,sr2,sr3,ds1,ds2,ds3
image=gv.affTransform(img,operate="H_FLIP")
cv2.imshow('H_FLIP Images',image)
cv2.waitKey(0)

sr1=(0,0)
sr2=(cols-1,0)
sr3=(0,rows-1)
ds1=(0,0,)
c=int(0.6*(cols-1))
ds2=(c,0)
d=int(0.4*(cols-1))
ds3=(d,rows-1)
image=gv.affTransform(img,"",sr1,sr2,sr3,ds1,ds2,ds3)
cv2.imshow('Affine Transform Image',image)
cv2.waitKey(0)




#4point_perspective
#plot x2 x1
#     x3 x4
#x2,x1,x3,x4
cnt=[[[284,32],[83,69],[85,332],[288,387]]]
image=gv.fourptperTransform(img,cnt)
cv2.imshow('image',image)
cv2.waitKey(0)
