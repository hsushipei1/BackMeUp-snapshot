#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

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

def backup_tagging():
	"""
	Ask user whether he wants backup tag or not. If yes, will he use
	the default one or custome by himself.

	* Default tag: [original_name]_backup_yyyymmdd

	"""

### "get_system_time" function

	default_tag = "_backup_"+ #time returned from "get_system_time"

	bakup_tag_prompt = """\
-----------------------------------------------------------
# Would you like to add a backup tag following the name?
  The default tag is: "_backup_<date>" 
  (For example, the original name of the directory is 
  "research", and a default tag "_backup_<date>" is added, 
  so becomes , like, "research_backup_20140722".)

# You can customize the tag later on! 
  Will you want to add it? (1)Yes. (2)No
-----------------------------------------------------------"""
	print_color(red, bakup_tag_prompt)

	while True:
		backup_tag_opt = raw_input(">")



### Testing the function
#backup_tagging()

