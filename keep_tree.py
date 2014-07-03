#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from sys import exit
from shutil import *
from os import walk
from print_color import print_color

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

def keep_tree_ornot(backup_loc):
	tree_prompt = """\
-----------------------------------------------------------
# Do you want to keep the directory tree(relative path of 
  each file)
  (1) Keep it => Will copy the directory tree into the backup
  place => %r
  (2) Dont keep it => All the backup directories and file will
  put in => %r
-----------------------------------------------------------"""\
	%(backup_loc,backup_loc)
	print_color(red,tree_prompt)

