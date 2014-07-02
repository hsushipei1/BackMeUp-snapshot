#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

"""
測試以module的方式把替文字上色的動作打包
"""

red =  "\33[31;1m"
blue = "\33[34;1m"
default =  "\033[0m"

def color_print(color,string):
	return color+string+default

print color_print(red,"HELLO")
