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
	"""
	User will choose whether he/she will keep the dir tree or not

	* Input
	backup_loc => the path to store backup files.
	
	* Ouput
	
	"""
	tree_prompt = """\
-----------------------------------------------------------
# Do you want to keep the directory tree(relative path of 
  each file)
  (1) Keep it => Will copy the directory tree into the backup
  place => %r
  (2) Dont keep it => All the backup directories and file will
  put in => %r

# Please choose one. (1/2)
-----------------------------------------------------------"""\
	%(backup_loc,backup_loc)
	print_color(red,tree_prompt)

	while True:
		tree_input = raw_input(">")
		if tree_input == "1":
			tree_opt_chose1 = "# 1 is chosen, keep tree."
			print tree_opt_chose1
			return tree_input
		elif tree_input == "2":
			tree_opt_chose2 = "2 is chosen, do not keep tree."
			print tree_opt_chose2
			return tree_input
		else:
			tree_opt_try_again = "# Please try again."
			print_color(gray,tree_opt_try_again)






