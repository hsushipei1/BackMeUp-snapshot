#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

def handle_non_preex_file(non_preex_file_info_dict):
	"""
	$ About this function:
	* Handle the files that are not pre-existing in backup location. 
		Just copy them into backup directory.
	
	$ Input parameters:
	* non_preex_file_info_dict=> dict that stores info of non pre-exist files.
	* Format of the dict: xxx_dict[file_name] = (1)ori_path_of_file,
		(2)file_path_backup_dir

	$ Parameter explaination:
	* (1)ori_path_of_file: The absolute path to the file in its original dir.
	* (2)file_path_backup_dir: If the file is pre-exist, this will the 
	absolute path to that file in its backup dir
	"""
	print "### This is non pre-exist section."

	for each_non_preex_file in non_preex_file_info_dict.keys():
		# Info: ori_path_of_file and backup_loc_of_file
		each_info = non_preex_file_info_dict[each_non_preex_file]
		# File name 
		file_name_non_preex_path = each_non_preex_file
		print file_name_non_preex_path






