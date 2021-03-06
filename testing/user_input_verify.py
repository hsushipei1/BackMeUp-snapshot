#!~/Software/python-stack/bin/python
#-*- coding: utf-8 -*-
import os, ntpath, sys

"""
提示使用者輸入欲備份的資料夾路徑
"""
def DirToBeBackup():
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


"""
 提示並接收使用者輸入欲備份的檔案類型。
 1. 使用者可以輸入n個類型
 2. 不同類型間以空格隔開
"""
def FileExtens():
    print"""\
-----------------------------------------------------------
# Please insert the file extensions you want this program 
  to search and then back up. For multiple extensions, please
  separate them by SPACE. e.g. *.c *.f *.gs *.ctl
-----------------------------------------------------------"""
    FilExtIn = raw_input(">")
    FilExtList = FilExtIn.split(" ")
    return FilExtList


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
                elif opt == "2":
                    print "# Please enter the absolute path for backup location again!"
                    break
                elif opt == "3":
                    sys.exit("QUIT!")
                else:
                    print "Please try again!"
                    pass			


"""
顯示使用者剛才輸入的內容，並讓使用者選擇是否繼續還是重新輸入。
"""
# 替輸出結果上色
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def VeryifyInput(DirToBeBackup,FilExtList,BkupPath):
    print"""\
-----------------------------------------------------------
# Please verify your inputs
-----------------------------------------------------------
@ Absolute path to the directory you want to make a backup
=> %s
@ List of file extensions
=> %s
@ Path to save your backup
=> %s

# Hit ENTER to continute or CTRL-C to quit."""\
 %(bcolors.OKBLUE+str(DirToBeBackup)+bcolors.ENDC,\
   bcolors.OKBLUE+str(FilExtList)+bcolors.ENDC,\
   bcolors.OKBLUE+str(BkupPath)+bcolors.ENDC)
