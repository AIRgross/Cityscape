#!/usr/bin/env python
# Martin Kersner, m.kersner@gmail.com
# 2016/01/25 

from __future__ import print_function
import os
import sys
from skimage.io import imread, imsave
import scipy.io
import struct
import numpy as np
from PIL import Image
#def Plant_classes():
#    Label(  'unlabeled'            ,  0 ,      255 , 'void'            , 0       , False        , True         , (  0,  0,  0) ),
#    Label(  'ego vehicle'          ,  1 ,      255 , 'void'            , 0       , False        , True         , (  0,  0,  0) ),
#    Label(  'rectification border' ,  2 ,      255 , 'void'            , 0       , False        , True         , (  0,  0,  0) ),
#    Label(  'out of roi'           ,  3 ,      255 , 'void'            , 0       , False        , True         , (  0,  0,  0) ),
#    Label(  'static'               ,  4 ,      255 , 'void'            , 0       , False        , True         , (  0,  0,  0) ),
#    Label(  'dynamic'              ,  5 ,      255 , 'void'            , 0       , False        , True         , (111, 74,  0) ),
#    Label(  'ground'               ,  6 ,      255 , 'void'            , 0       , False        , True         , ( 81,  0, 81) ),
#    Label(  'road'                 ,  7 ,        0 , 'flat'            , 1       , False        , False        , (128, 64,128) ),#
#    Label(  'sidewalk'             ,  8 ,        1 , 'flat'            , 1       , False        , False        , (244, 35,232) ),
#    Label(  'parking'              ,  9 ,      255 , 'flat'            , 1       , False        , True         , (250,170,160) ),
#    Label(  'rail track'           , 10 ,      255 , 'flat'            , 1       , False        , True         , (230,150,140) ),
#    Label(  'building'             , 11 ,        2 , 'construction'    , 2       , False        , False        , ( 70, 70, 70) ),
#    Label(  'wall'                 , 12 ,        3 , 'construction'    , 2       , False        , False        , (102,102,156) ),
#    Label(  'fence'                , 13 ,        4 , 'construction'    , 2       , False        , False        , (190,153,153) ),
#    Label(  'guard rail'           , 14 ,      255 , 'construction'    , 2       , False        , True         , (180,165,180) ),
#    Label(  'bridge'               , 15 ,      255 , 'construction'    , 2       , False        , True         , (150,100,100) ),
#    Label(  'tunnel'               , 16 ,      255 , 'construction'    , 2       , False        , True         , (150,120, 90) ),
#    Label(  'pole'                 , 17 ,        5 , 'object'          , 3       , False        , False        , (153,153,153) ),
#    Label(  'polegroup'            , 18 ,      255 , 'object'          , 3       , False        , True         , (153,153,153) ),
#    Label(  'traffic light'        , 19 ,        6 , 'object'          , 3       , False        , False        , (250,170, 30) ),
#    Label(  'traffic sign'         , 20 ,        7 , 'object'          , 3       , False        , False        , (220,220,  0) ),
#    Label(  'vegetation'           , 21 ,        8 , 'nature'          , 4       , False        , False        , (107,142, 35) ),
#    Label(  'terrain'              , 22 ,        9 , 'nature'          , 4       , False        , False        , (152,251,152) ),
#    Label(  'sky'                  , 23 ,       10 , 'sky'             , 5       , False        , False        , ( 70,130,180) ),
#    Label(  'person'               , 24 ,       11 , 'human'           , 6       , True         , False        , (220, 20, 60) ),
#    Label(  'rider'                , 25 ,       12 , 'human'           , 6       , True         , False        , (255,  0,  0) ),
#    Label(  'car'                  , 26 ,       13 , 'vehicle'         , 7       , True         , False        , (  0,  0,142) ),
#    Label(  'truck'                , 27 ,       14 , 'vehicle'         , 7       , True         , False        , (  0,  0, 70) ),
#    Label(  'bus'                  , 28 ,       15 , 'vehicle'         , 7       , True         , False        , (  0, 60,100) ),
#    Label(  'caravan'              , 29 ,      255 , 'vehicle'         , 7       , True         , True         , (  0,  0, 90) ),
#    Label(  'trailer'              , 30 ,      255 , 'vehicle'         , 7       , True         , True         , (  0,  0,110) ),
#    Label(  'train'                , 31 ,       16 , 'vehicle'         , 7       , True         , False        , (  0, 80,100) ),
#    Label(  'motorcycle'           , 32 ,       17 , 'vehicle'         , 7       , True         , False        , (  0,  0,230) ),
#    Label(  'bicycle'              , 33 ,       18 , 'vehicle'         , 7       , True         , False        , (119, 11, 32) ),
#    Label(  'license plate'        , -1 ,       -1 , 'vehicle'         , 7       , False        , True         , (  0,  0,142) ),

 

 

