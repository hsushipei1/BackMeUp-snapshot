#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

"""
Convert the file size in byte into human readable number.
"""

def sizeof_fmt(num):
    for x in ['bytes','KB','MB','GB']:
        if num < 1024.0 and num > -1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TB')
