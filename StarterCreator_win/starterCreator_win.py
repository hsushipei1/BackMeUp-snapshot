#!/usr/bin/python

"""
Creator for BackMeUp Starter(windows batch file)

path: ansicon, main.py

* This code will be compiled to *.pyc using "py_compile" module
  and then *.pyc binary will be launched in windows environment.


"""

# Welcome to BackMeUp Starter Creator
print " "
welcome_msg = ""

ask_ansiconPath_prmp = "# "


starterContent = """\
@ECHO OFF
cls

:: Enable ASNI color code and launch BackMeUp
powershell.exe ^
-noexit "C:\Users\HsuShiPei\python_project\ansi160\x86\ansicon.exe" ^
-noexit "powershell" ^
-noexit "python -B C:\cygwin\home\HsuShiPei\BackMeUp\main.py"
"""


