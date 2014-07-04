#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

def VeryifyInput\
	(immed_or_schedu,backup_dir_input,backup_loc,\
	 full_or_sel,keep_tree_ornot):
	"""
	Show user what he/she had entered and then CNOTINUE or QUIT.

	* Inputs
	"immed_or_schedu" => 
	"backup_dir_input" => 
	"backup_loc" =>
	"full_or_sel" => 
	"keep_tree_ornot" => 
	"""
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
 %(
