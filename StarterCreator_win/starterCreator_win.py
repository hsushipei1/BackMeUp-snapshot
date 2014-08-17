#!/usr/bin/python

"""
Creator for BackMeUp Starter(windows batch file)

path: ansicon, main.py

* This code will be compiled to *.pyc using "py_compile" module
  and then *.pyc binary will be launched in windows environment.


"""

# Welcome to BackMeUp Starter Creator
print " "
welcome_msg = """\
* Welcome to BackMeUp Starter Creator for Windows

1) Create BackMeUp starter
2) Checking if PowerShell is installed

"""
print " "
print welcome_msg

# Get ansicon.exe path
ask_ansiconPath_prmp = """\
-------------------------------------------------------------
# Please enter the path for \"ansicon.exe\". You can find it
  in xxxx\\ansi160\\x86\\ansicon.exe
e.g. C:\Users\Jack\\ansi160\\x86\\ansicon.exe
# Notice: Please make sure for your architecture(x86 or x64)
-------------------------------------------------------------
"""
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


# Create starter
starterContent = """\
@ECHO OFF
cls

:: Enable ASNI color code and launch BackMeUp
powershell.exe ^
-noexit "C:\Users\HsuShiPei\python_project\ansi160\x86\ansicon.exe" ^
-noexit "powershell" ^
-noexit "python -B C:\cygwin\home\HsuShiPei\BackMeUp\main.py"
"""

#
# Please use the following module to check user's os version
# os.name
# import platform
# print platform.system(), platform.release()

# and please check whether "PowerShell" is installed or not.

