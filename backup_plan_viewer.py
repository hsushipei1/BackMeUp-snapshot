#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import walk, chdir, getcwd
from glob import glob
from sys import exit
from print_color import print_color

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

	$ Note
	* This function will be just plan "viewer". I will improve it to 
	  backup plan "manager" after ver-1.0.
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
	

### testing the function
#print existn_database_finder\
(["/work/hsushipei/Programming/python/Project/BackMeUp"],["*.BakDataBase"])

