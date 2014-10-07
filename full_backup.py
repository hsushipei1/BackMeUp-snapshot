#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from sys import exit
from shutil import *
from os import walk

from print_color import print_color
from UnixNt_Encoding import UnixNt_Encoding
from SLASH import SLASH
from save2HomeDir import printDataBSavePath

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

# 
def locate_all_file_multi_dir\
         (sources_dir,data_base_name=".full_data_base.txt"):
	"""
	Copy entire dirctory
	
	*Inputs:
	"sources_dir" => a LIST. Absolute path(in UNICODE type) to the directories 
	this program will search
	"dest_dir" => a STRING. Absolute path to the place you want to store
				            the backup.
	"""
	# Load SLASH() module
	slash = SLASH()	

	# searching reminder
	searching_prompt = "# Searching files and creating data base..."
	print_color(blue,searching_prompt)
	# create data base and save it to $HOME/BackMeUp/database
	databSavePath = printDataBSavePath()
	databFullPath = databSavePath+slash+data_base_name
	data_base = open(databFullPath,"w+")	
	# core of full backup
	for each_input_path in sources_dir: # "each_input_path" UNICODE type
		for dir_path, sub_dir_name, file_list in walk(each_input_path):
			# "dir_path"=> A STRING represents each of "each_input_path" and 
			#   all sub-directories under "path".
			# "sub_dir_name"=> A LIST showing all directories under "dir_path"
			# "file_list"=> A LIST showing all files under "dir_path"
			# *For a simple demo, 
			#   for each_item in walk(path):
			#       print each_item
			for each_file in file_list: # for each file under "each_input_path"
				path_to_save = dir_path+\
								slash.decode(UnixNt_Encoding())+\
								each_file
				print path_to_save
				# Both "dir_path" and "each_file" are UNICODE type
				data_base.write(path_to_save.encode(UnixNt_Encoding()))
				data_base.write("\n")
	# data base is created
	done_search = "# Data base is created!"
	print_color(blue,done_search)
	




