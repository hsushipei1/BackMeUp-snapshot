#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import walk, chdir, getcwd
from glob import glob
from sys import exit

from print_color import print_color
from UnixNt_Encoding import UnixNt_Encoding
from SLASH import SLASH
from save2HomeDir import printDataBSavePath

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
  separate them by COMMA "," . e.g. *.c,*.f,*.gs,*.ctl
  and do not leave any SPACE between them.

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
			FilExtList = FilExtIn.split(",")
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
	"path_input" => a LIST. Absolute path(in UNICODE type) to the directories 
	this program will search  
	"exten_input" => a LIST. File extensions you want this program to look for 
	"""
	# Load SLASH() module
	slash = SLASH()

	# searching reminder
	searching_prompt = "# Searching files and creating data base..."
	print_color(blue,searching_prompt)	
	# create data base and save it to $HOME/BackMeUp/database
	databSavePath = printDataBSavePath()
	databFullPath = databSavePath+slash+data_base_name
	DataBase = open(databFullPath,"w+")
	
	# Get path of "./" Because I use "chdir" in loop below for traversing
	# into sub-directories, I need to go back to "./" after finish searching
	# files.
	pwd_path = getcwd()

	# function core
	for path in path_input:
		#print path
		# "path" is each paths(in UNICODE type) in "path_input" list
		for DirPath, SubDirNam, FileList in walk(path):
			# "DirPath"=> A STRING represents each of "path" and 
			#   all sub-directories under "path".
			# "SubDirNam"=> A LIST showing all directories under "DirPath"
			# "FileList"=> A LIST showing all files under "DirPath"
			# *For a simple demo, 
			#	for each_item in walk(path):
			#		print each_item
			chdir(DirPath)
			# "exten_input" is a list that contains several extensions *.X
			# For each file extension in extension list..
			for Each_Exten in exten_input:  
				# glob(Each_Exten): search files with "Each_Exten"
				# Encoding of "Each_Exten" is the default, UTF8, while 
				#   "DirPath" is UNICODE because "path" is UNICODE
				glob_find_ext = glob(Each_Exten)
				# "glob_find_ext"=> A LIST containing files with 
				#   extension "Each_Exten"
				if not glob_find_ext:  # if "glob_find_ext" is empty
					# NothingFoundMsg = \
					#   "# No "+Each_Exten+" files found!"
					# print_color( gray, NothingFoundMsg )
					pass
				else:
					for EachFileSamDir in glob_find_ext:
						# For each file with extension "Each_Exten" 
						#   in list "glob_find_ext"
						# Encoding of "EachFileSamDir" is UTF8/BIG5, must
						#   decode to unicode => "EachFileSamDir_Unicd"
						EachFileSamDir_Unicd = \
						EachFileSamDir.decode(UnixNt_Encoding())
						ToBeSave_path = DirPath+\
							slash.decode(UnixNt_Encoding())+\
							EachFileSamDir_Unicd		
							# Also decode slash into UNICODE
						print ToBeSave_path

						# Store the output(abs path) into DataBase
						#   for each loop
						# Will write "ToBeSave_path" to file, so encode
						#   to UTF8/BIG5
						DataBase.write(ToBeSave_path.encode(UnixNt_Encoding()))
						DataBase.write("\n")
	# data base is created
	done_search = "# Data base is created!"
	print_color(blue,done_search)
	
	# Go back to "./"
	chdir(pwd_path)

	# close the opened file
	DataBase.close()

