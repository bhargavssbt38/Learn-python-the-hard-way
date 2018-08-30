# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 11:38:23 2018

@author: bharg
"""

states = {
        'oregon' : 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
        }
cities = {'CA': 'San Franciso', 'MI': 'Detroit', 'FL': 'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print "=" *10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print "=" *10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has" , cities[states['Florida']]

print "=" *10

for state, abbrev in states.items():
    print "The State %s is abbreviated as %s" %(state, abbrev)

print '=' *10
for abbrev, city in cities.items():
    print "%s has the city %s" %(abbrev, city)
    
print '=' *10

for state, abbrev in states.items():
    print "%s is abbreviated as %s and has city %s" %(state, abbrev, cities[abbrev])

print "=" *10
state = states.get('Texas', None)

if not state:
 print "Sorry, no Texas"

city = cities.get('TX', 'Does Not Exist')

print " The city for the state TX is %s" %city
    