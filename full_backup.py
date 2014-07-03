#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from sys import exit
from shutil import *
from os import *

path_dir = ["/work/hsushipei/Programming/python/Project",\
            "/work/hsushipei/Programming/python/HardWay",\
		   ]
"""
path_dir = ["/work/hsushipei/Programming/python/Project"]
"""

dest_dir = "/home/hsushipei/Backup/testing"

def copy_entire_dir(sources_dir,dest_dir):
	"""
	Copy entire dirctory
	
	*Inputs:
	sources_dir => a LIST. Absolute path to the directories this program 
                          will search
	dest_dir => a STRING. Absolute path to the place you want to store
				            the backup.
	"""
	

	for each_input_path in sources_dir:
		for dir_path, sub_dir_name, file_list in walk(each_input_path):
			for each_file in file_list:
				print str(dir_path)+"/"+str(each_file)
	
	


copy_entire_dir(path_dir,dest_dir)



