#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import name, system

def clear_console():
	"""
	The Function:
	Clear the console.
	"""
	if name == "nt":
		system("cls")
		pass
	elif name == "posix":
		system("clear")

## testing the function
clear_console()
