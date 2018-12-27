from os import listdir
from os.path import isfile, join



my_label="/media/eamslab/Data/Dataset/Cityscape_crop/Labels_train" 

 
label=sorted(listdir(my_label))

text_file= open("label.txt","w+")
for i in range(len(label)) :
	txt= label[i]
	text_file.write("%s \n" %txt)

text_file.close()
