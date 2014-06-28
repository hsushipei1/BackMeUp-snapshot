#!~/Software/python-stack/bin/python
#-*- coding: utf-8 -*-
import os, ntpath, sys

"""
 提示使用者輸入備份存放路徑
"""

def BackupLoc():
	print """\
------------------------------------------------------------
# Please enter the absolute path where you want to save the
  backup files.
------------------------------------------------------------"""
	while True:
		BkupPath = raw_input(">")
		if os.path.exists(BkupPath):
			return BkupPath
		else:
			print "Path %r doesn't exist!" %(BkupPath)
			while True:
				DirNotExistPrm = "# What will you do?\
 1)Create it! 2)Try another 3)Leave (1/2/3)\n>"
				opt = raw_input(DirNotExistPrm)
				if opt == "1":
					os.makedirs(BkupPath)
					print "%r is created!" %(BkupPath)
					return BkupPath
				elif opt =="3":
					sys.exit("QUIT!")
				else:
					print "Please try again!"
					pass




