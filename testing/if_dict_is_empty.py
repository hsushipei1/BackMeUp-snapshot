
from sys import exit

dict_a = {}
dict_a["one"] = "1"
dict_a["two"] = "2"
dict_a["three"] = "3"
dict_a["four"] = "4"

#print dict_a

for each in dict_a.keys():	
	del dict_a[each]
	print dict_a
	print any(dict_a)
