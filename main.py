#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

"""
BackMeUp Project

o Version：1.0dev-2014-07-02
o Author: HsuShiPei(徐世裴) (hsushipei1@gmail.com)
o Features: 
o Program Flow Chart:
o Update Record:

"""

##### Import modules 
from os import system
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


##### Part 0: Welcome message, project and author info
# Clear the terminal screen at startup
system("clear")
# Show the project and author info 
ProjInfo()
AuthrInfo()
# Brief intro to BackMeUp?


##### Part 1: Backup configuration
# Immediate or Schduled backup(value returned)
immediate_or_scheduled_backup()
# User enter the dirs that will backup
path_input = path_to_backup()
# where to save backup
backup_loc = backup_location()
# backup entire dir or select extension(value returned)
backup_style = entire_or_extension_backup()
if backup_style == "1": # 1 go to full backup
	locate_all_file_multi_dir(path_input)
elif backup_style == "2": # 2 go to selected backup
	exten_input = extens_input()
	find_multi_type_in_multi_dir(path_input,exten_input)
# keep dir tree(relative path)?
keep_tree_ornot(backup_loc)


