#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

def backup_plan_viewer():
	"""
	$ The function
	* Show all previous backup plans(configuration) before any configuration
	  (will ask user to give a name to a plan everytime he/she configures
	  the backup settings) in order to prevent overwriting the previous 
	  database.

	$ Note
	* This function will be just plan "viewer". I will improve it to 
	  backup plan manager after ver-1.0.
	"""

	# To search the existing plans, try to use glob to search the extension
	# of the database. (like *.database) Please take a look at selected 
	# backup for using glob.

