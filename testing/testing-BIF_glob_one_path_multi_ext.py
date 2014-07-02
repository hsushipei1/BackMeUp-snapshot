#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import *
from glob import *

"""
# Use walk BIF to traverse subdirectoies and glob BIF to search for
  multiple extensions.
"""

# find multiple extension in one path
path = "/home/hsushipei/Software/src"
exten_Input = ("*.c","*.h","*.o")
for DirPath, SubDirNam, FileList in walk(path):
	chdir(DirPath)
	for Each_Exten in exten_Input:
		print DirPath+" => "+str(glob(Each_Exten))

# NEXT: find multiple extension in multiple path

