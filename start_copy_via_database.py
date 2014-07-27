#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from shutil import copy2
from posixpath import *
from os import path, makedirs, chdir
from sys import exit

def copying_keep_tree(data_base_in,backup_loc):
	"""
	Start copying, with directory tree preserved.

	*Inputs
	data_base_in => File name of the data base of either full or 
					selected backup
	backup_loc => path to store the backup files
	"""
	# read data base
	data_base = open(data_base_in)

	# read and handle each path(file)	
	for per_line in data_base:
		per_path = per_line.rstrip()  # drop the "\n"

		# Data format in data_base: "T,"+abs_path, (that's the var per_path)
		#	e.g. T,/home/jack/backup.c
		#	"T" is a tag designed for checking pre-exist file.

		# * "per_path_preex_tag" is the tag mentioned above.
		#	The meaning of the tag will be explained later.
		# * "per_path_input" is abs path for the file user wants to copy
		per_path_separ = per_path.split(",")
		per_path_input = per_path_separ[1]
		per_path_preex_tag = per_path_separ[0]

		# backup_loc_dirs: paths of the already-backup "directories"
		backup_loc_dirs = dirname(backup_loc+per_path_input)
		# backup_loc_files: paths of the already-backup "files"
		backup_loc_files = backup_loc+per_path_input
		# File name of each file in the database
		backup_file_name = basename(per_path_input)

		### Checking Pre-existing file section

############          NOTE ON 2014-07-27
##################### NO LONGER NEED TAG FOR PRE-EXISTING FILE
############## JUST CHECK WHETHER THE FILE IS PRE-EXIST OR NOT AND THEN
#############  SEPARATE THEM INTO TWO LISTS LIKE /testing/loop_store_list.py
##############  does.

		# Copy the directory tree. "makedirs" is same as "mkdir -p"
		# If the "backup_loc_dirs" is already exist
		if isdir(backup_loc_dirs):
			##print "%r\n exist" %(backup_loc_dirs)
			if isfile(backup_loc_files):
				#print "File %r is already exist!" %(backup_file_name)
				pass
			else:
				#print "File %r isnt exist!" %(backup_file_name) 
				pass
		else:
			##print "%r\n Not exist, but is created!" %(backup_loc_dirs)
			makedirs(backup_loc_dirs)

		
		# copy files into dir tree "backup_loc_dirs"
		#print "@ Copying: %r \n into %r.\n" %(per_path_input,backup_loc_dirs)	
		#copy2(per_path_input,backup_loc_dirs)

	print "Done copying files!"

## testing the "copy_keep_tree"
copying_keep_tree(".sele_data_base.txt","/home/hsushipei/PREEXIST_TEST")

############ Section above is under development ######################

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

    # read and handle each path(file)   
    for per_line in data_base:
        per_path_input = per_line.rstrip()  # drop the "\n"
        # copy files into dir tree "backup_loc_dirs"
        print "@ Copying: %r \n into %r.\n" %(per_path_input,backup_loc)
        copy2(per_path_input,backup_loc)

    print "Done copying files!"
	
## testing the "copy_keep_tree"
#copying_dont_keep_tree(".sele_data_base.txt","/home/hsushipei/PREEXIST_TEST")
