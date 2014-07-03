#-*- coding: utf-8 -*-

"""
測試以module的方式把替文字上色的動作打包
"""

# colors
default =  "\033[0m"
red = "\33[31;1m"
blue = "\33[34;1m"
gray = "\033[1;30m"
green = "\033[1;32m"
yellow = "\033[1;33m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
crimson = "\033[1;38m"

def print_color(color,string):
	print color+string+default



