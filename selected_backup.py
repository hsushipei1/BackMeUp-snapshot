#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import walk, chdir, getcwd
from glob import glob
from sys import exit
from print_color import print_color

"""
Modules for selected backup(CopyTree)
"""

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


# Ask user to enter file extensions he/she wants
def extens_input():
	"""
	Ask user to enter file extensions he/she wants

	* Accept one or more extensions
	* Separate by SPACE
	"""
	Ext_in_prompt = """\
-----------------------------------------------------------
# Please insert the file extensions you want this program 
  to search and then back up. For multiple extensions, please
  separate them by SPACE. e.g. *.c *.f *.gs *.ctl

# Watch out for the format: "star dot <extension>"
-----------------------------------------------------------"""
	print_color(red,Ext_in_prompt)

	while True:
		FilExtIn = raw_input(">")
		"""
		# "FilExtIn" must not end with space, or additonal element(space) 
		   will be appended in the list because he string was separate
		   by space
		"""
		if FilExtIn.endswith(" "): 
			end_wi_space_msg = \
			"""# Last character cannot be \"space\", please try again."""
			print_color(gray,end_wi_space_msg)
			pass
		else:
			FilExtList = FilExtIn.split(" ")
			return FilExtList


# Find multiple extension in multiple path
def find_multi_type_in_multi_dir\
		(path_input,exten_input,data_base_name=".sele_data_base.txt"):
	"""
	* Find multiple extension in multiple path

	* Use walk BIF to traverse subdirectoies and glob BIF to search for
      multiple extensions.
	* Ancestor: CopyTree-0.2dev
	* Inputs:
	path_input => a LIST. Absolute path to the directories this program 
                          will search  
	exten_input => a LIST. File extensions you want this program to look for 
	"""
	# searching reminder
	searching_prompt = "# Searching files and creating data base..."
	print_color(blue,searching_prompt)	
	# create data base
	DataBase = open(data_base_name,"w+")
	
	# Get path of "./" Because I use "chdir" in loop below for traversing
	# into sub-directories, I need to go back to "./" after finish searching
	# files.
	pwd_path = getcwd()

	# function core
	for path in path_input:
		# print path
		for DirPath, SubDirNam, FileList in walk(path):
			chdir(DirPath)
			for Each_Exten in exten_input:
				glob_find_ext = glob(Each_Exten)
				if not glob_find_ext:  # if glob_find_ext is empty
					# print "nothing is found"
					pass
				else:
					for EachFileSamDir in glob_find_ext:
						# print DirPath+"/"+EachFileSamDir
						ToBeSave_path = DirPath+"/"+EachFileSamDir
						# Store the output(abs path) into DataBase
						#	output format: "T,"+abs_path, "T" is a tag
						#	designed for checking pre-exist file.
						#	e.g. T,/home/jack/backup.c
						# for each loop
						DataBase.write("T,"+ToBeSave_path)
						DataBase.write("\n")
	# data base is created
	done_search = "# Data base is created!"
	print_color(blue,done_search)
	
	# Go back to "./"
	chdir(pwd_path)

	# close the opened file
	DataBase.close()

