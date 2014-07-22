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
  Do you want to add a backup tag? (1)Yes. (2)No
-----------------------------------------------------------"""\
  %(blue+str(default_tag)+red)
	print_color(red, backup_tag_prompt)

	while True:
		backup_tag_ornot = raw_input(">")
		# Dont want tag
		if backup_tag_ornot == "2":
			no_tag_msg = "# You don't want to use a backup tag."
			print_color(blue,no_tag_msg)
			break
		# Want a tag
		if backup_tag_ornot == "1":
			need_tag_msg = "# You want to use a backup tag."
			print_color(blue,need_tag_msg)
			
			default_or_custom_msg = """\
-----------------------------------------------------------
# What do you want to do?
(1) Use the default tag "%s"
(2) I want to customize it
-----------------------------------------------------------"""\
			%(blue+str(default_tag)+red)
			print_color(red, default_or_custom_msg)

			while True:
				backup_tag_opt = raw_input(">")
				# Chose default tag, return it right away
				if backup_tag_opt == "1":
					chose_default_tag = "# You chose to use the default tag \"%s\"."\
										%(default_tag)
					print_color(blue,chose_default_tag)
					return default_tag 
				# Want to customize the tag
				elif backup_tag_opt == "2":
					chose_customize_tag = "# You want to customize the backup tag."
					print_color(blue,chose_customize_tag)

					# Tips for showing date in customization
					tip_date_in_custom = \
					"If you want the date to be shown in your customization\n\
  , you can enter \"DATE\" at any place you want."
					# keyword for date in customization
					date_keyword = "DATE"

					# Prompt for customizing the tag
					customize_tag_prompt = """\
-----------------------------------------------------------
# Please enter the tag you desired
* %s
-----------------------------------------------------------"""\
					%(blue+tip_date_in_custom+red)
					print_color(red,customize_tag_prompt)
					
					while True:
						# customized backup tag
						customized_tag = raw_input(">")
						# user want date to be shown in their customization
						if date_keyword in customized_tag:
						

######### Trying to replace DATE with real date
	
							#customized_tag
							print "2"
							return default_tag
				else:
					backup_tag_opt_try_again = "# Please try again!"
					print_color(gray,backup_tag_opt_try_again)



### Testing the function
backup_tagging()

