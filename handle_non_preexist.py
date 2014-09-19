#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from shutil import copy
from posixpath import dirname

from print_color import print_color

## colors
default =  "\033[0m"
red = "\33[31;1m"
blue = "\33[34;1m"
gray = "\033[1;30m"
green = "\033[1;32m"
yellow = "\033[1;33m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
crimson = "\033[1;38m"

def handle_non_preex_file(non_preex_file_info_dict):
	"""
	$ About this function:
	* Handle the files that are not pre-existing in backup location. 
		Just copy them into backup directory.
	
	$ Input parameters:
	* "non_preex_file_info_dict"=> dict that stores info of non pre-exist files.
	* Format of the dict: xxx_dict[file_name] = (1)ori_path_of_file,
		(2)file_path_backup_dir

	$ Parameter explaination:
	* (1)"ori_path_of_file": The absolute path to the file in its original dir.
	* (2)"file_path_backup_dir": If the file is pre-exist, this will the 
	absolute path to that file in its backup dir
	"""
	for each_non_preex_file in non_preex_file_info_dict.keys():
		# Info: ori_path_of_file and backup_loc_of_file
		each_info = non_preex_file_info_dict[each_non_preex_file]
		# File name 
		file_name_non_preex_path = each_non_preex_file
		# Original path of the file
		each_non_preex_path = each_info[0]
		# Backup path of the file
		each_non_preex_backup_loc = each_info[1]
		# Path to backup directory
		path_to_backup_dir = dirname(each_non_preex_backup_loc)

		# Copy and show msg
		copy(each_non_preex_path,each_non_preex_backup_loc)
		file_copied_msg = "# File \"%s\" is copied to \"%s\"."\
			%(blue + file_name_non_preex_path + gray,
				blue + path_to_backup_dir + gray)
		print_color(gray, file_copied_msg)






