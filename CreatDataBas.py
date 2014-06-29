#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-
import os, ntpath, sys

"""
建立路徑資料庫
find ./ -name "*.c" -o -name "*.h"
"""

def FindFile(DirToBeBackup,FilExtList):
	if len(FilExtList) == 1:
		FilExt = FilExtList.pop()
		DirToBeBackup = str(DirToBeBackup)
		FilExt = str(FilExt)
		FindCmd = "find "+str(DirToBeBackup)+" -name "+str(FilExt)
		print FindCmd
	else:
		try:
			n = 0
			for EachExten in FilExtList:
				DirToBeBackup = str(DirToBeBackup)
				FirstExt = str(FilExtList[0])
				FindCmd = "find "+DirToBeBackup+" -name "+FirstExt
				FilExt = FilExtList[n+1]
				FindCmd.append(" -o -name "+FilExt)
				n = n + 1
		except:
			print "error occured!"
			print FindCmd
			pass
		

print "END!!"

FindFile("/home/hsushipei",["*.c","*.f","*.h"])
#FindFile("/home/hsushipei",["*.c"])

