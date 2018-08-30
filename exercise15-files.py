# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 14:16:33 2018

@author: bharg
"""

from sys import argv
script, file_name=argv
print " The filename that you wanted to read is %s" %file_name
txt = open(file_name)
print txt.read()
txt.close()

print "Type the filename again"
filename = raw_input('>')
txt_again = open(filename)
print txt_again.read()
txt_again.close()