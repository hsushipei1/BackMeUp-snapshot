#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
from sys import exit

from SLASH import SLASH

def handle_NTpath_out(BackMeUp_path):
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
	
def read_postHandled_NTpath(BackMeUp_path):
	"""
	"""
	# Load SLASH module
	slash = SLASH()

	# Path to the file containing post-handled NT path
	postHandled_NTpath_file = BackMeUp_path+slash+"POST_HANDLED_NT_PATH"

	# Read the post-handled path
	postHandled_file = open(postHandled_NTpath_file)
	postHandled_NTpath = postHandled_file.read()

	# Delete post
	try:
		os.remove(postHandled_NTpath_file)
	except:
		pass

	# Retrun post-handled path
	return postHandled_NTpath

###testing the function
#handle_NTpath_out("/home/hsushipei/Working/BackMeUp")
#print read_postHandled_NTpath("/home/hsushipei/Working/BackMeUp")


