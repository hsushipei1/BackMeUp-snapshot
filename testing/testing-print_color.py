#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

"""
測試以module的方式把替文字上色的動作打包
"""

# 顏色(http://www.siafoo.net/snippet/88)
default =  "\033[0m"
red =  "\33[31;1m"
blue = "\33[34;1m"
gray = "\033[1;30m"
green = "\033[1;32m"
yellow = "\033[1;33m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
crimson = "\033[1;38m"

def color_print(color,string):
	return color+string+default

print color_print(red,"HELLO")
print color_print(blue,"HELLO")
print color_print(gray,"HELLO")
print color_print(green,"HELLO")
print color_print(yellow,"HELLO")
print color_print(magenta,"HELLO")
print color_print(cyan,"HELLO")
print color_print(white,"HELLO")
print color_print(crimson,"HELLO")



