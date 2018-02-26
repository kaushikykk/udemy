#!/usr/bin/env python

file_sum = 0
f = 'text.txt'

for line in open(f):
  line = line.strip()
  if line:
    line_value = int(line) 
    file_sum = file_sum + line_value

print file_sum
