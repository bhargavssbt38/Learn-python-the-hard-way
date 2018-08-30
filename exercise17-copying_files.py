# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 15:46:11 2018

@author: bharg
"""

from sys import argv
from os.path import exists
script, from_file, to_file = argv

print "copying from %s to %s " %(from_file, to_file)

data = open(from_file, 'r')
in_data = data.read()

print "The input file is %d bytes long" %len(in_data)
print "Does the destination file exist %r" %exists(to_file)
print " Hit Enter to continue or press CTRL+C to abort"
raw_input("?")
out = open(to_file, 'a')
out.write(in_data)
print " Done and dusted"
data.close()
out.close()