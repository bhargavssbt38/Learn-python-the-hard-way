# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 18:33:50 2018

@author: bharg
"""

import os
print os.system('cls')
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


for number in the_count:
    print " This is count %d" %number

for fruit in fruits:
    print "The fruit is %s" %(fruit)

for x in change:
    print "I have %r as change" %(x)

elements = []

for i in range(0,6):
    print " Adding %d to the list" %i
    elements.append(i)

for element in elements:
    print " The element in the list is %d" %element


