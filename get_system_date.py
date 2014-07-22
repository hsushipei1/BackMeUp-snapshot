#!~/Software/python-stack/bin/python
#-*- coding: utf-8 -*-

from datetime import datetime

def get_system_date():
	"""
	Obtain system date and then return a list of three element: year, 
	month, and day.
	"""
	sys_date = str(datetime.now().date()).split("-")
	#output = sys_date[0]+sys_date[1]+sys_date[2]
	#return output
	return sys_date


