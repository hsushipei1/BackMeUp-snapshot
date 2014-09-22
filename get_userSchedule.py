#!/usr/bin/python

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

	Function input parameter

	Return

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
