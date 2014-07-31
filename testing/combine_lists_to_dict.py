#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from posixpath import *

data = open("../.sele_data_base.txt")

# Create dict
file_dict = {}

for each_path in data:
	each_path = each_path.rstrip()
	file_dir = dirname(each_path)
	file_name = basename(each_path)
	
	# Fill dict with file info
	file_dict[file_name] = each_path, file_dir
#print file_dict

# Access dict
for each_file in file_dict:
	full_lists = file_dict[each_file]
	print full_lists[1]
	



