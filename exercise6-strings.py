# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 13:50:19 2018

@author: bharg
"""
a = 27

print "%r" %a
x = " There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = " Those who know %s and those who %s" %(binary,do_not)

print x
print y


print " I said: %r" %x
#print " I said: %d" %x
print " I said: %s" %x

print " I also said: '%s'" %y

hilarious = False
joke_evaluation = "Isn't that joke so funny? %r" 

print joke_evaluation % hilarious

w = " This is the left side of ..."
e = " a string with a right side"

print w+e