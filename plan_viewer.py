#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import walk, chdir, getcwd
from glob import glob
from sys import exit
from print_color import print_color

def backup_plan_viewer(path_input,extension_list):
	"""
	$ The function
	* Show all previous backup plans(configuration) before any configuration
	  (will ask user to give a name to a plan everytime he/she configures
	  the backup settings) in order to prevent overwriting the previous 
	  database.
	$ Function parameters

	$ Returns

	$ Note
	* This function will be just plan "viewer". I will improve it to 
	  backup plan "manager" after ver-1.0.
	"""

    # Get path of "./" Because I use "chdir" in loop below for traversing
    # into sub-directories, I need to go back to "./" after finish searching
    # files.
	pwd_path = getcwd()

	# Search file that has user desired extension.
	for each_path in path_input:
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
						print DirPath+"/"+EachFileName_SameDir

	# Go back to "./"
	chdir(pwd_path)


### testing the function
backup_plan_viewer\
(["/work/hsushipei/Programming/python/Project/BackMeUp"],["*.BakDataBase"])

