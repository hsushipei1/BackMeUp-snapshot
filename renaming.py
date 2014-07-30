#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from shutil import copy2,move
from posixpath import *
from os import *
from sys import exit

def rename(file_abs_path,file_backup_loc):
	"""
	
	Input parameters
	* file_abs_path=> 
	* file_bacjup_loc=> 
	"""
	### Get necessary variables
	# present working directory
	pwd = getcwd()
	# File name
	file_name = basename(file_abs_path)
	# Path of the file in original directory
	file_path = dirname(file_abs_path)

	### Temp file settings
	# Copy the file as a temp file
	temp_file = "/tmp"
	# Temp file tag for the file
	temp_name = file_name+".temp"

	### Copy the ori file to a "temp" file in the same dir
	copy2(file_abs_path,file_path+temp_file)

	### Chdir to the dir of ori file and add temp file tag
	print "chdir"
	print "file_path= "+file_path
	chdir(file_path)
	print getcwd()
	print "temp_name= "+temp_name
	#rename("dec.c",temp_name)
	exit("exit before chdir")

	### Move it to backup location
	#print "file_backup_loc= "+file_backup_loc
	#move(temp_name,file_backup_loc)

	exit("exit!!")

"""
pwd = getcwd()
file = "/home/hsushipei/PREEXIST_TEST/home/hsushipei/Working/Programming/c/practice/ProbSolvingAndProgDesignC/ch1-var_declare/dec.c"
backup_loc = "/home/hsushipei"

file_name = basename(file)
file_path = dirname(file)
temp_file = "/temp"
temp_name = file_name+".temp"
copy2(file,file_path+temp_file)

chdir(file_path)
rename("temp",temp_name)

move(temp_name,backup_loc)

chdir(backup_loc)
new_name = file_name+".new"
rename(temp_name,new_name)

chdir(pwd)

"""



