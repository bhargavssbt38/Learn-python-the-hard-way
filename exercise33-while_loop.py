# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 18:55:29 2018

@author: bharg
"""

import os
os.system('cls')

i = 0
numbers = []

while i<6:
    numbers.append(i)
    i +=1

print " The numbers in the list are: \n"

for i in numbers:
    print "%d \n" %(i)
