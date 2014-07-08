#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from shutil import copy2

def copying_keep_tree(data_base_in):
	"""
	Start copying, with directory tree preserved.
	"""
	data_base = open(data_base_in)
	
	for per_line in data_base:
		per_path = per_line.rstrip()
		


copying_keep_tree(".sele_data_base.txt")
	
