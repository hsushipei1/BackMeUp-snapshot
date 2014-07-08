#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from shutil import copy2
from posixpath import *
from os import path, makedirs
from sys import exit

def copying_keep_tree(data_base_in,backup_loc):
	"""
	Start copying, with directory tree preserved.
	"""
	# read data base
	data_base = open(data_base_in)

	# read and handle each path(file)	
	for per_line in data_base:
		per_path_input = per_line.rstrip()  # drop the "\n"

		# backup_loc_dirs: paths of the already-backup directories
		backup_loc_dirs = dirname(backup_loc+per_path_input)

		# Copy the directory tree. "makedirs" is same as "mkdir -p"
		if isdir(backup_loc_dirs):
			print "exist"
		else:
			print "Not exist"
			print backup_loc_dirs
			makedirs(backup_loc_dirs)
			


copying_keep_tree(".sele_data_base.txt","/home/hsushipei/TESFDVDF")
	
