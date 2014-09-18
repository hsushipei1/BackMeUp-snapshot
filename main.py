#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

"""
BackMeUp Project

o Version：
o Author: HsuShiPei(徐世裴) (hsushipei1@gmail.com)
o Features: 
o Program Flow Chart:
o Update Record:
"""

##### Import modules 
from os import system, path, getcwd
import pickle
from clear_console import clear_console
from project_info import ProjInfo
from author_info import AuthrInfo
from backup_plan_viewer import existn_database_finder, \
								user_input_plan_name
from choose_mode import immediate_or_scheduled_backup,\
                        path_to_backup,\
					    backup_location,\
                        entire_or_extension_backup
from configure import configure_scheduled
from full_backup import locate_all_file_multi_dir
from selected_backup import extens_input,\
							find_multi_type_in_multi_dir 
from keep_tree import keep_tree_ornot
from backup_tag import backup_tagging,\
					   add_tag_2_backupLocation

from verify_inputs import verify_user_inputs
from start_copy_via_database import copying_keep_tree,\
									copying_dont_keep_tree

##### IMMEDIATE BACKUP
### Part 0: Welcome message, project and author info
# Clear the terminal screen at startup
clear_console()
# Show the project and author info 
ProjInfo()
AuthrInfo()
# Brief intro to BackMeUp?

### Part 1: Backup configuration
## Backup Plan Viewer
database_extension = ".BakDB"    # will use this var below

# Obtain the existing name of database
(preex_database_name_list, existn_DatabaseCheck) = \
	existn_database_finder(database_extension)

# Obtain new name for current backup plan
new_name_backup_plan = \
user_input_plan_name(preex_database_name_list, existn_DatabaseCheck)

# Immediate or Schduled backup(value returned)
immed_or_schedu = immediate_or_scheduled_backup()
if immed_or_schedu == "1": # immediate backup, continue
	pass
elif immed_or_schedu == "2": # schedule backup, jump to configure
	# Just create configuration file for scheduled backup
	#   The content of the configuration file will be written in 
	#   SCHEDULED BACKUP section.
	Cret_ConfigFil4Sched = open(new_name_backup_plan+".configure","wb")
	print "# You chose scheduled backup. "
	print "# After all backup configuration is done, BackMeUp will run  "
	print "   immediate backup once to deal with the pre-existing file."
	print "   After that, BackMeUp will overwrite the existing file at each"
	print "   scheduled backup."
	cont = raw_input("press enter to continue.")
	clear_console()
	#configure_scheduled()

# Path to directories that user wants to backup
# "path_input"=>  A LIST containing paths in UNICODE type.
path_input = path_to_backup()

# Choose backup entire dir or select extension(number is returned)
# The name of database is given here.
backup_style = entire_or_extension_backup()
if backup_style == "1": # 1 go to full backup
	database_name = new_name_backup_plan+database_extension
	locate_all_file_multi_dir(path_input, database_name)
	exten_input = 0  # "0" is to tell "verify_user_inputs" user chose full
elif backup_style == "2": # 2 go to selected backup
	database_name = new_name_backup_plan+database_extension
	exten_input = extens_input()
	find_multi_type_in_multi_dir(path_input,exten_input, database_name)

# keep dir tree(relative path)?(value returned)
keep_tree_value = keep_tree_ornot()

# Backup location
backup_loc = backup_location()

# Ask user if he/she needs a backup tag. 
backup_tag = backup_tagging()
new_backup_loc = add_tag_2_backupLocation(backup_tag, backup_loc)

### Part 2: Verify user inputs
verify_user_inputs(new_name_backup_plan, immed_or_schedu,\
path_input, backup_loc,	backup_style,exten_input,\
keep_tree_value, backup_tag)

### Part 3: Start backup(copying): keep tree or not
# Start copying. read data base and new backup path
# decide to preserve directory tree or not
if keep_tree_value == "1": # keep dir tree
	copying_keep_tree(database_name, new_backup_loc)
elif keep_tree_value == "2": # do not keep dir tree
    copying_dont_keep_tree(database_name, new_backup_loc)

##### SCHEDULED BACKUP SECTION
### Store information to backup configuration file, "Cret_ConfigFil4Sched"
### (0) Name of backup plan
### (1) Extension of database
### (2) Index of keeping tree(1=keep tree, 2=dont)
### (3) Backup location (already handled by backup tag)
###   Store them in list in output file(using pickle)
# Establish list to store backup configuration
config_2save = []
config_2save.append(new_name_backup_plan)	# Name of backup plan
config_2save.append(database_extension)     # extension of dataB 
config_2save.append(keep_tree_value)    # 1: keep tree, 2: Dont
config_2save.append(backup_loc)     # Backup location(post-backupTag)
# Store "config_2save" using pickle
pickle.dump(config_2save, Cret_ConfigFil4Sched)
# close file
Cret_ConfigFil4Sched.close()

