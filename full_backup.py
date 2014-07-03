#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from sys import exit
from shutil import *
from os import *
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


path_dir = ["/work/hsushipei/Programming/python/Project",\
            "/work/hsushipei/Programming/python/HardWay",\
		   ]
"""
path_dir = ["/work/hsushipei/Programming/python/Project"]
"""

dest_dir = "/home/hsushipei/Backup/testing"

def copy_entire_dir\
         (sources_dir,dest_dir,data_base_name=".full_data_base.txt"):
	"""
	Copy entire dirctory
	
	*Inputs:
	sources_dir => a LIST. Absolute path to the directories this program 
                          will search
	dest_dir => a STRING. Absolute path to the place you want to store
				            the backup.
	"""
	# searching reminder
	searching_prompt = "# Searching files and creating data base..."
	print_color(blue,searching_prompt)
	# create data base
	data_base = open(data_base_name,"w")	

	for each_input_path in sources_dir:
		for dir_path, sub_dir_name, file_list in walk(each_input_path):
			for each_file in file_list:
				print str(dir_path)+"/"+str(each_file)
	
	


copy_entire_dir(path_dir,dest_dir)



