#!/usr/bin/env python

import sys

current = 0
most = 0

with open(sys.argv[1], 'r') as input_data:
  for line in input_data:
    if line != '\n':
      current += int(line)
    else:
      if current > most:
        most = current
      current = 0
  print(most)
