#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

"""
Return the colors as global variable for the main flow strcture program to use
"""

def colors():
	# color (http://www.siafoo.net/snippet/88)
	global default
	global red
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
	return red
	

