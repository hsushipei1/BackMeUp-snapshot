#!~/Software/python-stack/bin/python
#-*- coding: utf-8 -*-
import os, ntpath, sys

# 提示使用者輸入欲備份的資料夾路徑
def DirToBeBackup():
	print """\
------------------------------------------------------------
# Please insert the absolute path of the directory you want to
  backup. e.g. /data1/jackhsu/research (All the subdirectory 
  under that directory will be backuped) 
------------------------------------------------------------"""

	while True:
		DataBasDir = raw_input(">")
		if os.path.exists(DataBasDir):
			return DataBasDir
		else:
			print "Path %r doesn't exist! \
Please try again or CTRL-C to quit" %(DataBasDir)
			
