#!/usr/bin/python

from ntpath import *

ntpath = raw_input("Please enter path.\n>")
#handledPath = repr(ntpath)[1:-1]
handledPath = repr(ntpath)
print handledPath

print "basename= "+basename(handledPath)
print "dirname= "+dirname(handledPath)
