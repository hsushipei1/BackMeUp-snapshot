#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from print_color import print_color
from sys import exit

# color (http://www.siafoo.net/snippet/88)
default =  "\033[0m"
red =  "\33[31;1m"
blue = "\33[34;1m"
gray = "\033[1;30m"
green = "\033[1;32m"
yellow = "\033[1;33m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
crimson = "\033[1;38m"

def immediate_or_scheduled_backup():
	prompt1 = """
------------------------------------------------------------
# There are two backup modes: 
  (1)Immediate backup =>
  (2)Configure for scheduled backup
------------------------------------------------------------"""
	print print_color(red, prompt1)

immediate_or_scheduled_backup()


