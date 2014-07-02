#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import *
from glob import *

"""
# Use walk BIF to traverse subdirectoies and glob BIF to search for
  multiple extensions.
"""

path = "/work/hsushipei/Programming/python/Project/"
extension = ("*.c","*.h")
ext_4_glob = []
for DirPath, SubDirNam, FileList in walk(path):
	chdir(DirPath)
	print DirPath+" => "+str(glob("*.py"))

