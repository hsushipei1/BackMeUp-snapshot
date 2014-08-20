#!/usr/bin/python


while True:
	path = raw_input("Please enter ntpath\n>")
	ntpath = repr(path)[1:-1]
	print ntpath
	print ntpath.split("\\")
