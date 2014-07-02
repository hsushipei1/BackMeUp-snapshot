#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import *

"""
# Use walk BIF to traverse subdirectoies and glob BIF to search for
  multiple extensions.
"""

path = "/work/hsushipei/Programming/python/Project/"

for DirPath, SubDirNam, FileList in walk(path):
	for EachFile in FileList:
		print DirPath+"/"+EachFile

