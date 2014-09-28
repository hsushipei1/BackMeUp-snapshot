#!/usr/bin/python

from UnixNt_Encoding import UnixNt_Encoding
import os

def pathHandling(multPathSeparator):
	"""
	The function
		This function receives (multi)paths input(separate with ",") from 
		user. Then separate each path with "multPathSeparator". Decode into
		unicode to deal with Chinese word. Change the backslash to normal
		slash if using Windows(For Unix systems, unchanged). Last, append 
		each path to a list and then return the list in UNICODE.
	Function input parameter
		"multPathSeparator"=> A STRING. The separator of multi paths. This 
		variable will be assigned to STRING.split().
	Return
		"postHandledPath_list"=> A LIST containing (multi) path in UNICODE
		type.
	"""
	multPathIn = raw_input(">>>")
	# The (multile) paths are separate(split) by "multPathSeparator"
	splitMultiPath = multPathIn.split(multPathSeparator)

	# Create an empty list to hold the post handled paths and to be returned
	#   by this function.
	postHandledPath_list = []

	for eachsplitPath in splitMultiPath:
		# Convert path to UNICODE type
		eachPathDecode = eachsplitPath.decode(UnixNt_Encoding())
		# Change the backslash in path to normal slash for Windows users
		if os.name == "nt": 
			splitWithBkSplash = eachPathDecode.split("\\")
			joinWithSlash = "/".join(splitWithBSplash)
			postHandledPath_list.append(joinWithSlash)
		else:  # For UNIX users, the slashs in paths remained unchanged. 
			postHandledPath_list.append(eachPathDecode)

	return postHandledPath_list
	
###TEsting the function
"""
LIST =pathHandling(",")
for each in LIST:
	print each
"""
