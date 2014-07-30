#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from shutil import copy2,move
from posixpath import *
from os import *
from sys import exit

pwd = getcwd()
file = "/home/hsushipei/PREEXIST_TEST/home/hsushipei/Working/Programming/c/practice/ProbSolvingAndProgDesignC/ch1-var_declare/dec.c"
backup_loc = "/home/hsushipei"

file_name = basename(file)
file_path = dirname(file)
temp_file = "/temp"
temp_name = file_name+".temp"
copy2(file,file_path+temp_file)

chdir(file_path)
rename("temp",temp_name)

#exit("exit")

move(temp_name,backup_loc)

chdir(backup_loc)
new_name = file_name+".new"
rename(temp_name,new_name)

chdir(pwd)





