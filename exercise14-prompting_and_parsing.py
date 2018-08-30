# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 13:54:03 2018

@author: bharg
"""

from sys import argv
script, user_name=argv
prompt = '>'
print "Hi %s, I'm the %s script" %(user_name, script)
print "I'd would like to ask you few questions"
print "Do you like me %s" %(user_name)
likes = raw_input(prompt)
print " where do you live %s" %user_name
lives = raw_input(prompt)

print "what kind of computer do you have ?"
computer = raw_input(prompt)

print """
Alright, so you said %s about liking me.
You live in %s and you have a %s computer """ %(likes,lives,computer)
 