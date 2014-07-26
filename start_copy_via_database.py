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
		per_path_input = per_line.rstrip()  # drop the "\n"

		# backup_loc_dirs: paths of the already-backup "directories"
		backup_loc_dirs = dirname(backup_loc+per_path_input)
		# backup_loc_files: paths of the already-backup "files"
		backup_loc_files = backup_loc+per_path_input

		#######################################
		##### Checking pre-existing file part
		#print backup_loc_dirs     # bak_loc+src_loc: dir need to be searched
		#print per_path_input      # file that will copy
		
		# Copy the directory tree. "makedirs" is same as "mkdir -p"
		# If the "backup_loc_dirs" is already exist
		if isdir(backup_loc_dirs):
			print "%r\n exist" %(backup_loc_dirs)
			if isfile(backup_loc_files):
				print "File %r is already exist! What to do?" %(basename(per_path_input))
				pass
			else:
				print "File %r isnt exist!" %(basename(per_path_input)) 
		else:
			print "%r\n Not exist, but is created!" %(backup_loc_dirs)
			makedirs(backup_loc_dirs)

		""" <REMINDER>
		Is it neccessary to check before copying that the previous
		backup file is exist, newer, older or...?? and should i also 
		check for the "backup_loc_dirs" ??
		"""
		
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
