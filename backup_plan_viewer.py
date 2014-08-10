#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

"""
Module: Backup Plan Viewer

* This function will be just plan "viewer". I will improve it to 
  backup plan "manager" after ver-1.0.
"""

from os import walk, chdir, getcwd, listdir
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

def existn_database_finder(database_extension):
	"""
	$ The function
	* Search previous backup plans(database) before any configuration
	  (will ask user to give a name to a plan everytime he/she configures
	  the backup settings), store the name of databases in a list and this 
	  function will return that list.

	$ Function parameters(Inputs)
	* "database_extension"=> A STRING that is ".BakDataBase" which is the 
	  extension of database in this case.

	$ Returns
	* The function will return "(A, B)"
	* A: "preex_database_name_list"=> A LIST that stores the name of existing
	  database.
	* B: "existn_DatabaseCheck"=> A BOOLEAN VALUE. True means at least one 
	  existing database is found and False means no database is found. The
	  main goal of this variable is to let "user_input_plan_name" function 
	  detect the result of searching existing databse and print "No existing 
	  backup plan is found".
	"""

    # Get path of "./"
	pwd_path = getcwd()

	# Create a list that stores the name of pre-existing databases.
	preex_database_name_list = []

	# A list for "no database can be found". Store the boolean value each time
	# when checking each file in current dir in if expression below.
	# If database is found, store True, and vice versa. If all boolean is F
	# that means no database can be found and will print the message.
	database_NotFoundCheck = []

	# Search file that has user desired extension.
	for EachFileName_CurrnDir in listdir(pwd_path):
		if EachFileName_CurrnDir.endswith(database_extension):
			# Database found!
			#print EachFileName_CurrnDir
			# Store the name of pre-existing database into list
			preex_database_name_list.append(EachFileName_CurrnDir)
			# Store True in "database_NotFoundCheck" list
			database_NotFoundCheck.append(True)
		elif not EachFileName_CurrnDir.endswith(database_extension): 
			# NOT FOUND!
			#print "nothing found"
			# Store True in "database_NotFoundCheck" list
			database_NotFoundCheck.append(False)
			pass
			#return

	# Print no existing backup plan if "database_NotFoundCheck" are all False
	existn_DatabaseCheck = any(database_NotFoundCheck)

	# Go back to "./"
	chdir(pwd_path)
	
	# Return the result
	return preex_database_name_list, existn_DatabaseCheck


def user_input_plan_name(preex_database_name_list, existn_DatabaseCheck):
	"""
	$ The function
	* Ask user to enter the name of curret backup configuration. User can
	  tell BackMeUp to list existing backup plans(database). The name of 
	  current backup can't be identical to any of the existing one.

	$ Function parameters(Inputs)
	* "preex_database_name_list"=> A LIST that stores the name of existing
      database.
	* "existn_DatabaseCheck"=> A BOOLEAN VALUE. If it is False, print 
	  "# No existing backup plan is found!" 

    $ Returns

	"""
	new_plan_name_prompt = """\
-----------------------------------------------------------
# First, you will need a name for the following backup
  configuration to avoid overwriting your previous plans.

# Please give a name to the following backup configuration.
# Type "l" to check the existing backup plan.
-----------------------------------------------------------"""
	print_color(red, new_plan_name_prompt)

	while True:
		new_plan_name = raw_input(">")
		if new_plan_name == "l":  # check for existing plan
			if existn_DatabaseCheck == True:  # At least one DBase is found
				show_preex_DBaseName = \
				"# The name of existing backup plans are:"
				print_color(gray, show_preex_DBaseName)
				for each_preex_DBaseName in preex_database_name_list:
					# "each_preex_DBaseName" is the name of existing database
					print "\"%s\"" %(blue + each_preex_DBaseName + default)
			elif existn_DatabaseCheck == False:  # No database found!
				NoDatabaseFound = "# No existing backup plan is found!"
				print_color(gray, NoDatabaseFound)
		else:  # new name for backup plan.
			# Check if the new name is already exist?
			while True:
				## Obtain the name(w/o extension) of existing database			
				# Create a new list to store the name(w/o extens)
				existn_DatebaseName_woExens = []  # wo=without
				for each_exsitn_databaseName in preex_database_name_list:
					(each_NamewoExtens, cut_extension) = \
						each_exsitn_databaseName.rsplit(".",1)
						# "rsplit" is to split word from end
					existn_DatebaseName_woExens.append(each_NamewoExtens)

				#if new_plan_name 
				print preex_database_name_list
				print existn_DatebaseName_woExens
				exit("=================")

				# Double check which the new name
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
					"# Please try other name for backup plan again or"+\
					" \"l\" to check \n  existing one."
					print_color(gray, reenter_NewName_msg)
					break


### testing the function
#print existn_database_finder(".BakDataBase")

#user_input_plan_name(a)



