#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

def check_elem_inList(Element, List):
	"""
	$ The function
	Return True if an element is in the list and vice versa.

	$ Function inputs
	"Element"=> A VARIABLE to be check if it is in "List"
	"List"=> A LIST that to be checked.

	$ Return
	True if the element is in list and vice versa.
	"""

	for each_elem in List:
		if Element == each_elem:
			return True
		else:
			return False

### testing function
#print check_elem_inList("one", ["one", "two", "three"])

