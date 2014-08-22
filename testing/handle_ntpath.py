#!/usr/bin/python
#-*- coding: utf-8 -*-

from ntpath import *
import shutil
import ntpath

"""
目標
1) NT路徑輸入再印出後不可以出現亂碼
2) windows是否接受路徑中目錄以foreward slash相隔
3) 將NT路徑輸出到螢幕上，是否可以指輸出單一正斜線
"""
# From
CopyFrom_prmp = "Enter the abs path to file you want to copy."
print CopyFrom_prmp
ToBeCopyFile_Path_In = raw_input(">")

ToBeCopyFile_Path= repr(ToBeCopyFile_Path_In)[1:-1]
ToBeCopy_FileName = ntpath.basename(ToBeCopyFile_Path)
toBeCopy_FileParentDirName = ntpath.dirname(ToBeCopyFile_Path)

splited_path = ToBeCopyFile_Path.split("\\")
#print splited_path

ReContru_Dirs_list = []

for each_ele in splited_path:
	if each_ele:
		ReContru_Dirs_list.append(each_ele)

#print ReContru_Dirs_list

final_ntpath = "/".join(ReContru_Dirs_list)
print final_ntpath



