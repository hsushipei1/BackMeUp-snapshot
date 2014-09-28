#!/usr/bin/python

ori_string = raw_input("Please insert NT path.>").decode("utf8")
#mod_string = ori_string
mod_string = ori_string.split("\\")
print"mod_string= "+str(mod_string)

#for eachEle in mod_string:
	#print eachEle.encode("utf8")
	
new_path = "/".join(mod_string)
print new_path
