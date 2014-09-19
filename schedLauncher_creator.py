#!/usr/bin/python
#-*- coding: utf-8 -*-

# Launcher for scheduled backup for UNIX-like.

import pickle
from start_copy_via_database import copying_keep_tree,\
                                    copying_dont_keep_tree

def create_schedLauncher(backupPlan_name, dataB_extension, \
						configFile_extension, keepTree_index, \
						backup_loc):
	"""
	The function

	Function input parameter

	Return

	"""
	# Name of configuration file for scheduled backup
	schedConfigFile_name = backupPlan_name+configFile_extension

	# Read(using pickle) the scheduled backup info list from 
	#   configuration file for scheduled backup.
	open_SchedConfigFile = open(schedConfigFile_name, "rb")
	schedInfo_list = pickle.load(open_SchedConfigFile)
	## The list contains:
	# (0) Name of backup plan
	# (1) Extension of database
	# (2) Index of keeping tree(1=keep tree, 2=dont)
	# (3) Backup location (already handled by backup tag)
	
	# **** THE FOLLOWING PART WONT WORK PROPERLY ****
	# **** So far, "copying_keep_tree" and "copying_dont_keep_tree" will ask
	#      user what to do when meeting the pre-existing file, but it is 
	#      not allowed in scheduled backup.
	#     Must force both "copying_keep_tree" and "copying_dont_keep_tree"
	# 	  to overwrite them when meeting any-pre-existing file.
	# Start copying(depend on kepp tree index)
	"""
	if keepTree_index == "1":   # Keep tree
		copying_keep_tree(database_name, new_backup_loc)
	elif keep_tree_value == "2": # do not keep dir tree
    	copying_dont_keep_tree(database_name, new_backup_loc)		
	"""

### Testing the function
create_schedLauncher("newPlan", ".BakDB", \
                        ".configure", "2", \
                        "/home/hsushipei/TESTING_backup_20140918")





