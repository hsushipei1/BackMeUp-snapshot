#!/usr/bin/python

import os
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

def getUserInputSched():
	"""
	The function
	  Ask user to input the time for scheduled backup, using the crontab time
	  format.
	Function input parameter
	  None
	Return
	  "sched_input"=> A STRING. Use the crontab format.
	"""
	ask4SchedPrmp = """\
------------------------------------------------------------
[Arrange a Time for Scheduled Backup]
# Please scheduled a time for your backup. Backup will start
  periodically at the time you set.

# NOTICE: The format for the time is: min hr day mon week.
  Please separate each number by SPACE. The space can ONLY 
  EXIST BETWEEN THOSE NUMBERS.
  e.g. Run backup at 3:00 and 6:00 for everyday(every month,
	   and every week)=> 0 3,6 * * *
------------------------------------------------------------"""	
	print_color(red, ask4SchedPrmp)

	while True:
		# Read the time from user input
		sched_input = raw_input(">")

		# Make double check for the time input
		dblCheckTimeInput = \
		"# Please check carefully for the time and its format."
		print_color(gray, dblCheckTimeInput)
		# Re-print the time
		rePrintTime = "# Are you sure for '%s'? (T: Yes /F: Retry)" \
		%(blue+str(sched_input)+gray)
		print_color(gray, rePrintTime)
		dblCheck_input = raw_input(">")

		if dblCheck_input == "T":     # User accepts the time input
			return sched_input      # Return the time to main.py
		elif dblCheck_input == "F":    # Re-enter the time input
			reEnterPrmp = "# Please re-enter the time again."
			print_color(gray, reEnterPrmp)
			pass
		else:
			trueOrFalseAllowed = "# Only T or F is allowed! Please re-enter the time again."
			print_color(gray, trueOrFalseAllowed)


### Testing the function
#print getUserInputSched()

	
def creatSched2Crontab(backupPlan_name, time4SchedBk, cronLog_name):
	"""
	The function
	  Generate the command(the time of scheduled backup and what command 
	  to launch for crontab) for setting up crontab. (like setting crontab -e)
	  Then "feed" this command to crontab using "os.system"(This is the "add 
	  schedule" section, for the "view, edit, and delete schedule" section, 
	  it's written in BASH.).

	  # Procedure to add a scheduled backup to crontab
	  1) Create a crontab log("~/BackMeUp/cronTab/cronLog") to obtain 
	     the current jobs.
		 $ crontab -l > cronLog 
	  2) Assign the command(backup time and python xxxx_configFile.py) to 
		 the crontab log
		 $ echo 'command' >> cronLog
	  3) Import the cronLog 
		 $ crontab cronLog

	Function input parameter
	  "backupPlan_name"=> A STRING. The name of backup plan.
	  "time4SchedBk"=> A STRING. The time to launch scheduled backup.
	  It use the crontab format=> min hr day mon week.
	  "cronLog_name"=> A STRING. The file name of crontab log.
	Return

	"""
	# Create command for crontab
	schedBk_cmd = \
	time4SchedBk+" python "+backupPlan_name+"_configFile.py"+\
    " # BackMeUp_scheduledBackup_"+backupPlan_name

	# Create a "crontab log" named "cronLog"
	os.system("crontab -l > "+cronLog_name)
	# Assign the command (add a job) to crontab log
	os.system("echo '"+schedBk_cmd+"' >> "+cronLog_name)
	# Add a job fron crontab log
	os.system("crontab "+cronLog_name)	

### Testing the function
#creatSched2Crontab("newPlan", "* * * 3 *", "testCronLog")







