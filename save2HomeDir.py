#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import os.path
from getpass import getuser
from SLASH import SLASH

"""
MODULE "save2HomeDir"

FUNCTIONS LIST
"get_userHomeDir()"
"printCrontabLogSavePath()"
"printDataBSavePath()"
"printConfigFileSavePath()"
"checkDirsExist(dir_path)"

The module
  This module helps saving files to user's HOME directory. It returns the 
  path to HOME directory and path in HOME to database, configFile, and
  crontab log.
  *database will be saved to=> "$HOME/BackMeUp/database"
  *configFile will be saved to=> "$HOME/BackMeUp/configFile"
  *crontab log will be saved to=> "$HOME/BackMeUp/crontabLog"
  
  Functions in this module,
  1) "get_userHomeDir"=> Return path to user's home directory.
  2) "printDataBSavePath"=> Return "$HOME/BackMeUp/database"
  3) "printConfigFileSavePath"=> Return "$HOME/BackMeUp/configFile"
  4) "printCrontabLogSavePath"=> Return "$HOME/BackMeUp/crontabLog"
  5) "checkDirsExist(dir_path)"=> Check if directory, "dir_path" exists.
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

def printDataBSavePath():
	"""
	The function
	  Return the path where database is placed.
	Function input parameter	
	  None
	Return
	  "dataBSavePath"=> A STRING. The dir path that the database will be 
	  saved to.
	"""
	# obtain the SLASH type of user's os
	slash = SLASH()

	# Path to user's HOME directory
	path2HOME = get_userHomeDir()

	# Path in HOME that database will be saved to.
	dataBSavePath = path2HOME + slash + "BackMeUp" + slash + "database"
	return dataBSavePath

def printConfigFileSavePath():
	"""
	The function
	  Return the path where configuration file is placed.
	Function input parameter
	  None
	Return
	  "dataBSavePath"=> A STRING. The dir path that the configuration file
	   will be saved to.
	"""
	# obtain the SLASH type of user's os
	slash = SLASH()

	# Path to user's HOME directory
	path2HOME = get_userHomeDir()

	# Path in HOME that configFile will be saved to.
	confgFilSavePath = path2HOME + slash + "BackMeUp" + slash + "conFigFile"
	return confgFilSavePath

def printCrontabLogSavePath():
	"""
	The function
	  Return the path where crontab log is placed.
	Function input parameter
	  None
	Return
	  "dataBSavePath"=> A STRING. The dir path that the crontab log
	   will be saved to.
	"""
	# obtain the SLASH type of user's os
	slash = SLASH()

	# Path to user's HOME directory
	path2HOME = get_userHomeDir()

	# Path in HOME that crontab log will be saved to.
	cronLogSavePath = path2HOME + slash + "BackMeUp" + slash + "crontabLog"
	return cronLogSavePath

def checkDirsExist(dir_path):
	"""
	The function
	  This function will check if dir "dir_path" exists. Nothing will happen
	  if it exist, but will create it if not exist.
	Function input
	  "dir_path"=> A STRING. The absolute path to the directory.
	Return
	  Nothing but will create the dir if it does not exist.
	"""
	# Will check if the dir (its path, "dir_path") exists or not, if 
	#   it is not exist, create it.
	if not os.path.isdir(dir_path):    # dir isnt exist
		os.makedirs(dir_path)    # create it
		#print dir_path," isnt exist, created now!!"
	else:
		#print dir_path, " is already exist!!"
		pass

### Testing functions
#print printCrontabLogSavePath()
#print printDataBSavePath()
#print printConfigFileSavePath()
checkDirsExist("/home/hsushipei/BackMeUp/database")
