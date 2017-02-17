'''
contours example

'''
import sys
import cv2
import numpy as np

def initial_step(img):
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('b and w',ref_gray)
    ret, thresh = cv2.threshold(ref_gray, 130, 255, 0)
    cv2.imshow('thresh',thresh)
    '''
    2nd parameter :
    1 for cv2.RETR_TREE
    2 for cv2.RETR_EXTERNAL

    3rd parameter
    1 for cv2.CHAIN_APPROX_NONE
    2 for cv2.CHAIN_APPROX_SIMPLE
    '''
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    return contours

if __name__=='__main__':

    img1 = cv2.imread('bricks2.png')
    img1=cv2.resize(img1,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
    original_cnt=initial_step(img1)

    original_areas=[]


    for contour in original_cnt:
        area = cv2.contourArea(contour)
        original_areas.append(area)
    #print "original pic areas",original_areas

    #draw all contours
    #cv2.drawContours(img1, original_cnt, -1, (0,0,0), 3)

    #draw only mentioned contour
    ref_contour=original_cnt[3]
    cv2.drawContours(img1, original_cnt, -1, (0,0,0), 3)



    cv2.imshow('Output', img1)
    cv2.waitKey(0)
