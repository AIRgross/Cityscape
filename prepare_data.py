from os import listdir
from os.path import isfile, join


my_data="/media/eamslab/Data/Dataset/Cityscape_crop/Images_train" 
my_label="/media/eamslab/Data/Dataset/Cityscape_crop/Instances_train" 

data=sorted(listdir(my_data))
label=sorted(listdir(my_label))

text_file= open("train.txt","w+")
for i in range(len(data)) :
	text_file.write("%s %s\n" % (my_data+"/"+data[i], my_label+"/"+label[i]))


text_file.close()
