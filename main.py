#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

"""
"Backup Tool" Project(still un-named)

o Version：1.0dev-2014-07-02
o Author: HsuShiPei(徐世裴) (hsushipei1@gmail.com)
o Features: 
o Program Flow Chart:
o Update Record:


"""

import os, ntpath, sys
from Project_info import ProjInfo
from AuthrInfo import AuthrInfo
from user_input_verify import DirToBeBackup, FileExtens,\
                              BackupLoc, VeryifyInput
from CreatDataBas import find_multi_type_in_multi_dir

## 清除終端機畫面
os.system("clear")

## 顯示專案版本以及作者資訊
ProjInfo()
AuthrInfo()

## 第一部份: 使用者輸入以及確認
# 提示使用者輸入預備份的資料夾路徑
DataBasDir = DirToBeBackup()
# 提示使用者輸入預備份的副檔名類型
FilExtList = FileExtens()
# 提示使用者輸入備份存放路徑
BkupPath = BackupLoc()
# 顯示使用者剛才輸入的內容，並讓使用者選擇是否繼續還是重新輸入。
VeryifyInput(DataBasDir,FilExtList,BkupPath)

## 第二部份：利用find指令搜尋使用者指定的副檔名檔案的位置
sys.exit("exit from main!")
#find_multi_type_in_multi_dir(path_input,exten_input)


#============== 正在開發中 Under development 2014/06/29 ================


#------------------------
# 建立新樹狀圖、複製檔案
#-------------------------
LocList = open(DataBaseNam2)              

for each_line in LocList:
    getPATH = ntpath.split(each_line)    # 獲得檔案所在資料夾路徑
    #print each_line.rstrip()      # rstrip(): 刪除行末之\n
    #print getPATH[0]

    os.system("mkdir -p "+backupLoc+getPATH[0]) # 建立新樹狀圖
    os.system("cp "+each_line.rstrip()+ " "+backupLoc+getPATH[0]) # 複製檔案
    print "Done copying %r" %(each_line.rstrip())   # 顯示進度



