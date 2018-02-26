#! /bin/env/python

for num in xrange(100,200):
  msg = ''
  if num % 3 == 0 and  num % 5 == 0:
    msg += 'Fizzbuzz'
  elif num % 3 == 0:
    msg += 'Fizz'
  elif num % 5 == 0:
    msg += 'buzz'
  print msg
