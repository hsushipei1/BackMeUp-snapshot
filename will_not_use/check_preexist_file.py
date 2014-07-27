#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

def check_preexist_file():
	"""
	If user will copy a file that is already exist in the backup location
	BackMeUp will show the name, size, and last modified time of these 
	files.
	"""

######### Use os.stat(file) to obtain the last modified time
#######     and convert the time with time.strftime()
#########     os.path.getsize(file) to get the file size
#########

#########                        NOTICE                 
########## Will move this part into "start_copy_via_database.py"
###         The way to check for the pre-exist file:
###         By the time BackMeUp reads each path from the database,
###         check whether the file is already exist, and then start
###         copying.



