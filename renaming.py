#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from shutil import copy2,move
from posixpath import *
from os import *
from sys import exit

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

def rename(file_abs_path,new_name,file_backup_loc):
	"""
	
	Input parameters
	* file_abs_path=> 
	* new_name=> 
	* file_bacjup_loc=> 
	"""
	### Get necessary variables
	# present working directory
	pwd = getcwd()
	# File name
	file_name = basename(file_abs_path)
	# Path of the file in original directory
	file_path = dirname(file_abs_path)

	### New name
	new_name_input = "/"+new_name

	### Copy the ori file to a "temp" file in the same dir
	copy2(file_abs_path,file_backup_loc+new_name_input)
	success_rename_msg = "# \"%s\" is copied to \"%s\"" \
		%(blue + str(new_name) + red, blue + str(file_backup_loc) + red)
	print_color(red,success_rename_msg)




