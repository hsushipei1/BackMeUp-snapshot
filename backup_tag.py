#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from print_color import print_color
from get_system_date import get_system_date

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

def backup_tagging():
	"""
	Ask user whether he wants backup tag or not. If yes, will he use
	the default one or custome by himself.

	* Default tag: [original_name]_backup_yyyymmdd

	"""

	# Get system date. Return a list, contains year, month, and day
	sys_time = get_system_date()

	# Default tag
	default_tag = "_backup_"+sys_time[0]+sys_time[1]+sys_time[2]

	backup_tag_prompt = """\
-----------------------------------------------------------
# To distinguish the original and the backup directories,
  BackMeUp offers a backup tag.
  For example, the original name of the directory is 
  "research", and a default tag "_backup_<date>" is added, 
  so becomes , like, "research_backup_20140722".

# The default backup tag is "%s"
  You can customize the tag later on if you'd like to! 
  Will you want to add a backup tag? (1)Yes. (2)No
-----------------------------------------------------------"""\
  %(blue+str(default_tag)+red)
	print_color(red, backup_tag_prompt)

	while True:
		backup_tag_opt = raw_input(">")
		# Chose default tag, return it right away
		if backup_tag_opt == "1":
			return default_tag 
		# Customize the tag
		elif backup_tag_opt == "2":


### Testing the function
backup_tagging()

