# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 20:00:36 2018

@author: bharg
"""

import os
print os.system('cls')

print "Let's practice everything"

print 'you\'d need to know \'bout escapes with \\ that do \n and \t tabs.'

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n \t where there is none.
"""

print "============"
print poem
print "============="

five = 10-2+3-6
print "This should be five %s" %five

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans / 100
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 1000
beans, jars, crates = secret_formula(start_point)
print " We'd have %d beans, %d jars, and %d crates." %(beans, jars,crates)
print "we can also do that this way:"
start_point = start_point /10
print "we'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)