#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from glob import *
from os import *

"""
建立路徑資料庫
<hot_testing3>
使用python BIF(build-in function)尋找檔案
最後輸出這些檔案的絕對路徑
"""

<Example: how to traverse directories>

def FindFile(DirToBeBackup,FilExtList):
	FilExt = FilExtList
	for dirName, SubDir, fileList in walk("/home/hsushipei/Software"):
		print "Dir %s found" %(dirName)
		for fname in fileList:
			print "\t%s" %(fname)

"""	
	for file in glob("*.c"):
			print file
"""

#FindFile(["/home/hsushipei","/home/hsushipei/Software"],["*.c","*.f","*.h"])

FindFile("/home/hsushipei",["*.c"])

"""
Example Code
<glob for multiple extension>
>>> import glob
>>> types = ('*.pdf', '*.cpp') # the tuple of file types
>>> files_grabbed = []
>>> for files in types:
...     files_grabbed.extend(glob.glob(files))
... 
>>> files_grabbed   # the list of pdf and cpp files

<how to use glob>
http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-with-python

"""
