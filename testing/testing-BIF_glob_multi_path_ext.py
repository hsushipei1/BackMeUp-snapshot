#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import walk, chdir
from glob import glob
from sys import exit
from pickle import load

"""
# Use walk BIF to traverse subdirectoies and glob BIF to search for
  multiple extensions.

# HsuShiPei(hsushipei1@gmail.com) 2014-07-02
"""

# input
path_input = ["/work/hsushipei/Programming/python/HardWay",\
              "/work/hsushipei/Programming/python/HeadFirst",\
              "/work/hsushipei/Programming/python/Project",\
              "/work/hsushipei/Programming/c",\
              ]
exten_input = ("*.c","*.py")
#data_base_name="DataBaseName.txt"

# function
def find_multi_type_in_multi_dir\
		(path_input,exten_input,data_base_name=".DataBase.txt"):
	"""
	* find multiple extension in multiple path
	path_input => a LIST. Absolute path to the directories this program 
                          will search  
	exten_input => a LIST. File extensions you want this program to look for 
	"""
	# create data base
	DataBase = open(data_base_name,"w")
	for path in path_input:
		# print path
		for DirPath, SubDirNam, FileList in walk(path):
			chdir(DirPath)
			for Each_Exten in exten_input:
				glob_find_ext = glob(Each_Exten)
				if not glob_find_ext:  # if glob_find_ext is empty
					# print "nothing is found"
					pass
				else:
					for EachFileSamDir in glob_find_ext:
						# print DirPath+"/"+EachFileSamDir
						ToBeSave_path = DirPath+"/"+EachFileSamDir
						# Store the output(abs path) into DataBase
						# for each loop
						DataBase.write(ToBeSave_path)
						DataBase.write("\n")

# testing the function
find_multi_type_in_multi_dir(path_input,exten_input)

