#!~/Software/python-stack/bin/python
#-*- coding: utf-8 -*-

# 提示並接收使用者輸入欲備份的檔案類型。（使用者可以輸入n個類型)

def FileExtens():
	
# 輸入請以空格隔開
inp = raw_input("> ")
print inp.split(" ")
