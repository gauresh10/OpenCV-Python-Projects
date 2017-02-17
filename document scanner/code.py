import cv2
import numpy as np
from gvutils import gvutilsa
gv=gvutilsa()
image=cv2.imread('receipt.jpg')
rows,cols=image.shape[:2]

image=cv2.resize(image,None,fx=0.9,fy=0.9,interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)


# show the original image and the edge detected image
print "STEP 1: Edge Detection"
cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()



(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

# loop over the contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)

	# if our approximated contour has four points, then we
	# can assume that we have found our screen
	if len(approx) == 4:
		screenCnt = approx
		break

# show the contour (outline) of the piece of paper
print "STEP 2: Find contours of paper"
print [screenCnt]
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow("Outline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
x1=tuple([screenCnt][0][1])[0][0]
y1=tuple([screenCnt][0][1])[0][1]

x2=tuple([screenCnt][0][0])[0][0]
y2=tuple([screenCnt][0][0])[0][1]

x3=tuple([screenCnt][1][0])[0][0]
y3=tuple([screenCnt][1][0])[0][1]

x4=tuple([screenCnt][1][1])[0][0]
y4=tuple([screenCnt][1][1])[0][1]
print "val of ",x1,y1
'''
'''x1=tuple([screenCnt][0][1])
x2=tuple([screenCnt][0][0])
x3=tuple([screenCnt][0][2])
x4=tuple([screenCnt][0][3])
src_points = np.float32([x1,x2,x3,x4])
dst_points = np.float32([[0,0], [cols-1,0], [0,rows-1], [cols-1,rows-1]])
projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
img_output = cv2.warpPerspective(image, projective_matrix, (cols,rows))
'''
cnt=[screenCnt]
img_output=gv.perTransform(image,cnt)
img_output=cv2.resize(img_output,None,fx=0.2,fy=0.2,interpolation=cv2.INTER_AREA)
cv2.imshow('final',img_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
