#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

"""
BackMeUp Project

o Version：1.0dev-2014-07-02
o Author: HsuShiPei(徐世裴) (hsushipei1@gmail.com)
o Features: 
o Program Flow Chart:
o Update Record:

"""

from os import system
from Project_info import ProjInfo
from AuthrInfo import AuthrInfo

from choose_mode import immediate_or_scheduled_backup,\
                        path_to_backup



## Clear the terminal screen at startup
system("clear")

## Show the project and author info 
ProjInfo()
AuthrInfo()

## Brief intro to BackMeUp?

## Immediate or Schduled backup
immediate_or_scheduled_backup()

## # User enters paths they want to make backup
path_to_backup()



