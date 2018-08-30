# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 21:26:46 2018

@author: bharg
"""
from sys import argv
import os
os.system('cls')
script, first, second, third = argv
age = int(raw_input("Enter your age"))
print "Your age is %d" %age

print "The script is called", script
print "Your first variable is", first
print "Your second variable is", second
print "Your third variable is", third