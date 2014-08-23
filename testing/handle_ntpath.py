#!/usr/bin/python
#-*- coding: utf-8 -*-

from ntpath import *
import shutil
import ntpath

"""
NT Path Handler

1) Input NT path(w/ backslash)
2) Outout NT path but use foreward slash instead of backslash
   Windows XX accepts foreward slash in file path.
"""
# Input
CopyFrom_prmp = "Enter the abs path to file you want to copy."
print CopyFrom_prmp
ToBeCopyFile_Path_In = raw_input(">")

# Handling
ToBeCopyFile_Path = repr(ToBeCopyFile_Path_In)[1:-1]
splited_path = ToBeCopyFile_Path.split("\\")
print ToBeCopyFile_Path

exit("==============")

ReContru_Dirs_list = []

for each_ele in splited_path:
	if each_ele:
		ReContru_Dirs_list.append(each_ele)

final_ntpath = "/".join(ReContru_Dirs_list)
print final_ntpath



