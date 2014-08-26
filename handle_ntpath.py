#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
from sys import exit

from SLASH import SLASH

def output_handled_NTpath(BackMeUp_path):
	"""
	"""
	# Load SLASH module
	slash = SLASH()

	# Path to ruby script that handles input of NT path
	ntPathIn_rbFile = BackMeUp_path+slash+"NT_path.rb"

	# Run ruby script that handles input of NT path and write
	# new path with foreward slash to file
	input_prmp = "# Please enter NT path."
	print input_prmp
	os.system("ruby "+ntPathIn_rbFile)
	
def Handling_NTpath_return(BackMeUp_path):
	"""
	"""
	# Load SLASH module
	slash = SLASH()

	# Path to the file containing post-handled NT path
	postHandled_NTpath_file = BackMeUp_path+slash+"POST_HANDLED_NT_PATHs"

	# Read the post-handled path
	postHandled_file = open(postHandled_NTpath_file)
	postHandled_NTpaths = postHandled_file.read()[1:-1].split(", ") 
           # drop "[" and "]" from rb output. NOTICE: split with "comma space"
	PostHandl_NtPath_unicd_list = []
	
	for each_postHandled_NtPath in postHandled_NTpaths:
		each_PostHandl_NtPath_unicd = each_postHandled_NtPath.decode("utf8")
		PostHandl_NtPath_unicd_list.append(each_PostHandl_NtPath_unicd)

	# Delete post
	try:
		os.remove(postHandled_NTpath_file)
	except:
		pass

	# Retrun post-handled path in unicode
	return PostHandl_NtPath_unicd_list

###testing the function
#output_handled_NTpath("/home/hsushipei/Working/BackMeUp")
#print Handling_NTpath_return("/home/hsushipei/Working/BackMeUp")


