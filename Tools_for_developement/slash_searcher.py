#!/usr/bin/python

from os import listdir, getcwd, chdir, path

pwd = getcwd()
chdir("/work/hsushipei/Programming/python/Project/BackMeUp")

for each_file_name in listdir(getcwd()):
	if not path.isdir(each_file_name):
		each_file_open = open(each_file_name)
		for each_line in each_file_open:
			each_line = each_line.rstrip()
			if "\"/\"" in each_line:
				print "Slash is in file: "+each_file_name

chdir(pwd)


