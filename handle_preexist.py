#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import path,stat,rename
from posixpath import *
from sys import exit
from shutil import copy, copy2

from print_color import print_color
from readable_size_convt import readable_format
from get_last_modified_time import get_last_modified_time
from preexist_renaming import renaming
from clear_console import clear_console

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

def handle_preex_file(preex_file_info_dict):
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
	# clear console before showing the list of pre-existing files.
	clear_console()

	### First, show all the files that are already exist at once.
	#   (and also the info of file)
	# Printing all the file at once.
	print_all_preex_prmp_begin = """\
==============================================================
# The following files are already exist in the backup location.
=============================================================="""
	print_color(red,print_all_preex_prmp_begin)

	### dict stores: file name, ori path of file, and the path to the file
	#		in backup directory.
	# Format: xxx_dict[file_name] = (1)ori_path_of_file,(2)file_path_backup_dir
	#	(1)ori_path_of_file: The absolute path to the file in its original dir.
	#	(2)file_path_backup_dir: If the file is pre-exist, this will the 
	#		absolute path to that file in its backup dir.
	
	# "n" for counting the number of file
	n = 0

	for each_preex_file in preex_file_info_dict.keys():
		# Info: ori_path_of_file + backup_loc_of_file
		each_info =  preex_file_info_dict[each_preex_file]
		# File name
		file_name_from_preex_path = each_preex_file
		# Original path of the file
		each_preex_path = each_info[0]
		# Backup path of the file(not dir)
		file_path_backup_dir = each_info[1]
		# Path to backup dir of the file
		each_preexist_backup_loc = dirname(file_path_backup_dir)

		# Get the file size and convert into human readable format
		file_size_not_readable = getsize(each_preex_path)		
		file_size = readable_format(file_size_not_readable)
		# Print the file info at once. Just to give user overiew.
		output_file_info_atOnce = \
				 "(%d) File= \"%s\", Size= \"%s\" in \"%s\" " \
				 %(n,\
					blue + str(file_name_from_preex_path) + default,\
					blue + str(file_size) + default,\
					blue + each_preexist_backup_loc + default)  
				 # Get the backup loc of preexist file from index
		print output_file_info_atOnce
		n = n + 1

	print_all_preex_prmp_end = """\
# Total= %s
# Press ENTER to Continue.""" %(str(n))
	print_color(red,print_all_preex_prmp_end)

	cont1 = raw_input(" ")

	# clear console before asking user file by file.
	clear_console()

	### Ask what to do file by file.
	print_one_by_one_prmp_begin = """\
==============================================================
# Now, BackMeUp will ask what will user do file by file.
=============================================================="""
	print_color(red,print_one_by_one_prmp_begin)

	# Count the number of the file
	m = 0

	for each_preex_file in preex_file_info_dict.keys():
	# Check whether the dict is empty. not empty=> 5 opts, Empty=> leave this
	#	module.
		if any(preex_file_info_dict):
			# Info: ori_path_of_file and backup_loc_of_file
			each_info =  preex_file_info_dict[each_preex_file]
			# File name
			file_name_from_preex_path = each_preex_file
			# Original path of the file
			each_preex_path = each_info[0]
			# Backup path of the file
			each_preexist_backup_loc = each_info[1]
			# Get the path of the original directory of the file
			original_dir_path = dirname(each_preex_path)
			# Get the path of the backup dir
			path_to_backup_dir = dirname(each_preexist_backup_loc)

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
# The same file is already exist in its backup location,
  "%s"
..............................................................

# Will you overwrite it? (1)Yes (2)No (3)Yes to all (4)No to all (5)Rename"""\
		%(blue + str(m) + red,\
			blue + file_name_from_preex_path + red,\
			blue + file_size + red,\
			blue + last_modif_time + red,\
			blue + original_dir_path + red,\
			blue + each_preexist_backup_loc+red)
				print_color(red,each_file_prmp)
				
				# Handling the option
				opt = raw_input(">")
				if opt == "1":  
				### 1 ==> Overwrite
					# Overwrite the file in backup loc
					copy(each_preex_path,each_preexist_backup_loc)
					opt1_overwrite_msg = \
						"# \"%s\" is overwritten in \"%s\" " \
							%(blue + file_name_from_preex_path + gray,\
								blue + each_preexist_backup_loc + gray)
					print_color(gray, opt1_overwrite_msg)
				
					# Delete the file in dict if it has been handled
					del preex_file_info_dict[each_preex_file]

					# Leave the while loop to continue the next file in dict
					break
	 
				elif opt == "2": 
				### 2 ==> Do not overwrite this file
					# Print that the file wont be overwrite
					opt2_dont_overwrite_msg = \
						"# \"%s\" will not be overwritten! " \
							%(blue + file_name_from_preex_path + gray)
					print_color(gray, opt2_dont_overwrite_msg)
				
					# Delete the file in dict if it has been handled
					del preex_file_info_dict[each_preex_file]
					# Leave the while loop to continue the next file in dict
					break

				elif opt == "3":
				### 3 ==> Overwrite the rest
					# Copy the rest of files in dict
					# 	"_sub" indicates the dict here is the same as the one
					# 	used in outer loop. 
					for each_preex_file_sub in preex_file_info_dict.keys():
						# Info: ori_path_of_file + backup_loc_of_file
						each_info_sub =  preex_file_info_dict[each_preex_file_sub]
						# Original path of the file
						each_preex_path_sub = each_info_sub[0]
						# File name
						file_name_from_preex_path_sub = each_preex_file_sub
						# Backup path of the file
						each_preexist_backup_loc_sub = each_info_sub[1]
						# Copy
						copy(each_preex_path_sub,each_preexist_backup_loc_sub)
						opt3_overwrite_msg = \
							"# \"%s\" is overwritten in \"%s\" " \
								%(blue + file_name_from_preex_path_sub + gray,\
									blue + each_preexist_backup_loc_sub + gray)
						print_color(gray, opt3_overwrite_msg)				

						# Delete the file in dict if it has been handled
						del preex_file_info_dict[each_preex_file_sub]
						#print "dict "+str(preex_file_info_dict)

					print "opt3 is done"

					# Leave this while loop
					break	

				elif opt == "4":
				### 4 ==> Do not overwrite the rest
					for each_preex_file_sub in preex_file_info_dict.keys():
						# Delete the file in dict if it has been handled
						del preex_file_info_dict[each_preex_file_sub]

					# Print a msg
					opt4_overwrite_msg =\
						 "# The rest of the file will not be copied."
					print_color(gray,opt4_overwrite_msg)

					# Leave this while loop
					break	

				elif opt == "5":
				### 5 ==> Renaming
					## Read the new name
					# Prompt for renaming
					rename_prmp = \
						"# Please enter a new name for \"%s\"." \
								%(blue + file_name_from_preex_path + red)
					print_color(red,rename_prmp)

					new_name = raw_input(">")
					## Copy and rename the file and save it to backup loc
					#	using copy2 BIF.
					renaming(each_preex_path,new_name,\
						path_to_backup_dir)

					# Delete the file in dict if it has been handled
					del preex_file_info_dict[each_preex_file]
					# Leave the while loop to continue the next file in dict
					break

				else:
					over_write_try_again = "# Please try again."
					print_color(gray,over_write_try_again)

			# Count for the nth file
			m = m + 1

			# Clear console as user have made decision
			clear_console()

		elif not(any(preex_file_info_dict)):
		# The dict is empty. Leave module!
			#print "The dict is empty."
			return "Ask file by file section is done!"


