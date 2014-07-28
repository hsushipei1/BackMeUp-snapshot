#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from os import path
from readable_size import sizeof_fmt

"""
Using a module (sizeof_fmt) that convert the file size in byte into 
human readsable number.
"""

file = "/home/hsushipei/Working/MeteorData/vor/nc/vor_850.nc"

file_size = path.getsize(file)

print sizeof_fmt(file_size)

