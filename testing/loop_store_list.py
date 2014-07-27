#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

"""
Try to separate data into list.
"""

# Read database sample 
data = open("database_sample.txt")

# Create empty lists
true_one = []
false_one = []

# Separate T and F into two lists. 
for each_path in data:
	each_path_split = each_path.split(",")
	if each_path_split[0] == "T":
		true_one.append(each_path_split[1])
		print "Detect a True one."
	elif each_path_split[0] == "F":
		false_one.append(each_path_split[1])
		print "Detect a False one."

# Print result
print "The T one=> %r" %(true_one)
print " "
print "The F one=> %r" %(false_one)



