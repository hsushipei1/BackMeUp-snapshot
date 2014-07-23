#!~/Software/python-stack/bin/python

from sys import exit

"""
Use the string method "replace" to replace words in string with 
things you like
"""

original = "backup_DATE_ok"
print original

new_DATE = "20140723"

modified = original.replace("DATE",new_DATE)

print modified
