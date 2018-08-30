# -*- coding: utf-8 -*-
"""

Created on Sun Jun 24 21:47:44 2018

@author: bharg
"""

import os
os.system('cls')

def print_two(*args):
    arg1, arg2 = args
    print "arg1 %r , arg2 %r" %(arg1, arg2)


def print_two_again(arg1,arg2):
    print "arg1 %r, arg2 %r" %(arg1, arg2)

def print_one(arg1):
   print "arg1 %r" %(arg1)
   
def print_none():
    print" I got no argument"
    
print_two("Hi","SSBT")
print_two_again("Hi", "SSBT")
print_one("watha")
print_none()
