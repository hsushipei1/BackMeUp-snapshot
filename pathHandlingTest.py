#!/usr/bin/python

from UnixNt_Encoding import UnixNt_Encoding

def pathHandling():
	multPathIn = raw_input(">>>")
	splitMultiPath = multPathIn.split(",")
	###print splitMultiPath

	postHandledPath_list = []

	for eachsplitPath in splitMultiPath:
		eachPathDecode = eachsplitPath.decode(UnixNt_Encoding())
		splitWithBSplash = eachPathDecode.split("\\")
		joinWithSlash = "/".join(splitWithBSplash)
		postHandledPath_list.append(joinWithSlash)
		###print joinWithSlash
		###print type(joinWithSlash)

	return postHandledPath_list
	

###TEsting the function
#pathHandling()
