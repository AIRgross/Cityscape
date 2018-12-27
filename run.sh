#resize and cut
python creat_crop.py
#create label text
python prepare_label.py

python convert_labels.py Labels_train label.txt Instances_train
#python clean_label.py
python prepare_data.py
