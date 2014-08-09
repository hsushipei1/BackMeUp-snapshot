#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

"""
Module: Backup Plan Viewer

* This function will be just plan "viewer". I will improve it to 
  backup plan "manager" after ver-1.0.
"""

from os import walk, chdir, getcwd
from glob import glob
from sys import exit

from print_color import print_color

## colors
default =  "\033[0m"
red = "\33[31;1m"
blue = "\33[34;1m"
gray = "\033[1;30m"
green = "\033[1;32m"
yellow = "\033[1;33m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
crimson = "\033[1;38m"

def existn_database_finder(search_path_list,extension_list):
	"""
	$ The function
	* Search previous backup plans(database) before any configuration
	  (will ask user to give a name to a plan everytime he/she configures
	  the backup settings), store the name of databases in a list and this 
	  function will return that list.

	$ Function parameters(Inputs)
	* "search_path_list"=> A LIST that stores the path to be searched. In 
	  this function, the search path will be current directory.
	* "extension_list"=> A LIST that stores the extensions to be looking
	  for. In this function, the extension is given "*.BakDataBase" which is
	  the extension of database.

	$ Returns
	* "preex_database_name_list"=> A LIST that stores the name of existing
	  database.
	"""

    # Get path of "./" Because I use "chdir" in loop below for traversing
    # into sub-directories, I need to go back to "./" after finish searching
    # files.
	pwd_path = getcwd()

	# Create a list that stores the name of pre-existing databases.
	preex_database_name_list = []

	# Search file that has user desired extension.
	for each_path in search_path_list:
		#print path
		for DirPath, SubDirNam, FileList in walk(each_path):
			chdir(DirPath)
			for each_extension in extension_list:
				glob_find_ext = glob(each_extension)
				if not glob_find_ext:  # if glob_find_ext is empty
					#print "nothing is found"
					pass
				else:
					for EachFileName_SameDir in glob_find_ext:
						#print DirPath+"/"+EachFileName_SameDir
						# Store the name of pre-existing database into list
						preex_database_name_list.append(EachFileName_SameDir)

	# Go back to "./"
	chdir(pwd_path)
	
	# Return the result
	return preex_database_name_list
	
def user_input_plan_name(preex_database_name_list):
	"""
	$ The function
	* Ask user to enter the name of curret backup configuration. User can
	  tell BackMeUp to list existing backup plans(database). The name of 
	  current backup can't be identical to any of the existing one.

	$ Function parameters(Inputs)
	* "preex_database_name_list"=> A LIST that stores the name of existing
      database.

    $ Returns

	"""
	new_plan_name_prompt = """\
-----------------------------------------------------------
# Now you will need to give a name to the following backup
  configuration.

# Type "l" to check for the existing backup plan.
-----------------------------------------------------------"""
	print_color(red, new_plan_name_prompt)

	while True:
		new_plan_name = raw_input(">")
		if new_plan_name == "l":  # check for existing plan
			show_preex_DBaseName = \
			"# The name of existing backup plans are:"
			print_color(gray, show_preex_DBaseName)
			for each_preex_DBaseName in preex_database_name_list:
				# "each_preex_DBaseName" is the name of existing database
				print "\"%s\"" %(blue + each_preex_DBaseName + default)
		else:  # new name for backup plan.
			# Double check
			while True:
				NewPlanName_DoubleCheck_Msg = \
				"# Are you sure for \"%s\"? (\"y\" to accept/\"n\" to retry)" \
				%(blue+new_plan_name+gray)
				print_color(gray, NewPlanName_DoubleCheck_Msg)
				NewPlanName_Sure_OrNot = raw_input(">")
				if NewPlanName_Sure_OrNot == "y":
					# Sure. Return the new name
					print new_plan_name
					return new_plan_name
				elif NewPlanName_Sure_OrNot == "n":
					# Retry the other new name
					reenter_NewName_msg = \
					"# Please try other name for backup plan again!"
					print_color(gray, reenter_NewName_msg)
					break


### testing the function
a = existn_database_finder\
(["/work/hsushipei/Programming/python/Project/BackMeUp"],["*.BakDataBase"])

user_input_plan_name(a)



