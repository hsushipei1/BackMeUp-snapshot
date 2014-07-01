#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-
import os, ntpath, sys

"""
建立路徑資料庫
<hot_testing3>
使用python BIF(build-in function)尋找檔案
最後輸出這些檔案的絕對路徑
"""

def FindFile(DirToBeBackup,FilExtList):

FindFile("/home/hsushipei",["*.c","*.f","*.h"])
#FindFile("/home/hsushipei",["*.c"])

