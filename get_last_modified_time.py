#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

import os.path, time

def get_last_modified_time(abs_path_file):
	"""
	Obtain the last modified time of the file.
	"""
	return time.ctime(os.path.getmtime(abs_path_file))

