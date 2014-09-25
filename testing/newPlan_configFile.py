#!/usr/bin/python
from start_copy_via_database import copying_keep_tree,copying_dont_keep_tree

if '2' == "1":
	copying_keep_tree('newPlan.BakDB', '/home/hsushipei/TESTING_backup_20140918', '2')
	print "Keep tree."
elif  '2' == "2":
	copying_dont_keep_tree('newPlan.BakDB', '/home/hsushipei/TESTING_backup_20140918', '2')
	print "Dont keep tree."
