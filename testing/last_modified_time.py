#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

import os.path, time

file = "/home/hsushipei/Working/MeteorData/vor/nc/vor_850.nc"

print "last modified: %s" % time.ctime(os.path.getmtime(file))

