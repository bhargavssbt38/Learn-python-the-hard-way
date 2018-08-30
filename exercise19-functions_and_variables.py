# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:22:33 2018

@author: bharg
"""

def cheese_and_crackers(cheese_count, crackers_count):
    print "You have %d cheeses with you" %(cheese_count)
    print "You have %d crackers with you" %(crackers_count)

cheese_and_crackers(20,30)

print " OR we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers =50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print" we can also directly pass values as arguments"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)
