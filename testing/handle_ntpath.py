#!/usr/bin/python
#-*- coding: utf-8 -*-

from ntpath import *
import shutil
import ntpath

"""
目標
1) NT路徑輸入再印出後不可以出現亂碼
2) windows是否接受路徑中目錄以foreward slash相隔
3) 將NT路徑輸出到螢幕上，是否可以指輸出單一反斜線
"""
# From
CopyFrom_prmp = "Enter the abs path to file you want to copy."
print CopyFrom_prmp
ToBeCopyFile_Path_In = raw_input(">")
#handledPath = repr(ntpath)[1:-1]
ToBeCopyFile_Path = repr(ToBeCopyFile_Path_In)
ToBeCopy_FileName = ntpath.basename(ToBeCopyFile_Path)

# To
CopyTo_prmp = "Enter abs path you want to put your file."
print CopyTo_prmp
CopyTo_Path_In = raw_input(">")
CopyTo_Path = repr(CopyTo_Path_In)

# Copy
shutil.copy2(ToBeCopyFile_Path, CopyTo_Path)

print "File %r is copied to %r." %(ToBeCopy_FileName, CopyTo_Path)



