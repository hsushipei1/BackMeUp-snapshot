#!/usr/bin/python
#-*- coding: utf-8 -*-

import os

def UnixNt_Encoding():
	"""
	Detemine encoding type of NT of Unix enviroment
	"""
	if os.name == "nt":
		return "big5"
	elif os.name == "posix":
		return "utf8"
