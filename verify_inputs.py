#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import walk, chdir
from glob import glob
from sys import exit
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

def verify_user_inputs\
	(immed_or_schedu,backup_dir_input,backup_loc,\
	 full_or_sel,sele_extens,keep_tree_ornot):

	"""
	Show user what he/she had entered and then CNOTINUE or QUIT.

	* Inputs
	"immed_or_schedu" => (1)immediate or (2)scheduled backup
	"backup_dir_input" => directories that user will backup
	"backup_loc" => backup location
	"full_or_sel" => (1)full or (2)selected(extension) backup
	"sele_extens" => if selected backup is chosen, the extension user 
                     entered will show here. if full is chosen,
                     "Copy whole dir" will show.
	"keep_tree_ornot" => (1)keep or (2)do not keep dir tree 
	"""

	# Showing more detailed info
	if immed_or_schedu == "1":
		immed_or_schedu_out = "Immediate backup"
	elif immed_or_schedu == "2":
		immed_or_schedu_out = "Scheduled backup"
	if full_or_sel == "1":
		full_or_sel_out = "Full backup"
	elif full_or_sel == "2":
		full_or_sel_out = "Selected extension backup"
	if keep_tree_ornot == "1":
		keep_tree_ornot_out = "Keep directory tree"
	elif keep_tree_ornot == "2":
		keep_tree_ornot_out = "Do not keep directory tree."

	# Output extension for selected backup, show "Copy the whole directory"
	#  if user chose full backup
	if sele_extens == 0:
		sele_extens = "Copy the whole directory."
	else:
		pass
		# pass means show extension user entered
	
	# Showing prompt
	verify_prompt = """\
-----------------------------------------------------------
# The followings are your previous inputs
-----------------------------------------------------------
@ Immediate or Scheduled backup
=> %s
@ Directories you want to backup
=> %s
@ Path to put your backup files
=> %s
@ Full or selected extension backup
=> %s
@ List of file extensions
=> %s
@ Preserve directory tree or not 
=> %s

# Please check them carefully. BackMeUp won't start copying
  anything before you continue.
# Insert "go" to continue or CTRL-C to quit.
-----------------------------------------------------------"""\
 %(blue+str(immed_or_schedu_out)+default,\
   blue+str(backup_dir_input)+default,\
   blue+str(backup_loc)+default,\
   blue+str(full_or_sel_out)+default,\
   blue+str(sele_extens)+default,\
   blue+str(keep_tree_ornot_out)+default,\
   )
	print verify_prompt

### MUST MAKE A DOUBLE CHECK BEFORE COPYING

# testing the function
"""
verify_user_inputs(immed_or_schedu,backup_dir_input,backup_loc,\
     full_or_sel,sele_extens,keep_tree_ornot)
"""


