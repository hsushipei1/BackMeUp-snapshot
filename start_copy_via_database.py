#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from shutil import copy2
from posixpath import *
from os import path, makedirs, chdir
from sys import exit
from handle_preexist import handle_preex_file

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

	# Lists to store paths of files that are exist/not exist
	preexist_lists = []
	not_preexist_lists = []

	# read and handle each path(file)	
	for per_line in data_base:
		per_path_input = per_line.rstrip()  # drop the "\n"

		# backup_loc_dirs: paths of the already-backup "directories"
		backup_loc_dirs = dirname(backup_loc+per_path_input)
		# backup_loc_files: paths of the already-backup "files"
		backup_loc_files = backup_loc+per_path_input
		# File name of each file in the database
		backup_file_name = basename(per_path_input)

		### Checking Pre-existing file section
		# Copy the directory tree. "makedirs" is same as "mkdir -p"
		# If the "backup_loc_dirs" is already exist
		if isdir(backup_loc_dirs):
			if isfile(backup_loc_files):
				# File is already exist in backup location
				print "File %r is already exist!" %(backup_file_name)
				# Append path to the list
				preexist_lists.append(per_path_input)
			elif not isfile(backup_loc_files):
				# File isnt there.
				print "File %r isnt exist!" %(backup_file_name) 
				# Append path to the list
				not_preexist_lists.append(per_path_input)
		else:
			makedirs(backup_loc_dirs)


##############    NOTE    #############
#### For the paths that are in "preexist_lists" will be assign into function
#### 	"handle_preex_file" to let user to make a decision (overwrite, or not)
#### For the files that are not pre-exist, start copying after the list is est.
	
	### Decide what to do for pre-exist/non-pre-exist files
	# Pre-exist files, assign into "handle_preex_file"
	handle_preex_file(preexist_lists)
		
	
		# copy files into dir tree "backup_loc_dirs"
		#print "@ Copying: %r \n into %r.\n" %(per_path_input,backup_loc_dirs)	
		#copy2(per_path_input,backup_loc_dirs)

	print "Done copying files!"
	
	#### testing 
	print "Pre-exist path %r" %(preexist_lists)
	print " "
	print "not pre-exist path %r" %(not_preexist_lists)

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
