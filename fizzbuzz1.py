#!/usr/bin/env python

msg = ''

for num  in  xrange(10,201):
  if num % 2 == 0 and num % 3 == 0:
    msg += 'fizzbuzz'
    print msg
  elif num % 2 == 0:
    msg = 'fizz'
  elif num % 3 == 0:
    msg += 'buzz'
  msg = msg.strip()
  print msg
