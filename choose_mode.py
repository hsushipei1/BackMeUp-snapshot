#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

import os
from print_color import print_color
from sys import exit

## colors
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


## choose for immediate or scheduled backup
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
		# 1 => immediate
		if time_2_backup == "1": 
			chose_immed_backup_msg = "# You chose immediate backup."
			print_color(blue,chose_immed_backup_msg)
			return time_2_backup
		# 2 => scheduled
		elif time_2_backup == "2":
			chose_sched_backup_msg = "# You chose scheduled backup."
			print_color(blue,chose_sched_backup_msg)
			return time_2_backup
		else:
			time2backup_try_again = "# Please try again"
			print_color(gray,time2backup_try_again)
	# as this module ends, will return "time_2_backup"
	# time_2_backup = 1 => immediate, 2 => scheduled


## User enters paths that they want to make backup
#  (borrow from AutoBackup-0.1)
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

## Place to put backup
def backup_location(backup_tag):
    """
	$ The function

	$ Function inputs

	$ Return
    """
    prompt4 = """\
------------------------------------------------------------
# Please enter the absolute path where you want to save the
  backup files.
------------------------------------------------------------"""
    print_color(red, prompt4)

	# Check whether there is a backup tag from "backup_tag"
    if backup_tag == " ":     # "space" means no backup tag
       print "User dont need a backup tag!"
    else:
       print "Have a backup tag!"

#########  developing

	# Check whether backup location is exist
    while True:
        BkupPath = raw_input(">")
        # Backup location is exist. Return the path
        if os.path.exists(BkupPath):
            return BkupPath
        else:
            backup_path_not_exi = "# Path %r doesn't exist!" %(BkupPath)
            print_color(gray,backup_path_not_exi)
            while True:
                DirNotExistPrm = "# What will you do?\
 1)Create it! 2)Try another 3)Leave (1/2/3)"
                print_color(red,DirNotExistPrm)
                opt = raw_input(">")
                if opt == "1":
                    os.makedirs(BkupPath)
                    dir_created = "# %r is created!" %(BkupPath)
                    print_color(blue,dir_created)
                    return BkupPath
                elif opt == "2":
                    enter_again = "# Please enter the absolute path for backup location again!"
                    print_color(red,enter_again)
                    break
                elif opt == "3":
                    exit("# QUIT.")
                else:
                    bkup_loc_try_again = "# Please try again."
                    print_color(red,bkup_loc_try_again)
                    pass

## backup entire dir or select file with desired extension
def entire_or_extension_backup():
	prompt3 = """\
------------------------------------------------------------
# Two ways to backup files:
  (1) Full backup => Backup(copy) the entire directories
  (2) Selected backup => Enter the kinds of extension of file
      you want to make backup, and separate them by SPACE
      For example => *.c *.f *.ncl *.gs *.ctl

# Please choose one (1/2) or press CTRL-C to quit.
------------------------------------------------------------"""
	print_color(red, prompt3)

	while True:
		way_2_backup = raw_input(">")
		# full backup
		if way_2_backup == "1":
			print "choose 1"
			return way_2_backup
		# selected backup
		elif way_2_backup == "2":
			print "choose 2"
			return way_2_backup
		else:
			way2backup_try_again = "# Please try again"
			print_color(gray,way2backup_try_again)
	# return 1 => full backup, 2 => selected backup
	# 


