#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from shutil import *
from os import listdir, path

#def backup_entire_dir(path_input,dest_input):
def backup_entire_dir():
	"""
	Copy entire dirctory
	
	*Inputs:
	path_input => a LIST. Absolute path to the directories this program 
                          will search
	dest_input => a STRING. Absolute path to the place you want to store
				            the backup.
	"""
	source_dir = "/work/hsushipei/Programming/python/Project"
	dest_dir = "/home/hsushipei/Backup/testing"

	#copyfile(source_dir,dest_dir)
	print listdir(source_dir)
	print path

backup_entire_dir()

