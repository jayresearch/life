#!/bin/python
#
# This is to count the number of variables and constraints in the model file.
# Date: 25th May, 2017 

import sys

try:

   mode_file = sys.argv[1]

except IndexError:
  
   print "Provide the input .mod model file \n"
   print "exiting...\n"
   exit()

mode_file_pr = open(mode_file, 'r')

output_file = mode_file.split('.')[0] + ".out"
print output_file 
output_file_pw = open(output_file, 'w+')

var_count = 0 
constraint_count = 0 

for line in mode_file_pr:
    try:
       first_word = line.split()[0]
    except IndexError: 
       continue

    if first_word == "var":
       var_count = var_count + 1
    
    if first_word == "s.t.":
       constraint_count = constraint_count + 1

output_file_pw.write("total number of variable: " + str(var_count) + "\n")
output_file_pw.write("total number of constraints: " + str(constraint_count) + "\n")






