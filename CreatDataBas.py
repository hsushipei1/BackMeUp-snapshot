#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-
import os, ntpath, sys

"""
建立路徑資料庫
find ./ -name "*.c" -o -name "*.h"
"""

def FindFile(DirToBeBackup,FilExtList):
	for EachExten in FilExtList:
		print EachExten
		#FindCmd = "find "+str(DirToBeBackup)+" -name "+str(FilExtList)
		#print FindCmd
		#print os.system(FindCmd)


FindFile("/home/hsushipei",["*.c","*,f","*.h"])

