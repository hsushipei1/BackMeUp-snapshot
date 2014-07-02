#!~/Software/python-stack/bin/python
#-*- coding: utf-8 -*-

import os
from os import system
from sys import exit

# 讀入欲備份的資料夾路徑
def ToBeBkupPaths():
	print """\
------------------------------------------------------------
# Please insert the absolute paths of the directories you want
  to backup and separate them with SPACEs 
  e.g. /data1/jackhsu /home/research /usr/share/fonts
------------------------------------------------------------"""
	while True:
		InPaths = raw_input(">")
		BkupPathList = InPaths.split(" ")
		# 製作陣列BoolChk，後面會依每個輸入的路徑檢查是否存在，把Boolean存入
		BoolChk = []
		# 依次判斷輸入的路徑是否存在
		for EachIn in BkupPathList:
			if os.path.exists(EachIn):
				# 如果路徑存在，則BoolChk填入True
				BoolChk.append("True")
			elif not(os.path.exists(EachIn)):
				# 如果路徑存在，則BoolChk填入False，並提示不存在
				BoolChk.append("False")
				print "%r does not exist! Please try again!" %(EachIn)
		# ExistNum統計有幾個路徑是存在(True)的
		ExistNum = BoolChk.count("True")
		# 統計boolean，BoolChk中必須全為True才過，否則必須重新輸入路徑。
		if ExistNum == len(BkupPathList):
			# 回傳輸入的路徑
			return BkupPathList
		else:
			# 重新輸入吧！
			pass


# 存放備份的目的地
def	BkupPlace():
	print """\
-----------------------------------------------------------
# Please enter the absolute path of a directory where you 
  want to put these backups.
-----------------------------------------------------------"""	
	while True:
		BkPlac = raw_input(">")
		# 檢查路徑是否存在
		if os.path.exists(BkPlac):
			# 存在！回傳
			return BkPlac
		else:
			# 不存在
			print "%r does not exist!" %(BkPlac)
			print "(1)Create it. (2)Try another one. (3)Quit. (1/2/3)"
			opt = raw_input(">")
			# 建立新的
			if opt == "1":
				system("mkdir "+BkPlac)
				print "Directory "+BkPlac+" is created!"
				return BkPlac
			# 離開程式
			elif opt =="3":
				exit("Quit. Thank you!")
			# 重試(包括選項2)
			else:
				print "Try another path."
				pass		

# 備份資料夾名稱標記
# 載入抓取系統時間的模組
from GetDate import GetDate

def BkupNamTag():
	# 完整的tag名稱
	InitTag = "_backup_"+GetDate()
	print """\
-----------------------------------------------------------
# The default tag of the already-backup files is %s.
  It will be added just following the original name.
  e.g. research => research%s
  
# Do you accept this tag? (1)Yes. (2)Change another one
-----------------------------------------------------------"""\
 %(InitTag,InitTag)

	while True:
		opt2 = raw_input(">")
		# 接受預設tag名稱，立即回傳
		if opt2 == "1":
			return InitTag
		# 要求更改名稱，此功能留待下一版
		elif opt2 == "2":
			print "Sorry! I'm still working on it. Please use the default \
tag."
			return InitTag
		else:
			print "Please try again!"
			pass
		



