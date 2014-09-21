#!/usr/bin/python
#-*- coding: utf-8 -*-

import pickle

def createSchedBkConfigFile(backupPlan_name, dataB_extension, \
							keepTree_value, backup_loc, immedSchedIndex):
	"""
	The function:
	Write the following information of scheduled backup and copying function 
	to a file as the scheduled backup launcher (will execute by	
	xxxx_launcherRun.sh) and return the
	list to "main.py". After "main.py" received the list, use pickle.dump() to 
	store the info to configuration file.
	Info to be stored:
	(0) Name of backup plan
	(1) Extension of database
	(2) Index of keeping tree(1=keep tree, 2=dont)
	(3) Backup location (already handled by backup tag)

	Function input parameters:
	"backupPlan_name"=> A STRING. The name of backup plan. This name is given
	  by function "user_input_plan_name" in "main.py".
	"dataB_extension"=> A STRING. The file extension of the databse. It is
	  given by variable "database_extension" in "main.py".
	"keepTree_value"=> A STRING. Value equals "1" means keep dir tree. "2"
	  means do not. It's given by function "keep_tree_ornot" in "main.py".
	"backup_loc"=> A STRING. The path to the backup location and it is 
	  already handled by backup tag(i.e., its value wont changed.). It's
	  given by function "add_tag_2_backupLocation" in "main.py".
	"immedSchedIndex"=> A STRING.  This index determines what kind of
      backup that user wants. If = "1", means immediate backup, and = "2",
      means scheduled backup.

	Return:
	"""
	# Name of configuration file of scheduled backup
	configFile_name = backupPlan_name+"_configFile.py"

	# Name of database
	database_name = backupPlan_name+dataB_extension	

	# Generate configuration file to hold the scheduled backup info and 
	#   the copying functions. The backup is executed simply by
	#   $ python [this_configure_file].py , but of course, it's executed by
	#   schedule management software of user's OS.
	configFile = open(configFile_name ,"w")

	# Content to write
	ConfigFile_content = \
"""\
#!/usr/bin/python
from start_copy_via_database import copying_keep_tree,copying_dont_keep_tree

if %r == "1":
	copying_keep_tree(%r, %r, %r)
	print "Keep tree."
elif  %r == "2":
	copying_dont_keep_tree(%r, %r, %r)
	print "Dont keep tree."
""" %(keepTree_value, \
	database_name, backup_loc, immedSchedIndex, \
    keepTree_value, \
    database_name, backup_loc, immedSchedIndex)

	# Write content to file
	configFile.write(ConfigFile_content)

### Testing the function
#createSchedBkConfigFile("newPlan", ".BakDB", "2", "/home/hsushipei/TESTING_backup_20140918","2")




