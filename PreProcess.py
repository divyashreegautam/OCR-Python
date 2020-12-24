import cv2
import numpy as np
from PIL import Image
import os

path1 = 'D:/ExactOCR/FINAL/Input_Path'

files = os.listdir(path1)

s1=''
for file in files:
    path = path1+'/'+file
    s1=file[:-4]

    if not os.path.exists(path1+'/'+s1):
        os.mkdir(path1+'/'+s1)

    im = cv2.imread(path,0)

    ret,thresh1 = cv2.threshold(im,127,255,cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        #bound the images
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),3)
    i=0
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
    #following if statement is to ignore the noises and save the images which are of normal size(character)
    #In order to write more general code, than specifying the dimensions as 100,
    # number of characters should be divided by word dimension
        if w>100 and h>100:
        #save individual images
            #cv2.imwrite(path1+'/'+s1+'/'+str(i)+".tif",thresh1[y:y+h,x:x+w])
            #img = cv2.imread(path1+'/'+s1+'/'+str(i)+".tif")
            img = thresh1[y:y+h,x:x+w]

            
            
            i=i+1