#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
from getpass import getuser

def get_userHomeDir():
	"""
	The function
	This function will return the path to user's home directory.
		
	Return
	"homeDir"=> A STRING. The path to user's home directory.
	"""
	# Get user name
	userName = getuser()

	# Return 
	if os.name == "posix":
		homeDir = "/home/"+userName+"/"
		return homeDir
	elif os.name == "nt":
		homeDir = "C:/Users/"+userName+"/"
		return homeDir
		
### testing the function
#print get_userHomeDir()
