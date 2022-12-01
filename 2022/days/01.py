#!/usr/bin/env python

import sys

current = 0
leaders = []
leaders_length = 3
smallest = 0

with open(sys.argv[1], 'r') as input_data:
  for line in input_data:
    if line != '\n':
      current += int(line)
    else:
      if current > smallest:
        leaders.append(current)
        smallest = min(leaders)
      current = 0
    
    if(len(leaders) > leaders_length):
      leaders.remove(smallest)

  print(sum(leaders))
