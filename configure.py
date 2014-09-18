#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from print_color import print_color
from sys import exit

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

def configure_scheduled():
	"""
	The Function: Configuration script for scheduled backup.
	If user chose scheduled backup in main.py, the flow of program will 
	jump from main.py to here and end(by exit() at the end) the scheduled 
	backup process of BackMeUp here. We dont move back to main.py again.
		
	* sample file: AutoBackup -> Configure.py
	* This script will be similar to main.py

	"""


	# Quit after configuration. Do not go back to main.py again
	end_of_configure = """\
# You finished setting configure script. Backup will start automatically at the time you've set."""
	print_color(blue,end_of_configure)
	exit()




