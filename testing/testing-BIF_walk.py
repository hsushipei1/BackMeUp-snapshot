#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import *

"""
# How to use walk BIF to traverse subdirctories.

DirPath => 路徑下，包含該路徑的絕對"路徑"。
SubDirNam => 路徑下資料夾的"名稱"(清單)。
FileList => 每個目錄下的檔案(清單)。
"""

path = "/work/hsushipei/Programming/python/Project/"

for DirPath, SubDirNam, FileList in walk(path):
	for EachFile in FileList:
		print DirPath+"/"+EachFile
	"""
	for EachDir in SubDirNam:
		print EachDir
	"""