def colormap():
  palette = { 
 (  0,  0,  0) :  18,
 (111, 74,  0) :  18,
 ( 81,  0, 81) : 0, 
 (128, 64,128) : 0, 
 (244, 35,232) : 1, 
 (250,170,160) : 1, 
 (230,150,140) : 18, 
 ( 70, 70, 70) : 2, 
 (102,102,156) : 3, 
 (190,153,153) : 4,
 (180,165,180) : 18,
 (150,100,100) : 18,
 (150,120, 90) : 18,
 (153,153,153) : 5,
 (250,170, 30) : 6,
 (220,220,  0) : 7,
 (107,142, 35) : 8,
 (152,251,152) : 9,
 ( 70,130,180) : 10,
 (220, 20, 60) : 11,
 (255,  0,  0) : 12,
 (  0,  0,142) : 13,
 (  0,  0, 70) : 14,
 (  0, 60,100) : 14,
 (  0,  0, 90) : 18,
 (  0,  0,110) : 18,
 (  0, 80,100) : 15,
 (  0,  0,230) : 16,
 (119, 11, 32) : 17
 }
  return palette



def convert_from_color_segmentation(arr_3d):
  np.set_printoptions(threshold=np.nan) 
#  print("shape",arr_3d.shape[0])
#  print("shape",arr_3d.shape[1])

  arr_2d = np.zeros((arr_3d.shape[0], arr_3d.shape[1]), dtype=np.uint8)
  palette = colormap()

  for c, i in palette.items():
  #  print("c",c)
  #  print("i",i)
  #  print(np.array(c).reshape(1, 1, 3))
    m = np.all(arr_3d == np.array(c).reshape(1, 1, 3), axis=2)
    arr_2d[m] = i
    if(i==255):
	print(c)
 #   print(i)
  return arr_2d

def main():
  ##
#  ext = '.png'
  ##

  path, txt_file, path_converted = process_arguments(sys.argv)

  # Create dir for converted labels
  if not os.path.isdir(path_converted):
    os.makedirs(path_converted)

  with open(txt_file, 'rb') as f:
    for img_name in f:
      img_base_name = img_name.strip()
#      img_name = os.path.join(path, img_base_name) + ext
      img_name = os.path.join(path, img_base_name)
      img = Image.open(img_name).convert("RGB")
      img = np.asarray(img)
#      if (len(img.shape) > 2 and len(img.shape) < 4 and img.shape[2]==3 ):
      img = convert_from_color_segmentation(img)
 #       imsave(os.path.join(path_converted, img_base_name) + ext, img)
      imsave(os.path.join(path_converted, img_base_name), img)
      print("process " + img_name)



def process_arguments(argv):
  if len(argv) != 4:
    help()

  path = argv[1]
  list_file = argv[2]
  new_path = argv[3]

  return path, list_file, new_path 

def help():
  print('Usage: python convert_labels.py PATH LIST_FILE NEW_PATH\n'
        'PATH points to directory with segmentation image labels.\n'
        'LIST_FILE denotes text file containing names of images in PATH.\n'
        'Names do not include extension of images.\n'
        'NEW_PATH points to directory where converted labels will be stored.'
        , file=sys.stderr)
  
  exit()

if __name__ == '__main__':
  main()
