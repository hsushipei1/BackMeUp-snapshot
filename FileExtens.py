#!~/Software/python-stack/bin/python
#-*- coding: utf-8 -*-

"""
 提示並接收使用者輸入欲備份的檔案類型。
 1. 使用者可以輸入n個類型
 2. 不同類型間以空格隔開
"""

def FileExtens():
	# 輸入請以空格隔開
	print"""\
-----------------------------------------------------------
# Please insert file extension yo
-----------------------------------------------------------"""
	inp = raw_input("> ")
	print inp.split(" ")
