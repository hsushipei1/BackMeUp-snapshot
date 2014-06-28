#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

"""
CopyTree 再製樹

o 版本：0.2dev-2014-06-22
o 作者：徐世裴(hsushipei1@gmail.com)
o 功能：複製原資料夾完整的樹狀圖，並選擇複製原資料夾中某特定副檔名的檔案到
        新的備份目錄中(維持原樹狀圖)的資料夾。
o 執行步驟：先以UNIX指令find再指定的目錄下搜尋具有指定副檔名檔案的絕對路徑，
          再建立絕對路徑資料庫。

    /-A -> p.ncl
Ori---B-C -> q.ncl, r.c
    \-D-E -> x.c, y.bin

Ori是原資料夾的最上層，其下分別有A, B, C, D, E子目錄。在新的目的
(例如，BACKUP/下)建立同Ori的樹狀圖

           /-A 
BACKUP-Ori---B-C  
           \-D-E  

再把*.ncl, *.c, *.bin等檔案放入樹狀圖中的同樣的位置。

o 需要使用者輸入的參數
1) DataBasDir
2) FilType
3) FilType


<<版本更新紀錄>>
* 0.01-2014-05-21 => 程式主架構出爐，並且可以正常運作。
* 0.02-2014-05-21 => 加入註解、整合資料庫建立功能進入本src。
* 0.1-2014-06-14 => 程式會詢問使用者要複製的資料夾路徑、副檔名名稱(
                    目前只能一次一種)，原本要進入src修改。另外針對
                    使用者輸入的內容加入判斷功能，例如資料夾路徑不存在
                    以及最後的確認等等。
* 0.2-2014-06-15 => 
"""

import os, ntpath, sys
from Project_info import ProjInfo
from AuthrInfo import AuthrInfo
from ToBeBkUp import DirToBeBackup
from FileExtens import FileExtens

# 顯示專案版本以及作者資訊
ProjInfo()
AuthrInfo()

# 提示使用者輸入預備份的資料夾路徑
DataBasDir = DirToBeBackup()
print DataBasDir
print type(DataBasDir)
sys.exit("exit from main!")

# 提示使用者輸入預備份的副檔名類型
FileExtens()


#============== 正在開發中 Under development 2014/06/20 ================

#----------------------------------------
# Print out the user-input variables and
# ask the user to double check the inputs
#----------------------------------------
print"""\
# Please verify your inputs
1) Parent directory to be backup
=> %s

2) Extensions of files you want to backup
=> %s

3) Backup location
=> %s

# Hit RETURN to continue or CTRL-C to quit
""" %(DataBasDir,FilType,backupLoc)

opt2 = raw_input(prompt)         # continue or not

#-------------------
# Establish database
#-------------------
os.system("find "+DataBasDir+" -iname "+FilType+" > "+DataBaseNam+"")

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



