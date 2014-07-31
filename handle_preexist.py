#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import path,stat,rename
from posixpath import *
from sys import exit
from shutil import copy2

from print_color import print_color
from readable_size_convt import readable_format
from get_last_modified_time import get_last_modified_time
from preexist_renaming import rename

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

def handle_preex_file(preexist_lists,preexist_backup_loc_lists):
	"""
	The program flow will move here if the file is already exist.
	First will show these files in lists for user to overview all of them,
	and then will ask your what to do one by one.

	* This module will first show:
	# The following files are already exist in the backup location.
	  (1) Name: "xxxx"
	  (2) Size: aaaa
	  (3) Last modified: yyyymmdd pp:qq
	  (4) Original location: "mm/nn/"
	  (5) Backup location: "aa/bb/cc"
	
	* Then will ask user what will he/she do one file by one file.
	# The file "xxxx" is already exist in "/aaa/bbb/ccc/", overwrite?
	(1) Yes (2) No (3) Yes to all (4) No to all (5) Rename "xxxx" (6)Quit
	* and the next file.....

	The inputs of this module
	* preexist_lists: A list that contains abs paths of the files that are
						already exist.
	* preexist_backup_loc_lists: A list that stores abs path of the backup
								location which contains the pre-exist file.

	"""
	### First, show all the files that are already exist at once.
	#   (and also the info of file)
	# Printing all the file at once.
	print_all_preex_prmp_begin = """\
==============================================================
# The following files are already exist in the backup location.
=============================================================="""
	print_color(red,print_all_preex_prmp_begin)

	# Give serial number to the files
	n = 0
	for each_preex_path in preexist_lists:
		# Get the "file name" in path
		file_name_from_preex_path = basename(each_preex_path)
		# Get the file size and convert into human readable format
		file_size_not_readable = getsize(each_preex_path)		
		file_size = readable_format(file_size_not_readable)
		# Print the file info at once. Just to give user overiew.
		output_file_info_atOnce = \
				 "(%d) File= \"%s\", Size= \"%s\" in \"%s\" " \
				 %(n,\
					blue + str(file_name_from_preex_path) + default,\
					blue + str(file_size) + default,\
					blue + preexist_backup_loc_lists[n] + default)  
				 # Get the backup loc of preexist file from index
		print output_file_info_atOnce
		n = n + 1

	print_all_preex_prmp_end = """\

# Total= %s

# Press ENTER to Continue.""" %(str(n))
	print_color(red,print_all_preex_prmp_end)

	cont1 = raw_input(" ")

	### Ask what to do file by file.
	print_one_by_one_prmp_begin = """\
==============================================================
# Now, BackMeUp will ask what will user do file by file.
=============================================================="""
	print_color(red,print_one_by_one_prmp_begin)

	# Give serial number to the files
	m = 0
	for each_preex_path in preexist_lists:
		# Get the "file name" in path
		file_name_from_preex_path = basename(each_preex_path)
		# Get the path of the original directory of the file
		original_dir_path = dirname(each_preex_path)
		# Get the file size and convert into human readable format
		file_size_not_readable = getsize(each_preex_path)
		file_size = readable_format(file_size_not_readable)
		# Get the last modified time
		last_modif_time = get_last_modified_time(each_preex_path)
		while True:
			each_file_prmp = """\
..............................................................
# The %sth pre-exist file found,
* Name= "%s"
* Size= "%s"
* Last modified= "%s"
* Original place= "%s"
# This file is already exist in its backup location,
  "%s"
..............................................................

# Will you overwrite? (1)Yes (2)No (3)Yes to all (4)No to all (5)Rename"""\
      %(blue + str(m) + red,\
		blue + file_name_from_preex_path + red,\
		blue + file_size + red,\
		blue + last_modif_time + red,\
		blue + original_dir_path + red,\
		blue + preexist_backup_loc_lists[m]+red)
			print_color(red,each_file_prmp)
			
			# Handling the option
			opt = raw_input(">")
			if opt == "1":  
			### 1 ==> Overwrite
				copy2(each_preex_path,preexist_backup_loc_lists[m])
				print "# \"%s\" is overwritten! " %(file_name_from_preex_path)
				return opt
 
			elif opt == "2": 
			### 2 ==> Do not overwrite this file
				print "# \"%s\" will not be overwritten! " \
					%(file_name_from_preex_path)
				return opt

			elif opt == "3":
			### 3 ==> Overwrite the rest
				print			
				return opt

			elif opt == "4":
			### 4 ==> Do not overwrite the rest
				print 
				return opt
	
			elif opt == "5":
			### 5 ==> Renaming
				while True:
					## Read the new name
					# Prompt for renaming
					rename_prmp = \
						"# Please enter a new name for \"%s\"." \
								%(blue + file_name_from_preex_path + red)
					print_color(red,rename_prmp)

					new_name = raw_input(">")
					## Copy and rename the file and save it to backup loc
					#	using copy2 BIF.
					rename(each_preex_path,new_name,\
						preexist_backup_loc_lists[m])

					# Return the opt
					return opt
			else:
				over_write_try_again = "# Please try again."
				print_color(gray,over_write_try_again)

			

#################### Opt5: Create temp file and move it to backup loc		
					


		m = m + 1



