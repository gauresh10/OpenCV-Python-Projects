'''
contours
assignment
'''
import sys
import cv2
import numpy as np

def initial_step(img):
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('b and w',ref_gray)
    ret, thresh = cv2.threshold(ref_gray, 190, 255, 0)
    cv2.imshow('thresh',thresh)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    return contours

if __name__=='__main__':
    # Boomerang reference image
    img1 = cv2.imread('image.png')
    img2 =cv2.imread('kite.png')

    original_cnt=initial_step(img1)
    part_cnt=initial_step(img2)


    original_areas=[]
    part_areas=[]

    for contour in original_cnt:
        area = cv2.contourArea(contour)
        original_areas.append(area)
    print "original pic areas",original_areas

    for contour1 in part_cnt:
        area = cv2.contourArea(contour1)
        part_areas.append(area)
    print "part pic areas",part_areas
    #print all_areas
    #ref_contour=contours[5]
    #area = cv2.contourArea(contours[5])
    #print area
    data_found=0
    #print len(part_areas)
    for original in range(len(original_areas)):
        for part in range(len(part_areas)):
            if(part_areas[part]==original_areas[original]):
                data_found=original
                break

    print "index number",data_found
    print "data found at ",original_areas[data_found]

    ref_contour=original_cnt[data_found]



    cv2.drawContours(img1, [ref_contour], -1, (0,0,0), 3)
    cv2.imshow('Output', img1)
    cv2.waitKey(0)
