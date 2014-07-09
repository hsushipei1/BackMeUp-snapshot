#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

"""
BackMeUp Project

o Version：1.0dev
o Author: HsuShiPei(徐世裴) (hsushipei1@gmail.com)
o Features: 
o Program Flow Chart:
o Update Record:

"""

##### Import modules 
from os import system, path
from Project_info import ProjInfo
from AuthrInfo import AuthrInfo

from choose_mode import immediate_or_scheduled_backup,\
                        path_to_backup,\
					    backup_location,\
                        entire_or_extension_backup
from full_backup import locate_all_file_multi_dir
from selected_backup import extens_input,\
							find_multi_type_in_multi_dir 
from keep_tree import keep_tree_ornot
from verify_inputs import verify_user_inputs
from start_copy_via_database import copying_keep_tree

##### Part 0: Welcome message, project and author info
# Clear the terminal screen at startup
system("clear")
# Show the project and author info 
ProjInfo()
AuthrInfo()
# Brief intro to BackMeUp?

##### Part 1: Backup configuration
# Immediate or Schduled backup(value returned)
immed_or_schedu = immediate_or_scheduled_backup()
# User enter the dirs that will backup
path_input = path_to_backup()
# where to save backup
backup_loc = backup_location()
# backup entire dir or select extension(value returned)
backup_style = entire_or_extension_backup()
if backup_style == "1": # 1 go to full backup
	locate_all_file_multi_dir(path_input)
	exten_input = 0
elif backup_style == "2": # 2 go to selected backup
	exten_input = extens_input()
	find_multi_type_in_multi_dir(path_input,exten_input)
# keep dir tree(relative path)?(value returned)
keep_tree_value = keep_tree_ornot(backup_loc)

##### Part 2: Verify user inputs
verify_user_inputs(immed_or_schedu,path_input,backup_loc,\
	backup_style,exten_input,keep_tree_value)

##### Part 3: Start backup(copying): full or sele / keep tree or not
# Decide which data base to read from "backup_style"
if backup_style == "1": # full backup
	data_base_in_file = ".full_data_base.txt"
elif backup_style == "2": # selected backup
	data_base_in_file = ".sele_data_base.txt"
# start copying. read data base and backup path
print path.isfile(data_base_in_file)
copying_keep_tree(data_base_in_file,backup_loc)


#==================== Under development 2014-07-09 ==================




