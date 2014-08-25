#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import name

def SLASH():
	"""
	The Function:
	Use this module to unify development of unix and win version.

	Return:
	Return "/" for posix, "\" for nt
	"""

	if name == "nt":
		#return "\\"
		return "/"
	elif name == "posix":
		return "/"



## testing the function
#print SLASH()
