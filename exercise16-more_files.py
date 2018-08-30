# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 15:04:21 2018

@author: bharg
"""

from sys import argv
script, filename = argv

print " we are going to erase %r" %(filename)
print " If you don't want that, hit CTRL-C"
print " If you do want to erase press return"

raw_input("?")

print "opening a file"
txt = open(filename, 'w')
print "Truncating the file. Bye"
txt.truncate()

print " Now you can write into the file"

line1 = raw_input("line1")
line2 = raw_input("line2")

txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.close()
target = open(filename)

print target.read()