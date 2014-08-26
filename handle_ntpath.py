#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
from sys import exit
import subprocess

from SLASH import SLASH
from UnixNt_Encoding import UnixNt_Encoding

def output_handled_NTpath(BackMeUp_path):
	"""
	The function
	Use ruby script "NT_path.rb" to read user input(backslash and 
	chinese big5 issue of python isnt solved yet...QQ, so use ruby 
	in current stage), replace backslash with foreward slash, and
	output the paths to file "POST_HANDLED_NT_PATHs"

	Function Inputs
	"BackMeUp_path"=> The path to BackMeUp where this script can find
	"NT_path.rb".
	"""
	# Load SLASH module
	slash = SLASH()

	# Path to ruby script that handles input of NT path
	ntPathIn_rbFile = BackMeUp_path+slash+"NT_path.rb"
	
	# Run ruby script that handles input of NT path and write
	# new path with foreward slash to file
	input_prmp = ">"
	print input_prmp
	os.system("ruby "+ntPathIn_rbFile)
	
def Handling_NTpath_return(BackMeUp_path):
	"""
	The function
	Read "POST_HANDLED_NT_PATHs" file created by "NT_path.rb". Convert
	each path into unicode to protect chinese words, and return all
	paths.

	Function Inputs
	"BackMeUp_path"=> The path to BackMeUp where this script can find
	"NT_path.rb".

	Returns
	"PostHandl_NtPath_unicd_list"=> A LIST containing post-handled(converted
	to foreward slash) paths in UNICODE type.
	"""
	# Load SLASH module
	slash = SLASH()

	# Path to the file containing post-handled NT path
	postHandled_NTpath_file = BackMeUp_path+slash+"POST_HANDLED_NT_PATHs"

	# Read the post-handled path
	postHandled_file = open(postHandled_NTpath_file)
	postHandled_NTpaths = postHandled_file.read()[1:-1].split(", ") 
           # drop "[" and "]" from rb output. NOTICE: split with "comma space"

	# Create empty list
	PostHandl_NtPath_unicd_list = []
	
	for each_postHandled_NtPath in postHandled_NTpaths:
		# Decode each paths into unicode
		each_PostHandl_NtPath_unicd = \
			each_postHandled_NtPath.decode(UnixNt_Encoding())
		PostHandl_NtPath_unicd_list.append(each_PostHandl_NtPath_unicd[1:-1])

	# Delete pre-existing file
	try:
		os.remove(postHandled_NTpath_file)
	except:
		pass

	# Return post-handled path list "in unicode type"
	return PostHandl_NtPath_unicd_list

###testing the function
#output_handled_NTpath("/home/hsushipei/Working/BackMeUp")
#print Handling_NTpath_return("/home/hsushipei/Working/BackMeUp")


