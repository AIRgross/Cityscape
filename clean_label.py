#!/usr/bin/python
from PIL import Image
import os, sys
import numpy as np
import cv2
def blank(img):

	mask1 = img[:,:,:] == (2212)
	mask2 = img[:,:,:] == (2214)
	mask3 = img[:,:,:] == (2216)
	mask=np.sum(mask1+mask2+mask3)
	if(mask<2000):
		return True
	else:
		return False

	
def clear_blank():
    dirs=os.walk(path)
    for (direpath,dirnames,filenames) in os.walk(path):
#	print direpath,dirnames,filenames
 	for f in filenames:
	   files=direpath+'/'+f
           if os.path.isfile(files):
              img = cv2.imread(files) 
              if blank(img):
		os.remove(files)
		files=files.replace('Instances','Labels')
		#print(files)
		os.remove(files)
		files=files.replace('Labels','Images')
		#print(files)
		files=files.replace('gtFine_color','leftImg8bit')
		#print(files)
		os.remove(files)
		#exit()
		
path ='/media/eamslab/Data/Dataset/Cityscape_crop/Instances_train'
clear_blank()


#path = "/media/eamslab/Data/Dataset/Plant_test/synthetic_label/"
#dirs = os.listdir( path )
#resize()

#path = "/media/eamslab/Data/Dataset/Plant_test/synthetic_label_grey/"
#dirs = os.listdir( path )
#resize()

