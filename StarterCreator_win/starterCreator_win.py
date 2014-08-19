#!/usr/bin/python

from sys import exit
from os import name, system
from subprocess import call
import platform

"""
Creator for BackMeUp Starter(windows batch file)

path: ansicon, main.py

* This code will be compiled to *.pyc using "py_compile" module
  and then *.pyc binary will be launched in windows environment.


"""

def clear_console():
	# Clear console
	if name == "nt":
		system("cls")
	elif name == "posix":
		system("clear")

# clear console at the beinning
clear_console()

# Welcome to BackMeUp Starter Creator
welcome_msg = """
* Welcome to BackMeUp Starter Creator for Windows

  This program will create BackMeUp starter. 
  You can launch BackMeUp by double clicking the starter.

  "PowerShell" is neccessary for BackMeUp.
  This program will check whether PowerShell is installed.
"""
print welcome_msg
cont1 = raw_input("[Press enter to continue]\n")

# Print OS name of user's 
OS_version = platform.system()+" "+platform.release()
print "# OS of this computer: "+OS_version

# Check whether PowerShell is installed.
try:
	subprocess.call(["powershell","exit"])
	print "\n# Great! PowerShell is installed! Press enter to continue."
except:
	print "\n# PowerShell isnt installed!"
	print "  Please install it and rerun this script."
	#exit("\n# QUIT")

cont2 = raw_input(" ")    # press enter to continue.

#exit("=============================")

clear_console()

# Get ansicon.exe path
ask_ansiconPath_prmp = """\
-------------------------------------------------------------
# Please enter the path for \"ansicon.exe\". You can find it
  in xxxx\\ansi160\\x86\\ansicon.exe
e.g. C:\Users\Jack\\ansi160\\x86\\ansicon.exe
# Notice: Please make sure for your architecture(x86 or x64)
-------------------------------------------------------------"""
print ask_ansiconPath_prmp
ansicon_path = raw_input(">")

# Get main.py path
ask_mainDOTpy_prmp = """\
-------------------------------------------------------------
# Please enter the path for \"main.py\". You can find it in 
  BackMeUp folder.
e.g. C:\User\Jack\BackMeUp\main.py
-------------------------------------------------------------
"""
print ask_mainDOTpy_prmp
mainDOTpy_path = raw_input(">")

# Content of starter
starterContent = """\
@ECHO OFF
cls

:: Enable ASNI color code and launch BackMeUp
powershell.exe ^
-noexit "%s" ^
-noexit "powershell" ^
-noexit "python -B %s"
""" %(ansicon_path, mainDOTpy_path)

# Create starter(windows batch file)
starter_name = "BackMeUp_starter.bat"
starter_open = open(starter_name, "w")
starter_open.write(starterContent)
starter_open.close()
print "BackMeUp Starter is created!"


