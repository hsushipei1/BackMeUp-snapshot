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
		if os.path.exist(BkupPath):
			return BkupPath
		else:
			print "Path %r doesn't exist!" %(BkupPath)
			while True:
				OptPrmt = "# What will you do?\
 1)Create it! 2)Try another 3)Leave (1/2/3)"
				opt = raw_input(">")
				if opt == "1":
					os.makedir(BkupPath)




