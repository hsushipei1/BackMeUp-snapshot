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
			
