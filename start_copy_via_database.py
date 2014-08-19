#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from shutil import copy2
from posixpath import *
from os import path, makedirs, chdir
from sys import exit

from handle_preexist import handle_preex_file
from handle_non_preexist import handle_non_preex_file
from SLASH import SLASH
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

def copying_keep_tree(data_base_in, backup_loc):
	"""
	$ The function
	Start copying, with directory tree preserved. Will check if the
	file is already existing in backup location.

	$ Inputs
	"data_base_in" => File name of the data base of either full or 
					selected backup
	"backup_loc" => path to store the backup files
	"""
	# read data base
	data_base = open(data_base_in)

	# Create new dict to store file info of each pre-existing and 
	# non pre-existing.
	preex_file_info_dict = {}
	not_preex_file_info_dict = {}
	# Format: xxxx_dict[file_name] = ori_path_of_file, file_path_backup_dir
	#   (1)ori_path_of_file: The absolute path to the file in its original dir.
    #   (2)file_path_backup_dir: If the file is pre-exist, this will the 
    #       absolute path to that file in its backup dir.

	# read and handle each path(file)	
	for per_line in data_base:
		per_path_input = per_line.rstrip()  # drop the "\n"

		# backup_loc_files: paths of the already-backup "files"
		backup_loc_files = backup_loc+per_path_input
		# backup_loc_dirs: Path to dir where the already-backup files reside.
		backup_loc_dirs = dirname(backup_loc_files)
		# File name of each file in the database(ori place)
		backup_file_name = basename(per_path_input)

		### Section that checks if each file is PRE-EXISTING or not,
		### and will store file info of preex/non preex into 
		### "preex_file_info_dict" and "not_preex_file_info_dict"
		
		## Dealing with copying the directory tree.
		if isdir(backup_loc_dirs): # If the "backup_loc_dirs" is already exist
			if isfile(backup_loc_files):
				# File is already exist in backup location
				#print "File %r is already exist!" %(backup_file_name)

				# Store file info (name, ori path, path in backup loc) of
				# these pre-existing files to dict
				preex_file_info_dict[backup_file_name] =\
					 per_path_input, backup_loc_files

			elif not isfile(backup_loc_files):
				# File isnt pre-existing
				#print "File %r isnt exist!" %(backup_file_name) 

				# Store file info of these non pre-existing files to dict
				not_preex_file_info_dict[backup_file_name] = \
					per_path_input, backup_loc_files

		else:
			makedirs(backup_loc_dirs) # If the "backup_loc_dirs" doesnt exist.
									  # create it!

	### What to do after separate files into pre-exist and non pre-exist one.
	#	o For the pre-existing files in "preex_file_info_dict", they will 
	#		be assign into function	"handle_preex_file" to let user to make 
	#		a decision. (overwrite, or not)
	handle_preex_file(preex_file_info_dict)	

	#	o For the files that are not pre-exist, start copying after the 
	#		list is established.
	handle_non_preex_file(not_preex_file_info_dict)	
	
	done_copying_msg = "# Done copying files!"
	print_color(gray, done_copying_msg)
	

## testing the "copy_keep_tree"
#copying_keep_tree(".sele_data_base.txt","/home/hsushipei/PREEXIST_TEST")


def copying_dont_keep_tree(data_base_in,backup_loc):
	"""
	Start copying, and do not keep directory tree. Just copy all files
	to the "backup_loc".

	*Inputs
	data_base_in => File name of the data base of either full or 
					selected backup
	backup_loc => path to store the backup files
	"""
	# read data base
	data_base = open(data_base_in)

	# Create new dict to store file info of each pre-existing and 
	# non pre-existing.
	preex_file_info_dict = {}
	not_preex_file_info_dict = {}
	# Format: xxxx_dict[file_name] = ori_path_of_file, file_path_backup_dir
	#   (1)ori_path_of_file: The absolute path to the file in its original dir.
	#   (2)file_path_backup_dir: If the file is pre-exist, this will the 
	#       absolute path to that file in its backup dir.

	# read and handle each path(file)   
	for per_line in data_base:
		per_path_input = per_line.rstrip()  # drop the "\n"

		# Load slash module
		slash = SLASH()
		# File name of each file in the database(ori place)
		backup_file_name = basename(per_path_input)
		# backup_loc_files: paths of the already-backup "files"
		backup_loc_files = backup_loc+slash+backup_file_name

		if isfile(backup_loc_files):
			# File is already exist in backup location
			#print "File %r is already exist!" %(backup_file_name)

			# Store file info (name, ori path, path in backup loc) of
			# these pre-existing files to dict
			preex_file_info_dict[backup_file_name] =\
				 per_path_input, backup_loc_files

		elif not isfile(backup_loc_files):
			# File isnt pre-existing
			#print "File %r isnt exist!" %(backup_file_name) 

			# Store file info of these non pre-existing files to dict
			not_preex_file_info_dict[backup_file_name] = \
				per_path_input, backup_loc_files

	### What to do after separate files into pre-exist and non pre-exist one.
	#   o For the pre-existing files in "preex_file_info_dict", they will 
	#       be assign into function "handle_preex_file" to let user to make 
	#       a decision. (overwrite, or not)
	handle_preex_file(preex_file_info_dict)

	#   o For the files that are not pre-exist, start copying after the 
	#       list is established.
	handle_non_preex_file(not_preex_file_info_dict)

	done_copying_msg = "# Done copying files!"
	print_color(gray, done_copying_msg)
	
## testing the "copy_keep_tree"
copying_dont_keep_tree("new.BakDataBase","/home/hsushipei/BACKUPLOC")
