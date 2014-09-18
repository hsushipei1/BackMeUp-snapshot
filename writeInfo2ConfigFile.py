#!/usr/bin/python
#-*- coding: utf-8 -*-

import pickle

def writeInfo2ConfigFile(backupPlan_name, dataB_extension, \
						keepTree_value, backup_loc):
	"""
	The function:
	Store the following information of scheduled backup to a list and return the
	list to "main.py". After "main.py" received the list, use pickle.dump() to 
	store the info to configuration file.
	Info to be stored:
	(0) Name of backup plan
	(1) Extension of database
	(2) Index of keeping tree(1=keep tree, 2=dont)
	(3) Backup location (already handled by backup tag)

	Function input parameters:
	"backupPlan_name"=> A STRING. The name of backup plan. This name is given
	  by function "user_input_plan_name" in "main.py".
	"dataB_extension"=> A STRING. The file extension of the databse. It is
	  given by variable "database_extension" in "main.py".
	"keepTree_value"=> A STRING. Value equals "1" means keep dir tree. "2"
	  means do not. It's given by function "keep_tree_ornot" in "main.py".
	"backup_loc"=> A STRING. The path to the backup location and it is 
	  already handled by backup tag(i.e., its value wont changed.). It's
	  given by function "add_tag_2_backupLocation" in "main.py".

	Return:
	"config_2save"=> A LIST that contains scheduled backup info (0) to (3)
	"""
	# Establish list to store backup configuration
	config_2save = []
	# Storing infos...
	config_2save.append(backupPlan_name)
	config_2save.append(dataB_extension)
	config_2save.append(keepTree_value)
	config_2save.append(backup_loc)
	# Return the list "config_2save" to "main.py"
	return config_2save





