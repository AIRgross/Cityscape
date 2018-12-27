#!/usr/bin/python
from PIL import Image
import os, sys
def resize_Images():
    dirs=os.walk(path)
    print dirs
    for (direpath,dirnames,filenames) in os.walk(path):
	print direpath,dirnames,filenames
 	for f in filenames:
	   files=direpath+'/'+f
           if os.path.isfile(files):

                img = Image.open(files)
	        half_the_width  = img.size[0] /2
	        half_the_height = img.size[1] /2

 		basewidth = 1024
		wpercent = (basewidth/float(img.size[0]))
		hsize = int((float(img.size[1])*float(wpercent)))
		img5= img.resize((basewidth,hsize), Image.ANTIALIAS)
	        half_the_width  = img5.size[0] /2
	        half_the_height = img5.size[1] /2
                img1=img5.crop((0   ,half_the_height - 192, 512,half_the_height  + 192)) 
	        img2=img5.crop((512 ,half_the_height - 192, 1024,half_the_height + 192))
#	        img3=img5.crop((1024,half_the_height - 192, 1536,half_the_height + 132))
#	        img4=img5.crop((1536,half_the_height - 192, 2048,half_the_height + 132))

	        half_the_width  = img.size[0] /2
	        half_the_height = img.size[1] /2
	        img5=img.crop((half_the_width-566,0, half_the_width+566,850))
		basewidth = 512
		wpercent = (basewidth/float(img5.size[0]))
		hsize = int((float(img5.size[1])*float(wpercent)))
		img5= img5.resize((basewidth,hsize), Image.ANTIALIAS)
#	        img5=img5.crop((1300,half_the_height - 120,1620,half_the_height + 120))
#	        img6=img6.crop((1600,half_the_height - 120,1920,half_the_height + 120))

#	        img7=img7.crop((700 ,half_the_height - 200,1020,half_the_height + 40))
#	        img8=img8.crop((1000,half_the_height - 200,1320,half_the_height + 40))
#		img9=img9.resize((320,240), Image.ANTIALIAS)

		f=os.path.splitext(f)[0]
	    	img1.save('/media/eamslab/Data/Dataset/Cityscape_crop/Images_train/'+f+'_a.png')
           	img2.save('/media/eamslab/Data/Dataset/Cityscape_crop/Images_train/'+f+'_b.png')
#           	img3.save('/media/eamslab/Data/Dataset/Cityscape_crop/Images_train/'+f+'_c.png')
#	    	img4.save('/media/eamslab/Data/Dataset/Cityscape_crop/Images_train/'+f+'_d.png')
           	img5.save('/media/eamslab/Data/Dataset/Cityscape_crop/Images_train/'+f+'_e.png')
#           	img6.save('/media/eamslab/Data/Dataset/Cityscape_crop/Images_train/'+f+'_f.png')
#	    	img7.save('/media/eamslab/Data/Dataset/Cityscape_crop/Images_train/'+f+'_g.png')
#           	img8.save('/media/eamslab/Data/Dataset/Cityscape_crop/Images_train/'+f+'_h.png')
#           	img9.save('/media/eamslab/Data/Dataset/Cityscape_crop/Images_train/'+f+'_i.png')

def resize_Labels():
    dirs=os.walk(path)
    print dirs
    for (direpath,dirnames,filenames) in os.walk(path):
	print direpath,dirnames,filenames
 	for f in filenames:
	   files=direpath+'/'+f
           if os.path.isfile(files):
            if 'polygons' in files:
		print(files)
		os.remove(files)
	    elif 'instanceIds' in files:
		os.remove(files)
	    elif 'labelIds' in files:
		os.remove(files)
	    else:

                img = Image.open(files)
	        half_the_width  = img.size[0] /2
	        half_the_height = img.size[1] /2

 		basewidth = 1024
		wpercent = (basewidth/float(img.size[0]))
		hsize = int((float(img.size[1])*float(wpercent)))
		img5= img.resize((basewidth,hsize), Image.ANTIALIAS)
	        half_the_width  = img5.size[0] /2
	        half_the_height = img5.size[1] /2
                img1=img5.crop((0   ,half_the_height - 192, 512,half_the_height  + 192)) 
	        img2=img5.crop((512 ,half_the_height - 192, 1024,half_the_height + 192))
#	        img3=img5.crop((1024,half_the_height - 192, 1536,half_the_height + 132))
#	        img4=img5.crop((1536,half_the_height - 192, 2048,half_the_height + 132))

	        half_the_width  = img.size[0] /2
	        half_the_height = img.size[1] /2
	        img5=img.crop((half_the_width-566,0, half_the_width+566,850))
		basewidth = 512
		wpercent = (basewidth/float(img5.size[0]))
		hsize = int((float(img5.size[1])*float(wpercent)))
		img5= img5.resize((basewidth,hsize), Image.ANTIALIAS)
#	        img5=img5.crop((1300,half_the_height - 120,1620,half_the_height + 120))
#	        img6=img6.crop((1600,half_the_height - 120,1920,half_the_height + 120))


		f=os.path.splitext(f)[0]
	    	img1.save('/media/eamslab/Data/Dataset/Cityscape_crop/Labels_train/'+f+'_a.png')
              	img2.save('/media/eamslab/Data/Dataset/Cityscape_crop/Labels_train/'+f+'_b.png')
  #           	img3.save('/media/eamslab/Data/Dataset/Cityscape_crop/Labels_train/'+f+'_c.png')
  #      	img4.save('/media/eamslab/Data/Dataset/Cityscape_crop/Labels_train/'+f+'_d.png')
             	img5.save('/media/eamslab/Data/Dataset/Cityscape_crop/Labels_train/'+f+'_e.png')
    #         	img6.save('/media/eamslab/Data/Dataset/Cityscape_crop/Labels_train/'+f+'_f.png')
    #     	img7.save('/media/eamslab/Data/Dataset/Cityscape_crop/Labels_train/'+f+'_g.png')
    #         	img8.save('/media/eamslab/Data/Dataset/Cityscape_crop/Labels_train/'+f+'_h.png')
    #           	img9.save('/media/eamslab/Data/Dataset/Cityscape_crop/Labels_train/'+f+'_i.png')		

path ='/media/eamslab/Data/Dataset/Cityscape_crop/gtFine/train'
resize_Labels()

path ='/media/eamslab/Data/Dataset/Cityscape_crop/leftImg8bit/train'
resize_Images()

#path = "/media/eamslab/Data/Dataset/Plant_test/synthetic_label/"
#dirs = os.listdir( path )
#resize()

#path = "/media/eamslab/Data/Dataset/Plant_test/synthetic_label_grey/"
#dirs = os.listdir( path )
#resize()

