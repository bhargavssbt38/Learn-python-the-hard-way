# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 20:52:25 2018

@author: bharg
"""

import os
print os.system('cls')

people = 20
cats = 30
dogs = 15

if people < cats:
    print " Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drolled on!"

if people > dogs:
    print "The world is dry!"

dogs +=5

if people >= dogs:
    print "People are greater than or equal to dogs"

if people <= dogs:
    print "people are less than equal to dogs"

if people == dogs:
    print "people are dogs"