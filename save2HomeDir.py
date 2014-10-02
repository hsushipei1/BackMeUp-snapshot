#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
from getpass import getuser
from SLASH import SLASH

"""
The module
  This module helps saving files to user's HOME directory. It returns the 
  path to HOME directory and path in HOME to database, configFile, and
  crontab log.
  *database will be saved to=> "$HOME/BackMeUp/database"
  *configFile will be saved to=> "$HOME/BackMeUp/configFile"
  *crontab log will be saved to=> "$HOME/BackMeUp/crontabLog"
  
  There are three functions in this module,
  1) "get_userHomeDir"=> Return path to user's home directory.
  2) "printDataBSavePath"=> Return "$HOME/BackMeUp/database"
  3) "printConfigFileSavePath"=> Return "$HOME/BackMeUp/configFile"
  4) "printCrontabLogSavePath"=> Return "$HOME/BackMeUp/crontabLog"
"""

def get_userHomeDir():
	"""
	The function
	This function will return the path to user's home directory.
		
	Return
	"homeDir"=> A STRING. The path to user's home directory.
	"""
	# Get user name
	userName = getuser()

	# obtain the SLASH type of user's os
	slash = SLASH()

	# Return 
	if os.name == "posix":
		homeDir = "/home/"+userName
		return homeDir
	elif os.name == "nt":
		homeDir = "C:/Users/"+userName
		return homeDir
		
### testing the function
#print get_userHomeDir()

def printDataBSavePath(path2Home):
	"""
	The function
	  Return the path where database is placed.
	Function input parameter	
	  "path2Home"=> A STRING. Path to user's HOME directory.
	Return
	  
	"""
	# obtain the SLASH type of user's os
	slash = SLASH()

	# Path to user's HOME directory
	path2HOME = path2Home

	# Path in HOME that database will be saved to.
	dataBSavePath = path2HOME + slash + "database"
	return dataBSavePath

def printConfigFileSavePath(path2Home):
	"""
	The function

	Function input parameter

	Return
	"""
	# obtain the SLASH type of user's os
	slash = SLASH()

	# Path to user's HOME directory
	path2HOME = path2Home

	# Path in HOME that configFile will be saved to.
	confgFilSavePath = path2HOME + slash + "conFigFile"
	return confgFilSavePath

def printCrontabLogSavePath(path2Home):
	"""
	The function

	Function input parameter

	Return
	"""
	# obtain the SLASH type of user's os
	slash = SLASH()

	# Path to user's HOME directory
	path2HOME = path2Home

	# Path in HOME that crontab log will be saved to.
	cronLogSavePath = path2HOME + slash + "crontabLog"
	return cronLogSavePath

### Testing functions
print printCrontabLogSavePath(get_userHomeDir())
print printDataBSavePath(get_userHomeDir())
print printConfigFileSavePath(get_userHomeDir())
