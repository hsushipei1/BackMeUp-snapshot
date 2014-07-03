#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

import os
from print_color import print_color
from sys import exit

# colors
default =  "\033[0m"
red = "\33[31;1m"
blue = "\33[34;1m"
gray = "\033[1;30m"
green = "\033[1;32m"
yellow = "\033[1;33m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
crimson = "\033[1;38m"

# choose for immediate or scheduled backup
def immediate_or_scheduled_backup():
	prompt1 = """\
------------------------------------------------------------
# There are two backup modes: 
  (1)Immediate backup => Backup(copying) will start right 
     after this configuration script.
  (2)Scheduled backup => Set up configuration for backup 
     first and then make a schedule for your backup, for 
     example, backup some data once a week.

# Please enter (1/2) or press CTRL-C to quit.
------------------------------------------------------------"""
	print_color(red, prompt1)

	while True:
		time_2_backup = raw_input(">")
		if time_2_backup == "1":
			print "choose 1"
			return time_2_backup
			break 
		elif time_2_backup == "2":
			print "choose 2"
			return time_2_backup
			break
		else:
			time2backup_try_again = "# Please try again"
			print_color(gray,time2backup_try_again)
	# as this module ends, will return "time_2_backup"
	# time_2_backup = 1 => immediate, 2 => scheduled


# User enters paths that they want to make backup
# (borrow from AutoBackup-0.1)
def path_to_backup():
    prompt2 = """\
------------------------------------------------------------
# Please insert the absolute paths of the directories you want
  to backup and separate them with SPACEs
  e.g. /data1/jackhsu /home/research /usr/share/fonts
------------------------------------------------------------"""
    print_color(red, prompt2)

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
                path_not_exi_again = \
				"# %r does not exist! Please try again!" %(EachIn)
                print_color(gray,path_not_exi_again)
        # ExistNum統計有幾個路徑是存在(True)的
        ExistNum = BoolChk.count("True")
        # 統計boolean，BoolChk中必須全為True才過，否則必須重新輸入路徑。
        if ExistNum == len(BkupPathList):
            # 回傳輸入的路徑
            return BkupPathList
        else:
            # 重新輸入吧！
            pass



# backup entire dir or select file with desired extension
def entire_or_extension_backup():
	prompt3 = """\
------------------------------------------------------------
# Please choose the way to backup files:
  (1) Full backup => Backup the entire
  (2) Selected backup
  
------------------------------------------------------------"""
	print_color(red, prompt3)



