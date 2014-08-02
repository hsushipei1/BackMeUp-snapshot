#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

from sys import exit

dict = {}
dict["one"] = "1"
dict["two"] = "2"
dict["three"] = "3"
dict["four"] = "4"


# Delete keys one by one
for each_key in dict.keys():
	print each_key
	#del dict[each_key]
	#print dict

for each_key_2 in dict:
	del dict[each_key_2]
	print dict
