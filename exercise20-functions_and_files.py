# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:37:15 2018

@author: bharg
"""

import os
from sys import argv
from os.path import exists
script, input_file =argv

print os.system('cls')
def print_contents(f):
  print  f.read()
    
def rewind(f):
    f.seek(0)

def read_line(line_number, f):
    print line_number, f.readline()
    

print " The provided file as input exists? %r " %exists(input_file)

current_file = open(input_file, 'r')
print_contents(current_file)
rewind(current_file)
current_line_number=1
read_line(current_line_number, current_file)
current_line_number +=1
read_line(current_line_number, current_file)
current_line_number +=1
read_line(current_line_number, current_file)
