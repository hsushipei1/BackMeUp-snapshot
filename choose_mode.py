#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from color_print import color_print
#red =  "\33[31;1m"

def immediate_or_scheduled_backup():
	prompt1 = """
------------------------------------------------------------
# There are two backup modes: 
  (1)Immediate backup =>
  (2)Configure for scheduled backup
------------------------------------------------------------"""
	color_print(red, prompt1)

immediate_or_scheduled_backup()


