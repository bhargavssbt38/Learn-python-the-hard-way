# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 22:03:53 2018

@author: bharg
"""

import os
print os.system('cls')

people = 30
cars =40
buses =15

if cars > people:
    print "we should take the cars"
elif cars < people:
    print "We should not take the cars"
else:
    print "we can't decide"

if buses > cars:
    print "That's too many buses"
elif buses < cars:
    print "Maybe we could take the buses"
else: 
    print "we still can't decide"

if people > buses:
    print "Alright, lets just take the buses"
else: 
    print " Fine, let's stay home then."