#!/usr/bin/env python

file_sum = 0
f = 'text.txt'

for x in open(f):
  line_value = x.strip()
  if len(line_value) > 0:
    line_value = int(line_value)
    file_sum = file_sum + line_value
print file_sum
