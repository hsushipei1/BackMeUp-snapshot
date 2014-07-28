#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

a = [1,2,3]
b = [4,5,6]

c = []
c.append(a)
c.append(b)
print c

n = 0
for x in a:
	print str(x)+" "+str(b[n])
	n = n + 1

