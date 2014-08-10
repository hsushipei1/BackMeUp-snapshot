#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

def get_DatabaseName_woExten(Name_wExtens, split_with, maxElem_inResult):
	"""
	$ The function
	This function is mainly designed for splitting the name and extension
	of the database. It can separate the ".BakDataBase" extension and its
	name.

	e.g. "ONE.TWO.THREE.BakDataBase" => "ONE.TWO.THREE" and ".BakDaaBase"

	$ Function inputs
	* "Name_wExtens"=> The original name(with extension) of database 
	* "split_with"=> Split the name with? (Usually ".")
	* "maxElem_inResult"=> Maximum "chops" of the ori name

	$ Return
	* "Name_woExtens"=> File name without extension.
	* "cut_extension"=> The extension
	"""
	(Name_woExtens, cut_extension) = \
	Name_wExtens.rsplit(split_with, maxElem_inResult)
	return Name_woExtens

### testing the function
#print get_DatabaseName_woExten("ONE.TWO.THREE.database", ".", 1)

