# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:14:48 2018

@author: bharg
"""
import os
import sys
print "print has", len(sys.path), "members"
print "The members are"
for member in sys.path:
    print member
#print all imported modules
print sys.modules.keys()
print sys.platform
print sys.version
print os.name
print os.getcwd()
files = os.listdir("C:")
for file in files:
    print file