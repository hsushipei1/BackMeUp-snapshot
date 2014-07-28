#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import path
from posixpath import *
from print_color import print_color
from readable_size_convt import readable_format
from sys import exit
from itertools import product

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

def handle_preex_file(preexist_lists,preexist_backup_loc_lists):
	"""
	The program flow will move here if the file is already exist.
	First will show these files in lists for user to overview all of them,
	and then will ask your what to do one by one.

	* This module will first show:
	# The following files are already exist in the backup location.
	  (1) Name: "xxxx"
	  (2) Size: aaaa
	  (3) Last modified: yyyymmdd pp:qq
	  (4) Original location: "mm/nn/"
	  (5) Backup location: "aa/bb/cc"
	
	* Then will ask user what will he/she do one file by one file.
	# The file "xxxx" is already exist in "/aaa/bbb/ccc/", overwrite?
	(1) Yes (2) No (3) Yes to all (4) No to all (5) Rename "xxxx" (6)Quit
	* and the next file.....

	The inputs of this module
	* preexist_lists

	"""
	### First, show all the files that are already exist at once.
	#   (and also the info of file)
	# Printing all the file at once.
	print_all_preex_prmp = """\
------------------------------------------------------------
# The following files are already exist in the backup location."""
	print (red+print_all_preex_prmp+red)

	# Give serial number to the files
	n = 0
	for each_preex_path in preexist_lists:
		# Get the "file name" in path
		file_name_from_preex_path = basename(each_preex_path)
		# Get the file size and convert into human readable format
		file_size_not_readable = getsize(each_preex_path)		
		file_size = readable_format(file_size_not_readable)

		output = "("+str(n)+") "+\
				 file_name_from_preex_path+" "+\
				 str(file_size)+" in "+\
				 preexist_backup_loc_lists[n]
				# Get the backup loc of preexist file from index
		print output
		n = n + 1



