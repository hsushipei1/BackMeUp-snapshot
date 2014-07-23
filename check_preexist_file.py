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
