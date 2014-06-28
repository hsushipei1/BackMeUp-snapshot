#!~/Software/python-stack/bin/python
#-*- coding: utf-8 -*-

"""
 提示並接收使用者輸入欲備份的檔案類型。
 1. 使用者可以輸入n個類型
 2. 不同類型間以空格隔開
"""

def FileExtens():
	print"""\
-----------------------------------------------------------
# Please insert the file extensions you want this program 
  to search and then back up. For multiple extensions, please
  separate them by SPACE. e.g. >*.c *.f *.gs *.ctl
-----------------------------------------------------------"""
	FilExtIn = raw_input("> ")
	FilExtList = FilExtIn.split(" ")
