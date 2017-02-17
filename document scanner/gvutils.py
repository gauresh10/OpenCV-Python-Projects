import cv2
import numpy as np
class gvutilsa:
    def __init__(self):
        pass
    def convertColor(self,img,src,des):
        if(src=="RGB" and des=="YUV"):
            self.temp= cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        elif(src=="RGB" and des=="HSV"):
            self.temp= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        elif(src=="YUV" and des=="RGB"):
            self.temp= cv2.cvtColor(img, cv2.COLOR_YUV2BGR)
        elif(src=="HSV" and des=="RGB"):
            self.temp= cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        elif(src=="RGB" and des=="GRAY"):
            self.temp= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif(src=="GRAY" and des=="RGB"):
            self.temp= cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        return self.temp
    def printg(self,data):
        print data
    def imgTranslate(self,img,xshift,yshift,xpad=0,ypad=0):
        num_rows,num_cols=img.shape[:2]
        self.translation_matrix = np.float32([ [1,0,xshift], [0,1,yshift]])
        self.img_translation = cv2.warpAffine(img, self.translation_matrix, (num_cols + ypad,
        num_rows + xpad))
        return self.img_translation
    def imgRotate(self,img,angle):
        angle=-(angle)
        print angle
        num_rows,num_cols=img.shape[:2]
        self.rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), angle, 1)
        self.img_rotation = cv2.warpAffine(img, self.rotation_matrix, (num_cols, num_rows))
        return self.img_rotation
    def imgResize(self,img,xscale=0.5,yscale=0.5):
        img_scaled = cv2.resize(img,None,fx=xscale, fy=yscale, interpolation =cv2.INTER_AREA)
        return img_scaled
    def affTransform(self,img,operate="",sr1=0,sr2=0,sr3=0,ds1=0,ds2=0,ds3=0):
        rows,cols=img.shape[:2]
        if(len(operate)!=0):
            if(operate=="H_FLIP"):
                sr1,sr2,sr3=(0,0),(cols-1,0),(0,rows-1)
                ds1,ds2,ds3=(cols-1,0),(0,0),(cols-1,rows-1)
            elif(operate=="V_FLIP"):
                sr1,sr2,sr3=(0,0),(cols-1,0),(0,rows-1)
                ds1,ds2,ds3=(0,rows-1),(cols-1,rows-1),(0,0)
        src_points = np.float32([sr1, sr2, sr3])
        dst_points = np.float32([ds1,ds2,ds3])
        affine_matrix = cv2.getAffineTransform(src_points, dst_points)
        img_output = cv2.warpAffine(img, affine_matrix, (cols,rows))
        return img_output
    def perTransform(self,img,screenCnt):
        rows,cols=img.shape[:2]
        x1=tuple(screenCnt[0][1])
        x2=tuple(screenCnt[0][0])
        x3=tuple(screenCnt[0][2])
        x4=tuple(screenCnt[0][3])
        src_points = np.float32([x1,x2,x3,x4])
        dst_points = np.float32([[0,0], [cols-1,0], [0,rows-1], [cols-1,rows-1]])
        projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        img_output = cv2.warpPerspective(img, projective_matrix, (cols,rows))
        return img_output
