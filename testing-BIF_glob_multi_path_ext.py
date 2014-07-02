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
exten_Input = ("*.c","*.py")

# find multiple extension in multiple path
for path in path_input:
	#print path
	for DirPath, SubDirNam, FileList in walk(path):
		chdir(DirPath)
		for Each_Exten in exten_Input:
			glob_find_ext = glob(Each_Exten)
			if not glob_find_ext:  # if glob_find_ext is empty
				# print "nothing is found"
				pass
			else:
				print DirPath+" => "+str(glob_find_ext)



