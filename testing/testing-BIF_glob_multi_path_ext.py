#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import *
from glob import *
from sys import *

"""
# Use walk BIF to traverse subdirectoies and glob BIF to search for
  multiple extensions.
"""

# input
path_input = ["/work/hsushipei/Programming/python/HardWay",\
              "/work/hsushipei/Programming/python/HeadFirst",\
              "/work/hsushipei/Programming/python/Project",\
              "/work/hsushipei/Programming/c",\
              ]
exten_input = ("*.c","*.py")

# function
def find_multi_type_in_multi_dir(path_input,exten_input):
	"""
	* find multiple extension in multiple path
	path_input => a LIST. Absolute path to the directories this program 
                          will search  
	exten_input => a LIST. File extensions you want this program to look for 
	"""
	for path in path_input:
		#print path
		for DirPath, SubDirNam, FileList in walk(path):
			chdir(DirPath)
			for Each_Exten in exten_input:
				glob_find_ext = glob(Each_Exten)
				if not glob_find_ext:  # if glob_find_ext is empty
					# print "nothing is found"
					pass
				else:
					print DirPath+" => "+str(glob_find_ext)

# testing the function
find_multi_type_in_multi_dir(path_input,exten_input)

